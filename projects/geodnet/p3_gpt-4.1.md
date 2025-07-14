```json
{
  "projectName": "GEODNET",
  "oneLiner": "전 세계에 소형 GNSS(위성항법) 노드를 설치, 블록체인 기반 분산 네트워크로 연결해, 누구나 이용 가능한 초정밀(cm급) 위치·환경 데이터를 제공하는 탈중앙화 물리 인프라 네트워크(DePIN) 프로젝트다.",
  "tags": ["IOT", "DePIN", "GNSS", "RTK", "블록체인"],
  "overview": {
    "summary": "GEODNET은 GNSS(위성항법) 데이터 수집을 위한 저가 하드웨어(마이너)를 이용해 누구나 글로벌 고정밀 위치·환경 관측 인프라의 일부가 될 수 있도록 설계된 탈중앙화 물리 인프라 네트워크(DePIN)이다.",
    "details": "기존 위치 데이터 산업은 GPS 등 로우 데이터의 정밀도 한계(수미터 오차), 가격 및 커버리지의 독점, 산업용 RTK 네트워크의 고비용·확장성 문제를 가지고 있었다. GEODNET은 블록체인과 토큰 인센티브를 통해 누구나 GNSS 노드를 손쉽게 설치·운영하면 토큰($GEOD) 보상을 받을 수 있으며, API로 수집된 보정 데이터를 수많은 산업군(자율주행, 드론, 정밀농업, 스마트건설, AR/VR 등)에 실시간 제공한다. 센티미터급의 초정밀 위치·환경 데이터가 6,000여 대의 분산 노드에서 실시간 집계되어, 기존 상용 RTK 서비스 대비 10~100배 경제적이며, 탈중앙·저비용·빠른 확장이 가능하다. GEODNET은 특히 데이터 민주화와 물리 인프라의 공유라는 패러다임 혁신을 노린다."
  },
  "technology": {
    "coreConcept": "개방형 GNSS 노드들이 위성 신호(여러 GNSS 시스템: GPS, Galileo, GLONASS 등)를 수집해 네트워크에 실시간 업로드하고, 멀티노드 교차 검증(Proof-of-Location), 블록체인 기반 기록 및 보상, 오픈 API 제공 구조로 구현된 DePIN(Decentralized Physical Infrastructure Network)이다.",
    "keyFeatures": [
      {
        "name": "노드 참여/마이닝",
        "description": "누구나 공식 인증 GNSS 수신기(Geodnet Miner)를 구입·설치한 뒤, 네트워크에 데이터 송신 및 마이닝 형태의 토큰 보상",
        "details": "노드는 옥상, 개방된 야외 등에서 위성 신호, 환경, 위치, 고도, 기상 데이터를 수집하여 실시간 전송하고, 탈중앙적 검증을 거쳐 기여도에 따라 실시간으로 $GEOD 토큰을 보상받는다."
      },
      {
        "name": "데이터 검증 및 위변조 방지",
        "description": "멀티노드 PoL(Proof-of-Location) 및 교차 검증 기술",
        "details": "방대한 노드 간의 신호 비교, 위성 신호 간섭·오류 검증, 위치 및 신뢰성 스코어링으로 허위 데이터/위변조 방지. 오프라인 노드, 오동작 노드는 자동 배제."
      },
      {
        "name": "API 및 서비스 소비",
        "description": "RTK(Real-Time Kinematic) correction 데이터와 위치·환경 데이터를 개발자/기업/서비스에 API 형태로 제공",
        "details": "초정밀 데이터 활용처로는 자율주행차, 무인드론 배송, 정밀 농기계, 로보틱스, AR/VR, 측량 및 스마트도시 서비스가 있다. 기존 GPS·RTK보다 월등히 낮은 비용, 실시간과 글로벌 커버리지가 장점."
      },
      {
        "name": "블록체인 기반 인센티브",
        "description": "Polygon(폴리곤) 메인넷 블록체인 기반 기록, 보상, 투명한 데이터 로그",
        "details": "데이터 제공-소비-검증-보상까지 온체인화, 노드 운영자·데이터 사용자·커뮤니티에 투명한 보상 구조. 토큰 소각(Burn-to-Access) 등 디플레이션 경제 구조 도입."
      }
    ]
  },
  "tokenomics": {
    "tokenName": "GEODNET Token",
    "tokenTicker": "GEOD",
    "utility": "노드(마이너) 보상, 데이터/API 이용료, 커뮤니티 거버넌스(예정), Burn-to-Access(이용시 토큰 소각)",
    "details": "토탈 10억(1,000,000,000) GEOD 토큰이 발행된다. 55~60%가 네트워크 채굴/커뮤니티 기여자에게, 15~25%가 팀/창업/어드바이저(2~4년 락업 포함), 15~20%가 투자자, 5~10%가 재단·마케팅·생태계 확장에 배정된다(공식 whitepaper 및 Rootdata 기준). 보상은 초기엔 노드 기여에 집중, 시간이 갈수록 반감기 구조로 감소한다. API 등 네트워크 유료 사용에 따라 토큰이 소각(burn)되어, 실제 수요가 상승시 토큰 희소성이 실현된다. 모든 토큰 흐름과 분배, 소각 내역은 온체인 상에서 투명하게 기록된다."
  },
  "team": [
    {
      "name": "Mike Horton",
      "role": "CEO/Co-founder",
      "background": "센서·위치인식 산업 20년+, Crossbow(무선 센서 스타트업, $1억 이상에 M&A), ANELO Photonics(정밀 IMU), 위성항법/센서 IoT 분야 창업자",
      "details": "하드웨어와 분산형 GNSS 분야에서 세계적 창업가로, 글로벌 DePIN 인프라 사업화 경험 풍부. GEODNET을 통한 '탈중앙 인프라 세상'에 집중."
    },
    {
      "name": "Yudan Yi",
      "role": "Chief Scientist",
      "background": "스탠포드 박사, GPS·RF·정밀 위치항법 분야 세계적 학자",
      "details": "GNSS 알골리즘, 위치 데이터 정확도 및 네트워크 검증 프로토콜을 총괄 설계 및 리드."
    }
  ],
  "investors": [
    {
      "name": "Multicoin Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "DePIN·Web3 선구 VC, Helium 등 IoT 인프라·실물 데이터 베팅이 강점",
      "details": "GEODNET의 DePIN 구조와 세계 공간데이터 시장의 중장기 혁신성, Helium과 유사한 산업적 확장 모델에 높은 평가를 가짐."
    },
    {
      "name": "Pantera Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "글로벌 대형 블록체인·디지털 자산 전문 VC",
      "details": "블록체인·실물융합 인프라 시장의 성장성, 장기 산업혁신 사례를 찾아 전략적으로 조기 투자."
    },
    {
      "name": "VanEck",
      "type": "VC",
      "tier": "Tier 1",
      "description": "전통 ETF/자산운용사",
      "details": "크립토·전통 산업의 브릿지, DePIN의 대중화 가능성 베팅, 실생활 데이터 기반 인프라 잠재력 중심 평가."
    },
    {
      "name": "Santiago Roel Santos",
      "type": "Angel",
      "tier": "Tier 1",
      "description": "크립토 파워 엔젤, DePIN·Web3 프로젝트 전문",
      "details": "프로젝트 초기부터 적극적 네트워킹과 후속투자 유도."
    },
    {
      "name": "CoinFund",
      "type": "VC",
      "tier": "Tier 2",
      "description": "블록체인·Web3 전문 투자사",
      "details": "DePIN 및 인프라 네트워크의 중장기 경쟁력에 베팅."
    },
    {
      "name": "ParaFi Capital",
      "type": "VC",
      "tier": "Tier 2",
      "description": "탈중앙 금융·블록체인 인프라 투자",
      "details": "Web3 기반 데이터·인프라의 가치 보증 단기/장기 분배 포트폴리오 지원."
    },
    {
      "name": "Animoca Brands",
      "type": "기타",
      "tier": "추정",
      "description": "글로벌 GameFi·Web3 플랫폼사, 전략 투자자",
      "details": "Web3 실물 데이터 활용 신규 게임/메타버스 등 확장 가능성 타진"
    }
  ],
  "userActions": {
    "currentActivities": "누구나 공식 Geodnet Miner 하드웨어(수십~수백 달러)를 구입·설치해 노드로서 네트워크에 참여할 수 있다. 노드 운영 지역(옥상, 옥외 등)에서 위성신호를 수집·전송하면 실시간으로 기여도 계산을 받아 $GEOD 토큰을 보상받는다. 개발자나 기업은 실시간 고정밀 RTK·환경 데이터 API를 신청·구독해 자율주행, 농업, 측량, 로보틱스 등 실제 활용에 직접 사용할 수 있다. 각국 커뮤니티(Discord, Telegram 등)가 매우 활발하며, 다양한 해커톤, 버그헌트, 지역별 배치이벤트 등으로 참여 기회가 많다.",
    "airdropPotential": {
      "status": "Medium",
      "reasoning": "대규모 ‘에어드랍’이 아닌 실제 노드 마이닝 및 실질기여 기반 보상 정책이 주력이나, 기간 한정 Testnet, 신규커버리지 지역, 커뮤니티 액티비티, 개발자 해커톤 등에 한정 보너스/에어드랍성 리워드가 자주 시행되고 있다.",
      "details": "공식 Docs, X 공지에 따르면 SuperHex 등 커버리지 취약지역 신규 노드, 앰버서더·일부 홍보/기술 체험 이벤트, 개발자 해커톤에 추가 토큰이 에어드랍(Reward) 형태로 지급되고 있다. 토큰 상장 이후 대규모 단발성 에어드랍보다는, 실제 네트워크 기여 중심의 꾸준한 리워드·인센티브형 에어드랍이 지속될 가능성이 높다."
    }
  },
  "competitors": [
    {
      "name": "Trimble, Leica 등 전통 RTK/GNSS 기업",
      "differentiation": "폐쇄형, 초고가 인프라, 느린 확장 구조에서 GEODNET은 분산형, 개방형, 급속 확장, 초저가 서비스로 차별화.",
      "details": "기존 RTK/위치정확도 시장 강자는 수억~수십억 단위의 사업비, 인증된 B2B 기반, 신뢰기관 이미지. GEODNET은 블록체인·토큰 보상으로 네트워크 밀도와 커버리지, 가격 임팩트에서 우위. 단, 시장 레퍼런스와 장기 안정성, 데이터 신뢰성에서는 치열한 인증/신뢰 경쟁."
    },
    {
      "name": "Helium (DePIN, 무선 통신 인프라)",
      "differentiation": "유사한 탈중앙 인프라/토큰채굴 모델이나, Helium은 무선/IoT 커버리지, GEODNET은 초정밀 위치·환경 데이터에 특화됨.",
      "details": "Helium의 폭발적 확장/토큰모델을 블루프린트로 삼되, 실제 데이터 활용성과 정밀 플랫폼 측면에서는 GEODNET이 독특한 지위를 가짐."
    },
    {
      "name": "Hivemapper",
      "differentiation": "카메라 데이터로 실시간 맵 구축(지도DePIN)이지만, GEODNET은 위성 신호 기반 초정밀 위치와 실시간 환경 검증 데이터에 특화.",
      "details": "실재 이동 경로 데이터(도로·거리 등)에 강한 Hivemapper와 달리, 전문 위치정확/기기제어, 산업용 RTK 활용이 강점."
    },
    {
      "name": "FOAM",
      "differentiation": "위치증명(소프트웨어/비콘 기반)으로 탈중앙 위치 서비스, GEODNET은 물리 GNSS/RTK 데이터에 특화",
      "details": "FOAM은 스마트도시/위치 인증(B2B·IoT) 특화, GEODNET은 실제 위성-SoC 하드웨어 머니타이즈와 산업 활용성이 핵심."
    }
  ],
  "risks": [
    {
      "type": "기술적",
      "description": "노드-위치 데이터 품질·정확도 및 하드웨어 운영 안정성",
      "details": "기상·지형·건물 음영 등 환경요소, GNSS 신호간섭, 오동작/펌웨어 취약점 등에 의해 데이터 품질이 편차를 보일 수 있음. 대량 노드 해킹·위변조에도 대비 필요."
    },
    {
      "type": "사업적",
      "description": "시장 수요 확장 속도, 네트워크 품질, 대기업의 대응력",
      "details": "전통적 대규모 고객(정부·산업체 등)의 신뢰 확보, Helium 쇼크와 유사한 탈중앙 인프라의 운영 불안정성 리스크, 수익 모델 수립 전까지의 캐시플로우 안정성 문제 존재."
    },
    {
      "type": "시장/토큰 경제",
      "description": "토큰 가격 변동성, 규제, 커뮤니티 이탈 등",
      "details": "탈중앙 인프라 프로젝트 특유의 토큰 급락시 마이너 이탈, 글로벌 토큰·IoT·개인정보 규제 불확실성, DePIN 시장 내 과포화·중복경쟁 가능성, 실질 매출·지속성 검증 필요."
    }
  ]
}
```