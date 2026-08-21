import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import re

st.set_page_config(page_title="나만의 영어 단짝", page_icon="🗣️", layout="wide")

# -------------------------------------------------------------
# 📚 무한 대화 은행 (이곳에 시나리오를 계속 추가할 수 있습니다)
# -------------------------------------------------------------
scenarios = {
    "✈️ [공항] 입국 심사": {
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
    },
    "⛳ [스포츠] 파크골프 라운딩": {
        "description": "해외 파크골프장에 도착해 체크인하고 라운딩을 시작합니다.",
        "image": "https://images.unsplash.com/photo-1587174486073-ae5e5cff23aa?q=80&w=1000&auto=format&fit=crop",
        "dialogue": [
            ("직원", "Hello! Do you have a reservation?", "안녕하세요! 예약하셨나요?"),
            ("나", "Yes, I booked a morning tee time under the name Kim.", "네, 김(Kim)이라는 이름으로 오전 티타임을 예약했습니다."),
            ("직원", "Great! Do you need to rent any clubs?", "확인되었습니다! 골프채 대여가 필요하신가요?"),
            ("나", "Yes, please. I'd like to rent one park golf club.", "네, 부탁합니다. 파크골프 채 하나를 대여하고 싶어요.")
        ]
    }
}

# -------------------------------------------------------------
# 🎨 화면 구성 (사이드바 메뉴)
# -------------------------------------------------------------
st.sidebar.title("📚 내 학습 보관소")
st.sidebar.caption("지난 대화도 언제든 검색해서 다시 꺼내볼 수 있습니다.")

selected_topic = st.sidebar.selectbox("🔍 주제 검색 및 선택:", list(scenarios.keys()))
st.sidebar.write("---")
st.sidebar.info("💡 매일 코드를 조금씩 추가해 나만의 회화 사전을 완성해 보세요!")

current_data = scenarios[selected_topic]
dialogue = current_data["dialogue"]

st.title(selected_topic)
st.caption(current_data["description"])
st.image(current_data["image"], use_column_width=True)
st.write("---")

tab1, tab2, tab3 = st.tabs(["📖 전체 대화", "🗣️ 한 문장 연습", "🎭 실전 롤플레잉 (AI 채점)"])

# --- 탭 1: 전체 대화 ---
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

# --- 탭 2: 한 문장 연습 ---
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

# --- 탭 3: 실전 롤플레잉 & AI 발음 채점 ---
def clean_text(text):
    # 특수문자를 제거하고 소문자로 변환하여 비교하기 쉽게 만듦
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()

with tab3:
    st.subheader("3. 실전 롤플레잉 & AI 발음 채점")
    
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
    st.write("👇 **내가 대답할 정답 문장:**")
    st.success(f"**나:** {my_turn[1]} \n\n({my_turn[2]})")
    
    st.write("🎙️ **마이크를 켜고 정답 문장을 말해보세요! (AI가 채점합니다)**")
    audio_value = audio_recorder(text="터치하여 말하기", icon_size="2x", pause_threshold=3.0)
    
    if audio_value:
        st.audio(audio_value)
        st.write("⏳ AI가 회원님의 발음을 분석 중입니다...")
        
        try:
            r = sr.Recognizer()
            audio_file = io.BytesIO(audio_value)
            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
            
            # 구글 음성 인식(STT)을 사용해 영어로 텍스트 변환
            recognized_text = r.recognize_google(audio_data, language="en-US")
            st.write(f"📝 **AI가 들은 내 목소리:** {recognized_text}")
            
            # 정답 문장과 내 발음 비교
            target_clean = clean_text(my_turn[1])
            recog_clean = clean_text(recognized_text)
            
            if target_clean == recog_clean:
                st.success("🎉 완벽합니다! 원어민과 토시 하나 안 틀리고 똑같이 발음하셨네요!")
            elif recog_clean in target_clean or target_clean in recog_clean:
                st.warning("👍 아주 좋습니다! 핵심 단어가 들어가 있어서 의사소통이 완벽하게 됩니다.")
            else:
                st.error("💪 조금 다르게 인식되었어요! 원어민 발음을 다시 듣고 도전해 보세요.")
                
        except sr.UnknownValueError:
            st.error("앗, 목소리가 잘 안 들렸어요. 주변이 너무 시끄럽거나 발음이 뭉개졌을 수 있으니 다시 시도해 주세요!")
        except Exception as e:
            st.error("마이크 인식 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")
