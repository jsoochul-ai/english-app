import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import re
from data import scenarios

# 📱 1. 페이지 기본 설정
st.set_page_config(page_title="나만의 영어 단짝", page_icon="🎤", layout="centered")

if 'my_records' not in st.session_state:
    st.session_state.my_records = []

# 🎨 2. 예쁜 카드 디자인 (CSS)
st.markdown("""
<style>
    .title-text { text-align: center; font-size: 24px; font-weight: bold; color: #1f3b4d; margin-top: 10px; }
    .subtitle-text { text-align: center; font-size: 15px; color: #666; margin-bottom: 20px; }
    .sentence-card { padding: 15px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.05); margin-bottom: 15px; }
    .role-label { font-size: 13px; font-weight: bold; margin-bottom: 5px; }
    .eng-text { font-size: 18px; font-weight: bold; color: #333; }
    .kor-text { font-size: 14px; color: #777; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

def clean_text(text):
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()

# 📌 3. 주제 선택 (모든 탭에 공통 적용)
selected_topic = st.selectbox("👇 학습할 대본을 선택하세요:", list(scenarios.keys()))
current_data = scenarios[selected_topic]
dialogue = current_data["dialogue"]

st.markdown(f"<div class='title-text'>{selected_topic.split(']')[1].strip()}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle-text'>{current_data['description']}</div>", unsafe_allow_html=True)
st.write("---")

# 📑 4. 세 가지 기능 탭 분리
tab1, tab2, tab3 = st.tabs(["📖 전체 대본", "🎙️ 실전 롤플레잉", "📚 내 기록"])

# --- [첫 번째 탭: 눈으로 보고 귀로 듣기] ---
with tab1:
    if st.button("🔊 전체 대화 이어서 듣기", use_container_width=True):
        full_english = " ".join([eng for role, eng, kor in dialogue])
        tts = gTTS(text=full_english, lang='en', slow=False)
        audio_io = io.BytesIO()
        tts.write_to_fp(audio_io)
        st.audio(audio_io, format='audio/mp3')
    
    st.write("---")
    for role, eng, kor in dialogue:
        if role in ["직원", "손님", "친구", "승무원", "기사", "행인"]:
            # 상대방: 회색
            st.markdown(f"<div class='sentence-card' style='background-color: #f8f9fa; border-left: 4px solid #adb5bd;'><div class='role-label' style='color: #6c757d;'>{role}</div><div class='eng-text'>{eng}</div><div class='kor-text'>{kor}</div></div>", unsafe_allow_html=True)
        else:
            # 나: 파란색
            st.markdown(f"<div class='sentence-card' style='background-color: #e3f2fd; border-left: 4px solid #1976d2;'><div class='role-label' style='color: #1976d2;'>나</div><div class='eng-text'>{eng}</div><div class='kor-text'>{kor}</div></div>", unsafe_allow_html=True)

# --- [두 번째 탭: 회원님이 찾으시던 바로 그 학습 기능!] ---
with tab2:
    st.write("🗣️ **단계별로 상대방의 말을 듣고 대답해 보세요!**")
    turns = [f"{i+1}단계" for i in range(len(dialogue)//2)]
    step = st.radio("진행할 상황 선택:", turns, horizontal=True)
    
    step_idx = turns.index(step) * 2
    staff_turn = dialogue[step_idx]
    my_turn = dialogue[step_idx + 1]
    
    # 1. 상대방의 질문
    st.markdown(f"<div class='sentence-card' style='background-color: #f8f9fa; border-left: 4px solid #adb5bd;'><div class='role-label' style='color: #6c757d;'>{staff_turn[0]}의 말</div><div class='eng-text'>{staff_turn[1]}</div><div class='kor-text'>{staff_turn[2]}</div></div>", unsafe_allow_html=True)
    tts_staff = gTTS(text=staff_turn[1], lang='en', slow=False)
    audio_io_staff = io.BytesIO()
    tts_staff.write_to_fp(audio_io_staff)
    st.audio(audio_io_staff, format='audio/mp3')
    
    st.write("👇 **내가 대답할 정답 문장:**")
    st.markdown(f"<div class='sentence-card' style='background-color: #e3f2fd; border-left: 4px solid #1976d2;'><div class='role-label' style='color: #1976d2;'>나</div><div class='eng-text'>{my_turn[1]}</div><div class='kor-text'>{my_turn[2]}</div></div>", unsafe_allow_html=True)
    
    # 2. 내 대답 녹음 및 채점
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    audio_value = audio_recorder(text="마이크를 누르고 말씀하세요", icon_size="2x", pause_threshold=3.0)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if audio_value:
        st.write("⏳ AI가 발음을 분석 중입니다...")
        try:
            r = sr.Recognizer()
            audio_file = io.BytesIO(audio_value)
            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
            
            recognized_text = r.recognize_google(audio_data, language="en-US")
            st.write(f"📝 **AI가 들은 내 목소리:** {recognized_text}")
            
            target_clean = clean_text(my_turn[1])
            recog_clean = clean_text(recognized_text)
            
            if target_clean == recog_clean:
                st.success("🎉 100점! 원어민과 똑같이 발음하셨네요!")
            elif recog_clean in target_clean or target_clean in recog_clean:
                st.info("👍 훌륭해요! 핵심 단어가 전달되어 의사소통이 가능합니다.")
            else:
                st.error("💪 다르게 인식되었어요! 원어민 발음을 다시 듣고 시도해 보세요.")
            
            # 내 기록에 추가
            st.session_state.my_records.append({"topic": selected_topic, "said": recognized_text})
            
        except sr.UnknownValueError:
            st.error("앗, 목소리가 잘 안 들렸어요. 스마트폰 마이크 권한을 허용했는지 확인해 주세요!")
        except Exception as e:
            st.error("오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")

# --- [세 번째 탭: 내 학습 기록 보관소] ---
with tab3:
    st.caption("내가 마이크로 연습했던 문장들이 시간순으로 쌓입니다. (앱을 껐다 켜면 초기화됩니다)")
    if len(st.session_state.my_records) == 0:
        st.info("아직 녹음된 기록이 없습니다. '실전 롤플레잉' 탭에서 연습을 시작해 보세요!")
    else:
        for record in reversed(st.session_state.my_records):
            st.markdown(f"<div class='sentence-card' style='background-color: #ffffff; border: 1px solid #e0e0e0;'><span style='color: #888; font-size: 12px;'>{record['topic']}</span><br><span class='eng-text'>🗣️ {record['said']}</span></div>", unsafe_allow_html=True)
