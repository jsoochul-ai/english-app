import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="나만의 영어 단짝", page_icon="⛳")

st.markdown("""
    <style>
    .stApp { background-color: #1B263B; color: #F8F9FA; }
    .big-english { font-size: 28px !important; font-weight: bold; text-align: center; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

question = "The weather is perfect for a round today. Shall we walk slowly?"
st.markdown(f'<p class="big-english">{question}</p>', unsafe_allow_html=True)

# 질문 음성 듣기
tts = gTTS(text=question, lang='en', slow=False)
audio_fp = io.BytesIO()
tts.write_to_fp(audio_fp)
st.audio(audio_fp, format='audio/mp3')

with st.expander("한글 뜻 보기"):
    st.write("오늘 라운딩하기 딱 좋은 날씨네요. 천천히 걸어볼까요?")

st.write("---")

# 스마트폰에서 더 잘 작동하는 방식의 녹음
audio_value = st.audio_input("🎙️ 터치해서 영어로 대답하세요")

if audio_value:
    st.success("녹음 완료! 정답을 확인하세요.")
    st.audio(audio_value)
    
    # 정답 표시
    st.info("💡 모범 답안")
    answer = "Yes, let's go! The weather is great."
    st.write(f"**{answer}**")
    
    # 정답 음성
    tts_answer = gTTS(text=answer, lang='en', slow=False)
    answer_fp = io.BytesIO()
    tts_answer.write_to_fp(answer_fp)
    st.audio(answer_fp, format='audio/mp3')
