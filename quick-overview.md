# 주요 기능 훑어보기

회원 등록부터 승급까지, 주짓주짓 매니저의 핵심 기능을 실제 운영 순서대로 소개합니다. 🥋\
주짓수 도장과 태권도 도장 모두 같은 흐름으로 씁니다.

---

## 0. 3분이면 시작

1. **휴대폰 번호**로 로그인 → [로그인](getting-started/login.md)
2. **종목(주짓수 / 태권도)**을 고르고 도장 등록 → [도장 등록](getting-started/gym-registration.md)
3. 승인 대기 없이 바로 대시보드로. [시작 가이드](getting-started/setup-checklist.md) 5단계를 따라가면 준비가 끝납니다.

---

## 1. 계약서 준비

**새 계약서 만들기**를 누르면 종목에 맞는 계약서 초안이 채워집니다.\
태권도 초안에는 보호자 동의·차량 이용 동의가 처음부터 들어 있습니다.

<div align="left"><figure><img src=".gitbook/assets/계약서 기본 템플릿 제공.png" alt="계약서 기본 초안" width="563"><figcaption>기본 조항 — 이용약관, 수업 규정, 면책 규정, 개인정보 동의 등</figcaption></figure></div>

계약서 PDF에 들어갈 **지도자 서명**도 미리 등록해 두세요.

<div align="left"><figure><img src=".gitbook/assets/서명관리_등록완료.png" alt="지도자 서명 등록" width="375"><figcaption>등록한 서명은 모든 계약서에 함께 들어갑니다</figcaption></figure></div>

→ 자세히 보기: [전자 계약서](contracts/README.md)

---

## 2. 회원 등록

### A. 계약서 보내기

회원권을 고르고 이름·전화번호를 넣으면 **카카오 알림톡**으로 서명 링크가 갑니다.\
회원은 앱 설치 없이 **휴대폰 브라우저에서 바로 서명**하고, 서명하면 회원 목록에 자동으로 들어옵니다.

<div align="left"><figure><img src=".gitbook/assets/계약서 발송.png" alt="계약서 보내기" width="563"><figcaption>회원권 선택 → 받는 사람 입력 → 보내기</figcaption></figure></div>

<div align="center"><figure><img src=".gitbook/assets/계약서 수신.jpg" alt="회원이 받는 알림톡" width="280"><figcaption>회원이 받는 카카오 알림톡</figcaption></figure></div>

→ 자세히 보기: [계약서 보내기](contracts/sending.md) · [회원 서명 과정](contracts/signing-flow.md)

### B. 기존 프로그램에서 옮기기

다짐 등에서 내려받은 **엑셀을 올리면** 회원이 한 번에 옮겨집니다. 보통 1~2 영업일 안에 끝납니다.

→ 자세히 보기: [회원 데이터 옮기기](data-migration.md)

---

## 3. 출석 키오스크

도장 입구에 태블릿 하나만 두세요. 회원이 **휴대폰 뒷자리 4자리**를 누르면 출석이 끝납니다.

<div align="left"><figure><img src=".gitbook/assets/키오스크 모드.gif" alt="키오스크 출석" width="563"><figcaption>뒷자리 4자리 → 본인 선택 → 출석 완료</figcaption></figure></div>

- **횟수제**는 출석할 때 1회 차감, **기간제**는 기록만 남습니다.
- **주짓수 도장**은 벨트가 없는 회원이 출석할 때 한 번만 벨트를 직접 고르게 할 수 있습니다.

→ 자세히 보기: [출석 키오스크](attendance/kiosk.md)

---

## 4. 키즈 등·하원 알림

회원 정보에 **보호자 전화번호**를 넣으면 키즈부 회원이 됩니다.\
아이가 출석하면 보호자에게 **등원 알림**이, 하원 버튼을 누르면 **하원 알림**이 갑니다.

- 사범님은 휴대폰 **등·하원** 화면에서 픽업 주소를 보고 전화·지도·등원·하원을 처리합니다.
- 픽업 주소는 보호자가 링크로 직접 입력합니다.

→ 자세히 보기: [키즈 등·하원](kids/README.md)

---

## 5. 회원 관리

<div align="left"><figure><img src=".gitbook/assets/회원관리.png" alt="회원 목록" width="563"><figcaption>회원 상태·회원권·연령대·벨트 필터로 바로 검색</figcaption></figure></div>

| 기능 | 설명 |
|---|---|
| 상태 필터 | 만료 임박 · 만료 · 장기 미출석 · 횟수 부족 |
| 만료 안내 알림톡 | 만료 임박 회원에게 한 번에 갱신 안내 |
| 회원권 연장 · 환불 · 횟수 조정 | 회원 상세에서 바로 처리 |
| 보호자 정보 · 지도자 메모 | 키즈부 관리, 부상 이력 등 기록 |

→ 자세히 보기: [회원 관리](members/README.md) · [회원 상세](members/detail.md)

---

## 6. 승급

출석 기준으로 승급 대상자를 **자동으로 뽑고**, 검토한 뒤 **한 번에 승급**합니다. 승급한 회원에게는 축하 메시지가 갑니다.

```
만들기 → 최소 출석일 설정 → 대상자 검색 → 검토·조정 → 확정 → 일괄 승급
```

| 주짓수 도장 | 태권도 도장 |
|---|---|
| **승급식** — IBJJF 벨트·그랄 | **승급 심사** — 급·품·단, 나이에 맞는 품·단 자동 제안 |
| [승급식](jiujitsu/ceremonies.md) | [승급 심사](taekwondo/promotion-test.md) · [띠 설정](taekwondo/ranks.md) |

<div align="left"><figure><img src=".gitbook/assets/승급식 승급대상회원.png" alt="승급 대상자" width="563"><figcaption>출석 기준으로 뽑힌 대상자 — 목표 벨트·띠를 개별 조정</figcaption></figure></div>

---

## 7. 매출

<div align="left"><figure><img src=".gitbook/assets/정산대시보드.png" alt="매출 현황" width="563"><figcaption>순매출, 환불률, 만료 임박·이탈 회원</figcaption></figure></div>

- **매출 현황**: 이번 달 순매출, 월별 추세, 환불률, 이탈 회원
- **수납 관리**: 결제 내역 조회, 결제 수단 수정, Excel 내보내기

→ 자세히 보기: [매출](settlement.md)

---

궁금한 점은 [카카오톡 채널](https://pf.kakao.com/_NnxmZX)로 문의해 주세요.
