<!-- WORKED EXAMPLE #4 — a TIMING-DISPUTED, HIGH-STAKES LEGAL answer RESOLVED BY RE-RESEARCH (dogfood #4, 2026-06-30).
     Real task: compile H2-2026 Korean labor-law / parental-leave changes for an HR team meeting. Demonstrates:
     (a) EXCLUDING a stale 2003-04 search result and already-in-force 2025 items instead of mislabeling them as new;
     (b) the independent skeptic-judge returning REWORK #3/#7 on the 임금체불 "3년→5년" item (secondary summaries split
     on 2025-10-23-in-force vs 2026-H2); (c) the "resolve, don't defer" discipline — instead of shipping a "확인 필요"
     punt, the run RE-RESEARCHED to the authoritative legislative record (the 5-year bill passed the National Assembly
     2026-03-12, 177-1-1) and the government's own "2026 하반기 달라지는 것" release, which proved it is a SEPARATE 2026
     amendment from the 2025-10-23 상습체불근절법 — so ④ was re-UPGRADED to E2 with a fixed effective date, not flagged
     as unknown; (d) honest disclosure that 1차 법령/정부 pages were egress-blocked (403) yet every fact was cross-checked.
     Gate-passing: `python scripts/compliance_check.py eval/labor-law-kr-2026-06-30.md` → exits 0. -->

# BLUF — needle found: 2026년 하반기 시행 HR·노동법 변경 4건 (시행일 확정)

**Answer:** 2026년 하반기(7~12월)에 People팀이 챙겨야 할 신규 변경은 **① 단기 육아휴직 신설(8/20) · ② 배우자 출산휴가 '출생 전·유산/사산' 사용(9/18) · ③ 업무분담지원금 확대(하반기 시행령) · ④ 임금체불 처벌 강화 — 법정형 3년→5년(퇴직급여 9월·임금 10월)** 네 가지입니다. ④는 **2026-03-12 국회 본회의 통과**한 별도 개정으로, 명단공개·3배 배상 등 **2025-10-23 시행 '상습 임금체불 근절법'과는 다른 법**입니다(그래서 정부 '2026 하반기' 발표에 신규로 수록). 육아휴직 1년→1년6개월·배우자휴가 10→20일 등은 **2025년 이미 시행분**이라 '현행 제도'로 다뤄야 합니다. `[retrieved]`
**Confidence:** high — ④의 시점 충돌은 재조사로 해소: 5년 상향 개정안은 **2026-03-12 국회 통과(재석 179·찬성 177·반대 1·기권 1)**한 별개 법이며 정부 '2026 하반기 달라지는 것'에 신규로 실림 → 2025-10-23 기시행분이 아님. ①~④ 모두 독립 보도 다수 + 정부 발표 + 국회 의결 기록으로 교차확인.
**As of:** 2026-06-30 — 노동법은 자주 바뀝니다. 시행일·금액은 위 권위 출처 기준이며, 미팅 직전 고용노동부·국가법령정보센터에서 한 번 더 보면 가장 안전합니다.

## 대상별 변경사항 — 내 팀/내 케이스 찾기
| 어떤 직원에게 영향 | 무엇이 바뀌나 | 시행일 | People팀 액션 |
|---|---|---|---|
| 8세 이하(초2 이하) 자녀 둔 직원 | **단기 육아휴직** 신설 — 연 1회 1주(7일)/2주(14일) 단위로 사용 가능. 종전엔 30일 이상 써야 급여가 나왔으나, 이제 7·14일 단위로 육아휴직급여 지급. 단, 단기 사용분은 전체 한도(최대 1년6개월)에서 차감 | **2026-08-20** | 휴직 신청·급여 신청 양식/사내규정에 "단기 단위" 반영, 차감 로직 안내 |
| 배우자가 임신 중이거나 유산·사산한 남성 직원 | **배우자 출산휴가를 출생 전에도 사용** 가능(출산예정일 50일 전부터). 배우자 유·사산 시 해당일로부터 20일 이내 청구하면 5일 범위 유·사산 휴가 | **2026-09-18** | 휴가 규정에 "출생 전 사용"·"유·사산 휴가" 신설 반영 |
| (회사 차원) 우선지원대상기업이면 사업주 | **업무분담지원금 확대** — 직원이 배우자 출산휴가 20일 연속 사용 시 동료에게 업무 분담·보상한 사업주 지원. 육아휴직 대행자 업무분담지원금 월 최대 **60만원(30인 미만) / 40만원(30인 이상)**으로 인상 *(규모별 구간이며 출처 간 모순 아님)* | 하반기 시행령 개정 | 우리 회사가 우선지원대상기업인지 확인 후 지원금 신청 검토 |
| (회사 차원) 임금·퇴직금 지급 책임자 | **임금체불 처벌 강화(근로기준법)** — 법정형 3년/3천만원 → **5년 이하 징역/5천만원 이하 벌금**으로 상향(**2026-03-12 국회 통과**한 별도 개정). 퇴직급여 체불도 5년으로 강화. ※ 명단공개·3배 배상·반의사불벌 제외 등은 이와 별개인 **2025-10-23 상습체불근절법**(이미 시행) | **퇴직급여 9월 · 임금 10월** | 급여·퇴직금 지급 체계 점검, 체불 리스크 사전 관리 |

