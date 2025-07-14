```json
{
  "projectName": "GEODNET",
  "oneLiner": "전 세계 커뮤니티가 운영하는 위성 수신국 네트워크를 통해, 센티미터(cm)급 초정밀 실시간 위치 보정 데이터를 제공하는 탈중앙화 물리적 인프라 네트워크(DePIN).",
  "tags": [
    "IOT",
    "DePIN",
    "GNSS",
    "RTK"
  ],
  "overview": {
    "summary": "기존의 초정밀 위치 정보(RTK) 서비스는 Trimble과 같은 소수 기업이 독점하여 연간 수백만 원에 달하는 고비용 구조를 가지고 있었습니다. GEODNET은 DePIN 모델을 통해 이 비용을 혁신적으로 낮추고 데이터 접근성을 민주화하여 자율주행, 드론, 정밀 농업, 증강현실(AR) 등 미래 산업의 상용화를 가속화합니다.",
    "networkStatus": "현재 전 세계적으로 6,600개 이상의 기준국(스테이션)이 활발하게 운영 중입니다."
  },
  "technology": {
    "coreConcept": "실시간 이동 측위 (RTK, Real-Time Kinematic)",
    "blockchain": "폴리곤(Polygon) 네트워크 기반의 ERC-20 토큰",
    "keyFeatures": [
      {
        "name": "작동 원리 (Working Principle)",
        "description": "참여자가 설치한 위성 수신기(기준국)가 위성 신호 오차를 계산하여 '보정 데이터'를 생성하고, 이를 최종 사용자가 활용하여 자신의 위치 정확도를 높이는 메커니즘입니다.",
        "details": "1. 데이터 수집: 전 세계 참여자(마이너)가 GEODNET 위성 수신기를 설치하면, 고정된 위치에서 GPS, Galileo 등 GNSS 위성 신호를 수신합니다.\n2. 오차 계산: 수신기는 대기층 통과 시 발생하는 신호 오차를 실시간으로 계산하여 '보정 데이터'를 생성합니다.\n3. 데이터 전송: 생성된 보정 데이터를 인터넷을 통해 GEODNET 네트워크로 전송합니다.\n4. 데이터 활용: 최종 사용자(예: 자율주행차, 드론)는 GEODNET 네트워크에서 자신과 가장 가까운 기준국의 보정 데이터를 받아, 자신의 위치 오차를 실시간으로 보정하여 cm 단위 정확도를 확보합니다."
      },
      {
        "name": "검증 메커니즘 (Validation Mechanism)",
        "description": "여러 노드 간 데이터를 상호 검증하는 평판 기반(Reputation-based) 알고리즘을 사용합니다.",
        "details": "각 노드는 데이터의 품질, 지속적인 업타임, 주변 노드와의 데이터 일관성 등을 종합적으로 평가받아 신뢰도를 쌓고, 이에 따라 보상이 차등 지급됩니다. 이는 악의적이거나 품질이 낮은 데이터를 걸러내는 역할을 합니다."
      }
    ]
  },
  "tokenomics": {
    "tokenName": "GEODNET Token",
    "tokenTicker": "$GEOD",
    "utility": "채굴 보상 (Mining), 데이터 접근 및 소각 (Burn-to-Access), 거버넌스 투표권",
    "details": {
      "totalSupply": "1,000,000,000 (10억) 개",
      "utilityDetails": {
        "miningRewards": "기준국을 운영하며 신뢰할 수 있는 데이터를 제공하는 대가로 $GEOD를 채굴합니다.",
        "burnToAccess": "기업 등 데이터 사용자는 RTK 보정 데이터를 이용하기 위해 $GEOD 토큰을 구매 후 소각(Burn)해야 합니다. 이는 네트워크 사용량 증가가 토큰 가치 상승으로 직접 이어지는 디플레이션 모델입니다.",
        "governance": "향후 프로토콜의 주요 의사결정에 참여하는 투표권으로 사용될 예정입니다."
      },
      "allocation": {
        "miningRewards": "40% (400,000,000)",
        "foundation": "20% (200,000,000)",
        "teamAndAdvisors": "20% (200,000,000)",
        "seedAndPrivate": "15% (150,000,000)",
        "ecosystemFund": "5% (50,000,000)"
      }
    }
  },
  "team": [
    {
      "name": "Mike Horton",
      "role": "Project Creator",
      "background": "GEODNET의 모회사인 ANELO Photonics의 CEO. 이전에 무선 센서 기업 Crossbow Technology의 사업부를 인수하고, 초정밀 위치 센서 기업 Decawave(Qorvo에 인수)에서 컨설턴트로 활동하는 등 GNSS 및 관성 센서 분야에서 20년 이상의 경력을 가진 도메인 전문가입니다.",
      "vision": "\"위치 데이터의 민주화\"를 목표로, 신뢰성 있고 개방된 글로벌 네트워크를 구축하여 실제 산업에서의 채택을 최우선으로 강조합니다."
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
      "description": "DePIN 분야의 선구적인 투자사",
      "details": "DePIN 분야의 선구자인 Multicoin, 블록체인 업계의 거물 Pantera, 그리고 전통 금융 강자인 VanEck의 투자는 GEODNET이 크립토 네이티브 시장을 넘어 전통 산업까지 아우르는 파괴적 잠재력을 가졌음을 시사합니다."
    },
    {
      "name": "Pantera Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "블록체인 업계의 가장 오래되고 존경받는 펀드 중 하나",
      "details": "DePIN 분야의 선구자인 Multicoin, 블록체인 업계의 거물 Pantera, 그리고 전통 금융 강자인 VanEck의 투자는 GEODNET이 크립토 네이티브 시장을 넘어 전통 산업까지 아우르는 파괴적 잠재력을 가졌음을 시사합니다."
    },
    {
      "name": "VanEck",
      "type": "Corporate",
      "tier": "Tier 1",
      "description": "전통 금융(TradFi) 시장의 거물",
      "details": "DePIN 분야의 선구자인 Multicoin, 블록체인 업계의 거물 Pantera, 그리고 전통 금융 강자인 VanEck의 투자는 GEODNET이 크립토 네이티브 시장을 넘어 전통 산업까지 아우르는 파괴적 잠재력을 가졌음을 시사합니다."
    }
  ],
  "userActions": {
    "currentActivities": [
      {
        "activity": "기준국 운영 (채굴)",
        "description": "공식 웹사이트나 유통사를 통해 위성 수신기 하드웨어(약 $400 ~ $700)를 구매 및 설치하고, 네트워크에 데이터를 제공하여 $GEOD 토큰을 보상받을 수 있습니다."
      },
      {
        "activity": "데이터 사용",
        "description": "개발자나 기업은 API를 통해 RTK 보정 데이터를 구독하여 자사 서비스에 통합할 수 있습니다."
      }
    ],
    "airdropPotential": {
      "status": "Low",
      "reasoning": "불특정 다수를 위한 대규모 에어드랍보다는, 현재 진행 중인 채굴 보상이 가장 직접적인 보상 형태입니다.",
      "details": "네트워크가 부족한 전략적 위치에 노드를 설치하는 등 특정 기여 활동에 대한 추가 인센티브 프로그램이 존재하며, 향후에도 실제 기여자 중심의 보상이 이루어질 가능성이 높습니다."
    }
  },
  "competitors": [
    {
      "name": "Trimble, Leica Geosystems (전통 중앙화 기업)",
      "differentiation": "GEODNET은 비용 경쟁력에서 절대 우위를 가집니다. 기존 서비스의 강점은 높은 신뢰도와 기존 고객 기반이지만, 약점은 압도적으로 높은 비용과 폐쇄적인 생태계입니다.",
      "details": "GEODNET은 DePIN 모델을 통해 기존 시장의 1/100 수준의 비용으로 동등한 품질의 서비스를 제공할 잠재력을 가집니다."
    },
    {
      "name": "Hivemapper",
      "differentiation": "Hivemapper는 지도 이미지 데이터 수집에 특화된 DePIN인 반면, GEODNET은 센티미터급 실시간 GNSS 보정 데이터에 집중합니다.",
      "details": "서로 다른 종류의 물리적 데이터를 다루므로 직접적인 경쟁보다는 DePIN 생태계 내에서 각자의 영역을 구축하는 관계에 가깝습니다."
    },
    {
      "name": "FOAM",
      "differentiation": "FOAM은 블록체인 기반의 '위치 증명(Proof of Location)' 프로토콜 자체에 초점을 맞추지만, GEODNET은 '실시간 위치 보정 서비스'라는 명확한 상업적 유틸리티를 제공합니다.",
      "details": "GEODNET은 FOAM과 달리 cm 단위의 초정밀 실시간 데이터 스트림을 제공하며, 이는 자율주행과 같은 즉각적인 산업 수요에 더 부합합니다."
    }
  ],
  "risks": [
    {
      "type": "기술적 리스크 (Technical Risk)",
      "description": "네트워크 밀도가 낮은 지역에서는 서비스 품질이 저하될 수 있으며, 악의적인 데이터 공격에 대한 방어 체계의 지속적인 고도화가 필요합니다.",
      "details": "특정 지역에만 마이너가 집중되는 '콜드 스타트' 문제는 글로벌 네트워크라는 가치를 퇴색시킬 수 있으므로 지역별 인센티브 조정이 중요합니다."
    },
    {
      "type": "사업적 리스크 (Business Risk)",
      "description": "대기업 고객들이 검증된 기존 솔루션에서 탈중앙화 네트워크로 전환하는 데 필요한 신뢰와 레퍼런스를 쌓는 데 시간이 걸릴 수 있습니다.",
      "details": "초기 기업 고객 확보와 성공적인 사용 사례를 구축하여 시장에 신뢰를 주는 것이 프로젝트의 중기적 성공에 매우 중요합니다."
    },
    {
      "type": "시장 리스크 (Market Risk)",
      "description": "$GEOD 토큰 가격의 변동성은 마이너들의 참여 유인에 직접적인 영향을 줄 수 있으며, 이는 모든 DePIN 프로젝트가 가진 공통적인 과제입니다.",
      "details": "토큰 가격이 마이너 운영 비용(전기세 등) 이하로 하락할 경우, 네트워크 이탈이 발생하여 네트워크의 안정성이 저해될 수 있습니다."
    }
  ]
}
```