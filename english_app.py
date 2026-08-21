import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder

# 화면을 넓게 쓰도록 layout="wide" 추가
st.set_page_config(page_title="나만의 영어 단짝", page_icon="🗣️", layout="wide")

# -------------------------------------------------------------
# 📚 무한 대화 은행 (이곳에 시나리오를 계속 추가할 수 있습니다)
# -------------------------------------------------------------
scenarios = {
    "⛳ 파크골프 라운딩": {
        "description": "해외 파크골프장에 도착해 체크인하고 라운딩을 시작합니다.",
        "image": "https://images.unsplash.com/photo-1587174486073-ae5e5cff23aa?q=80&w=1000&auto=format&fit=crop",
        "dialogue": [
            ("직원", "Hello! Welcome to our park golf club. Do you have a reservation?", "안녕하세요! 저희 파크골프장에 오신 것을 환영합니다. 예약하셨나요?"),
            ("나", "Yes, I booked a morning tee time under the name Kim.", "네, 김(Kim)이라는 이름으로 오전 티타임을 예약했습니다."),
            ("직원", "Great! Do you need to rent any clubs or balls today?", "확인되었습니다! 오늘 골프채나 공 대여가 필요하신가요?"),
            ("나", "Yes, please. I'd like to rent one park golf club and two balls.", "네, 부탁합니다. 파크골프 채 하나와 공 두 개를 대여하고 싶어요.")
        ]
    },
    "✈️ 공항 입국 심사": {
        "description": "해외 여행의 첫 관문! 긴장되는 입국 심사대에서 심사관의 질문에 대답합니다.",
        "image": "https://images.unsplash.com/photo-1436491865332-7a615061c4ca?q=80&w=1000&auto=format&fit=crop",
        "dialogue": [
            ("직원", "May I see your passport and arrival card, please?", "여권과 입국 신고서를 보여주시겠습니까?"),
            ("나", "Here they are.", "여기 있습니다."),
            ("직원", "What is the purpose of your visit?", "방문 목적이 무엇인가요?"),
            ("나", "I'm here for traveling.", "여행하러 왔습니다."),
            ("직원", "How long will you be staying?", "얼마나 머무르실 예정인가요?"),
            ("나", "I will be staying for 5 days.", "5일 동안 머무를 예정입니다.")
        ]
    }
}

# -------------------------------------------------------------
# 🎨 화면 구성 시작
# -------------------------------------------------------------
# 왼쪽 사이드바 (주제 선택)
st.sidebar.title("📚 학습 주제 선택")
selected_topic = st.sidebar.radio("원하는 상황을 고르세요:", list(scenarios.keys()))

# 선택된 데이터 불러오기
current_data = scenarios[selected_topic]
dialogue = current_data["dialogue"]

# 메인 화면 제목과 이미지 출력 (시각 테마)
st.title(selected_topic)
st.caption(current_data["description"])
st.image(current_data["image"], use_column_width=True)
st.write("---")

# 3개의 탭 생성
tab1, tab2, tab3 = st.tabs(["📖 전체 대화", "🗣️ 한 문장 연습", "🎭 실전 롤플레잉"])

with tab1:
    st.subheader("1. 대화 흐름 파악하기")
    st.write("🎧 **전체 대화 이어서 듣기**")
    full_english_text = " ".join([eng for role, eng, kor in dialogue])
    tts_full = gTTS(text=full_english_text, lang='en', slow=False)
    audio_io_full = io.BytesIO()
    tts_full.write_to_fp(audio_io_full)
    st.audio(audio_io_full, format='audio/mp3')
    
    st.write("---")
    for role, eng, kor in dialogue:
        if role == "직원":
            st.info(f"**직원:** {eng} \n\n({kor})")
        else:
            st.success(f"**나:** {eng} \n\n({kor})")

with tab2:
    st.subheader("2. 문장별 집중 연습")
    options = [f"[{role}] {eng}" for role, eng, kor in dialogue]
    selected_option = st.selectbox("연습할 문장을 고르세요:", options)
    
    idx = options.index(selected_option)
    role, eng_text, kor_text = dialogue[idx]
    st.write(f"**한글 뜻:** {kor_text}")
    
    tts_sentence = gTTS(text=eng_text, lang='en', slow=False)
    audio_io_sentence = io.BytesIO()
    tts_sentence.write_to_fp(audio_io_sentence)
    st.audio(audio_io_sentence, format='audio/mp3')

with tab3:
    st.subheader("3. 실전 롤플레잉")
    
    # 턴 수에 맞게 단계 자동 생성
    turns = [f"{i+1}단계" for i in range(len(dialogue)//2)]
    step = st.radio("진행할 대화 단계를 선택하세요:", turns, horizontal=True)
    
    step_idx = turns.index(step) * 2
    staff_turn = dialogue[step_idx]
    my_turn = dialogue[step_idx + 1]
    
    st.info(f"**직원:** {staff_turn[1]} \n\n({staff_turn[2]})")
    tts_staff = gTTS(text=staff_turn[1], lang='en', slow=False)
    audio_io_staff = io.BytesIO()
    tts_staff.write_to_fp(audio_io_staff)
    st.audio(audio_io_staff, format='audio/mp3')
    
    st.write("---")
    st.write("👇 **내가 대답할 문장:**")
    st.success(f"**나:** {my_turn[1]} \n\n({my_turn[2]})")
    
    audio_value = audio_recorder(text="터치하여 말하기", icon_size="2x", pause_threshold=3.0)
    if audio_value:
        st.write("✅ **녹음 완료!** 내 목소리를 들어보세요:")
        st.audio(audio_value)
