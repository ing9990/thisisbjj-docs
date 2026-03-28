# 주요 기능 훑어보기

도장 운영에 필요한 모든 것을 하나의 화면에서 관리합니다.\
회원 등록부터 승급식까지, 주짓주짓 매니저의 핵심 기능을 소개합니다.

---

## 지도자가 미리 준비해야 할 사항

회원을 받기 전에 **계약서**와 **지도자 서명**을 미리 준비하세요.

### 1. 계약서 만들기

기본 제공되는 템플릿(이용약관, 수업 규정, 면책 규정 등)을 바탕으로 도장에 맞는 계약서를 구성합니다.

<div align="left"><figure><img src=".gitbook/assets/계약서 기본 템플릿 제공.png" alt="계약서 기본 템플릿" width="563"><figcaption>기본 제공 섹션 — 이용약관, 수업 규정, 면책 규정, 개인정보 동의 등</figcaption></figure></div>

각 섹션을 눌러 내용을 자유롭게 수정할 수 있습니다.\
도장 규칙에 맞게 조항을 추가하거나 삭제하세요.

<div align="left"><figure><img src=".gitbook/assets/계약서 조항 커스터마이징.png" alt="계약서 조항 커스터마이징" width="563"><figcaption>섹션 내용을 도장에 맞게 직접 수정</figcaption></figure></div>

완성된 계약서는 저장 후 회원권에 연결하면 바로 사용할 수 있습니다.

<div align="left"><figure><img src=".gitbook/assets/계약서 템플릿 저장됨.png" alt="계약서 템플릿 저장" width="563"><figcaption>계약서 템플릿 저장 완료 — 회원권에 연결하면 바로 발송 가능</figcaption></figure></div>

→ 자세히 보기: [계약서 관리](contracts/)

### 2. 지도자 서명 등록

계약서 PDF에 포함될 **지도자 서명**을 미리 등록합니다.\
직접 그리거나 서명 이미지를 업로드할 수 있습니다.

<div align="left"><figure><img src=".gitbook/assets/서명관리_이미지 업로드.png" alt="서명 이미지 업로드" width="375"><figcaption>서명 이미지 파일(PNG, JPG)을 업로드</figcaption></figure></div>

<div align="left"><figure><img src=".gitbook/assets/서명관리_사진 자르기.png" alt="서명 영역 자르기" width="375"><figcaption>드래그로 서명 영역을 조정</figcaption></figure></div>

<div align="left"><figure><img src=".gitbook/assets/서명관리_등록완료.png" alt="서명 등록 완료" width="375"><figcaption>등록된 서명은 모든 계약서 템플릿에 일괄 적용</figcaption></figure></div>

→ 자세히 보기: [계약서 관리](contracts/)

---

## 회원 등록하기

준비가 끝났으면 회원을 등록합니다.

### A. 계약서 발송하기

회원권을 선택하고 이름·전화번호를 입력하면 **카카오 알림톡**으로 계약서 링크가 발송됩니다.

<div align="left"><figure><img src=".gitbook/assets/계약서 발송.png" alt="계약서 발송 화면" width="563"><figcaption>회원권 선택 → 수신자 정보 입력 → 링크 생성</figcaption></figure></div>

회원은 앱 설치 없이 **모바일 브라우저에서 바로 서명**합니다.

<div align="center"><figure><img src=".gitbook/assets/계약서 수신.jpg" alt="회원이 받는 카카오 알림톡" width="280"><figcaption>회원이 받는 카카오 알림톡</figcaption></figure></div>

서명이 완료되면 **실시간 알림**이 오고, 결제를 확인하면 회원 등록이 완료됩니다.

→ 자세히 보기: [계약서 발송](contracts/sending.md) · [서명 과정](contracts/signing-flow.md)

### B. 타 업체에서 회원 데이터 이전하기

기존 시스템(다짐 등)에서 **엑셀 파일로 내보낸 후 업로드**하면 회원 정보가 일괄 이전됩니다.\
현재 다짐(DaGym) 형식을 지원하며, 추후 다른 프로그램도 지원 예정입니다.

<div align="left"><figure><img src=".gitbook/assets/데이터 이전 프로그램 선택_다짐.png" alt="이전 프로그램 선택" width="563"><figcaption>이전할 프로그램 선택 후 엑셀 파일 업로드</figcaption></figure></div>

파일 업로드 후 관리자 검토를 거쳐 보통 **1\~2 영업일** 이내에 이전이 완료됩니다.

→ 자세히 보기: [데이터 이관](data-migration.md)

---

## 계약서 발송 이후 회원이 해야 할 것

계약서 링크를 받은 회원은 모바일에서 간단히 온보딩을 완료합니다.

1. **카카오 알림톡**으로 받은 링크를 클릭
2. 계약서 내용 확인 후 **전자 서명**
3. 본인 인증(휴대폰 번호 확인)
4. 서명 완료 — 지도자에게 실시간 알림

{% hint style="info" %}
회원은 별도 앱 설치 없이 **모바일 브라우저에서 모든 과정을 완료**합니다.
{% endhint %}

→ 자세히 보기: [회원 서명 과정](contracts/signing-flow.md)

---

## 키오스크 모드

도장 입구에 태블릿 하나만 두세요.\
회원이 **휴대폰 뒷자리 4자리**를 입력하면 출석 체크가 끝납니다.

<div align="left"><figure><img src=".gitbook/assets/키오스크 모드.gif" alt="키오스크 체크인" width="563"><figcaption>뒷자리 4자리 입력 → 회원 확인 → 체크인 완료</figcaption></figure></div>

- **횟수제 회원권** — 체크인 시 자동으로 1회 차감
- **기간제 회원권** — 출석 기록만 남김

