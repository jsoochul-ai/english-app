# data.py : 글로벌 표준 회화 커리큘럼 (정석 심화판)

scenarios = {
    # -------------------------------------------------------------
    # ☕ [일상 필수] 카페 및 식당
    # -------------------------------------------------------------
    "☕ [카페] 상세한 음료 주문하기": {
        "description": "카페에서 음료의 사이즈, 얼음 양을 조절하고 디저트까지 주문하는 가장 표준적인 상황입니다.",
        "dialogue": [
            ("직원", "Welcome. What can I get for you today?", "환영합니다. 오늘 어떤 걸로 주문하시겠어요?"),
            ("나", "I'd like an iced Americano, please.", "아이스 아메리카노 한 잔 부탁드립니다."),
            ("직원", "What size would you like? We have tall, grande, and venti.", "사이즈는 어떤 걸로 하시겠어요? 톨, 그란데, 벤티가 있습니다."),
            ("나", "Grande, please. Oh, can I get it with less ice?", "그란데로 주세요. 아, 얼음은 조금만 넣어주실 수 있나요?"),
            ("직원", "Sure, less ice. Would you like anything to eat with that?", "네, 얼음 적게요. 같이 드실 음식도 주문하시겠어요?"),
            ("나", "Yes, I'll take a slice of the cheesecake.", "네, 치즈 케이크 한 조각 할게요."),
            ("직원", "Great. Is that for here or to go?", "좋습니다. 드시고 가시나요, 아니면 포장해 드릴까요?"),
            ("나", "For here. Can I also get the Wi-Fi password?", "먹고 갈게요. 와이파이 비밀번호도 알 수 있을까요?"),
            ("직원", "It's printed on the bottom of your receipt. Your total is $12.", "영수증 하단에 인쇄되어 있습니다. 총 12달러입니다."),
            ("나", "Here's my card. Thanks.", "여기 제 카드입니다. 감사합니다.")
        ]
    },

    # -------------------------------------------------------------
    # 🗺️ [여행 필수] 길 찾기 및 교통
    # -------------------------------------------------------------
    "🚇 [길 찾기] 목적지 묻고 길 안내받기": {
        "description": "해외에서 길을 잃었을 때 행인에게 목적지까지 가는 방법을 상세히 묻는 상황입니다.",
        "dialogue": [
            ("나", "Excuse me, I think I'm lost. Can you help me?", "실례합니다, 제가 길을 잃은 것 같아요. 좀 도와주시겠어요?"),
            ("행인", "Of course! Where are you trying to go?", "물론이죠! 어디로 가려고 하시나요?"),
            ("나", "I'm looking for the National Museum. Is it far from here?", "국립 박물관을 찾고 있어요. 여기서 먼가요?"),
            ("행인", "Not too far. It's about a 15-minute walk.", "별로 멀지 않아요. 걸어서 15분 정도 걸립니다."),
            ("나", "Could you tell me the best way to get there?", "그곳으로 가는 가장 좋은 길을 알려주시겠어요?"),
            ("행인", "Go straight down this street for two blocks, then turn left at the bank.", "이 길을 따라 두 블록 직진하시고, 은행에서 왼쪽으로 도세요."),
            ("나", "Straight for two blocks, then left at the bank. Got it.", "두 블록 직진 후 은행에서 왼쪽이요. 알겠습니다."),
            ("행인", "Yes. You'll see the museum on your right, next to a large park.", "네. 큰 공원 옆, 오른쪽에서 박물관을 보실 수 있을 거예요."),
            ("나", "Thank you so much for your help.", "도와주셔서 정말 감사합니다."),
            ("행인", "No problem. Have a safe trip!", "천만에요. 안전한 여행 되세요!")
        ]
    },

    # -------------------------------------------------------------
    # 🗣️ [사교 및 친목] 원어민과의 스몰토크
    # -------------------------------------------------------------
    "🤝 [스몰토크] 주말 일상 나누기": {
        "description": "외국인 친구나 동료와 주말에 무엇을 했는지 자연스럽게 묻고 답하는 필수 대화입니다.",
        "dialogue": [
            ("친구", "Hey, how was your weekend?", "안녕, 주말 잘 보냈어?"),
            ("나", "It was pretty good, thanks. I just relaxed at home mostly.", "꽤 좋았어, 고마워. 주로 집에서 쉬었지."),
            ("친구", "That sounds nice. Did you watch any good movies?", "좋네. 재밌는 영화라도 봤어?"),
            ("나", "Yeah, I watched a new action movie on Netflix. It was really exciting.", "응, 넷플릭스에서 새로운 액션 영화를 봤는데 정말 재밌더라."),
            ("친구", "I think I know which one you're talking about. I want to see it too.", "무슨 영화 말하는지 알 것 같아. 나도 보고 싶었는데."),
            ("나", "You should! What about you? What did you do this weekend?", "꼭 봐! 너는 어때? 이번 주말에 뭐 했어?"),
            ("친구", "I went hiking with some friends on Saturday morning.", "토요일 아침에 친구들이랑 등산 다녀왔어."),
            ("나", "Wow, the weather was perfect for hiking. Was the trail difficult?", "와, 등산하기 완벽한 날씨였지. 코스는 안 어려웠어?"),
            ("친구", "A little bit, but the view from the top was totally worth it.", "조금 어려웠는데, 정상에서 본 경치가 완전 그럴 만한 가치가 있었지."),
            ("나", "I'd love to go with you guys next time.", "다음에는 나도 같이 가고 싶다.")
        ]
    },

    # -------------------------------------------------------------
    # 🏢 [비즈니스] 업무 및 네트워킹
    # -------------------------------------------------------------
    "🏢 [비즈니스] 첫인사와 명함 교환": {
        "description": "외국인 클라이언트나 파트너를 처음 만나 정중하게 인사하고 미팅을 시작하는 상황입니다.",
        "dialogue": [
            ("나", "Hello, you must be Mr. Smith from the marketing department.", "안녕하세요, 마케팅 부서의 스미스 씨 맞으시죠."),
            ("바이어", "Yes, that's me. It's a pleasure to finally meet you in person.", "네, 맞습니다. 드디어 직접 뵙게 되어 반갑습니다."),
            ("나", "The pleasure is mine. I'm Sarah, the project manager.", "저야말로 반갑습니다. 저는 프로젝트 매니저 사라입니다."),
            ("바이어", "Nice to meet you, Sarah. Here is my business card.", "만나서 반갑습니다, 사라 씨. 제 명함입니다."),
            ("나", "Thank you. And here is mine. Did you have any trouble finding our office?", "감사합니다. 그리고 이건 제 명함입니다. 저희 사무실 찾는데 어려움은 없으셨나요?"),
            ("바이어", "Not at all. The directions you sent me were very clear.", "전혀요. 보내주신 오시는 길이 아주 명확했습니다."),
            ("나", "I'm glad to hear that. Would you like some coffee or tea before we start?", "다행이네요. 시작하기 전에 커피나 차 좀 준비해 드릴까요?"),
            ("바이어", "A cup of black coffee would be great, thank you.", "블랙커피 한 잔이면 좋겠습니다. 감사합니다."),
            ("나", "Coming right up. Let's head to the conference room.", "금방 준비해 드리겠습니다. 회의실로 가시죠."),
            ("바이어", "Sounds good. Lead the way.", "좋습니다. 안내해 주시죠.")
        ]
    }
}