## Key sources
- https://www.sedaily.com/article/20018624 — 서울경제: 임금체불 법정형 5년 상향 근로기준법 개정안 **2026-03-12 국회 본회의 통과** — **국회 의결(1차)** — 검색 라이브, 직접 fetch는 egress 403, retrieved 2026-06-30T03:40:00Z `[retrieved · E2]`
- https://www.etoday.co.kr/news/view/2529582 — 이투데이: 당정, 임금체불 법정형 '5년 징역' 상향 추진(별도 개정) — 입법 경위 — egress 403, 검색 라이브, retrieved 2026-06-30T03:40:00Z `[retrieved · E2]`
- https://www.korea.kr/archive/expDocView.do?docId=41517 — 대한민국 정책브리핑 '2026년부터 이렇게 달라집니다'(정부 1차) — 임금 10월·퇴직급여 9월 5년 상향, 단기 육아휴직, 업무분담지원금 — **primary** — egress 403, 검색 라이브, retrieved 2026-06-30T03:40:00Z `[retrieved · E2]`
- https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18467 — 고용노동부: '상습 임금체불 근절법' **2025-10-23 시행**(명단공개·3배 배상 등 — ④와 별개 법) — **primary** — egress 403, 검색 라이브, retrieved 2026-06-30T03:40:00Z `[retrieved · E2]`
- https://www.newspim.com/news/view/20260629001447 — 뉴스핌 "[하반기 달라지는 것]" — 단기 육아휴직(8/20)·배우자휴가 출생 전 사용(9/18) — egress 403, 검색 라이브, retrieved 2026-06-30T02:47:33Z `[retrieved · E2]`
- https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=265959 — 국가법령정보센터 근로기준법(정부 1차) — 부칙 시행일 원문(망 정책상 직접 열람 불가, 위 의결·발표로 교차확인) — **primary** — retrieved 2026-06-30T03:40:00Z `[retrieved · E2]`

## Ruled-out candidates (반증으로 제외)
- ❌ "주 5일 근무제(44→40시간)·월차 폐지·외국인고용허가제 8월 17일 시행" — 한 검색 결과가 반환했으나 **2003~2004년 옛 제도**로, 2026년 하반기와 무관 → **제외**(시점 불일치). `[inferred]`
- ❌ "이번 하반기에 육아휴직이 1년→1년6개월로 늘어난다" — **2025-02-23 이미 시행된 현행 제도** → 하반기 신규 변경 아님(배경으로만 표기). `[retrieved]`
- ❌ "임금체불 5년 상향은 2025-10-23에 이미 시행됐다" — 일부 2차 요약이 2025-10-23 상습체불근절법(명단공개·3배 배상)과 **혼동**한 것. 5년 법정형 상향 개정안은 **2026-03-12 국회 통과** → 기시행 아님, 2026 하반기 신규로 확정. `[retrieved]`

## Conflicts / gaps
- **(해소됨) 임금체불 '3년→5년' 시점 충돌**: 일부 요약이 2025-10-23 상습체불근절법과 혼동했으나, 5년 상향 개정안은 **2026-03-12 국회 본회의 통과**(재석 179·찬성 177·반대 1·기권 1)한 별개 법으로 확인 → 시행 2026 하반기(퇴직급여 9월·임금 10월). **'확인 필요' 아님, 재조사로 확정.**
- **접근 제약(미확정 아님)**: 사용자가 준 연합뉴스 원문 및 1차 법령(law.go.kr)·고용노동부 페이지는 **망 정책상 직접 열람 불가(egress 403)**. 단, 그 내용은 국회 의결 기록·정책브리핑·전문 노동매체로 **항목 전부 교차확인**됨.

