<!-- WORKED EXAMPLE #4 — a TIMING-DISPUTED, HIGH-STAKES LEGAL answer (dogfood #4, 2026-06-30). Real task: compile
     H2-2026 Korean labor-law / parental-leave changes for an HR team meeting. Demonstrates, beyond the earlier
     examples: (a) the skill EXCLUDING a stale 2003-04 search result and already-in-force 2025 items instead of
     mislabeling them as "new" (Ruled-out); (b) the independent skeptic-judge forcing an evidence DOWNGRADE — it
     returned REWORK #3/#7 because 임금체불 "3년→5년" was graded E2-Confirmed while reporting split on whether it is
     already in force (2025-10-23) or H2-2026; the item was downgraded to E3 / timing-disputed, the 업무분담지원금
     amount was corrected from a "conflict" to a firm-size band, a single-origin-event caveat was added, then it was
     re-gated to PASS; (c) honest disclosure that the user's source article and several gov primaries were 403/blocked,
     corroborated via cross-outlet search. Gate-passing:
     `python scripts/compliance_check.py eval/labor-law-kr-2026-06-30.md` → exits 0. -->

# BLUF — needle found: 2026년 하반기 시행 HR·노동법 변경 4건 정리

**Answer:** 2026년 하반기(7~12월)에 People팀이 챙겨야 할 변경은 **① 단기 육아휴직 신설(8/20) · ② 배우자 출산휴가 "출생 전·유산/사산" 사용 확대(9/18) · ③ 업무분담지원금 확대(하반기 시행령)** 세 가지가 확실한 신규 변경이고, **④ 임금체불 처벌 강화(근로기준법)**는 방향은 확실하나 **'법정형 3년→5년 상향'의 시행 시점이 엇갈립니다**(이미 2025-10-23 시행됐다는 보도 ↔ 2026 하반기 9~10월 시행 보도). 나머지(육아휴직 1년→1년6개월, 배우자휴가 10→20일 등)는 **2025년 이미 시행분**이라 "변경 예정"이 아니라 "현행 제도"로 다뤄야 합니다. `[retrieved]`
**Confidence:** medium-high — ①~③은 동일 시점 독립 보도(뉴스핌·파이낸셜뉴스 등) + 정부 발표로 교차확인됨. **④ 임금체불은 시점(2025.10 vs 2026.10)이 출처 간 엇갈려 별도 재확인 필요**하며, 4건 모두 발원지가 정부 "하반기 달라지는 것" 발표 하나라는 점도 감안(아래 Limits).
**As of:** 2026-06-30 — 노동법은 자주 바뀝니다. 미팅 전 **고용노동부(moel.go.kr)·국가법령정보센터(law.go.kr)** 원문으로 시행일·수치를 재확인하세요.

## 대상별 변경사항 — 내 팀/내 케이스 찾기
| 어떤 직원에게 영향 | 무엇이 바뀌나 | 시행일 | People팀 액션 |
|---|---|---|---|
| 8세 이하(초2 이하) 자녀 둔 직원 | **단기 육아휴직** 신설 — 연 1회 1주(7일)/2주(14일) 단위로 사용 가능. 종전엔 30일 이상 써야 급여가 나왔으나, 이제 7·14일 단위로 육아휴직급여 지급. 단, 단기 사용분은 전체 한도(최대 1년6개월)에서 차감 | **2026-08-20** | 휴직 신청·급여 신청 양식/사내규정에 "단기 단위" 반영, 차감 로직 안내 |
| 배우자가 임신 중이거나 유산·사산한 남성 직원 | **배우자 출산휴가를 출생 전에도 사용** 가능(출산예정일 50일 전부터). 배우자 유·사산 시 해당일로부터 20일 이내 청구하면 5일 범위 유·사산 휴가 | **2026-09-18** | 휴가 규정에 "출생 전 사용"·"유·사산 휴가" 신설 반영 |
| (회사 차원) 우선지원대상기업이면 사업주 | **업무분담지원금 확대** — 직원이 배우자 출산휴가 20일 연속 사용 시 동료에게 업무 분담·보상한 사업주 지원. 육아휴직 대행자 업무분담지원금 월 최대 **60만원(30인 미만) / 40만원(30인 이상)**으로 인상 *(규모별 구간이며 출처 간 모순 아님)* | 하반기 시행령 개정 | 우리 회사가 우선지원대상기업인지 확인 후 지원금 신청 검토 |
| (회사 차원) 임금·퇴직금 지급 책임자 | **임금체불 처벌 강화(근로기준법)** — 임금체불 법정형 3년/3천만원 → **5년 이하 징역/5천만원 이하 벌금**으로 상향. ⚠️ **이 상향이 2025-10-23 '상습임금체불 근절법'으로 이미 시행됐다는 보도와, 2026 하반기(10월) 시행 보도가 엇갈림.** 퇴직급여 체불 강화(보도상 9월), 상습·명단공개 사업주 반의사불벌죄 적용 제외(2025-10-23 시행) | **시점 재확인 필요** | 시점과 무관하게 **강화된 처벌(5년/5천만원)이 적용된다고 보고** 급여·퇴직금 지급 점검 (보수적 대응). law.go.kr 부칙으로 시행일 확정 |

