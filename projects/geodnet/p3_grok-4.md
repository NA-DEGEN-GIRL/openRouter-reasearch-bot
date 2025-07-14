{
  "projectName": "GEODNET",
  "oneLiner": "GEODNET은 지구 전역의 GNSS(위성항법시스템) 데이터를 실시간으로 수집하고 분산화된 네트워크를 통해 제공하는 탈중앙화된 IoT(사물인터넷) 플랫폼으로, 정확한 위치 기반 관측 데이터를 누구나 접근 가능하게 만드는 글로벌 DePIN 네트워크입니다.",
  "tags": ["IOT", "DePIN"],
  "overview": {
    "summary": "GEODNET은 지구 전역의 GNSS(위성항법시스템) 데이터를 실시간으로 수집하고 분산화된 네트워크를 통해 제공하는 탈중앙화된 IoT(사물인터넷) 플랫폼으로, 정확한 위치 기반 관측 데이터를 누구나 접근 가능하게 만드는 글로벌 네트워크입니다.",
    "details": "GEODNET은 기존 중앙화된 GNSS 시스템(예: GPS)의 높은 비용, 제한된 데이터 접근, 지역별 정확도 불균형 문제를 해결합니다. 이는 자율주행 자동차(1m 오차로 인한 사고 방지), 드론 배송(정확한 착륙 지점 지정), 정밀 농업(작물 매핑 비용 절감), AR(가상 객체의 현실 융합) 같은 분야에서 필수적입니다. 예: 농부가 기존 고가 RTK 서비스 대신 저비용 GEODNET으로 cm급 데이터를 사용해 비료를 효율적으로 배분하면 비용을 90% 줄일 수 있습니다. DePIN 모델로 중앙화 독점을 깨며, 글로벌 데이터 민주화를 통해 AI/IoT 시대의 실생활 문제를 해결합니다 (글로벌 시장 규모 $100B+)."
  },
  "technology": {
    "coreConcept": "GEODNET의 작동 원리는 GNSS 데이터를 블록체인 기반 분산 네트워크로 수집하고 검증하는 데 초점을 맞춥니다. 단계: 1. 노드(마이너) 설치: 사용자가 GEODNET 인증 GNSS 수신기(하드웨어, 가격 $300~700)를 구매해 지붕이나 야외에 설치합니다. 2. 데이터 수집 및 전송: 수신기가 GPS/갈릴레오/베이두 신호를 캡처하고, 대기 오차를 계산해 보정 데이터를 폴리곤 기반 블록체인 네트워크로 전송합니다 (RTK로 cm급 정확도). 3. 검증 및 합의: PoL(Proof-of-Location) 메커니즘과 이중화(truth validation) 프로토콜로 데이터 정확성을 다중 노드 상호 검증; 비정상 노드 자동 배제. 4. 데이터 배포 및 사용: 검증된 데이터가 API로 제공되며, 사용자는 GEOD 토큰으로 구매 (예: 자율주행 앱 통합). 5. 네트워크 확장: AI 최적화로 품질 향상; 현재 7,000+ 노드 운영 중 (6대륙 150국가, 2024년 10월 X 확인).",
    "keyFeatures": [
      {
        "name": "차별점",
        "description": "기존 중앙화 RTK(Trimble 등)는 고비용/독점 vs. GEODNET은 DePIN으로 비용 1/10~1/100, 탈중앙성으로 데이터 투명성/보안 강화 (블록체인 로그), 빠른 확장 (커뮤니티 주도). Helium(무선 IoT)과 비교해 GNSS 특화 cm급 정확도 우위; Hivemapper(지도 매핑)보다 실시간 위치 데이터에 강함. 혁신: 토큰 인센티브로 개인 참여 유도, 실시간 RTK 보정으로 밀리초 응답.",
        "details": "기존 GNSS 시스템(예: 미국 정부의 GPS)은 중앙화되어 있어 비용이 높고(연간 수백만 달러), 데이터가 제한적이며, 보안 취약점(스푸핑 공격)이 있습니다. GEODNET의 혁신은 DePIN 모델로, 탈중앙성을 강조합니다: 노드 소유자가 데이터를 직접 기여해 비용을 90% 이상 줄입니다 (공식 문서: cm급 정확도 데이터가 기존 1/10 가격). 속도 면에서는 실시간 RTK로 밀리초 단위 응답을 제공하며, 블록체인으로 보안을 강화 – 데이터 위조를 방지합니다."
      },
      {
        "name": "기술 용어 해설",
        "description": "GNSS: GPS 등 위성 신호를 종합하는 시스템; '전 세계 위치 별자리 지도' 비유. RTK: cm급 위치 보정; '정답지 친구가 실시간 오답 수정' 비유. PoL: 위치 기반 합의; '실제 위치 사진 증명 그룹 채팅' 비유. DePIN: 블록체인으로 물리 인프라 공유; 'Uber처럼 개인 차 공유 네트워크' 비유.",
        "details": "GNSS: Global Navigation Satellite System. 비유: 스마트폰의 GPS 앱처럼, 하늘의 위성들이 당신의 위치를 알려주는 '별자리 지도'입니다. GEODNET은 이 지도를 더 세밀하게 만들어줍니다. RTK (Real-Time Kinematic): cm급 정확도 위치 기술. 비유: 일반 GPS가 '이 도시 어딘가'라고 말한다면, RTK는 '이 테이블 위의 이 잔'이라고 정확히 가리킵니다. 마치 확대경으로 지도를 보는 것. PoL (Proof-of-Location): 위치 증명 합의. 비유: 친구들이 '내가 여기 있어!'라고 사진으로 증명하는 그룹 채팅처럼, 노드들이 실제 위치 데이터를 증명해 네트워크가 믿을 수 있게 합니다. DePIN: Decentralized Physical Infrastructure Network. 비유: Uber처럼 중앙 회사가 아닌, 사람들(운전자)이 직접 차를 공유하는 네트워크 – 여기서는 위치 데이터를 공유합니다."
      }
    ]
  },
  "tokenomics": {
    "tokenName": "GEODNET Token",
    "tokenTicker": "$GEOD",
    "utility": "마이닝 보상, 데이터 구매/판매 (Burn-to-Access: 사용 시 토큰 소각), 거버넌스 투표, API 액세스 결제 (폴리곤 메인넷, 2024년 7월 런칭).",
    "details": "총 공급량: 10억 개 (1,000,000,000 GEOD, 고정). 분배: 채굴/커뮤니티 보상 55~60% (장기 점진 유통), Foundation/재단 20%, 팀/투자자 15~25%, 에코시스템/기타 5~10% (팀 vesting 2년). 인플레이션: 없음, 채굴 보상 반감기 모델로 점진 감소. 디플레이션: 트랜잭션/서비스 수수료 소각 (사용 증가 시 공급 감소, 순환 공급 약 4천만 개)."
  },
  "team": [
    {
      "name": "Mike Horton",
      "role": "CEO",
      "background": "GNSS 20년 경력, Crossbow Technology 창업/매각 (ANELO Photonics CEO).",
      "details": "이전 회사 매각 $1억 이상, 위치 인식·센서 하드웨어·IoT 분야 전문."
    },
    {
      "name": "David Jung",
      "role": "CTO",
      "background": "IoT 하드웨어/특허 보유.",
      "details": "여러 GNSS 특허 보유자, 실생활 기술 배경 강함."
    },
    {
      "name": "Yudan Yi",
      "role": "Chief Scientist",
      "background": "스탠포드 박사, GPS 전문.",
      "details": "학술적 배경으로 기술 신뢰도 강화."
    },
    {
      "name": "기타 팀원",
      "role": "엔지니어/개발자",
      "background": "Qualcomm/Apple/Google 출신 엔지니어, NASA 관련 전문가 (10~15명, 실리콘 밸리 기반, Rootdata 확인).",
      "details": "Blockchain.com 출신 포함, 대부분 GNSS 하드웨어, 저전력 SoC 설계 전문가, 기상·위치 데이터 전문가로 구성."
    }
  ],
  "investors": [
    {
      "name": "Multicoin Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "DePIN 전문, 시장 잠재력 베팅, 총 $15M 투자 중 일부.",
      "details": "Helium 등 DePIN 포트폴리오, GNSS $100B 시장 디스럽션 예상, 2024년 투자."
    },
    {
      "name": "Pantera Capital",
      "type": "VC",
      "tier": "Tier 1",
      "description": "탈중앙 인프라, AI 붐 시너지, 총 $15M 투자 중 일부.",
      "details": "블록체인 업계 존경받는 펀드, 기술 혁신성 투자."
    },
    {
      "name": "Santiago Roel Santos",
      "type": "Angel",
      "tier": "Tier 1",
      "description": "개인 투자자, 총 $15M 투자 중 일부.",
      "details": "크립토 전문 투자자, DePIN 성장 잠재력 베팅."
    },
    {
      "name": "VanEck",
      "type": "Corporate",
      "tier": "Tier 1",
      "description": "전통 금융, 장기 산업 표준 잠재력, 총 $15M 투자 중 일부.",
      "details": "TradFi 거물, 자율주행/스마트 시티 성장 예상."
    },
    {
      "name": "CoinFund",
      "type": "VC",
      "tier": "Tier 2",
      "description": "총 $15M 투자 중 일부.",
      "details": "크립토-블록체인 전문."
    },
    {
      "name": "ParaFi Capital",
      "type": "VC",
      "tier": "Tier 2",
      "description": "총 $15M 투자 중 일부.",
      "details": "DePIN 및 IoT 스페셜리스트."
    },
    {
      "name": "기타 투자자",
      "type": "VC/Angel",
      "tier": null,
      "description": "Borderless Capital, North Island Ventures, Animoca Brands, DACM, IoTeX, JDI Global, Modular Capital, Reverie, Road Capital, Tangent 등, 총 $15M 투자 중 일부.",
      "details": "크립토-블록체인, IoT 전문가들, Web3 + 실물 데이터 융합 베팅."
    }
  ],
  "userActions": {
    "currentActivities": "마이닝: GNSS 하드웨어($299+ Starter Kit) 구매/설치, 앱으로 등록 (옥상 등, 인터넷 연동). 데이터 사용: API로 RTK 데이터 구독 (개발자/기업 대상). 커뮤니티: X/Discord (10,000+ 멤버), 해커톤/웨비나 참여.",
    "airdropPotential": {
      "status": "Medium",
      "reasoning": "현재 대규모 에어드랍 없음; 대신 Testnet 피드백/조기 마이너 리워드 프로그램 (X 및 Docs, 2024년). 예상: 메인넷 후 기여자 에어드랍 가능 (Helium 패턴 근거), 하지만 실제 네트워크 기여 중심 (SuperHex 보너스 등).",
      "details": "X와 Discord에서 '커뮤니티 리ワード 프로그램'을 언급하며, 메인넷 런칭 후(2024년 7월) 초기 기여자 에어드랍을 암시합니다. 비슷한 DePIN 프로젝트(Helium, Render) 패턴과 GEODNET의 백서(40% 토큰이 커뮤니티 보상)로, 노드 운영자나 테스터에게 $GEOD 에어드랍이 있을 수 있습니다. 그러나 공식 발표 없으므로, 리스크 없이 참여하려면 마이닝부터 시작하세요."
    }
  },
  "competitors": [
    {
      "name": "Hivemapper",
      "differentiation": "지도 매핑, vs. GEODNET의 cm급 GNSS 특화 우위.",
      "details": "Hivemapper가 카메라 기반 지도라면, GEODNET은 위성 데이터로 더 과학적입니다 (예: 농업/재난 분야 우위)."
    },
    {
      "name": "Helium",
      "differentiation": "IoT 무선, vs. 위치 데이터 강점.",
      "details": "Helium은 무선 IoT, Hivemapper는 지도 매핑과 비교해 GEODNET의 강점은 GNSS 특화: 위치 데이터의 cm급 정밀도(기존 GPS의 10m vs. GEODNET의 1cm)."
    },
    {
      "name": "Trimble/Leica",
      "differentiation": "중앙화, 고비용 vs. GEODNET 저비용/빠른 확장.",
      "details": "기존 RTK 위치 데이터 벤더(Trimble, Leica 등), 대형 GNSS 인프라 서비스 업체(Topcon 등). GEODNET은 비용 효율, 글로벌 네트워크 효과 (7,000+ 노드), 토큰 인센티브 강점."
    },
    {
      "name": "FOAM/Wayfinder/PocketGNSS",
      "differentiation": "위치 증명 프로토콜이나 초기 단계 프로젝트 vs. GEODNET의 성숙한 네트워크.",
      "details": "간접/잠재 경쟁: ‘위치 데이터’ 중심 DePIN/블록체인 프로젝트, 예: Wayfinder, PocketGNSS 등(성장 초기 단계)."
    }
  ],
  "risks": [
    {
      "type": "기술적",
      "description": "신호 간섭/위조 (날씨, 공격), 노드 환경 편차.",
      "details": "GNSS 신호의 판독·정확도·데이터 위변조 방지 어려움. 노드 설치 환경(지형, 기상 등)에 따라 데이터 품질 편차. 하드웨어/펌웨어 취약점, 보안 사고 가능성."
    },
    {
      "type": "사업적",
      "description": "규제 (데이터 프라이버시, GDPR), 대기업 경쟁/채택 지연.",
      "details": "블록체인/토큰 기반 데이터 인프라에 대한 규제(예: 각국 데이터 보안, 토큰 증권성 논란). ‘채굴형 DePIN’의 보상/보상감소, 토큰 가치하락 시 노드 운영자 이탈 위험. 상업적 레퍼런스 확보, 메인클라이언트 유치 등 ‘네트워크 효과’가 수익화까지 확보되어야 함."
    },
    {
      "type": "시장",
      "description": "토큰 변동성 (운영자 이탈), DePIN 버블 붕괴, 콜드 스타트 문제 (지역 불균형).",
      "details": "Helium, Hivemapper 등 DePIN계 대기업의 시장 점유율, 블록체인 인프라간의 병목/중복. Web3 시장 내 ‘실사용 수요’ 확대 속도에 대한 불확실성(과점→초기흥미→장기정착 과정). 네트워크 밀도 불균형: 수익성이 높은 북미, 유럽 등지에만 마이너가 집중되고 다른 지역의 커버리지가 부족해지면 '글로벌' 네트워크라는 가치가 퇴색될 수 있습니다."
    },
    {
      "type": "기타",
      "description": "하드웨어 내구성/유지보수, 법적 이슈 (인증/데이터 이전).",
      "details": "대량 참여자 네트워크 내 고장/업데이트/교체율이 단기 운영전략에 직접 영향. 국가별 GNSS 데이터의 해외 이전, IoT 하드웨어 인증, 블록체인사업 규제 등 관련 이슈."
    }
  ]
}