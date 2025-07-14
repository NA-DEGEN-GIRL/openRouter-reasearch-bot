```json
{
  "projectName": "GEODNET",
  "oneLiner": "전 세계 커뮤니티가 운영하는 위성 수신국 네트워크를 통해, 센티미터(cm)급 초정밀 실시간 위치 보정 데이터를 제공하는 탈중앙화 물리적 인프라 네트워크(DePIN).",
  "tags": [
    "IOT",
    "DePIN",
    "GNSS",
    "RTK",
    "블록체인"
  ],
  "overview": {
    "summary": "GEODNET은 GNSS(위성항법) 데이터 수집을 위한 저가 하드웨어(마이너)를 이용해 누구나 글로벌 고정밀 위치·환경 관측 인프라의 일부가 될 수 있도록 설계된 탈중앙화 물리적 인프라 네트워크(DePIN)입니다.",
    "details": "기존 위치 데이터 산업은 GPS 등 로우 데이터의 정밀도 한계(수미터 오차), 가격 및 커버리지의 독점, 산업용 RTK 네트워크의 고비용·확장성 문제를 가지고 있었습니다. GEODNET은 블록체인과 토큰 인센티브를 통해 누구나 GNSS 노드를 손쉽게 설치·운영하면 토큰($GEOD) 보상을 받을 수 있으며, API로 수집된 보정 데이터를 수많은 산업군(자율주행, 드론, 정밀농업, 스마트건설, AR/VR 등)에 실시간 제공합니다. 센티미터급의 초정밀 위치·환경 데이터가 분산 노드에서 실시간 집계되어, 기존 상용 RTK 서비스 대비 10~100배 경제적이며, 탈중앙·저비용·빠른 확장이 가능합니다. DePIN 모델로 중앙화 독점을 깨며, 글로벌 데이터 민주화를 통해 AI/IoT 시대의 실생활 문제를 해결합니다 (글로벌 시장 규모 $100B+).",
    "networkStatus": "현재 전 세계적으로 6,600개 이상의 기준국(스테이션)이 6대륙 150개국에 활발하게 운영 중입니다."
  },
  "technology": {
    "coreConcept": "개방형 GNSS 노드들이 위성 신호(여러 GNSS 시스템: GPS, Galileo, GLONASS, BeiDou 등)를 수집해 네트워크에 실시간 업로드하고, 평판 기반 알고리즘과 멀티노드 교차 검증(Proof-of-Location)을 거쳐, 블록체인 기반으로 기록 및 보상하며, 오픈 API로 데이터를 제공하는 구조로 구현된 DePIN(Decentralized Physical Infrastructure Network)입니다.",
    "blockchain": "폴리곤(Polygon) 네트워크 기반의 ERC-20 토큰",
    "keyFeatures": [
      {
        "name": "작동 원리 및 노드 참여/마이닝",
        "description": "누구나 공식 인증 GNSS 수신기(Geodnet Miner, 가격 $299~$700)를 구입·설치하여 네트워크에 참여하고, 데이터 송신을 통해 마이닝 형태의 토큰 보상을 받습니다. 이 과정은 데이터 수집, 오차 계산, 전송, 활용의 4단계로 이루어집니다.",
        "details": "1. 데이터 수집: 사용자가 GEODNET 인증 GNSS 수신기(하드웨어)를 구매해 지붕이나 야외에 설치하면, 실시간으로 GPS/갈릴레오/베이두 같은 위성 신호를 캡처하고, 위치, 고도, 기상 데이터 등을 모읍니다.\n2. 오차 계산 및 전송: 수신기는 대기층 통과 시 발생하는 신호 오차를 실시간으로 계산하여 '보정 데이터'를 생성하고, 이를 폴리곤 기반 블록체인 네트워크로 전송합니다 (RTK 기술로 cm급 정확도 달성).\n3. 검증 및 활용: 검증된 데이터는 API를 통해 앱 개발자나 기업(예: 자율주행 회사)에 제공되며, 최종 사용자는 이 데이터를 받아 자신의 위치 오차를 실시간으로 보정하여 cm 단위 정확도를 확보합니다.\n4. 보상: 노드 운영자는 데이터 기여도(품질, 업타임, 위치 중요도)에 따라 실시간으로 $GEOD 토큰을 보상받습니다."
      },
      {
        "name": "데이터 검증 및 위변조 방지",
        "description": "평판 기반 알고리즘, 멀티노드 PoL(Proof-of-Location) 및 교차 검증 기술을 통해 데이터의 신뢰성을 확보하고 위변조를 방지합니다.",
        "details": "방대한 노드 간의 신호 비교, 위성 신호 간섭·오류 검증, 위치 및 신뢰성 스코어링으로 허위 데이터/위변조를 방지합니다. 각 노드는 데이터의 품질, 지속적인 업타임, 주변 노드와의 데이터 일관성 등을 종합적으로 평가받아 신뢰도를 쌓고, 이에 따라 보상이 차등 지급됩니다. 오프라인 노드나 오동작 노드는 자동 배제됩니다."
      },
      {
        "name": "데이터 접근 및 API 소비",
        "description": "초정밀 RTK(Real-Time Kinematic) 보정 데이터와 위치·환경 데이터를 개발자/기업/서비스에 API 형태로 제공합니다.",
        "details": "초정밀 데이터 활용처로는 자율주행차, 무인드론 배송, 정밀 농기계, 로보틱스, AR/VR, 측량 및 스마트도시 서비스가 있습니다. 기존 GPS·RTK보다 월등히 낮은 비용, 실시간성, 글로벌 커버리지가 장점입니다. 사용자는 $GEOD 토큰으로 데이터 구매 비용을 지불합니다."
      },
      {
        "name": "기술 용어 해설",
        "description": "GNSS: '전 세계 위치 별자리 지도' / RTK: '정답지 친구가 실시간 오답 수정' / PoL: '실제 위치 사진 증명 그룹 채팅' / DePIN: 'Uber처럼 개인 차 공유 네트워크'",
        "details": "GNSS: Global Navigation Satellite System. 비유: 스마트폰의 GPS 앱처럼, 하늘의 위성들이 당신의 위치를 알려주는 '별자리 지도'입니다. GEODNET은 이 지도를 더 세밀하게 만들어줍니다.\nRTK (Real-Time Kinematic): cm급 정확도 위치 기술. 비유: 일반 GPS가 \"이 도시 어딘가\"라고 말한다면, RTK는 \"이 테이블 위의 이 잔\"이라고 정확히 가리킵니다. 마치 확대경으로 지도를 보는 것.\nPoL (Proof-of-Location): 위치 증명 합의. 비유: 친구들이 \"내가 여기 있어!\"라고 사진으로 증명하는 그룹 채팅처럼, 노드들이 실제 위치 데이터를 증명해 네트워크가 믿을 수 있게 합니다.\nDePIN: Decentralized Physical Infrastructure Network. 비유: Uber처럼 중앙 회사가 아닌, 사람들(운전자)이 직접 차를 공유하는 네트워크 – 여기서는 위치 데이터를 공유합니다."
      }
    ]
  },
  "tokenomics": {
    "tokenName": "GEODNET Token",
    "tokenTicker": "GEOD",
    "utility": "노드(마이너) 보상, 데이터/API 이용료, 커뮤니티 거버넌스(예정), Burn-to-Access(이용시 토큰 소각)",
    "details": {
      "totalSupply": "1,000,000,000 (10억) 개 (고정)",
      "economicModel": "채굴 보상을 통해 토큰이 발행되나, 시간이 갈수록 반감기 구조로 감소하는 인플레이션 모델과, 서비스 사용료로 지불된 토큰이 소각(Burn)되는 디플레이션 모델이 결합되어 있습니다. 실제 네트워크 사용량이 증가할수록 토큰의 희소성이 높아지는 구조입니다. 모든 토큰 흐름과 분배, 소각 내역은 온체인 상에서 투명하게 기록됩니다.",
      "allocation": {
        "miningRewardsAndCommunity": "55-60%",
        "foundation": "20%",
        "teamAndAdvisors": "15-25% (2~4년 락업 포함)",
        "seedAndPrivateInvestors": "15-20%",
        "ecosystemAndMarketing": "5-10%"
      }
    }
  },
  "team": [
    {
      "name": "Mike Horton",
      "role": "CEO / Co-founder / Project Creator",
      "background": "센서·위치인식 산업 20년+ 베테랑. Crossbow Technology(무선 센서 스타트업, $1억 이상에 M&A), Decawave(초정밀 위치 센서 기업) 컨설턴트, ANELO Photonics(정밀 IMU) CEO. 위성항법/센서 IoT 분야 창업가.",
      "details": "하드웨어와 분산형 GNSS 분야에서 세계적 창업가로, 글로벌 DePIN 인프라 사업화 경험이 풍부합니다. GEODNET을 통한 '데이터의 민주화'와 '탈중앙 인프라 세상' 구축에 집중하고 있습니다."
    },
    {
      "name": "Yudan Yi",
      "role": "Chief Scientist",
      "background": "스탠포드 박사, GPS·RF·정밀 위치항법 분야 세계적 학자",
      "details": "GEODNET의 GNSS 알고리즘, 위치 데이터 정확도 및 네트워크 검증 프로토콜을 총괄 설계 및 리드하여 기술적 신뢰도를 높입니다."
    },
    {
      "name": "David Jung",
      "role": "CTO",
      "background": "IoT 하드웨어 전문가. 여러 GNSS 관련 특허 보유자.",
      "details": "실생활 기술 배경이 강하며, GEODNET의 하드웨어 개발을 이끌고 있습니다."
    },
    {
      "name": "기타 팀원",
      "role": "엔지니어/개발자",
      "background": "Qualcomm, Apple, Google, NASA, Blockchain.com 등 빅테크 및 전문 기업 출신 엔지니어들로 구성 (10~15명, 실리콘 밸리 기반).",
      "details": "GNSS 하드웨어, 저전력 SoC 설계, 블록체인 개발, 기상·위치 데이터 분야 전문가들이 포진해 있습니다."
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
      "type": "Corporate",
      "tier": "Tier 1",
      "description": "전통 ETF/자산운용사",
      "details": "크립토·전통 산업의 브릿지, DePIN의 대중화 가능성, 실생활 데이터 기반 인프라의 잠재력을 높이 평가."
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
      "name": "기타 투자자",
      "type": "VC/Angel/Corporate",
      "tier": null,
      "description": "Borderless Capital, North Island Ventures, Animoca Brands, DACM, IoTeX, JDI Global, Modular Capital, Reverie, Road Capital, Tangent 등",
      "details": "크립토-블록체인, IoT 스페셜리스트, GameFi/메타버스 플랫폼사 등 다양한 분야의 전략적 투자자들이 참여하여 Web3와 실물 데이터 융합 가능성에 베팅함."
    }
  ],
  "userActions": {
    "currentActivities": "누구나 공식 Geodnet Miner 하드웨어(수십~수백 달러, 스타터 킷 포함)를 구입·설치해 노드로서 네트워크에 참여할 수 있습니다. 노드 운영 지역(옥상, 옥외 등)에서 위성신호를 수집·전송하면 실시간으로 기여도 계산을 받아 $GEOD 토큰을 보상받습니다. 개발자나 기업은 실시간 고정밀 RTK·환경 데이터 API를 신청·구독해 자율주행, 농업, 측량, 로보틱스 등 실제 활용에 직접 사용할 수 있습니다. 각국 커뮤니티(Discord, Telegram, X 등, 10,000+ 멤버)가 매우 활발하며, 다양한 해커톤, 버그헌트, 지역별 배치 이벤트 등으로 참여 기회가 많습니다.",
    "airdropPotential": {
      "status": "Medium",
      "reasoning": "대규모 ‘에어드랍’이 아닌 실제 노드 마이닝 및 실질 기여 기반 보상 정책이 주력이나, 특정 조건의 기여자에게 보너스/리워드 형태의 지급이 자주 시행됩니다.",
      "details": "공식 Docs, X 공지에 따르면 SuperHex(커버리지 취약지역) 신규 노드, 앰버서더·일부 홍보/기술 체험 이벤트, 개발자 해커톤 등에 추가 토큰이 리워드 형태로 지급되고 있습니다. 토큰 상장 이후 대규모 단발성 에어드랍보다는, 실제 네트워크 성장에 기여하는 참여자 중심의 꾸준한 인센티브형 보상이 지속될 가능성이 높습니다. 메인넷 런칭 후 초기 기여자에 대한 추가 보상 기대감도 존재합니다."
    }
  },
  "competitors": [
    {
      "name": "Trimble, Leica 등 전통 RTK/GNSS 기업",
      "differentiation": "폐쇄형, 초고가 인프라, 느린 확장 구조에서 GEODNET은 분산형, 개방형, 급속 확장, 초저가 서비스로 차별화됩니다.",
      "details": "기존 RTK/위치정확도 시장 강자는 수억~수십억 단위의 사업비, 인증된 B2B 기반, 신뢰기관 이미지를 가집니다. GEODNET은 블록체인·토큰 보상으로 네트워크 밀도와 커버리지, 가격 임팩트에서 우위를 점합니다. 단, 시장 레퍼런스와 장기 안정성, 데이터 신뢰성에서는 치열한 인증/신뢰 경쟁이 필요합니다."
    },
    {
      "name": "Helium (DePIN, 무선 통신 인프라)",
      "differentiation": "유사한 탈중앙 인프라/토큰 채굴 모델이나, Helium은 무선/IoT 커버리지에, GEODNET은 초정밀 위치·환경 데이터에 특화되어 있습니다.",
      "details": "Helium의 폭발적 확장/토큰모델을 블루프린트로 삼되, 전문적인 위치 정확도 및 산업용 RTK 활용성과 같은 실제 데이터 유틸리티 측면에서는 GEODNET이 독특한 지위를 가집니다."
    },
    {
      "name": "Hivemapper (지도 DePIN)",
      "differentiation": "Hivemapper는 카메라 데이터로 실시간 맵을 구축하는 반면, GEODNET은 위성 신호 기반의 초정밀 위치와 실시간 환경 검증 데이터에 특화되어 있습니다.",
      "details": "실제 이동 경로 데이터(도로·거리 등)에 강한 Hivemapper와 달리, 전문적인 기기 제어, 농업/재난 분야 등 산업용 RTK 데이터 활용이 필요한 영역에서 강점을 보입니다."
    },
    {
      "name": "FOAM, Wayfinder, PocketGNSS 등",
      "differentiation": "이들은 위치 증명 프로토콜 또는 초기 단계 프로젝트인 반면, GEODNET은 이미 성숙한 글로벌 네트워크와 명확한 상업적 유틸리티를 갖추고 있습니다.",
      "details": "FOAM은 스마트도시/위치 인증(B2B·IoT)에 특화되었고, 다른 프로젝트들은 아직 초기 성장 단계입니다. GEODNET은 물리적 GNSS/RTK 하드웨어 기반의 실시간 데이터 스트림을 제공하며 산업 활용성이 더 명확합니다."
    }
  ],
  "risks": [
    {
      "type": "기술적 리스크",
      "description": "노드-위치 데이터 품질·정확도 및 하드웨어 운영 안정성",
      "details": "기상·지형·건물 음영 등 환경요소, GNSS 신호간섭, 오동작/펌웨어 취약점 등에 의해 데이터 품질이 편차를 보일 수 있습니다. 대량 노드 해킹·위변조에도 대비가 필요하며, 하드웨어의 내구성과 유지보수 이슈도 존재합니다."
    },
    {
      "type": "사업적 리스크",
      "description": "시장 수요 확장 속도, 네트워크 품질, 대기업의 대응력 및 규제 문제",
      "details": "전통적 대규모 고객(정부·산업체 등)의 신뢰 확보와 상업적 레퍼런스 구축에 시간이 걸릴 수 있습니다. 또한 블록체인 기반 데이터 인프라에 대한 각국의 데이터 보안, 토큰 증권성, 개인정보(GDPR), IoT 하드웨어 인증 등 규제 불확실성이 존재합니다."
    },
    {
      "type": "시장 및 토큰 경제 리스크",
      "description": "토큰 가격 변동성, 네트워크 밀도 불균형(콜드 스타트), 경쟁 심화",
      "details": "탈중앙 인프라 프로젝트 특유의 토큰 가격 급락 시 마이너 이탈 위험이 있습니다. 수익성이 높은 지역에만 마이너가 집중되는 네트워크 불균형 문제, 그리고 DePIN 시장 내 과포화·중복경쟁 가능성도 잠재적 리스크입니다. Web3 시장 전체의 실사용 수요 확대 속도에 대한 불확실성도 고려해야 합니다."
    }
  ]
}
```