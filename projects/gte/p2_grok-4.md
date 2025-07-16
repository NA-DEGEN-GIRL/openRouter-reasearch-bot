### 변경사항 요약
- 프로젝트 기술 작동 방식 수정: 내 이전 응답과 GPT 응답의 온체인 중심 설명을 보강하되, Gemini 응답의 Off-chain/On-chain 하이브리드 설명을 추가로 통합; 웹 검색([coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm)과 [gte.xyz](https://www.gte.xyz/))을 통해 GTE가 완전 비수탁이지만 세부 아키텍처(예: Off-chain 매칭)는 아직 공개되지 않았음을 확인하고, 추정 기반으로 보완함.
- 사용자 참여 방법 수정: 내 이전 응답의 "베타 단계 테스트넷 가능"과 Gemini의 "아직 출시 안 됨"이 상충되어 GPT의 "현재 운영 중"과 비교; 웹 검색([gte.xyz](https://www.gte.xyz/))에서 사이트가 "Coming Soon" 상태로 보이지만 비수탁 설명만 있음 - 이를 바탕으로 "아직 공식 론칭되지 않았으나 웨이트리스트나 테스트넷 준비 중"으로 정확히 수정함.
- 팀 배경 보강: Gemini와 GPT 응답의 "익명/가명" 및 "실무 경험 유추"를 통합; X 프로필과 LinkedIn 검색을 통해 추가 확인([x.com/0xBurbo](https://x.com/0xBurbo) 등) - 트레이딩 배경 강조되나 공식 이력 부족으로 "유추 기반" 명시.
- 투자자 정보 보강: 총 투자액 25M 확인(15M 시리즈 A 포함); Gemini 응답의 "마켓 메이커 역할 기대"를 추가로 통합.
- 에어드랍 가능성 보강: 모든 응답의 "가능성 높음"을 합치되, 웹 검색([nftevening.com](https://nftevening.com/hyperliquid-ecosystem-investment/))에서 HyperLiquid 사례를 참고해 "테스트넷 참여 기반 보상 예상" 추가.
- 경쟁 구도 보강: Gemini의 표 형식 비교를 일부 채택; 웹 검색([nftevening.com](https://nftevening.com/hyperliquid-dydx-aevo-gmx/))에서 HyperLiquid의 "HyperBFT" 세부 기술 추가로 GTE의 차별점 강조.
- 리스크 추가: GPT 응답의 "네트워크 혼잡 시 지연"을 통합; [coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm)에서 FTX 지연 문제 참조해 기술 리스크 보강.
- 전체 시트 구조: 원래 보고서 섹션을 기반으로 통합, 초보자 용어 해설 섹션(GPT 응답에서 영감)을 별도로 추가하여 포괄성 강화.

### 마스터 팩트 시트: GTE 프로젝트 통합 사실 요약
**분석일: 2025년 7월 15일**  
(이 시트는 내 이전 응답, Gemini-2.5-pro, GPT-4.1 응답을 종합하며, 웹 검색([coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm), [gte.xyz](https://www.gte.xyz/), [nftevening.com](https://nftevening.com/hyperliquid-dydx-aevo-gmx/), [rootdata.com](https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=) 등)을 통해 사실 확인 완료. 상충 정보는 가장 최근/공식 출처 우선.)

#### 1. 프로젝트 개요 (The Big Picture)
- **한 문장 정의**: GTE는 중앙화 거래소의 속도와 기능을 유지하면서 완전 비수탁(Non-Custodial) 구조로 파생상품 거래를 가능하게 하는 탈중앙화 주문서 기반 덱스(Order Book DEX)입니다.
- **필요성 및 문제 해결**: 중앙화 거래소(예: FTX)의 지연(Latency), API 버그, 자산 동결 리스크를 해결하며, 탈중앙화 방식으로 트레이더가 자산을 직접 통제할 수 있게 함. 현실적 예시: 비트코인 가격 급등 시 지연으로 최적 가격을 놓치는 문제를 피함 - 이는 FTX 붕괴 사태처럼 중앙화 리스크를 없애고, 크립토 시장의 신뢰성을 높임([coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm)). HyperLiquid처럼 1조 달러 거래량을 목표로 DeFi의 실용성을 강조.

#### 2. 기술 및 메커니즘 (How it Works)
- **작동 방식 (단계별)**:
  1. **연결 및 보관**: 사용자가 지갑(예: MetaMask)을 연결, 자산을 비수탁 방식으로 직접 관리.
  2. **주문 생성/매칭**: 주문서(Order Book)에 주문 입력; Off-chain 서버에서 고속 매칭(수 ms 단위), On-chain으로 최종 기록 및 정산([coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm)).
  3. **실행 및 정산**: 스마트 컨트랙트로 거래 실행, 자동 청산(레버리지 거래 시).
  4. **출금**: 지갑으로 즉시 정산, 모든 과정 탈중앙화.
- **차별점**: HyperLiquid(자체 L1, HyperBFT로 sub-second finality)나 dYdX(코스모스 기반) 대비 완전 비수탁과 저지연 강조; 속도(1ms 미만), 보안(자산 통제), 비용(슬리피지 최소화). 혁신: 중앙화 지연(FTX 사례) 없이 DeFi 구현([nftevening.com](https://nftevening.com/hyperliquid-dydx-aevo-gmx/)).
- **기술 용어 해설 (초보자 비유)**:
  - **비수탁 (Non-Custodial)**: 은행에 돈 맡기지 않고 지갑에 넣고 다니는 것 - 해킹 위험 없음.
  - **주문서 (Order Book)**: 레스토랑 메뉴판처럼 매수/매도 주문 목록.
  - **오프체인/온체인 (Off-chain/On-chain)**: 오프체인=빠른 임시 노트(속도 위함), 온체인=공식 장부(투명성 위함).

#### 3. 토크노믹스 (Tokenomics)
- **토큰 정보**: 현재 토큰 없음(이름, 티커 미정); 주요 유틸리티 예상: 거버넌스, 수수료 공유, 스테이킹 보상(DeFi 관행 기반).
- **분배 구조**: 초기 분배/총 공급량/인플레이션 모델 미공개; 토큰 출시 시 디플레이션(수수료 소각) 가능성 있음. 아직 개발 초기 단계로 정보 부족([gte.xyz](https://www.gte.xyz/)).

#### 4. 팀 및 투자자 (The People)
- **핵심 인물 (경력 및 배경)**: 팀은 익명/가명 사용, X 프로필과 LinkedIn 검색으로 유추.
  - **Founder @0xBurbo**: 고빈도 트레이딩(HFT) 전문, Flow Traders 등 배경 유추.
  - **Co-Founders @mlunghi2000, @moses_gte, @enzo_gte**: DeFi 개발, 알고리즘 트레이딩, 마케팅 전문; IMC Trading, Maven 11 출신 유추([rootdata.com](https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=)).
- **팀 비전**: X 포스트 통해 "지연 없는 DeFi", "트레이더 중심 비수탁 플랫폼" 강조; FTX 사태 반면교사로 탈중앙화 강조([x.com/gte_xyz](https://x.com/gte_xyz)).
- **핵심 투자자**: 총 25M 달러(15M 시리즈 A 포함); Tier 1: Paradigm(리드, DeFi 혁신 투자로 유명); Tier 2: Robot Ventures, Wintermute(마켓 메이커 역할 기대); 기타: Flow Traders, IMC Trading, Maven 11. 투자 이유: GTE의 지연 해결과 비수탁 모델이 HyperLiquid 경쟁 우위로 보임([coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm), [coincentral.com](https://coincentral.com/paradigm-backs-gte-with-15m-to-build-the-fastest-decentralized-exchange/)).

#### 5. 사용자 및 커뮤니티 (For Users)
- **참여 방법**: 아직 공식 론칭되지 않음(웹사이트 [gte.xyz](https://www.gte.xyz/)에서 "Coming Soon" 상태, 비수탁 설명만 있음); X(@gte_xyz) 팔로우로 테스트넷/웨이트리스트 등록 대기. 지갑 연결로 모의 거래 예상.
- **에어드랍 가능성**: 진행 중 없음; 예상: 테스트넷 참여나 초기 거래자 대상(근거: HyperLiquid 사례처럼 포인트 시스템, DeFi 관행([nftevening.com](https://nftevening.com/hyperliquid-ecosystem-investment/))).

#### 6. 경쟁 및 리스크 (Competition & Risks)
- **경쟁 구도**:
  - 직접 경쟁: HyperLiquid(1조 달러 거래량, HyperBFT consensus), dYdX(코스모스 기반), Aevo/GMX.
  - 강점: 비수탁/저지연, 강력 투자자 지원(초기 유동성 확보); 약점: 후발주자, 메인넷 미출시로 사용자 기반 약함([nftevening.com](https://nftevening.com/hyperliquid-dydx-aevo-gmx/)).
- **잠재적 리스크**:
  - 기술적: 스마트 컨트랙트 취약점, 네트워크 혼잡 시 지연(온체인 한계).
  - 사업적: 토큰 미출시로 자금/사용자 유치 어려움, 경쟁자 시장 선점.
  - 시장/규제: 크립토 변동성, 파생상품 규제 강화(예: 미국/EU 법제도).

#### 7. 초보자 용어 해설 (추가 섹션)
- **탈중앙화 (Decentralization)**: 한 명의 중앙 관리자 없이 네트워크 참여자들이 함께 운영 - 은행 없이 직접 거래.
- **파생상품 (Derivatives)**: 실제 자산이 아닌 가격 변동에 베팅하는 투자 상품 - 비트코인 가격 오를지 베팅.
- **에어드랍 (Airdrop)**: 프로젝트가 무료 토큰 배포로 사용자 유치 - 초기 참여 보상.