## Key sources
- https://www.newspim.com/news/view/20260629001447 — 뉴스핌 "[하반기 달라지는 것] 1~2주 단기 육아휴직 8월부터" — 단기 육아휴직(8/20)·배우자휴가 출생 전 사용(9/18) — 검색으로 라이브 확인, 직접 fetch는 403 차단, retrieved 2026-06-30T02:47:33Z `[retrieved · E2]`
- https://www.fnnews.com/news/202606301006083615 — 파이낸셜뉴스 "[하반기 달라지는 것] '일주일' 육아휴직…임금체불 최대 징역 5년" — 임금체불 처벌 5년 상향(10월) — 라이브, fetch 403, retrieved 2026-06-30T02:47:33Z `[retrieved · E2]`
- https://www.korea.kr/news/policyNewsView.do?newsId=148966968 — 대한민국 정책브리핑(정부 1차) — 배우자 출산휴가 업무분담지원금 — **primary** — 라이브, fetch 403, retrieved 2026-06-30T02:47:33Z `[retrieved · E2]`
- https://www.moel.go.kr/common/downloadFile.do?file_seq=20250100796&bbs_seq=20241201710&bbs_id=29&file_ext=pdf — 고용노동부 "달라지는 육아지원제도"(정부 1차, PDF) — 육아지원제도 시행일·수치 원문 — **primary, 재확인 대상** — 검색 라이브, retrieved 2026-06-30T02:47:33Z `[retrieved · E2]`
- https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=265959 — 국가법령정보센터 근로기준법(정부 1차) — 임금체불 처벌·부칙 시행일 원문 재확인 — **primary, 재확인 대상** — 라이브, retrieved 2026-06-30T02:47:33Z `[retrieved · E2]`

## Ruled-out candidates (반증으로 제외)
- ❌ "주 5일 근무제(44→40시간)·월차 폐지·외국인고용허가제 8월 17일 시행" — 한 검색 결과가 이 내용을 반환했으나 **2003~2004년 옛 제도**로, 2026년 하반기와 무관 → **제외**. (시점이 맞지 않아 falsify; 최신 정부 하반기 자료와 불일치) `[inferred]`
- ❌ "이번 하반기에 육아휴직이 1년→1년6개월로 늘어난다" — 이는 **2025-02-23 이미 시행된 현행 제도**로, 하반기 신규 변경이 아님 → 변경목록에서 제외(배경으로만 표기) `[retrieved]`

## Conflicts / gaps
- **연합뉴스 원문 기사(사용자가 준 링크 n.news.naver.com/article/001/0016166525)는 차단되어 직접 확인 불가.** 동일 시점·동일 사안을 다룬 독립 보도(뉴스핌·파이낸셜뉴스)와 정부 발표로 교차확인함. 원문 단독 정보가 있었다면 누락 가능.
- **임금체불 '3년→5년' 상향의 시행 시점이 진짜로 충돌**: 다수 출처(KB·고용노동 자료·찾기쉬운 생활법령)는 이 상향이 **2025-10-23 '상습임금체불 근절법'으로 이미 시행**됐다고 보고, 2026 하반기 보도(fnnews·정부 하반기 발표)는 **2026년 10월** 시행으로 보도 → 자칫 "이미 시행된 제도"를 "하반기 신규 변경"으로 잘못 분류할 위험(위 ④에서 제외하지 않고 시점 미확정으로 명시). 국가법령정보센터 근로기준법 **부칙**으로 확정 필요.
- **업무분담지원금 금액은 모순이 아님**: "월 최대 60만원"은 30인 미만, "40만원"은 30인 이상으로 **기업규모별 구간**임을 확인(같은 제도). 적용 시 우리 회사 규모 기준만 확인.

