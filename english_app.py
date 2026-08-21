import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="나만의 영어 단짝", page_icon="🗣️")

st.title("⛳ 실전 파크골프 영어 회화")
st.write("상황: 파크골프장에 도착해 체크인을 하고 장비를 빌려 라운딩을 시작합니다.")

# 3개의 탭 생성
tab1, tab2, tab3 = st.tabs(["📖 전체 대화", "🗣️ 한 문장 연습", "🎭 실전 롤플레잉"])

dialogue = [
    ("직원", "Hello, I'd like to check in for my tee time.", "안녕하세요, 티타임 체크인하려고 합니다."),
    ("나", "It's under Kim. I also need to rent a park golf club.", "예약자 이름은 김입니다. 파크골프 채도 하나 빌려야 해요."),
    ("직원", "Here is your club. The weather is perfect for a round today!", "여기 채 있습니다. 오늘 라운딩하기 딱 좋은 날씨네요!"),
    ("나", "Thank you. Shall we walk slowly?", "감사합니다. 천천히 걸어가 볼까요?")
]

with tab1:
    st.subheader("1. 대화 흐름 파악하기")
    
    st.write("🎧 **전체 대화 한 번에 이어서 듣기**")
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
    st.subheader("2. 내 대사 집중 연습")
    my_lines = {eng: kor for role, eng, kor in dialogue if role == "나"}
    selected_eng = st.selectbox("연습할 문장을 고르세요:", list(my_lines.keys()))
    st.write(f"**뜻:** {my_lines[selected_eng]}")
    
    tts = gTTS(text=selected_eng, lang='en', slow=False)
    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    st.audio(audio_io, format='audio/mp3')

with tab3:
    st.subheader("3. 실전 롤플레잉 (직원의 말에 대답해 보세요!)")
    st.info(f"**직원:** {dialogue[2][1]} \n\n(오늘 라운딩하기 딱 좋은 날씨네요!)")
    st.write("👇 마이크를 한 번 톡 누르고 대답한 뒤, 다시 터치해서 완료하세요.")
    st.success(f"**나:** {dialogue[3][1]} \n\n(감사합니다. 천천히 걸어가 볼까요?)")
    
    # 💡 녹음이 2초 만에 끊기지 않도록 대기 시간(pause_threshold)을 3초로 늘렸습니다!
    audio_value = audio_recorder(text="마이크 터치 (3초 대기 가능)", icon_size="2x", pause_threshold=3.0)
    
    if audio_value:
        st.write("✅ 훌륭합니다! 실전처럼 아주 잘 대답하셨습니다.")
        st.audio(audio_value)
