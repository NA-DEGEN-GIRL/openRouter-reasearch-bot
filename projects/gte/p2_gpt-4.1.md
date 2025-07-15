### 변경사항 요약

- **기술 메커니즘 관련**  
  - ‘MegaETH’의 정의 및 현황(레이어1/레이어2 여부와 온체인 주문장 실제 구현) 부분에 불확실성이 있으므로, 공식 웹과 외부 기사 기반으로 “이전답변의 추정”을 명확히 구분하고, 기능적으로 증명된 부분만 채택함.
- **토크노믹스**  
  - 모든 리서치에서 공통적으로 ‘토큰 정보 미공개’임이 확인되어, 사업의 성장 단계상 확정 사안이 없음을 명확히 표기.
- **사용자 경험(참여 경로)**  
  - 웹사이트에서 실제 ‘테스트넷’ 또는 ‘거래 인터페이스’가 공개되어 있음을 공식 사이트 기준으로 바로 명시(이전 일부 답변은 투자전 랜딩페이지만 언급하였으나, 검색 결과 현재 서비스 체험 가능).
- **경쟁 프로젝트 및 시장 점유율**  
  - 하이퍼리퀴드(Hyperliquid) 등의 실거래량 및 시장 데이터의 정확성과 최신성을 유지하기 위해 필요한 부분만 인용.
- **용어 설명**  
  - 초보자 안내 전용 섹션을 분리하여, ‘DEX’, ‘오더북’ 등 반드시 필요한 핵심 용어는 간결·명료하게 설명.
- **디테일 및 FAQ 강점 추가**  
  - AI B의 디테일(예: 투자자의 ‘유형’, 커뮤니티 펀딩 라운드 정보), AI A의 현실적 예시 설명, 그리고 ‘거래자/에어드랍 참여’ 등 가능한 활동 경로를 통합 보강.

---

### GTE 프로젝트 마스터 팩트 시트  
(분석일: 2025년 07월 15일)

#### 1. 한눈에 보는 GTE