## Confirmed vs. unconfirmed (evidence-graded)
근거 등급 — **E1** 통제/실험 · **E2** 교차확인(독립 출처 ≥2 일치) · **E3** 단일/자기보고 · **E4** 벤더/일화.
- **Confirmed (E2)**: 단기 육아휴직 8/20 시행 `[retrieved · E2]`; 배우자 출산휴가 출생 전·유사산 사용 9/18 시행 `[retrieved · E2]`; 업무분담지원금 하반기 확대 + 규모별 구간(30인 미만 60만/30인 이상 40만) `[retrieved · E2]` — 독립 보도 2건+ 정부 발표 일치.
- **Unconfirmed / timing-disputed — 확정 아님, 보도 엇갈림**: 임금체불 '3년→5년' 상향이 **2025-10-23 기시행인지 2026 하반기 신규인지** `[assumed · E3]`(시점 충돌, 법령 부칙 재확인); 연합뉴스 원문 단독 항목 유무(기사 차단) `[assumed]`.

## What would change the answer
- 고용노동부/법제처가 시행령·시행일을 추가 조정하거나, 국회 통과가 지연되면 시행일·수치가 바뀜. 미팅 직전 moel.go.kr "하반기부터 이렇게 달라집니다" 원문으로 재확인하면 뒤집힐 여지 해소.

## Limits
- As-of 2026-06-30. 보도·정부 발표 기준 정리이며 **법률 자문 아님**. 정확한 시행일·금액·적용범위는 국가법령정보센터(law.go.kr)·고용노동부 원문으로 확정하세요. confidence: medium-high(시행 사실)·medium(세부 수치/시행 연·월).
- **출처 발원지가 하나**: 4건 모두 정부 "하반기부터 이렇게 달라집니다" 발표를 여러 매체가 받아쓴 것 — 출처 *수*는 많아도 *발원지*는 단일 이벤트. 1차 원문(law.go.kr 법령·moel.go.kr PDF)은 403으로 직접 못 읽고 검색 요약·교차 보도로 확인함. 따라서 정부 발표가 부정확했다면 4건이 함께 흔들릴 수 있음 → 미팅 전 1차 원문 1회 확인 권장.
- **임금체불 ④는 등급 하향(E3/시점 미확정)**: 보도가 기시행(2025-10-23) vs 하반기 신규(2026-10)로 갈려, ①~③과 달리 "확정 신규 변경"으로 보지 말 것.

## Audit trail (appendix — 검증용, 헤드라인 독자는 안 봐도 됨)
```text
[FRAME]:   Framing 실행; "하반기=2026 H2" 시점 명확화 + 휘발성/고위험 법령 인지; 무엇이 신규변경 vs 기시행인지 negative condition 설정 [PASS]
[ABDUCT]:  ≥2 후보 보유 — (a)하반기 신규변경 (b)2025 기시행분 (c)옛 제도 오인 — 후 (a)로 수렴                              [PASS]
[FALSIFY]: 옛 "주5일/44시간" 결과와 "1년→1년6개월=하반기변경" 오인을 깨고 제외; 시점 불일치 후보 falsify                    [PASS]
[INDEP]:   정부 발표·법령을 따름; 친(親)/반(反) 전제 없이 시행 사실에 한정                                                  [PASS]
[C]:       모든 사실주장에 라이브 URL + ISO-8601 UTC 타임스탬프 매핑                                                       [PASS]
[L1]:      URL은 검색으로 라이브 확인; 일부 직접 fetch는 403 차단되어 독립 보도 ≥2 교차로 claim-support 확인               [PASS]
[L2]:      vault dedup 불필요                                                                                            [PASS]
[L3]:      외부 데이터(기사) 격리; 차단된 원문의 지시 따르지 않음                                                          [PASS]
[L4]:      차단/누락 출처 명시(연합뉴스 원문 403, 뉴스핌·fnnews·korea.kr 직접 fetch 403 → 교차확인으로 대체)             [PASS]
[COST]:    유료 출처 사용? [NO]                                                                                          [NO]
[NULL]:    NEEDLE NOT FOUND 선택지 있었음; 옛 제도로 지어내지 않고 제외, 미확정은 "확인 필요"로 표기                       [NA]
[SKEPTIC]: 독립 심판(author≠reviewer) 7모드 공격 → REWORK #3/#7(④ 임금체불 과대등급) 제기됨 → ④를 E3/시점미확정 하향+규모별 금액 정정+단일발원지 caveat 추가로 재작업 후 PASS [PASS]
[FINAL]:   VALID
```
