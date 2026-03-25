# 주요 기능 훑어보기

실제 도장 운영에서 자주 마주치는 상황별로 주짓주짓 매니저의 핵심 기능을 안내합니다.

---

## 1. 회원이 도장에 오면 뭘 하면 되나요?

> **전자 계약서**를 보내고, 서명이 완료되면 결제를 확인합니다.

### 과정

<figure><img src=".gitbook/assets/contract-flow.png" alt="계약서 발송 과정"><figcaption>계약서 발송부터 결제 확인까지</figcaption></figure>

```
계약서 템플릿 만들기 → 수업권 만들기 → 수업권에 계약서 연결
→ 회원에게 계약서 발송 (카카오/SMS) → 회원이 모바일에서 서명 → 결제 확인
```

| 단계 | 설명 | 가이드 |
|---|---|---|
| ① 계약서 양식 작성 | 환불 규정, 동의 항목 등 도장에 맞는 양식을 만듭니다 | [계약서 관리](contracts/) |
| ② 수업권 만들기 | 1개월권, 3개월권 등 판매할 요금제를 등록합니다 | [수업권 관리](membership-plans.md) |
| ③ 계약서 발송 | 회원 이름과 번호를 입력하면 알림톡으로 링크가 전송됩니다 | [계약서 발송](contracts/sending.md) |
| ④ 결제 확인 | 회원이 서명하면 결제를 확인하고 수업권을 활성화합니다 | [서명된 계약서 관리](contracts/signed-management.md) |

{% hint style="warning" %}
**사전 필요 작업**

이 기능을 사용하려면 아래 3가지가 완료되어야 합니다.

1. [전화번호 인증](getting-started/phone-verification.md)
2. [지도자 인증 (사업자 인증)](getting-started/leader-verification.md)
3. [PARTNER 구독](subscription.md) (계약서 발송은 PARTNER 전용)
{% endhint %}

---

## 2. 출석 체크는 어떻게 하나요?

> 도장 입구에 태블릿을 두고 **키오스크 모드**로 셀프 체크인합니다.

### 과정

<figure><img src=".gitbook/assets/kiosk-checkin.png" alt="키오스크 체크인 화면"><figcaption>휴대폰 뒷자리 4자리로 간편 체크인</figcaption></figure>

```
회원이 전화번호 뒷 4자리 입력 → 본인 확인 → 체크인 완료
```

- **횟수제 수업권**은 체크인 시 자동으로 1회 차감됩니다.
- **기간제 수업권**은 출석만 기록됩니다.

### 벨트 자동 설정

벨트가 아직 등록되지 않은 신규 회원이 체크인하면, **벨트 색상 선택 화면**이 나타나도록 설정할 수 있습니다.

<figure><img src=".gitbook/assets/belt-picker.png" alt="벨트 색상 선택"><figcaption>원형 컬러 피커로 직관적 벨트 선택</figcaption></figure>

| 설정 | 방법 |
|---|---|
| 토글 켜기 | [대시보드](dashboard.md) → **"출석 시 벨트 설정"** 토글 ON |
| 대상 | 벨트가 미설정된 회원만 (기존 회원은 표시 안 됨) |

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

<figure><img src=".gitbook/assets/belt-upgrade.png" alt="원클릭 벨트 승급"><figcaption>회원 상세에서 원클릭 승급</figcaption></figure>

[회원 관리](members/) → 회원 클릭 → **"승급"** 버튼 → 다음 벨트로 즉시 승급

| 가이드 |
|---|
| [벨트 관리](members/belt-management.md) |

### 승급식 — 여러 명 한 번에 승급

<figure><img src=".gitbook/assets/ceremony.png" alt="승급식 워크플로우"><figcaption>후보자 자동 추출 → 검토 → 일괄 승급</figcaption></figure>

```
승급식 생성 → 출석 기준으로 후보자 자동 추출 → 검토/조정 → 확정 → 일괄 승급 실행
```

| 가이드 |
|---|
| [승급식](ceremonies.md) |

{% hint style="warning" %}
승급식은 [PARTNER 구독](subscription.md)이 필요합니다. 개별 승급은 FREE에서도 가능합니다.
{% endhint %}

---

## 4. 회원들에게 공지를 보내려면?

> 카카오 알림톡 또는 SMS로 **단체 메시지**를 발송합니다.

<figure><img src=".gitbook/assets/announcement.png" alt="공지 발송 화면"><figcaption>수신자 필터로 대상을 정밀하게 선택</figcaption></figure>

| 필터 예시 | 활용 |
|---|---|
| 흰 벨트만 | 기초 특강 안내 |
| 만료 7일 이내 | 수업권 갱신 안내 |
| 30대 이상 | 낮 시간 오픈매트 안내 |

**반복 발송이 번거롭다면?** → [자동 메시지](announcements/auto-messages.md)를 설정하면 만료 알림, 환영 메시지 등이 조건 충족 시 자동 발송됩니다.

| 가이드 |
|---|
| [공지 발송](announcements/manual.md) |
| [자동 메시지](announcements/auto-messages.md) |

{% hint style="warning" %}
공지 발송은 [전화번호 인증](getting-started/phone-verification.md), [지도자 인증](getting-started/leader-verification.md), [PARTNER 구독](subscription.md)이 모두 필요합니다.
{% endhint %}

---

## 5. 매출을 확인하고 싶어요

> [정산](settlement.md) 메뉴에서 매출 현황, 결제 내역을 확인하고 Excel로 내보냅니다.

<figure><img src=".gitbook/assets/settlement.png" alt="정산 대시보드"><figcaption>총 매출, 신규/갱신 매출, 결제 수단별 비중</figcaption></figure>

| 기능 | 설명 |
|---|---|
| 매출 대시보드 | 총 매출, 신규 회원 매출, 갱신 매출, 결제 수단별 비중 |
| 결제 내역 | 모든 결제 건 날짜순 조회, 결제 수단 수정 가능 |
| Excel 내보내기 | 기간 설정 후 XLSX 다운로드 (세무/회계용) |

| 가이드 |
|---|
| [정산](settlement.md) |

{% hint style="warning" %}
정산은 [PARTNER 구독](subscription.md)이 필요합니다.
{% endhint %}

---

## 6. 다른 시스템에서 회원 데이터를 옮기려면?

> 기존 시스템(다짐 등)에서 **Excel 파일**로 내보낸 후 업로드합니다.

<figure><img src=".gitbook/assets/data-migration.png" alt="데이터 이관"><figcaption>Excel 업로드 → 검증 → 승인 → 이관 완료</figcaption></figure>

```
기존 시스템에서 Excel 다운로드 → 매니저에서 업로드 → 자동 검증 → 관리자 승인 → 완료
```

| 가이드 |
|---|
| [데이터 이관](data-migration.md) |

{% hint style="warning" %}
데이터 이관은 [지도자 인증](getting-started/leader-verification.md)이 필요합니다. FREE 요금제는 15명 제한이 있으므로 대량 이관 시 [PARTNER 구독](subscription.md)을 권장합니다.
{% endhint %}

---

## 사진이 없는 항목이 있나요?

이 페이지의 스크린샷은 순차적으로 추가됩니다.\
궁금한 점은 [카카오톡 채널](https://pf.kakao.com/_NnxmZX)로 문의해 주세요.
