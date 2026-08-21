import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import re
from data import scenarios

st.set_page_config(page_title="나만의 영어 단짝", page_icon="🎤", layout="centered")

# 💾 세션 상태 (페이지 이동 및 내 기록 저장용)
if 'page' not in st.session_state:
    st.session_state.page = 'cover'  # 첫 화면은 'cover' (표지)
if 'my_records' not in st.session_state:
    st.session_state.my_records = []

# 🎨 공통 CSS 디자인 (표지용 디자인 추가)
st.markdown("""
<style>
    .cover-title { text-align: center; font-size: 32px; font-weight: bold; color: #1f3b4d; margin-top: 60px; margin-bottom: 10px; }
    .cover-subtitle { text-align: center; font-size: 16px; color: #666; margin-bottom: 60px; }
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

# 페이지 이동 함수
def go_to_page(page_name):
    st.session_state.page = page_name

# ==========================================
# 🏠 1. 첫 화면 (대문 / 표지 페이지)
# ==========================================
if st.session_state.page == 'cover':
    st.markdown("<div class='cover-title'>✈️ 나만의 영어 단짝</div>", unsafe_allow_html=True)
    st.markdown("<div class='cover-subtitle'>하루 10분, 나를 위한 맞춤형 회화 도서관</div>", unsafe_allow_html=True)
    
    st.write("---")
    
    # 3개의 메인 버튼
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📖\n1. 오늘의\n학습", use_container_width=True):
            go_to_page('today')
            st.rerun()
    with col2:
        if st.button("🔄\n2. 어제\n복습", use_container_width=True):
            go_to_page('yesterday')
            st.rerun()
    with col3:
        if st.button("🚀\n3. 내일\n예습", use_container_width=True):
            go_to_page('tomorrow')
            st.rerun()
            
    st.write("---")
    st.info("💡 **[1. 오늘의 학습]**을 눌러 우리가 만든 회화 연습을 시작해 보세요!")

# ==========================================
# 📖 2. 오늘의 학습 (기존에 만들었던 메인 화면)
# ==========================================
elif st.session_state.page == 'today':
    # 뒤로가기 버튼
    if st.button("🔙 첫 화면으로 돌아가기"):
        go_to_page('cover')
        st.rerun()
        
    selected_topic = st.selectbox("👇 학습할 대본을 선택하세요:", list(scenarios.keys()))
    current_data = scenarios[selected_topic]
    dialogue = current_data["dialogue"]

    st.markdown(f"<div class='title-text'>{selected_topic.split(']')[1].strip()}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle-text'>{current_data['description']}</div>", unsafe_allow_html=True)
    st.write("---")

    tab1, tab2, tab3 = st.tabs(["📖 전체 대본", "🎙️ 실전 롤플레잉", "📚 내 기록"])

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
                st.markdown(f"<div class='sentence-card' style='background-color: #f8f9fa; border-left: 4px solid #adb5bd;'><div class='role-label' style='color: #6c757d;'>{role}</div><div class='eng-text'>{eng}</div><div class='kor-text'>{kor}</div></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='sentence-card' style='background-color: #e3f2fd; border-left: 4px solid #1976d2;'><div class='role-label' style='color: #1976d2;'>나</div><div class='eng-text'>{eng}</div><div class='kor-text'>{kor}</div></div>", unsafe_allow_html=True)

    with tab2:
        st.write("🗣️ **단계별로 상대방의 말을 듣고 대답해 보세요!**")
        turns = [f"{i+1}단계" for i in range(len(dialogue)//2)]
        step = st.radio("진행할 상황 선택:", turns, horizontal=True)
        
        step_idx = turns.index(step) * 2
        staff_turn = dialogue[step_idx]
        my_turn = dialogue[step_idx + 1]
        
        st.markdown(f"<div class='sentence-card' style='background-color: #f8f9fa; border-left: 4px solid #adb5bd;'><div class='role-label' style='color: #6c757d;'>{staff_turn[0]}의 말</div><div class='eng-text'>{staff_turn[1]}</div><div class='kor-text'>{staff_turn[2]}</div></div>", unsafe_allow_html=True)
        tts_staff = gTTS(text=staff_turn[1], lang='en', slow=False)
        audio_io_staff = io.BytesIO()
        tts_staff.write_to_fp(audio_io_staff)
        st.audio(audio_io_staff, format='audio/mp3')
        
        st.write("👇 **내가 대답할 정답 문장:**")
        st.markdown(f"<div class='sentence-card' style='background-color: #e3f2fd; border-left: 4px solid #1976d2;'><div class='role-label' style='color: #1976d2;'>나</div><div class='eng-text'>{my_turn[1]}</div><div class='kor-text'>{my_turn[2]}</div></div>", unsafe_allow_html=True)
        
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
                
                st.session_state.my_records.append({"topic": selected_topic, "said": recognized_text})
                
            except sr.UnknownValueError:
                st.error("앗, 목소리가 잘 안 들렸어요. 스마트폰 마이크 권한을 허용했는지 확인해 주세요!")
            except Exception as e:
                st.error("오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")

    with tab3:
        st.caption("내가 마이크로 연습했던 문장들이 시간순으로 쌓입니다.")
        if len(st.session_state.my_records) == 0:
            st.info("아직 녹음된 기록이 없습니다. '실전 롤플레잉' 탭에서 연습을 시작해 보세요!")
        else:
            for record in reversed(st.session_state.my_records):
                st.markdown(f"<div class='sentence-card' style='background-color: #ffffff; border: 1px solid #e0e0e0;'><span style='color: #888; font-size: 12px;'>{record['topic']}</span><br><span class='eng-text'>🗣️ {record['said']}</span></div>", unsafe_allow_html=True)

# ==========================================
# 🔄 3. 어제 복습 & 🚀 4. 내일 예습 (임시 화면)
# ==========================================
elif st.session_state.page == 'yesterday':
    if st.button("🔙 첫 화면으로 돌아가기"):
        go_to_page('cover')
        st.rerun()
    st.title("🔄 어제 복습")
    st.info("여기는 어제 연습했던 문장들을 복습하는 공간입니다. (곧 업데이트 예정입니다!)")

elif st.session_state.page == 'tomorrow':
    if st.button("🔙 첫 화면으로 돌아가기"):
        go_to_page('cover')
        st.rerun()
    st.title("🚀 내일 예습")
    st.info("여기는 내일 배울 대본을 미리 들어보는 공간입니다. (곧 업데이트 예정입니다!)")