- **정의**  
  GTE는 ‘MegaETH’ 기반의 중앙화 거래소 수준 속도와 경험을 목표로 하는 탈중앙화 주문장(오더북) 거래소(Decentralized Orderbook Exchange, DEX) 프로젝트다. 사용자는 자산을 직접 지갑에서 관리하며, 낮은 지연 속도와 높은 투명성을 양립하고자 한다.  
  출처: [gte.xyz](https://www.gte.xyz/), [coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm),  
  기본 배경: [coincentral.com](https://coincentral.com/paradigm-backs-gte-with-15m-to-build-the-fastest-decentralized-exchange/)

#### 2. 왜 중요한가?  
- 기존 CEX(중앙화 거래소)는 사용 편의성과 속도는 높으나 자산을 맡겨야 하는 보안 위험이 있다. FTX 사태 등에서 보듯, 거래소가 파산하면 자산도 증발한다.  
- 기존 DEX(탈중앙화 거래소)는 보안성(자산 직접 관리)은 높으나 주문 처리 속도/사용성에서 크게 뒤쳐진다.  
- GTE는:  
  - ‘내 자산은 내가 통제(비커스터디얼)’  
  - ‘거래는 주식시장만큼 빠르고 편하게(온체인 CLOB, 중앙 지정가 주문서 구조)’  
  를 동시에 추구한다.
- 현실 예시: 간편 결제 앱에서 누구나 실시간 송금/거래를 기대하듯, 암호화폐도 온체인에서 “내가 직접 내 돈을 빠르게” 운용하고 싶은 요구.

#### 3. 기술 및 메커니즘
- **핵심 구조**  
  - MegaETH(메가이더리움)라는 전용 초고속 블록체인 인프라 위에 구축(이더리움과의 관계는 공식 사이트 기준 ‘독자체인’이 강점)  
  - 모든 주문 처리(입력~체결~정산)가 온체인에서 즉시 처리되도록 설계
  - 주문장(Central Limit Order Book, CLOB): 주식시장 등에서와 유사하게 거래 가격별 주문을 쌓고, 맞는 주문을 실시간 체결
  - 논커스터디얼: 사용자가 거래소에 자산을 맡기지 않고, 직접 자기 지갑(메타마스크 등) 연결로 거래
- **차별점**  
  - 기존 DEX 대비 속도(낮은 지연), 높은 확장성, 주문·체결·정산 전체의 투명성  
  - 기존 ‘AMM(자동화 마켓메이커)’ 기반 DEX(예: 유니스왑) 대비, 전문 트레이더에게 익숙한 오더북 방식  
  - **기술적으로 중요한 점:** 실제 모든 주문의 온체인 처리와 사용자 경험, 그리고 확장성의 동시 달성(이전 일부 온체인 오더북은 속도 저하/가스비 문제 등의 한계가 있음)
- **용어설명**  
  - *On-chain CLOB*: 거래창의 모든 주문을 블록체인에 기록·처리하는 방식. 주문이 투명하게 모두 기록되고 체결도 자동화
  - *Non-custodial*: 거래소가 고객 자산을 일시도 보관 안함, 거래 실행만 중계
  
#### 4. 토크노믹스(토큰 모델)
- (2025년 7월 기준) 공식 토큰은 런칭되지 않았으며, 토큰 이름·티커·분배 구조·거버넌스 정책 등 전혀 공개된 정보 없음.
- 업계 관례상, 추후 사용자·리워드·거버넌스용 토큰 도입은 유력(하이퍼리퀴드, dYdX 선례 참조)
- 공식 발표 전까지 투자/참여 시 투기성 루머에 주의

#### 5. 팀 및 투자자
- **핵심 인물**  
  - 공식 GitHub 등에서 구체적 팀원 명단은 미공개, 일부 투자자(예: Guy Young)는 이름이 외부 자료에 노출됨.
  - 팀 백그라운드는 트레이딩/블록체인 특화 개발자가 주축
- **비전**  
  - “탈중앙성과 ‘거래소만큼 빠른 UX’를 모두 만족하는 차세대 글로벌 인프라 구축”  
  - X(구 트위터) 공식채널서 “Speed+Trustless+Transparency”를 반복 강조  
- **주요 투자자**  
  - Tier 1: Paradigm(업계 TOP 벤처, $15M 단독 리드라운드)  
  - Tier 2: Robot Ventures, Wintermute(유동성 공급+VC 겸업),  
  - 기타: Flow Traders, IMC Trading 등 실제 마켓메이커 중심의 전략적 투자자 다수  
  - 펀딩 총액: $25,000,000+ (Pre-seed~SeriesA 포함), [rootdata.com](https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=), [theblock.co](https://www.theblock.co/post/335132/megaeth-based-dex-gte-funding-cobie-echo)

#### 6. 사용자 경험 및 커뮤니티
- **직접 사용 방법**  
  - gte.xyz 접속→지갑 연결→빠른 UI에서 직접 거래 테스트 가능(테스트넷 및 일부 메인넷 서비스 진행 중)  
- **에어드랍/보상 가능성**  
  - 아직 공식 발표는 없으나,  
    - 토큰 미상장 상태  
    - 커뮤니티 펀딩(초기 Echo 라운드) 이력  
    - Early DEX 사용자 대상 에어드랍이 크립토 업계 관례(하이퍼리퀴드, dYdX 등)  
    => ‘테스트넷·초기 거래·커뮤니티 활동 등’ 참여자는 잠재적 보상 기회 있음(단, 최종 정책 여부는 추후 확인 필요)
- **커뮤니티**  
  - X(트위터)에서 활발한 인게이지, 테스트넷 경험자 리뷰 다수(공식 X: [x.com/gte_xyz](https://x.com/gte_xyz))

#### 7. 시장 내 경쟁 구도 및 리스크
- **직접 경쟁자**:  
  - Hyperliquid (온체인 DEX 파생상품 시장 점유율 선두), dYdX(앱체인 기반),  
  - 기존 대형 DEX(AMM 기반): Uniswap 등
- **경쟁력**  
  - 하이퍼리퀴드와 달리 ‘완전 온체인 CLOB’를 추구하며, MegaETH 기반으로 더 낮은 지연/높은 탈중앙성 추구
  - Paradigm 등 대형 투자자 직·간접 참여로 신뢰도 높음
- **약점/리스크**  
  - MegaETH 기반 신규 체인 의존, 유동성 확보 초기 진입장벽  
  - 네트워크 이슈 혹은 메이저 CEX의 지속적 기술 혁신  
  - 합의(Consensus)/기술적 결함 드러나면 신뢰저하 가능  
  - 규제환경 변화, 토큰 미공개→기대 심리 불일치 시 커뮤니티 이탈 우려

#### 8. 용어 FAQ(초보자 전용)
- **DEX(탈중앙화 거래소)**: 중앙 서버/회사 없이, 블록체인에서 거래자가 직접 거래/자산통제. 보안은 높으나 전통적으로 느렸음 ([coinmarketcap.com](https://coinmarketcap.com/alexandria/article/what-are-decentralized-exchanges-dex), [openware.com](https://www.openware.com/news/articles/the-future-of-decentralized-exchanges-dexs), [blog.chainport.io](https://blog.chainport.io/what-are-dexs))
- **오더북(CLOB)**: 거래소 내 ‘가격표 게시판’에 여러 사람이 실시간으로 매수/매도 주문을 쌓고, 맞는 주문끼리 자동 체결되는 구조.
- **Non-custodial**: 거래소가 고객 자산을 잠시도 보관하지 않는 모델(사용자 지갑→직접 거래).
- **AMM**: 거래소에서 ‘알고리즘’을 통한 자동 유동성 공급/교환구조, 초보자에겐 편하지만 큰 주문엔 슬리피지 등 불리할 수 있음([binance academy](https://academy.binance.com/en/articles/what-is-a-decentralized-exchange-dex), [blog.chainport.io](https://blog.chainport.io/what-are-dexs))

---

**주요 참고**  
- 공식 웹: [gte.xyz](https://www.gte.xyz/)  
- 공식 X: [x.com/gte_xyz](https://x.com/gte_xyz)  
- 외부 투자/시장 기사: [coindesk.com](https://www.coindesk.com/business/2025/06/23/hyperliquid-rival-gte-raises-usd15m-in-series-a-led-by-paradigm), [coincentral.com](https://coincentral.com/paradigm-backs-gte-with-15m-to-build-the-fastest-decentralized-exchange/), [rootdata.com](https://www.rootdata.com/Projects/detail/GTE?k=MTQ4ODc=), [theblock.co](https://www.theblock.co/post/335132/megaeth-based-dex-gte-funding-cobie-echo)  
- DEX 구조/용어/기본: [coinmarketcap.com](https://coinmarketcap.com/alexandria/article/what-are-decentralized-exchanges-dex), [binance academy](https://academy.binance.com/en/articles/what-is-a-decentralized-exchange-dex), [openware.com](https://www.openware.com/news/articles/the-future-of-decentralized-exchanges-dexs), [blog.chainport.io](https://blog.chainport.io/what-are-dexs)