벨트가 설정되지 않은 회원이 체크인하면 **1회만 벨트 선택 화면이 노출**됩니다.\
데이터 이관 직후나 신규 회원이 많을 때, 일일이 벨트를 등록할 필요 없이 출석 시 자연스럽게 설정됩니다.

<div align="left"><figure><img src=".gitbook/assets/출석체크 벨트설정 기능.gif" alt="출석 시 벨트 자동 설정" width="563"><figcaption>체크인 → 벨트 색상 선택 → 설정 완료 (1회만 노출)</figcaption></figure></div>

{% hint style="info" %}
**키오스크 세팅 팁**: 태블릿 브라우저를 전체 화면(F11)으로 설정하고, 자동 잠금을 꺼두세요.\
→ 자세한 설정: [키오스크 설정](attendance/kiosk.md)
{% endhint %}

→ 자세히 보기: [출석 & 키오스크](attendance/) · [출석 통계](attendance/stats.md)

---

## 회원 관리

등록된 회원 전체를 한눈에 파악하고, 개별 관리까지 한 곳에서 처리합니다.

<div align="left"><figure><img src=".gitbook/assets/회원관리.png" alt="회원 목록" width="563"><figcaption>벨트·연령대·만료일 필터로 원하는 회원을 즉시 검색</figcaption></figure></div>

| 기능 | 설명 |
|---|---|
| 벨트·연령대·만료일 필터 | 원하는 조건으로 회원을 즉시 검색 |
| 원클릭 승급 | 회원 상세에서 버튼 한 번으로 다음 벨트 승급 |
| 횟수 조정 | 횟수제 회원의 잔여 횟수를 직접 가감 (사유 기록) |
| 메모 | 회원별 메모 작성 — 부상 이력, 개인 목표 등 |
| 운동 시작일·건강 정보 | 훈련 시작일, 건강 메모, 비상연락처 기록 |
| 만료 알림 발송 | 만료 임박 회원에게 카카오 알림톡으로 갱신 안내 |

<div align="left"><figure><img src=".gitbook/assets/회원상세.png" alt="회원 상세" width="563"><figcaption>회원 상세 — 프로필, 벨트 이력, 출석, 메모를 한 화면에서 관리</figcaption></figure></div>

→ 자세히 보기: [회원 관리](members/) · [회원 상세](members/detail.md) · [벨트 관리](members/belt-management.md)

---

## 정산 관리

### 1. 정산 대시보드

이번 달 매출과 도장 상태를 한 화면에서 확인합니다.

<div align="left"><figure><img src=".gitbook/assets/정산대시보드.png" alt="정산 대시보드" width="563"><figcaption>월 매출 추이, 환불률, 만료 임박 회원을 한눈에</figcaption></figure></div>

| 지표 | 내용 |
|---|---|
| 월 매출 추이 | 최근 6개월 순매출·총매출 그래프 |
| 환불률 | 환불 금액·건수·비율 |
| 만료 임박 회원 | 7일 이내 만료 예정 목록 |
| 이탈 회원 | 최근 30일 내 이탈 회원 수 |
| 출석 저조 회원 | 출석 3회 미만 회원 파악 — 이탈 사전 감지 |

### 2. 수납 관리

모든 결제 건을 날짜순으로 조회하고, 세무 자료로 바로 활용합니다.

<div align="left"><figure><img src=".gitbook/assets/정산 수납관리.png" alt="수납 관리" width="563"><figcaption>기간·상태별 결제 내역 조회 + Excel 내보내기</figcaption></figure></div>

| 기능 | 설명 |
|---|---|
| 기간별 조회 | 날짜 범위를 설정해 결제 내역 검색 |
| 상태 필터 | 계약 체결 / 결제 완료 / 환불 등 상태별 보기 |
| 결제 수단 수정 | 잘못 기록된 결제 수단 정정 |
| 결제 상세 | 회원명·회원권·결제일·출석 횟수·타임라인 확인 |
| 환불 처리 | 환불 금액·사유·처리일 기록 |
| Excel 내보내기 | XLSX 파일로 다운로드 (세무·회계 제출용) |

→ 자세히 보기: [정산](settlement.md)

---

## 승급식

출석 기준으로 승급 후보자를 **자동 추출**하고, 검토 후 **일괄 승급**합니다.\
더 이상 엑셀이나 수첩에 출석일수를 세지 않아도 됩니다.

<div align="left"><figure><img src=".gitbook/assets/승급식 관리.png" alt="승급식 관리" width="563"><figcaption>승급식 목록 — 회차별 상태, 대상 인원, 승급 현황을 한눈에</figcaption></figure></div>

```
승급식 생성 → 최소 출석일 설정 → 후보자 자동 추출 → 벨트 검토·조정 → 확정 → 일괄 승급
```

<div align="left"><figure><img src=".gitbook/assets/승급식 승급대상회원.png" alt="승급 대상 회원" width="563"><figcaption>마지막 승급일 기준 N일 출석한 회원을 자동 추출 — 목표 벨트 개별 조정 가능</figcaption></figure></div>

| 기능 | 설명 |
|---|---|
| 출석 기준 후보 추출 | "60일 이상 출석" 등 조건을 설정하면 대상자를 자동 선별 |
| 벨트 개별 조정 | 후보자별로 승급 벨트를 변경하거나 제외 가능 |
| 일괄 승급 실행 | 확정 후 한 번에 모든 후보자의 벨트를 업데이트 |
| 이전 기준 불러오기 | 지난 승급식 조건을 그대로 재사용 |

→ 자세히 보기: [승급식](ceremonies.md)

---

궁금한 점은 [카카오톡 채널](https://pf.kakao.com/_NnxmZX)로 문의해 주세요.
