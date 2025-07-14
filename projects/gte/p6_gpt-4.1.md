```json
{
  "projectName": "GTE (Generalized Trade Engine)",
  "oneLiner": "온체인 오더북 DEX 인프라로, 모든 금융상품(현물, 선물, 옵션 등) 거래를 고성능으로 지원하는 범용 엔진 플랫폼. A highly flexible and generalized decentralized trading infrastructure designed to support any type of asset or financial product.",
  "tags": [
    "DeFi",
    "DEX",
    "OrderBook DEX",
    "Infrastructure",
    "Generalized Engine",
    "On-chain Infra"
  ],
  "overview": {
    "summary": "GTE(Generalized Trade Engine)는 온체인의 오더북 인프라(DEX infra)로, 현물, 선물, 옵션 등 다양한 자산을 단일 엔진에서 거래할 수 있도록 설계된 “범용 엔진” 기반 플랫폼임. GTE is a decentralized trading infrastructure that aims to solve the fragmentation of the DeFi market by providing a universal, high-performance engine. This engine allows developers to create and launch any kind of financial market (spot, futures, options, etc.) on a single, unified platform, combining the performance of centralized exchanges with the security of blockchain.",
    "details": "GTE는 기존 DeFi 시장의 파편화(상품마다 별도 DEX 및 운영 인프라 필요)와 낮은 자본 효율, 업무 중복의 비효율성 문제를 해결하기 위해 개발되고 있다. 개발자는 하나의 코어 엔진 위에서 다양한 거래 규칙(현물, 선물, 옵션, 예측시장, 신형 상품 등)을 직접 정의 및 적용할 수 있다. 이를 통해 DeFi에서 트레이더, 개발자, 기관이 마치 금융 운영체제처럼 다양한 자산을 통합적으로 거래할 수 있도록 한다. 사용자 측면에서는 지정가, 시장가 등 다양한 거래방식, 효율성, 신뢰성, 탈중앙화 구현을 기대한다. However, a critical view suggests this 'do-everything' approach is a strategic flaw. The project risks becoming a 'Jack of all trades, master of none,' unable to compete with specialized protocols that are highly optimized for a single function. The argument is that this 'one-size-fits-all' model has historically failed in DeFi, as communities prefer dedicated, best-in-class solutions over a mediocre universal platform. 실사용·체험 가능한 테스트넷, 알파/베타 제품, 코드 공개 등은 2024년 6월 기준 미출시이며, 진짜 ‘혁신’ 실체에 대해 내부/외부 모두 검증된 바는 없다."
  },
  "strengths": [
    {
      "point": "범용성 및 강력한 유연성",
      "details": "GTE는 하나의 범용 오더북 엔진에서 현물/선물/옵션 등 다양한 금융상품의 거래 규칙을 개발자가 직접 프로그래밍해서 구축 가능. Unlike competitors focused on specific products like perpetuals, GTE's core innovation is its 'Generalized Engine.' This allows developers to define their own trading rules (State Transition Functions), enabling the creation of markets for spot, futures, options, RWAs, and even yet-to-be-invented financial instruments on the same infrastructure. This dramatically reduces development time and cost for new financial products. 잠재적으로 기존 DEX의 파편화 문제를 근본적으로 해소할 수 있음."
    },
    {
      "point": "고성능 트레이딩 인프라 제공 목표",
      "details": "오프체인 주문 매칭 엔진과 온체인 자산 결제 구조를 통해 신속한 체결과 투명한 체인 확인을 결합하려 함. A hybrid model utilizing a high-performance off-chain matching engine for speed and on-chain settlement for security and finality. 이론적으로 중앙화 거래소(CEX)급 속도와 DeFi의 탈중앙성을 융합."
    },
    {
      "point": "강력한 투자사와 팀(Top-Tier Team and Strategic Investors)",
      "details": "Paradigm(최상급 인프라 VC)을 비롯, Wintermute, Robot Ventures, Flow Traders, IMC 등 시장조성자·트레이딩 대기업이 투자. The founding team consists of high-caliber engineers from elite High-Frequency Trading (HFT) firms like Jump Trading, Wintermute, and DRW. The project is backed by a $25M investment led by Paradigm, one of the most respected VCs in crypto, known for backing foundational projects like Uniswap and Blur. Strategic investors also include major market makers like Wintermute, Flow Traders, and IMC Trading, who are not just financial backers but also potential core users and initial liquidity providers, mitigating the cold-start problem."
    },
    {
      "point": "크로스마진, API 제공 등 개발자 및 기관 친화형 / Potential for Superior Capital Efficiency",
      "details": "Integrated cross-margining allows users to use a single pool of collateral (e.g., USDC in one account) to trade across all different markets built on GTE (spot, perps, options). This maximizes capital efficiency, a highly attractive feature for professional traders and institutions. 다양한 상품을 하나의 계정·자산 기반 위에서 크로스마진 처리, 개발자가 쉽게 맞춤형 마켓·상품을 론칭할 수 있도록 SDK/API를 제공한다."
    }
  ],
  "weaknesses_and_risks": [
    {
      "point": "'Generalized' as a Marketing Gimmick & Performance Sacrifice",
      "details": "The core concept of a 'Generalized Engine' is criticized as a marketing term for a 'master of none' system. In the high-performance trading world, a slightly slower but more flexible system has little value. Competitors who focus on optimizing a single product will likely always outperform GTE on speed and efficiency for that specific product, making GTE unattractive to serious traders. 기술 자체에 대해 기존 거래소(예: dYdX, Aevo, CEX 등)에서 이미 상용화된 기술의 재포장 혹은 조합에 불과하다는 비판이 많고, 실제 작동하는 MVP, 벤치마크, 퍼포먼스 수치 등은 세상에 공개된 적 없음."
    },
    {
      "point": "코어 기술/제품 실체 없음 및 Vaporware Risk",
      "details": "Despite the funding announcement, there is no public product, demo, or even a detailed technical paper. The project exists only as a vision, raising significant 'vaporware' risk. GTE는 2024년 6월 기준 테스트넷/데모/공개된 깃허브/오픈 소스 코드가 존재하지 않고, 실사용자 검증 혹은 외부 평가 불가. 모두 '곧 출시 예정', '핵심 기술 발표'만 반복. There is a high risk that the project's ambition remains unfulfilled and never materializes."
    },
    {
      "point": "Opaque, VC-Centric Tokenomics & 'Insider Exit' Scenario",
      "details": "The complete lack of public tokenomics is a major red flag. The $25M investment strongly implies that a huge portion of the token supply is allocated to insiders. This creates a high risk of the token being used as an exit vehicle for VCs, with massive sell pressure upon launch. 토큰 구조, 분배(팀/VC/커뮤니티 비중), 락업 및 인플레이션/디플레이션 메커니즘, 실제 유틸리티 등은 일절 비공개. 과거 DeFi 프로젝트에서 반복된 덤핑, 단기 투기 유도 패턴 재현 위험."
    },
    {
      "point": "Team's Mismatched Experience & Lack of Execution Proof",
      "details": "The team's HFT background is not directly transferable to building secure, decentralized, open-source protocols. HFT operates in closed, trusted environments, whereas DeFi requires expertise in adversarial public environments, smart contract security, and community-driven governance. The team has zero track record of successfully launching and scaling a DeFi protocol from scratch. Their closed development style, with no public code or active community engagement, further undermines confidence in their ability to execute. GTE 팀의 온체인 프로토콜 구축·운영 실전 역량 미증명."
    },
    {
      "point": "High 'Vaporware' Risk & Saturated Market",
      "details": "GTE is a latecomer to the hyper-competitive Order Book DEX market, which is already dominated by established players like dYdX and Hyperliquid. GTE lacks a compelling, proven advantage to capture market share from these incumbents. 오더북 DEX 시장은 dYdX, Hyperliquid, Aevo 등 강력한 선점자와 TVL·거래량·커뮤니티 파워에서 앞선 경쟁자가 즐비하며, GTE만의 독자적 강점/이미 유저 기반 유치 등 객관적 성과 전무. 시장 내 진입 장벽·취약 포지셔닝."
    },
    {
      "point": "커뮤니티 및 실사용자 기반 약화와 투기 중심",
      "details": "공식 X, 디스코드 등 소셜 채널의 활성도/상호작용 낮음. 커뮤니티 활동은 공개개발 부재와 에어드랍 기대감에 의존, 사용자의 장기 생태계를 견인할 긍정적 동력이 부족."
    },
    {
      "point": "Governance & Centralization Risk",
      "details": "The off-chain matching engine will initially be a centralized point of failure and control. The heavy VC investment suggests that governance, if/when implemented, will likely be dominated by a small number of large stakeholders, undermining the principle of decentralization. GTE가 내세운 오프체인 매칭 엔진은 본질적으로 '검열 가능·중앙화된 단일 실패점'이라는 잠재적 위험 요소를 가진다."
    },
    {
      "point": "Regulatory/Network/Technical Risk",
      "details": "Order book DEXs are under increasing scrutiny from global regulators (e.g., the SEC and CFTC). These platforms can be deemed unregistered securities exchanges, posing a significant legal and operational threat to the project, its team, and its token holders. 네트워크(예: Solana, Ethereum L2 등) 자체 기술 사고, 거래 중단, 해킹 등 외부 위협에도 취약."
    }
  ],
  "technology": {
    "coreConcept": "A hybrid model utilizing a high-performance off-chain matching engine for speed and on-chain settlement for security and finality. The core innovation is that this engine is 'generalized,' meaning it is not hardcoded for any specific financial product. 오더북(주문장) 기반 온체인 인프라와 오프체인 매칭 하이브리드 구조에서, 개발자가 직접 금융상품의 거래 논리와 룰을 정의하고 론칭할 수 있도록 하는 SDK/API 등 범용 엔진 플랫폼.",
    "keyFeatures": [
      {
        "name": "Generalized Engine/Generalized Orderbook Engine",
        "description": "An engine that is not tied to any specific trading logic. Developers can define their own rules for how state should transition, allowing for the creation of any type of market. 각기 다른 금융상품(현물/선물/옵션/예측시장/B2B 등)의 거래 규칙을 개발자가 직접 올릴 수 있는 주문장 매칭 및 상태 전이 프레임워크 제공.",
        "details": "This provides ultimate flexibility and speeds up innovation. Instead of building a trading system from scratch, developers can simply deploy their unique market logic on top of GTE's proven infrastructure. The critical view is that this is an idealistic architectural choice that ignores market demands for performance. This flexibility inherently introduces complexity and abstraction layers that will likely make it slower and less efficient than specialized, optimized competitors. 타 프로젝트 대비 강한 범용성·확장성 어필, 실제 구현/실체 미공개라는 의구심 혼재."
      },
      {
        "name": "Off-chain Matching & On-chain Settlement / 하이브리드 매칭 모델",
        "description": "User orders are matched at high speed in an off-chain system without incurring gas fees. The final results of settled trades are then batched and recorded on-chain, ensuring trustless ownership transfer. 주문 체결(매칭)은 오프체인 고속 엔진에서, 자산 이전(결제)은 이더리움 L2 등 온체인 컨트랙트에서 처리.",
        "details": "This model aims for the best of both worlds: CEX-level performance and DEX-level security. However, the off-chain component is simply a centralized server controlled by the GTE team, reintroducing risks of censorship, downtime, and data manipulation. The promise of future decentralization is a common, often unfulfilled, trope in DeFi. 속도·수수료 효율 추구, 그러나 중앙화·조작 가능성·보안/신뢰성 문제 상존."
      },
      {
        "name": "Integrated Cross-Margin (Potential)",
        "description": "A potential feature stemming from the generalized architecture, allowing users to collateralize and trade across all GTE-based markets from a single account. 하나의 계정/자산으로 현물, 파생 등 모든 상품에서 크로스마진 전략, 개발자에게 맞춤형 개발 API/SDK 제공.",
        "details": "This would be a powerful feature for professional traders, greatly enhancing capital efficiency. However, this feature is still hypothetical and its secure implementation across diverse, user-defined markets presents a significant technical challenge. 실제 구현범위·성능·보안성은 미확정."
      },
      {
        "name": "기술 용어 해설",
        "description": "초보자 이해를 위한 비유",
        "details": "- Order Book: 매매 주문 목록 (카페 메뉴판 비유). - Slippage: 가격 변동 손실 (슈퍼마켓 대기열 가격 상승 비유). - MEV: 거래 순서 조작 이득 (블록 생성자 부당 이득). - Generalized Engine: 특정 상품 아닌 범용 거래 엔진 (레고 블록 비유)."
      }
    ]
  },
  "tokenomics": {
    "tokenName": null,
    "tokenTicker": null,
    "utility": null,
    "details": "2024년 6월 기준 공식 토큰(GTE 등) 발행 및 분배구조, 유통량, 락업, 거버넌스 정보 일절 미공개. 업계 관행상 거래 수수료 할당, 유동성·거버넌스 인센티브, 보상/스테이킹 등 예측 가능, 그러나 실제 유틸리티/분배 구조/중장기 가치 유지 모델 모두 검증 불가. The complete lack of public tokenomics is a major red flag. It suggests that the tokenomics may be heavily skewed towards the team and VCs. The lack of a clear value accrual model beyond generic 'governance' and 'fee sharing' raises serious doubts about the token's long-term sustainability. The token risks being primarily a tool for short-term airdrop hype and an exit liquidity vehicle for early investors."
  },
  "team": [
    {
      "name": "Zane Huffman",
      "role": "Co-founder",
      "background": "Wintermute(Head of DeFi, 글로벌 마켓메이커), Jump Trading 소프트웨어 엔지니어 경험. Former Head of DeFi at Wintermute, Software Engineer at Jump Trading.",
      "details": "His background provides deep expertise in both DeFi and institutional-grade HFT. The critical view is that this experience, while impressive, is in market operations and centralized systems, which is fundamentally different from building and securing a decentralized, open-source protocol in an adversarial environment. 고빈도 트레이딩·시장조성·TradFi 도메인의 고급 경력 보유, 다만 온체인 프로토콜 구축, 커뮤니티 운영, Web3 실전 DAO 설계 등 직접적 성공 경험/오픈소스 투명성은 입증되지 않았음."
    },
    {
      "name": "Konrad Kopp",
      "role": "Co-founder",
      "background": "DRW, D1 등 글로벌 HFT·헤지펀드 경력. Former roles at DRW/Cumulus and D1.",
      "details": "His background is also in elite, traditional trading and investment firms. The critical view is the same: the team lacks proven experience in building successful DeFi protocols from the ground up, and their closed, non-transparent development culture is antithetical to the ethos of Web3. 중화화 대형 트레이딩 인프라(속도/최적화) 역량 강점, 그러나 대규모 Web3 커뮤니티 관리, 블록체인/스마트컨트랙트 보안 실적은 미확인."
    },
    {
      "name": "기타(Flow Traders, IMC Trading, Max Resnick, Guy Young 등)",
      "role": "자문/투자자/커뮤니티 파트너 추정",
      "background": "IMC Trading, Flow Traders 등 글로벌 트레이딩 기업, Solana 개발자, TradFi-크립토 다수",
      "details": "실무 기여/개발진은 준익명 수준. 공식 깃허브, 블로그, SDK 문서 등 실명 기반 팀 정보 및 생태계 빌더 확보 여부 불확실."
    }
  ],
  "investors": [
    {
      "name": "Paradigm",
      "type": "VC",
      "tier": "Tier 1",
      "description": "Lead investor in the $25M funding round. Known for backing foundational and technically ambitious crypto projects. Paradigm's involvement provides immense credibility and signals strong belief in GTE's long-term vision. The critical view is that this large investment creates a dynamic where the project's primary goal becomes generating a return for VCs, potentially at the expense of the community. Paradigm's backing creates huge hype but also immense pressure, and their portfolio projects often have token distributions that heavily favor insiders.",
      "details": "공식 투자자, 기술 인프라/탈중앙화 지향 포트폴리오 지향. 시장 내 신뢰도는 높으나, 내부자 우위 구조 논란도 다수."
    },
    {
      "name": "Wintermute",
      "type": "VC/Corporate",
      "tier": "Tier 2",
      "description": "A leading global algorithmic trading firm and crypto market maker. This is a strategic investment. Wintermute is not just a fund, but a potential day-one power user and liquidity provider for GTE, which is a significant advantage. The critical view is that their involvement further centralizes the project around a few powerful entities.",
      "details": "유동성, 마켓메이킹 전략 투자 성격. 실제 시장조성자(주요 고객/생태계 활용자)로서 역할 기대."
    },
    {
      "name": "Robot Ventures",
      "type": "VC",
      "tier": "Tier 2",
      "description": "A crypto-focused venture capital firm. Adds to the roster of crypto-native investors, strengthening the project's network within the industry.",
      "details": ""
    },
    {
      "name": "Flow Traders",
      "type": "Corporate/VC",
      "tier": "기타",
      "description": "A leading global financial technology-enabled liquidity provider in financial products. 트레이딩 및 DeFi 전문 VC. 유럽 기반 기관 투자자, 초대형 시장조성/마켓메이커. 전통 재무·마켓메이킹-크립토간 브릿지",
      "details": ""
    },
    {
      "name": "IMC Trading",
      "type": "Corporate/VC",
      "tier": "기타",
      "description": "A proprietary trading firm and market maker for various financial instruments. Further strengthens the roster of strategic trading firm investors, crucial for a project building a high-performance exchange.",
      "details": ""
    },
    {
      "name": "Maven 11",
      "type": "VC",
      "tier": "기타",
      "description": "DeFi 전문 VC",
      "details": ""
    },
    {
      "name": "Max Resnick",
      "type": "Angel/개인/커뮤니티",
      "tier": "기타",
      "description": "Solana 및 크립토 커뮤니티 인플루언서/개발자 추정",
      "details": ""
    },
    {
      "name": "Guy Young",
      "type": "Angel/개인/자문",
      "tier": "기타",
      "description": "IMC Trading 출신/자문/커뮤니티 리더 추정",
      "details": ""
    }
  ],
  "userActions": {
    "currentActivities": "The only official way for users to participate at present is by visiting the official website (https://www.gte.xyz/) and registering for the Private Alpha waitlist. There are no active point systems or testnets available to the public. 공식 웹/대기자 명단(이메일, 지갑 주소 등록), 테스트베드/베타 론칭 전. 지금은 커뮤니티 이벤트, 트위터/디스코드 참여, waitlist 등록, 커뮤니티 활동 포인트 적립 등 외에는 실 사용 불가.",
    "airdropPotential": {
      "status": "High",
      "reasoning": "The combination of being a high-profile, venture-backed project without a token, plus the precedent set by other Paradigm-backed projects and competitors, makes a future airdrop highly likely as a go-to-market and community-building strategy. Paradigm 등 VC 주도 대형 프로젝트에서 일반적으로 초기 커뮤니티·테스터 대상 토큰 에어드랍이 진행된 선례 다수이고, waitlist/포인트제 운용, 공식 유저 리워드 언급 빈도 높음.",
      "details": "An airdrop would be used to bootstrap an initial user base and decentralize governance. However, the critical perspective is that airdrops primarily attract mercenary 'farmers' who will dump the token immediately after receiving it, causing massive sell pressure and harming long-term community health. The airdrop can be seen as a marketing gimmick to create temporary hype rather than a genuine distribution of value. 실제 토큰 론칭이 이루어지면 커뮤니티 초기 참여자(베타 테스터, 포인트 적립자, 커뮤니티 활동자) 등에 대규모 에어드랍 가능성 높음."
    }
  },
  "competitors": [
    {
      "name": "dYdX",
      "differentiation": "시장 선점·성능·유동성·TVL, 온체인 오더북 구조 완성, 탈중앙화 커뮤니티 및 DAO 구축 성과. dYdX is a powerful but specialized order book DEX, currently focused on perpetuals and running on its own Cosmos-based app-chain. GTE's claimed differentiation is its 'generality,' allowing it to support a much wider array of assets beyond just perps.",
      "details": "dYdX has a massive head start with a proven product, significant trading volume, and a strong brand. GTE, as a latecomer, faces the immense challenge of luring away established users and liquidity. dYdX, Hyperliquid, Aevo 등 이미 여러 측면에서 우위. GTE만의 독자적 강점/이미 유저 기반 유치 등 객관적 성과 전무. 시장 내 진입 장벽·취약 포지셔닝."
    },
    {
      "name": "Hyperliquid",
      "differentiation": "자체 L1, 초고속 처리·저비용 환경 제공. 무기한 선물시장 등에 특화. Hyperliquid is another specialized, high-performance L1 for perpetuals trading, known for its extremely fast transaction speeds. GTE aims to offer similar performance but with the flexibility to support other asset types.",
      "details": "Hyperliquid has proven its performance capabilities in a live environment. GTE's performance is, as of now, purely theoretical. It must not only match Hyperliquid's speed but also convince the market that its 'generality' is a feature worth switching for, which is a difficult proposition. 실사용성과 거래량에서 2024년 기준 월등."
    },
    {
      "name": "Aevo",
      "differentiation": "옵션·파생상품 DEX, 자체 L2, 트레이딩 친화형 플랫폼. Aevo is an L2 focused on options and perpetuals, combining an off-chain order book with on-chain settlement. GTE proposes a similar hybrid model but with a broader, more generalized scope for developers.",
      "details": "Aevo has already carved out a strong niche, especially in the pre-launch futures market. GTE will be competing directly for the same pool of sophisticated traders and developers."
    },
    {
      "name": "Vertex",
      "differentiation": "온체인 오더북 기반 파생시장, 하이브리드 구조. 고성능·거래 UI/UX 장점, GTE가 지향하는 포지션과 일부 유사.",
      "details": "고성능·거래 UI/UX 장점, GTE가 지향하는 포지션과 일부 유사."
    }
  ],
  "risks": [
    {
      "type": "기술/제품 실체 부재",
      "description": "Vaporware(실체 없는 공약), 테스트넷/코드 미공개, 실 기능 미증명. Technical Risk: Implementation and Security of a 'Generalized' System",
      "details": "‘Generalized Engine’ 및 핵심 오더북 구조가 백서/블로그/마케팅 이상으로 실 현장적 테스트베드, 코드 등 전혀 외부에 오픈되지 않음. 퍼포먼스, 보안, 투자자 검증 불가. The vision for a universal engine is technically complex. Ensuring its stability and security, especially when allowing third-party developers to define arbitrary trading rules, is a monumental challenge. A single flaw in the core engine could have catastrophic consequences across all markets built on top of it."
    },
    {
      "type": "토크노믹스/가치분배 구조 실패 리스크",
      "description": "토큰 정보 비공개, 내부자(팀/VC) 이익 집중 구조, 단기 투기화 위험. Opaque, VC-centric tokenomics and the risk of 'Insider Exit.'",
      "details": "에어드랍, 분배, 락업, 실제 커뮤니티 지분 등 비공개. VC 펀딩 DeFi DEX서 종종 반복되는 펌프·덤프, 시장 하락시 토큰 가치 급락, 사용자 신뢰 붕괴 등 사례가 존재. The lack of a clear value accrual model beyond generic 'governance' and 'fee sharing' raises serious doubts about the token's long-term sustainability."
    },
    {
      "type": "팀 역량/책임성 부족",
      "description": "온체인 인프라 구축 실적 부족, 오픈 개발·커뮤니티 투명성 결여. Team's mismatched experience and lack of execution proof.",
      "details": "HFT·TradFi 경험은 충분하나 Web3 특유의 공개적 거버넌스, 코드 감사, 커뮤니티 빌딩 역량 검증 불가. 실명공개도 일부 외 투명성 결여. HFT operates in closed, trusted environments, whereas DeFi requires expertise in adversarial public environments, smart contract security, and community-driven governance."
    },
    {
      "type": "시장 경쟁 과열 및 후발주자 불리",
      "description": "강력 선점자多, 차별성 부족, 유동성·커뮤니티 기반 열세. Market Risk: Cold Start Problem in a Saturated Market.",
      "details": "dYdX·Hyperliquid 등 이미 여러 측면에서 우위. GTE만의 독자적 강점/이미 유저 기반 유치 등 객관적 성과 전무. 시장 내 진입 장벽·취약 포지셔닝."
    },
    {
      "type": "커뮤니티/사용자 기반 약화",
      "description": "소셜·대화형 생태계, 진정한 DAO·빌더생태계 형성 실패 가능성. 활동성 부족, 투기 유도, 단타성 유저 위주.",
      "details": "공식 채널 상호작용 낮고, 핵심 유저·생태계 지지 기반 미약. 대규모 PoS·에어드랍만으로는 장기 경쟁 불리. 커뮤니티 활동은 공개개발 부재와 에어드랍 기대감에 의존, 사용자의 장기 생태계를 견인할 긍정적 동력이 부족."
    },
    {
      "type": "Governance & Centralization Risk",
      "description": "The off-chain matching engine will initially be a centralized point of failure and control.",
      "details": "The heavy VC investment suggests that governance, if/when implemented, will likely be dominated by a small number of large stakeholders, undermining the principle of decentralization. GTE가 내세운 오프체인 매칭 엔진은 본질적으로 '검열 가능·중앙화된 단일 실패점'이라는 잠재적 위험 요소를 가진다."
    },
    {
      "type": "Regulatory/Network/Technical Risk",
      "description": "Order book DEXs are under increasing scrutiny from global regulators (e.g., the SEC and CFTC). These platforms can be deemed unregistered securities exchanges, posing a significant legal and operational threat to the project, its team, and its token holders.",
      "details": "주문장 DEX는 글로벌 규제 타깃. 거래·자산보관 인프라·네트워크 다운 및 외부 해킹사고 등에 취약. 네트워크(예: Solana, Ethereum L2 등) 자체 기술 사고, 거래 중단, 해킹 등 외부 위협에도 취약."
    }
  ],
  "totalFunding": "$25,000,000",
  "roadmap": "2024년 메인넷 출시 예정, 크로스체인 확장 계획 (웹사이트/X 확인); Points Program으로 사용자 참여 유도 중."
}
```