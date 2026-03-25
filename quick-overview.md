# 주요 기능 훑어보기

실제 도장 운영에서 자주 마주치는 상황별로 주짓주짓 매니저의 핵심 기능을 안내합니다.

---

## 1. 회원이 도장에 오면 뭘 하면 되나요?

> **전자 계약서**를 보내고, 서명이 완료되면 결제를 확인합니다.

### ① 계약서 양식 만들기

환불 규정, 동의 항목 등 도장에 맞는 계약서 양식을 만듭니다.\
지도자 서명도 미리 등록해 두세요. 회원이 서명하면 PDF에 함께 표시됩니다.

<div align="left"><figure><img src=".gitbook/assets/서명 등록.png" alt="지도자 서명 등록" width="375"><figcaption>서명을 직접 그려서 등록</figcaption></figure></div>

<div align="left"><figure><img src=".gitbook/assets/서명 등록 완료됨.png" alt="서명 등록 완료" width="375"><figcaption>등록된 서명은 모든 계약서에 일괄 적용</figcaption></figure></div>

→ 자세히 보기: [계약서 관리](contracts/)

### ② 회원권 만들기

기간제(1개월, 3개월 등) 또는 횟수제(10회, 20회 등) 회원권을 등록합니다.

<div align="left"><figure><img src=".gitbook/assets/회원권 생성_1.png" alt="회원권 타입 선택" width="375"><figcaption>기간권 / 횟수권 선택 후 기본 정보 입력</figcaption></figure></div>

<div align="left"><figure><img src=".gitbook/assets/회원권 생성_2.png" alt="횟수 및 금액 설정" width="375"><figcaption>횟수·금액 설정 + 계약서 템플릿 연결</figcaption></figure></div>

→ 자세히 보기: [회원권 관리](membership-plans.md)

### ③ 계약서 발송

회원권을 선택하고 회원 이름과 번호를 입력하면 **카카오 알림톡**으로 계약서 링크가 전송됩니다.

<div align="left"><figure><img src=".gitbook/assets/발송할 회원권과 회원정보 입력.png" alt="계약서 발송 화면" width="563"><figcaption>발송할 회원권 선택 → 수신자 정보 입력 → 링크 생성</figcaption></figure></div>

→ 자세히 보기: [계약서 발송](contracts/sending.md)

### ④ 회원이 서명

회원은 카카오 알림톡으로 링크를 받고, 별도 앱 설치 없이 **모바일 브라우저에서 바로 서명**합니다.

<div align="center"><figure><img src=".gitbook/assets/계약서 수신.jpg" alt="회원이 받는 카카오 알림톡" width="280"><figcaption>회원이 받는 카카오 알림톡</figcaption></figure></div>

→ 자세히 보기: [회원 서명 과정](contracts/signing-flow.md)

### ⑤ 결제 확인

서명이 완료되면 매니저에서 결제를 확인하고 회원권을 활성화합니다.

→ 자세히 보기: [서명된 계약서 관리](contracts/signed-management.md)

{% hint style="warning" %}
**사전 필요 작업**

이 기능을 사용하려면 아래 3가지가 완료되어야 합니다.

1. [전화번호 인증](getting-started/phone-verification.md)
2. [지도자 인증 (사업자 인증)](getting-started/leader-verification.md)
3. [PARTNER 구독](subscription.md) (계약서 발송은 PARTNER 전용)
{% endhint %}

