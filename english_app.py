# data.py 파일에 이 내용을 통째로 복사해서 붙여넣으세요!

scenarios = {
    # --- [공항 및 비행기] ---
    "✈️ [공항 1] 탑승 수속 (Check-in)": {
        "description": "공항 카운터에서 비행기 탑승 수속을 하고 수하물을 부치는 상황입니다.",
        "dialogue": [
            ("직원", "Where are you flying to today?", "오늘 어디로 가시나요?"),
            ("나", "I'm flying to New York.", "뉴욕으로 갑니다."),
            ("직원", "May I see your passport and ticket, please?", "여권과 항공권을 보여주시겠습니까?"),
            ("나", "Here you are. Can I get an aisle seat?", "여기 있습니다. 통로 쪽 좌석으로 받을 수 있을까요?"),
            ("직원", "Sure. Are you checking any bags?", "네. 위탁 수하물이 있으신가요?"),
            ("나", "Yes, just this one suitcase.", "네, 이 캐리어 하나입니다.")
        ]
    },
    "✈️ [공항 2] 보안 검색대 (Security Check)": {
        "description": "보안 검색대를 통과하며 직원의 지시에 따르는 상황입니다.",
        "dialogue": [
            ("직원", "Please empty your pockets and put your electronics in the bin.", "주머니를 비우시고 전자기기는 바구니에 넣어주세요."),
            ("나", "Do I need to take off my shoes?", "신발도 벗어야 하나요?"),
            ("직원", "Yes, shoes and jackets off, please.", "네, 신발과 재킷 모두 벗어주세요."),
            ("나", "Okay. Is this laptop fine here?", "알겠습니다. 노트북은 여기 두면 되나요?"),
            ("직원", "Yes. Now step through the scanner, please.", "네. 이제 스캐너를 통과해 주세요.")
        ]
    },
    "✈️ [공항 3] 기내 서비스 요청 (In-flight)": {
        "description": "비행기 안에서 승무원에게 필요한 것을 요청하는 상황입니다.",
        "dialogue": [
            ("승무원", "Would you like something to drink?", "마실 것 좀 준비해 드릴까요?"),
            ("나", "Can I get a cup of water and some apple juice?", "물 한 잔이랑 사과 주스 좀 주시겠어요?"),
            ("승무원", "Here you go. Anything else?", "여기 있습니다. 더 필요한 건 없으신가요?"),
            ("나", "Could I also get an extra blanket? It's a bit cold.", "담요를 하나 더 받을 수 있을까요? 조금 춥네요.")
        ]
    },
    "✈️ [공항 4] 수하물 분실 신고 (Lost Baggage)": {
        "description": "도착지에서 위탁 수하물이 나오지 않아 분실 신고를 하는 아찔한 상황입니다.",
        "dialogue": [
            ("나", "Excuse me, my baggage hasn't come out yet.", "실례합니다, 제 수하물이 아직 안 나왔어요."),
            ("직원", "May I see your baggage claim tag?", "수하물 표를 보여주시겠습니까?"),
            ("나", "Here it is. It's a large silver suitcase.", "여기 있습니다. 큰 은색 캐리어입니다."),
            ("직원", "Let me check the system. Please fill out this form.", "시스템을 확인해 보겠습니다. 이 서류를 작성해 주세요.")
        ]
    },

    # --- [교통 수단] ---
    "🚕 [교통 1] 택시 타기 (Taking a Taxi)": {
        "description": "공항에서 택시를 타고 목적지를 말하며 이동하는 상황입니다.",
        "dialogue": [
            ("기사", "Where to, sir?", "어디로 모실까요, 손님?"),
            ("나", "To the Hilton Hotel downtown, please.", "시내에 있는 힐튼 호텔로 가주세요."),
            ("기사", "Sure thing. It'll take about 40 minutes.", "알겠습니다. 40분 정도 걸립니다."),
            ("나", "How much will it cost roughly?", "대략 요금이 얼마나 나올까요?"),
            ("기사", "It should be around 50 dollars.", "50달러 정도 될 겁니다.")
        ]
    },
    "🚇 [교통 2] 지하철/버스 길 묻기 (Directions)": {
        "description": "현지에서 지하철역이나 목적지로 가는 길을 물어보는 상황입니다.",
        "dialogue": [
            ("나", "Excuse me, could you tell me how to get to the nearest subway station?", "실례지만, 가장 가까운 지하철역으로 가는 길을 알려주시겠어요?"),
            ("행인", "Go straight for two blocks and turn right.", "두 블록 직진하시고 오른쪽으로 도세요."),
            ("나", "Is it far to walk?", "걸어가기엔 먼가요?"),
            ("행인", "Not at all. It's only a 5-minute walk.", "전혀요. 걸어서 5분밖에 안 걸립니다.")
        ]
    },

    # --- [호텔 및 숙소] ---
    "🏨 [숙소 1] 호텔 체크인 (Hotel Check-in)": {
        "description": "예약한 호텔에 도착해 체크인하고 객실을 안내받는 상황입니다.",
        "dialogue": [
            ("직원", "Welcome! How can I help you?", "환영합니다! 무엇을 도와드릴까요?"),
            ("나", "I'd like to check in. The reservation is under Kim.", "체크인하고 싶습니다. 김 이름으로 예약했습니다."),
            ("직원", "I see your reservation for three nights. May I have your credit card for incidentals?", "3박 예약 확인되었습니다. 보증금 결제를 위해 신용카드를 주시겠습니까?"),
            ("나", "Here you are. What time is breakfast served?", "여기 있습니다. 조식은 몇 시에 제공되나요?"),
            ("직원", "Breakfast is from 7 AM to 10 AM on the first floor.", "조식은 1층에서 오전 7시부터 10시까지입니다.")
        ]
    },
    "🏨 [숙소 2] 룸서비스 및 수건 요청 (Room Service)": {
        "description": "객실에서 프론트 데스크로 전화해 필요한 물품을 요청하는 상황입니다.",
        "dialogue": [
            ("직원", "Front desk, how may I help you?", "프론트 데스크입니다, 무엇을 도와드릴까요?"),
            ("나", "Hi, I'm in room 402. Could we get some extra towels?", "안녕하세요, 402호입니다. 수건 좀 더 받을 수 있을까요?"),
            ("직원", "Of course. Anything else you need?", "물론입니다. 더 필요하신 게 있나요?"),
            ("나", "Yes, could you also send up two bottles of water?", "네, 생수도 두 병 올려보내 주시겠어요?"),
            ("직원", "I'll send someone right up.", "바로 직원을 올려보내겠습니다.")
        ]
    },
    "🏨 [숙소 3] 객실 문제 해결 (Room Issues)": {
        "description": "객실의 에어컨이나 화장실에 문제가 생겨 수리를 요청하는 상황입니다.",
        "dialogue": [
            ("나", "I have a problem in my room. The air conditioner isn't working.", "방에 문제가 좀 있습니다. 에어컨이 작동하지 않아요."),
            ("직원", "I apologize for the inconvenience. What is your room number?", "불편을 드려 죄송합니다. 객실 번호가 어떻게 되시나요?"),
            ("나", "It's room 505. It's too hot in here.", "505호입니다. 안이 너무 덥네요."),
            ("직원", "I will send a maintenance person immediately.", "즉시 수리 직원을 보내겠습니다.")
        ]
    },
    "🏨 [숙소 4] 체크아웃 및 짐 보관 (Check-out)": {
        "description": "호텔 체크아웃을 하며 남은 시간 동안 짐을 맡겨두는 상황입니다.",
        "dialogue": [
            ("직원", "Are you checking out? How was your stay?", "체크아웃하시나요? 머무시는 동안 어떠셨습니까?"),
            ("나", "It was wonderful, thank you. Here is the key.", "정말 좋았습니다, 감사합니다. 여기 키 있습니다."),
            ("직원", "You're all set. Do you need a taxi to the airport?", "결제 완료되었습니다. 공항 가는 택시가 필요하신가요?"),
            ("나", "No, thanks. But can I leave my luggage here until 3 PM?", "아니요, 괜찮습니다. 하지만 오후 3시까지 여기에 짐을 좀 맡길 수 있을까요?"),
            ("직원", "Certainly. I'll give you a baggage tag.", "물론입니다. 수하물 보관증을 드리겠습니다.")
        ]
    }
}
