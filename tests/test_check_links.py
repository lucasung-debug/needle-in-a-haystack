#!/usr/bin/env python3
"""Offline classification test for compliance_check.check_links_live (PDCA Cycle 11, red-team fixes).

Monkeypatches the network so the dead / nxdomain / suspect / unverified / live classification is proven
deterministically — no real requests, CI-safe, and kept out of the frozen eval (eval stays format-only).

  python tests/test_check_links.py        # exit 0 = classification correct
"""
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import compliance_check as cc  # noqa: E402


class _Resp:
    def __init__(self, status, final):
        self.status = status
        self._final = final

    def geturl(self):
        return self._final

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _make_opener(table):
    """table[url] = (head_outcome, get_outcome); an outcome is an int code, a (code, final_url) tuple,
    or an Exception instance to raise."""
    def fake_urlopen(req, timeout=None):
        url = req.full_url
        out = table[url][0 if req.get_method() == "HEAD" else 1]
        if isinstance(out, Exception):
            raise out
        if isinstance(out, tuple):
            return _Resp(out[0], out[1])
        if out >= 400:
            raise urllib.error.HTTPError(url, out, f"err{out}", {}, None)
        return _Resp(out, url)
    return fake_urlopen


def run():
    nx = urllib.error.URLError(socket.gaierror(-2, "Name or service not known"))
    transient = urllib.error.URLError(TimeoutError("timed out"))
    table = {
        "https://a/live": (200, 200),                              # live
        "https://a/notfound": (404, 404),                          # dead
        "https://a/gone": (410, 410),                              # dead
        "https://a/head500-get200": (500, 200),                    # transient HEAD, live GET -> live
        "https://a/persist503": (503, 503),                        # transient -> unverified
        "https://a/forbidden": (403, 403),                         # access -> unverified
        "https://a/method": (405, 405),                            # method -> unverified
        "https://a/teapot501": (501, 501),                         # not-implemented -> unverified
        "https://a/ratelimited": (429, 429),                       # rate -> unverified
        "https://a/badhead-get200": (400, 200),                    # 400 on HEAD, live GET -> live
        "https://nope.invalidtld/x": (nx, nx),                     # NXDOMAIN -> nxdomain
        "https://a/timeout": (transient, transient),               # transient -> unverified
        "https://a/deep/path": ((200, "https://a/"), (200, "https://a/")),  # 200 but redirected to root -> suspect
    }
    text = "\n".join(f"- {u} retrieved 2026-06-29T00:00:00Z [retrieved]" for u in table)

    orig = urllib.request.urlopen
    urllib.request.urlopen = _make_opener(table)
    try:
        lc = cc.check_links_live(text, timeout=1, limit=99, budget=999)
    finally:
        urllib.request.urlopen = orig

    got = {
        "dead": {u for u, _ in lc["dead"]},
        "nxdomain": set(lc["nxdomain"]),
        "suspect": {u for u, _ in lc["suspect"]},
        "unverified": {u for u, _ in lc["unverified"]},
    }
    got["live"] = set(table) - got["dead"] - got["nxdomain"] - got["suspect"] - got["unverified"]
    expect = {
        "dead": {"https://a/notfound", "https://a/gone"},
        "nxdomain": {"https://nope.invalidtld/x"},
        "suspect": {"https://a/deep/path"},
        "unverified": {"https://a/persist503", "https://a/forbidden", "https://a/method",
                       "https://a/teapot501", "https://a/ratelimited", "https://a/timeout"},
        "live": {"https://a/live", "https://a/head500-get200", "https://a/badhead-get200"},
    }
    for k in expect:
        assert got[k] == expect[k], f"{k}: got {sorted(got[k])} != expected {sorted(expect[k])}"
    print("check_links_live classification OK — " + " ".join(f"{k}={len(expect[k])}" for k in expect))


if __name__ == "__main__":
    run()