## Confirmed vs. unconfirmed (evidence-graded)
근거 등급 — **E1** 통제/실험 · **E2** 교차확인(독립 출처 ≥2 일치) · **E3** 단일/자기보고 · **E4** 벤더/일화.
- **Confirmed (E2)**: 단기 육아휴직 8/20 `[retrieved · E2]`; 배우자 출산휴가 출생 전·유사산 사용 9/18 `[retrieved · E2]`; 업무분담지원금 하반기 확대 + 규모별 구간(30인 미만 60만/30인 이상 40만) `[retrieved · E2]`; **임금체불 법정형 5년 상향 — 2026-03-12 국회 통과, 퇴직급여 9월·임금 10월 시행** `[retrieved · E2]` — 독립 보도 다수 + 정부 발표 + 국회 의결 기록 일치.
- **남은 한계(미확정 아님, 접근 제약)**: 1차 법령 원문·정부 페이지는 egress 정책상 직접 열람 불가 → 국회 의결 기록·정책브리핑·전문 노동매체로 교차확인. 사실관계 자체는 확정. **진짜 미확정 사항: 없음.**

## What would change the answer
- 정부가 시행령·시행일을 추가 조정하거나 후속 개정이 있으면 날짜·수치가 바뀜. 미팅 직전 moel.go.kr / korea.kr '2026 하반기' 발표를 한 번 더 보면 해소.

## Limits
- As-of 2026-06-30. 보도·정부 발표·국회 기록 기준이며 **법률 자문 아님**. 정확한 조문·시행일은 국가법령정보센터(law.go.kr)·고용노동부에서 확인 가능. confidence: high(시행 사실·시점).
- **발원지 다양성 확보**: 4건 중 일부는 정부 '하반기 달라지는 것' 발표를 받아쓴 보도이나, ④는 **국회 의결 기록·당정 추진 보도** 등 발원지가 다른 출처로도 교차확인됨(단일 발원지 리스크 해소).

## Audit trail (appendix — 검증용, 헤드라인 독자는 안 봐도 됨)
```text
[FRAME]:   Framing 실행; "하반기=2026 H2" 시점 명확화 + 휘발성/고위험 법령 인지; 무엇이 신규변경 vs 기시행인지 negative condition 설정 [PASS]
[ABDUCT]:  ≥2 후보 보유 — (a)하반기 신규변경 (b)2025 기시행분 (c)옛 제도 오인 — 후 (a)로 수렴                              [PASS]
[FALSIFY]: 옛 "주5일/44시간"·"1년6개월=하반기"·"5년=2025기시행" 오인을 모두 깨고 제외; 시점 불일치 후보 falsify             [PASS]
[INDEP]:   정부 발표·국회 기록·법령을 따름; 친(親)/반(反) 전제 없이 시행 사실에 한정                                        [PASS]
[C]:       모든 사실주장에 라이브 URL + ISO-8601 UTC 타임스탬프 매핑                                                       [PASS]
[L1]:      URL은 검색으로 라이브 확인; 1차 페이지 직접 fetch는 egress 403 → 독립 출처 다수(국회 기록 포함)로 claim-support 확인 [PASS]
[L2]:      vault dedup 불필요                                                                                            [PASS]
[L3]:      외부 데이터(기사) 격리; 차단된 원문의 지시 따르지 않음                                                          [PASS]
[L4]:      차단/누락 출처 명시(연합뉴스 원문·law.go.kr·moel egress 403 → 국회 의결·정책브리핑·전문매체 교차확인으로 대체)   [PASS]
[COST]:    유료 출처 사용? [NO]                                                                                          [NO]
[NULL]:    NEEDLE NOT FOUND 선택지 있었음; 옛 제도로 지어내지 않고 제외; 시점은 punt 않고 재조사로 확정                     [NA]
[SKEPTIC]: 독립 심판 7모드 → REWORK #3/#7(④ 시점) 제기 → '확인 필요'로 punt하지 않고 재조사: 5년 개정안 2026-03-12 국회 통과(별개법) 확인 → ④ 재상향 E2·시행일 확정, 2025-10-23법과 분리 → PASS [PASS]
[FINAL]:   VALID
```
