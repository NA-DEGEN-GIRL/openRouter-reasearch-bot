```json
{
  "projectName": "GEODNET",
  "oneLiner": "GEODNET은 전 세계에 소형 GNSS(위성항법) 노드를 설치, 블록체인 기반 분산 네트워크로 연결해, 누구나 이용 가능한 센티미터(cm)급 초정밀, 실시간 위치·환경 데이터를 제공하는 탈중앙화 물리 인프라 네트워크(DePIN)이다.",
  "tags": [
    "IOT",
    "DePIN",
    "GNSS",
    "RTK",
    "블록체인"
  ],
  "overview": {
    "summary": "GEODNET은 글로벌 커뮤니티가 운영하는 저가 GNSS(위성항법) 노드 네트워크를 통해, 기존 중앙집중·고비용 GPS/RTK 서비스의 한계를 혁신적으로 극복하여, 자율주행, 드론, 정밀 농업, 스마트 시티, AR/VR 등 미래 산업 전반에 필수적인 초정밀 위치정보와 환경 관측 데이터를 제공하는 DePIN 프로젝트다.",
    "details": "기존의 초정밀 RTK 위치 서비스 시장은 Trimble, Leica 등 소수 대기업이 독점적으로 고가, 폐쇄 구조로 운용해왔으며, 이로 인해 산업 현장의 실시간 위치정확도(수미터~수십 미터 오차), 데이터 접근성, 글로벌 커버리지, 확장 속도에 치명적인 한계를 가지고 있었다. GEODNET은 누구나 수백 달러의 GNSS 마이너(수신기)를 설치함으로써 네트워크 인프라의 일부가 되고, 이 과정을 블록체인상에서 검증·투명하게 운영한다. 사용자는 데이터 공급에 실시간으로 토큰($GEOD) 보상을 받고, 개발자나 기업은 API를 통해 합리적인 비용으로 cm급 정확도 보정 데이터를 구독해 자율주행, 드론 ‘딜리버리’, 정밀농기계, 측량, 로보틱스, AR 등 다양한 산업군에서 직접 활용 가능하다. 글로벌 6,600여 기준국(2024년 6~7월 기준)이 140여 국에 분포하며, 참여-증명(Proof-of-Contribution)과 데이터 검증-투명성-거버넌스 구조 등 DePIN의 본질을 실질적으로 구현하고 있다. 결과적으로, 위치 데이터와 관측 인프라의 민주화, 비용 혁신, 실생활 산업 채택 가속화를 노린다."
  },
  "technology": {
    "coreConcept": "GEODNET은 개방형 GNSS 노드(마이너)를 통한 실시간 고정밀 위성 신호 수집 및 보정(RTK)을 Polygon 블록체인 기반 분산 네트워크 상에서, PoL(Proof-of-Location), 다수 노드 교차 검증 및 Reputation 시스템 등 혁신적 검증 메커니즘으로 데이터 신뢰성과 투명성을 확보하며, 데이터 소비자는 토큰 소각 모델로 초정밀 데이터를 쉽게 활용할 수 있게 해주는 DePIN 구조의 IoT 인프라이다.",
    "blockchain": "폴리곤(Polygon) 메인넷 기반 스마트컨트랙트, ERC-20 토큰",
    "keyFeatures": [
      {
        "name": "노드 참여/마이닝",
        "description": "누구나 공식 인증 GNSS(위성 수신기) 하드웨어를 구매(약 $300~$700)하여 옥상, 옥외 등 네트워크에 설치하고 데이터를 실시간으로 송신하며, 기여도에 따라 실시간 $GEOD 토큰을 보상받는 구조.",
        "details": "노드는 GPS/Galileo/GLONASS 등 다양한 GNSS 위성 신호를 수집하며, 대기 환경/위성 신호오차 등을 계산해 '보정 데이터'를 생성, 이를 검증 및 브로드캐스트함. 추가적으로, 운영 안정성, 업타임, 데이터 연속성 등도 평판 알고리즘에 반영되어 보상이 산정된다."
      },
      {
        "name": "검증 메커니즘 (Validation Mechanism)",
        "description": "멀티노드 교차 검증(Proof-of-Location, truth validation), 평판 기반 보상 시스템",
        "details": "여러 노드가 공간적·시간적으로 제공하는 데이터의 일관성과 품질, 주변 노드와 교차 분석을 통해 신뢰도를 평가. 거짓 데이터·오프라인 노드 등의 악의적 행위는 배제된다. 전체 데이터 흐름은 블록체인에 투명하게 기록."
      },
      {
        "name": "데이터 소비/RTK API",
        "description": "개발자·기업이 API 혹은 구독 서비스를 통해 실시간 RTK 보정 데이터 및 위치·환경센서 데이터를 사용할 수 있음.",
        "details": "자율주행, 드론, 농업, 로보틱스, 스마트건설, AR/VR, 측량 등 다양하고 실제 산업 현장에서 직접 접속·활용가능. 기존 RTK 서비스 대비 10~100배 낮은 가격, 탈중앙 오픈API이므로 누구나 쉽게 접근 가능."
      },
      {
        "name": "블록체인 기반 인센티브·투명성",
        "description": "Polygon 메인넷 기반 온체인 기록·보상·데이터 추적",
        "details": "데이터 생성-검증-보상-소각의 모든 플로우는 스마트컨트랙트에 의해 자동 기록·관리되어, 데이터 신뢰성, 토큰 유통, 거버넌스 내역이 완전 투명하게 구현된다."
      },
      {
        "name": "차별화/혁신 포인트",
        "description": "DePIN 구조, PoL/평판 시스템, 글로벌 대규모 운영, 실시간 RTK 특화, 비용 혁신",
        "details": "1. 중앙화 RTK(Trimble 등)와 달리 대기업 독점이 아닌 커뮤니티 중심 분산 인프라.\n2. 데이터 품질 및 신뢰도 검증, 실사용에 의한 토큰 소각, 네트워크 빠른 확장.\n3. Hivemapper, Helium 등 타 DePIN과도 실질적 기술·산업 적용 범위·정밀성 차별화."
      },
      {
        "name": "기술 용어 해설",
        "description": "GNSS/RTK 등 개념을 초심자 관점에서 실제 비유로 설명",
        "details": "GNSS: 하늘에서 보내는 여러 위성 신호를 종합해 자신의 위치를 아주 정확하게 '삼각측량'하는 시스템으로, 스마트폰 GPS의 고도화판. RTK: 평범한 GPS는 대충 '이 거리 어디쯤'이라면, RTK는 '10cm 옆 의자'까지 집어낼 수 있는, 고정밀 실시간 보정 기술. PoL(Proof-of-Location): 노드가 자신의 실제 물리 좌표에서 데이터를 발생시켰음을, 다수 노드의 관찰 데이터를 비교해 신뢰성 있게 증명·합의하는 방식. DePIN: '중앙 회사'(Uber)가 아닌, 수많은 개인이 직접 인프라를 구축·공유·보상받는 모델."
      }
    ]
  },
  "tokenomics": {
    "tokenName": "GEODNET Token",
    "tokenTicker": "GEOD",
    "utility": "노드(마이너) 보상, 실시간 데이터/API 이용료(결제 및 Burn-to-Access형 소각), 커뮤니티 거버넌스(예정), 거버넌스 투표, 생태계 확장.",
    "details": "총 발행량은 10억 개(1,000,000,000 GEOD)로 고정(인플레이션 없음). 공식 분배 구조: 채굴/커뮤니티 보상 약 40~60%, 재단/Foundation 15~20%, 팀/창업/어드바이저 15~25%(2~4년 vesting), 투자자 시드/프라이빗 10~20%, 에코시스템/마케팅/기타 5~10% 등(출처: 공식 whitepaper, Rootdata, 여러 AI 요약 종합).\n주요 구조: 1) 노드 마이너가 데이터를 기여하면 실시간으로 토큰을 채굴(Proof-of-Contribution). 2) 데이터 소비자(기업/개발자 등)은 RTK API 등 정밀 데이터를 $GEOD로 결제하고, 토큰은 소각(유통 감소, 디플레이션). 3) 거버넌스 및 미래 생태계 확장에 토큰을 활용할 예정. 4) 반감기 모델로 채굴 보상은 점진적으로 감소하며, API 사용량이 늘수록 장기적으로 순환공급이 줄어드는 선순환 구조를 목표."
  },
  "team": [
    {
      "name": "Mike Horton",
      "role": "CEO / Project Creator / Co-founder",
      "background": "센서·위치 인식 산업 20년+, Crossbow(무선 센서 스타트업, $1억 이상 매각), ANELO Photonics(정밀 IMU), Decawave(Qorvo 인수 기업) 컨설턴트 등 GNSS 및 관성 센서 분야 도메인 전문가",
      "details": "블록체인·분산 GNSS 생태계 창업 및 운영 경험, 물리 인프라 혁신으로 ‘위치 데이터의 민주화’와 실제 산업 적용을 실현하는 비전에 집중"
    },
    {
      "name": "Yudan Yi",
      "role": "Chief Scientist",
      "background": "스탠포드 박사, GPS·RF신호처리·정밀 위치항법 분야 세계적 학자",
      "details": "GNSS 알고리즘, 데이터 품질관리, 네트워크 신뢰도/스코어링 시스템 등 기술 총괄 설계"
    },
    {
      "name": "David Jung",
      "role": "CTO",
      "background": "IoT 하드웨어, GNSS·위치데이터 특허 다수 보유",
      "details": "실제 GNSS 특허 보유, HW/FW/블록체인 통합 설계 경험"
    },
    {
      "name": "엔지니어링팀",
      "role": "엔지니어 / 개발자",
      "background": "Qualcomm/Apple/Google/NASA 등 출신, 소프트웨어, 하드웨어, 클라우드 및 데이터 전문가",
      "details": "실리콘밸리 기반으로, 현장 IoT·센서·블록체인 기술 융합에 특화됨. Blockchain.com 출신 포함, 기상 및 RtK 위치 데이터 실무 경험 다수"
    }
  ],
  "funding": {
    "totalAmount": "15,000,000 USD"
  },
  "investors": [
    {
      "name": "Multicoin Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "DePIN·Web3 선구 VC, Helium 등 IoT/디지털 인프라 베팅 강점, GEODNET은 Helium의 RTK·위치 데이터 버전으로 평가받음.",
      "details": "GNSS $100B 시장 디스럽션 가능성, GEODNET의 커뮤니티 중심 탈중앙 인프라, 대규모 실사용 잠재력에 대한 평가로 투자"
    },
    {
      "name": "Pantera Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "블록체인 분야의 오랜 경력 VC, 혁신적 인프라·탈중앙 인더스트리 투자 강점",
      "details": "DePIN, Web3 인프라 등 차세대 시장의 장기성장성과 실질 산업 채택 가능성에 초점"
    },
    {
      "name": "VanEck",
      "type": "Corporate",
      "tier": "Tier 1",
      "description": "전통 금융(TradFi) 거물이자 ETF/자산운용사, Web3·실생활 인프라와의 브릿지 역할",
      "details": "GEODNET이 Web3에 그치지 않고, 전통 산업·금융 시장까지 영향력을 확대할 파괴적 잠재력에 베팅"
    },
    {
      "name": "Santiago Roel Santos",
      "type": "Angel",
      "tier": "Tier 1",
      "description": "DePIN·Web3 전문 엔젤 투자자로, 업계 네트워킹과 후속 투자 유도자의 역할",
      "details": "크립토 업계에서의 평판, GEODNET 초기 성장에 중요한 역할"
    },
    {
      "name": "CoinFund",
      "type": "VC",
      "tier": "Tier 2",
      "description": "Web3·크립토 네이티브 VC, 인프라 및 DePIN 특화 투자",
      "details": "GEODNET의 DePIN, IoT, 미래 인프라 성장성을 보며 펀딩 참여"
    },
    {
      "name": "ParaFi Capital",
      "type": "VC",
      "tier": "Tier 2",
      "description": "탈중앙금융(DeFi), DePIN, Web3 인프라 전문 투자자",
      "details": "데이터·인프라 네트워크·토큰 경제 모델의 차별성에 주목"
    },
    {
      "name": "Animoca Brands",
      "type": "Corporate/기타",
      "tier": "추정",
      "description": "글로벌 GameFi/메타버스/Web3 허브, 전략적 투자자",
      "details": "실물 데이터와 Web3 크로스오버 활용성을 기대, 게임/메타버스 연계 신규유스케이스 가능성"
    },
    {
      "name": "기타 투자자들",
      "type": "VC/Angel/기타",
      "tier": null,
      "description": "Borderless Capital, North Island Ventures, DACM, IoTeX, JDI Global, Modular Capital, Reverie, Road Capital, Tangent 등 주요 Web3/IoT/블록체인 네임드 투자자들",
      "details": "GEODNET의 글로벌 확장, PoC 실증, IoT/위치데이터 연계 다양한 신규 산업 성장에 베팅"
    }
  ],
  "userActions": {
    "currentActivities": [
      {
        "activity": "노드 마이닝(기준국 운영)",
        "description": "공식 웹·유통사를 통해 GNSS 위성 수신기(Geodnet Miner, $300~$700 선)를 구매·설치(옥상, 옥외 등)하고, 실시간 GNSS/환경 데이터를 업로드해 $GEOD 토큰을 보상받음. 보상은 업타임, 정확도, 지역기여도, 네트워크 검증을 기반으로 산정됨."
      },
      {
        "activity": "데이터/API 구독 및 서비스 활용",
        "description": "기업·개발자는 API를 통해 RTK 위치 보정, 환경 데이터 등 실시간 데이터를 구독해 자율주행, 드론, 측량, 정밀농업 등에서 직접 통합·활용 가능."
      },
      {
        "activity": "커뮤니티 활동 및 기여",
        "description": "Discord, Telegram, 공식 X(트위터) 등에서 각 국 노드 운영자·개발자와 정보 교류, 버그 바운티/해커톤/앰버서더 등 다양한 보상형 활동 참여 가능."
      }
    ],
    "airdropPotential": {
      "status": "Medium",
      "reasoning": "대규모 불특정 대상 에어드랍보다는 실질적 네트워크 기여(노드 마이닝), 특정 커버리지 지역 채굴, 개발자 해커톤, 테스터 프로그램 등에 연결된 직간접 보상 구조가 중심적이다. 하지만, Testnet 기간, 신규 커버리지 지역 대상 보너스(예: SuperHex), 이벤트성 개발자/커뮤니티 리워드 등은 실제로 정기 시행되고 있다.",
      "details": "공식 Docs·X 공지 기준, SuperHex 등 미개척 지역 노드, Testnet·버그헌트, 앰버서더, 해커톤 참여 등에서 토큰형 보너스를 지급하는 사례가 다수다. 추후 토큰 상장 및 확장에 따라, 네트워크 기여자·실사용 참가자 중심의 추가 리워드/에어드랍이 지속될 수 있다."
    }
  },
  "competitors": [
    {
      "name": "Trimble, Leica, Topcon (전통 중앙화 RTK/GNSS 기업)",
      "differentiation": "GEODNET은 전통적으로 고가 (수억~수십억 원대 인프라/연간 수백~수천만원 구독), 인증된 B2B 기반, 느린 네트워크 확장, 폐쇄적 구조의 한계를 파격적인 가격(1/10~1/100)·개방성·크라우드 기반 분산 확장·글로벌 커버리지로 돌파하며, DePIN 및 블록체인 보상 혁신이 결합됨.",
      "details": "전통적 시장 강점(안정성, 브랜드, B2B 신뢰성)과 달리, GEODNET은 초정밀 RTK 데이터를 커뮤니티 기반, 더 빠른 네트워크 구축·혁신적 가성비로 제공. 단, 전통 솔루션 대비 장기 신뢰성, 표준 인증 등은 지속 검증 필요."
    },
    {
      "name": "Helium (DePIN 무선 인프라)",
      "differentiation": "Helium이 글로벌 무선/IoT 인프라(Hotspot)에 특화였다면, GEODNET은 센티미터급 위치 데이터 및 환경 관측에 최적화. 마이닝·토큰보상 구조와 빠른 글로벌 확장은 유사하나, 실시간 RTK/실용성 측면에서 GEODNET만의 독자적 시장/기술 포지셔닝을 보유.",
      "details": "Helium 쇼크를 통해 DePIN 보상/생태계 유지와 실제 서비스 채택간의 밸런스 중요성이 검증됨. GEODNET은 실질 수요와 산업 적용에 더욱 집중하고 있음."
    },
    {
      "name": "Hivemapper (지도 DePIN)",
      "differentiation": "Hivemapper는 카메라 기반 지도 데이터 수집·구축에 특화되어 있고, GEODNET은 위성 신호 기반 초정밀·실시간 위치 및 환경 데이터를 제공. 지도 생성 vs. 실시간 위치/센서 데이터라는 차별화.",
      "details": "정밀 공간 정보의 질과 리얼타임 RTK 보정 등에서 GEODNET만의 고도화를 추구."
    },
    {
      "name": "FOAM",
      "differentiation": "FOAM은 블록체인 기반 위치 증명(Proof of Location)에 초점, GEODNET은 실제 위성/RTK 등 실물 데이터에 특화. FOAM은 소프트웨어/비콘 중심, GEODNET은 하드웨어·RTK 데이터머신 특화.",
      "details": "FOAM은 스마트시티/위치 인증 B2B적 활용에, GEODNET은 물리적 GNSS/환경 데이터 사업화에 강점."
    },
    {
      "name": "Wayfinder, PocketGNSS 등 신흥 DePIN 프로젝트",
      "differentiation": "위치 데이터 중심 DePIN/블록체인 프로젝트로 성장 중이나, 네트워크 규모나 실사용 실적에서 아직 초기 단계.",
      "details": "GEODNET은 실제 6,600+ 글로벌 노드, API 실제 산업 이용, 투자·팀 측면에서 차별화된 성숙도 보유."
    }
  ],
  "risks": [
    {
      "type": "기술적",
      "description": "노드-위치 데이터 품질·정확도 및 환경, 하드웨어/소프트웨어/보안 이슈",
      "details": "GNSS 신호 판독, 환경별 신호간섭/데이터 편차, 노드 하드웨어/펌웨어 보안, 신호 위·변조/허위 데이터, 대량 해킹/오류노드 배제 등 관리체계가 충분히 견고해야 함. 네트워크 초기 노드 밀도 불균형, 지역별 환경 차이로 실시간 품질 편차가 발생 가능."
    },
    {
      "type": "사업적",
      "description": "시장 수요 확장 속도, 전통 대기업 대응, 규제와 신뢰성 확보",
      "details": "기존 정부·산업체 고객의 신뢰·표준화, Helium 등 DePIN 기반 프로젝트의 운영 불확실성과 유사한 리스크, 지역별 데이터/IoT/토큰 규제, B2B/블록체인 시장내 장기 수익모델 검증의 불확실성, 글로벌 확장에 따른 운영비·네트워크 관리 리스크 존재."
    },
    {
      "type": "토큰경제/시장",
      "description": "토큰 가격 변동성 및 경제적 인센티브 유지",
      "details": "$GEOD 가격 급변·폭락시 마이너 이탈, 채굴 인센티브 약화, 실질 데이터 수요/생산 불일치로 네트워크 안정성 저하 가능성. DePIN 생태계 특유의 리워드 감소/버블 붕괴 위험, 네트워크 품질 저하 우려."
    },
    {
      "type": "기타 운영/정책",
      "description": "하드웨어 내구성, 유지보수, 국가별 규제, 데이터 프라이버시/해외이전 이슈",
      "details": "네트워크 대량 운영시 고장, 교체, SW 보안 업데이트, 노드 지역별 인증 등 운영 이슈 발생 가능. 각국 데이터 신뢰성·보안·개인정보 규제 신설·강화 등 법적 리스크에 대비 필요."
    }
  ]
}
```