{% hint style="info" %}
회원에게 발송할 회원권 목록을 [주짓주짓 매니저](https://manager.thisisbjj.com)에서 확인할 수 있습니다.

<img src=".gitbook/assets/등록된 회원권 목록.png" alt="앱에서 본 회원권 목록" width="240">
{% endhint %}

---

## 2. 출석 체크는 어떻게 하나요?

> 도장 입구에 태블릿을 두고 **키오스크 모드**로 셀프 체크인합니다.

### 키오스크 체크인

<div align="left"><figure><img src=".gitbook/assets/키오스크 모드.gif" alt="키오스크 체크인" width="563"><figcaption>휴대폰 뒷자리 4자리 입력 → 회원 확인 → 체크인 완료</figcaption></figure></div>

- **횟수제 회원권**은 체크인 시 자동으로 1회 차감됩니다.
- **기간제 회원권**은 출석만 기록됩니다.

### 출석 시 벨트 자동 설정

[데이터 이관](data-migration.md) 후 또는 신규 관원 등록 후, 회원 한 명 한 명의 벨트를 일일이 등록하기 번거로울 수 있습니다.\
이 기능을 켜면 **벨트가 설정되지 않은 회원이 키오스크에서 체크인할 때 1회만 벨트 선택 화면이 노출**됩니다. 한번 설정된 이후에는 다시 나타나지 않습니다.

**① [대시보드](dashboard.md)에서 "출석체크로 벨트설정하기" 토글을 켭니다.**

<div align="left"><figure><img src=".gitbook/assets/대시보드 토글.png" alt="대시보드 벨트 설정 토글" width="563"><figcaption>대시보드 → 도장 설정 → 출석체크로 벨트설정하기 토글 ON</figcaption></figure></div>

**② 벨트가 미설정된 회원이 체크인하면 벨트 선택 화면이 나타납니다.**

<div align="left"><figure><img src=".gitbook/assets/출석체크 벨트설정 기능.gif" alt="출석 시 벨트 설정" width="563"><figcaption>체크인 → 벨트 색상 선택 → 설정 완료 (벨트 미설정 회원에게 1회만 노출)</figcaption></figure></div>

### 출석 확인

| 확인 방법 | 설명 | 가이드 |
|---|---|---|
| 오늘의 출석 | 실시간 체크인 현황 확인 | [출석 & 키오스크](attendance/) |
| 회원별 출석 | 회원 상세에서 월간 출석 달력 확인 | [회원 상세](members/detail.md) |
| 출석 통계 | 월별/요일별/시간대별 분석 | [출석 통계](attendance/stats.md) |

{% hint style="info" %}
**키오스크 세팅 팁**: 태블릿 브라우저를 전체 화면(F11)으로 설정하고, 자동 잠금을 꺼두세요. 자세한 설정은 [키오스크 설정](attendance/kiosk.md)을 참고하세요.
{% endhint %}

---

## 3. 회원의 벨트를 승급하려면?

> **개별 승급**과 **승급식(일괄 승급)** 두 가지 방법이 있습니다.

### 개별 승급 — 지금 바로 1명 승급

[회원 관리](members/) → 회원 클릭 → **"승급"** 버튼 → 다음 벨트로 즉시 승급

→ 자세히 보기: [벨트 관리](members/belt-management.md)

### 승급식 — 여러 명 한 번에 승급

```
승급식 생성 → 출석 기준으로 후보자 자동 추출 → 검토/조정 → 확정 → 일괄 승급 실행
```

→ 자세히 보기: [승급식](ceremonies.md)

{% hint style="warning" %}
승급식은 [PARTNER 구독](subscription.md)이 필요합니다. 개별 승급은 FREE에서도 가능합니다.
{% endhint %}

---

## 4. 회원들에게 공지를 보내려면?

> 카카오 알림톡 또는 SMS로 **단체 메시지**를 발송합니다.

| 필터 예시 | 활용 |
|---|---|
| 흰 벨트만 | 기초 특강 안내 |
| 만료 7일 이내 | 회원권 갱신 안내 |
| 30대 이상 | 낮 시간 오픈매트 안내 |

**반복 발송이 번거롭다면?** → [자동 메시지](announcements/auto-messages.md)를 설정하면 만료 알림, 환영 메시지 등이 조건 충족 시 자동 발송됩니다.

→ 자세히 보기: [공지 발송](announcements/manual.md) · [자동 메시지](announcements/auto-messages.md)

{% hint style="warning" %}
공지 발송은 [전화번호 인증](getting-started/phone-verification.md), [지도자 인증](getting-started/leader-verification.md), [PARTNER 구독](subscription.md)이 모두 필요합니다.
{% endhint %}

---

## 5. 매출을 확인하고 싶어요

> [정산](settlement.md) 메뉴에서 매출 현황, 결제 내역을 확인하고 Excel로 내보냅니다.

| 기능 | 설명 |
|---|---|
| 매출 대시보드 | 총 매출, 신규 회원 매출, 갱신 매출, 결제 수단별 비중 |
| 결제 내역 | 모든 결제 건 날짜순 조회, 결제 수단 수정 가능 |
| Excel 내보내기 | 기간 설정 후 XLSX 다운로드 (세무/회계용) |

→ 자세히 보기: [정산](settlement.md)

{% hint style="warning" %}
정산은 [PARTNER 구독](subscription.md)이 필요합니다.
{% endhint %}

---

## 6. 다른 시스템에서 회원 데이터를 옮기려면?

> 기존 시스템(다짐 등)에서 **Excel 파일**로 내보낸 후 업로드합니다.

### ① 이전할 프로그램 선택

현재 다짐(DaGym) 형식을 지원합니다. 추후 다른 프로그램도 지원할 예정입니다.

<div align="left"><figure><img src=".gitbook/assets/데이터 이전 프로그램 선택_다짐.png" alt="이전 프로그램 선택" width="563"><figcaption>다짐 선택 시 엑셀 파일 예시와 필수 컬럼 안내</figcaption></figure></div>

### ② 약관 동의 후 Excel 파일 업로드

<div align="left"><figure><img src=".gitbook/assets/데이터 파일 업로드.png" alt="데이터 파일 업로드" width="563"><figcaption>데이터 이전 약관 동의 → Excel 파일 업로드</figcaption></figure></div>

### ③ 업로드 완료 → 관리자 검토

파일 업로드가 완료되면 관리자가 검토 후 처리합니다. 보통 **1~2 영업일** 이내에 완료됩니다.

<div align="left"><figure><img src=".gitbook/assets/회원 이전 데이터 업로드 완료.png" alt="업로드 완료" width="563"><figcaption>접수 완료 — 검토 후 처리 안내</figcaption></figure></div>

→ 자세히 보기: [데이터 이관](data-migration.md)

{% hint style="warning" %}
데이터 이관은 [지도자 인증](getting-started/leader-verification.md)이 필요합니다. FREE 요금제는 15명 제한이 있으므로 대량 이관 시 [PARTNER 구독](subscription.md)을 권장합니다.
{% endhint %}

---

궁금한 점은 [카카오톡 채널](https://pf.kakao.com/_NnxmZX)로 문의해 주세요.
