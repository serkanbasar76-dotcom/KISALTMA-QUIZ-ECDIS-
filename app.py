import streamlit as st
import pandas as pd
import random

# --- VERİ SETİ ---
data = [
    {"abbr": "AIS", "eng": "Automatic Identification System", "tr": "Otomatik Kimliklendirme Sistemi"},
    {"abbr": "ARCS", "eng": "Admiralty Raster Chart Service", "tr": "Admiralty Raster Harita Servisi"},
    {"abbr": "ARPA", "eng": "Automatic Radar Plotting Aid", "tr": "Otomatik Radar Plotlama Yardımcısı"},
    {"abbr": "BRG", "eng": "Bearing", "tr": "Kerteriz"},
    {"abbr": "BTW", "eng": "Bearing to Waypoint", "tr": "Waypoint'e Kerteriz"},
    {"abbr": "BWW", "eng": "Bearing Waypoint to Waypoint", "tr": "Waypoint'ten Waypoint'e Kerteriz"},
    {"abbr": "C Up", "eng": "Course Up", "tr": "Rota Yukarıda (Ekran Yönü)"},
    {"abbr": "COG", "eng": "Course Over Ground", "tr": "Yere Göre Rota"},
    {"abbr": "CPA", "eng": "Closest Point of Approach", "tr": "Azami Yaklaşma Noktası"},
    {"abbr": "DIST", "eng": "Distance", "tr": "Mesafe"},
    {"abbr": "DR", "eng": "Dead Reckoning", "tr": "Parakete Mevki"},
    {"abbr": "DTW", "eng": "Distance to Waypoint", "tr": "Waypoint'e Mesafe"},
    {"abbr": "DTWOL", "eng": "Distance to Wheel Over Line", "tr": "Dümen Basma Hattına Mesafe"},
    {"abbr": "EBL", "eng": "Electronic Bearing Line", "tr": "Elektronik Kerteriz Hattı"},
    {"abbr": "ECDIS", "eng": "Electronic Chart Display and Information System", "tr": "Elektronik Harita Gösterim ve Bilgi Sistemi"},
    {"abbr": "ECHO", "eng": "Echosounder", "tr": "Elektronik İskandil"},
    {"abbr": "ENC", "eng": "Electronic Navigational Chart", "tr": "Elektronik Seyir Haritası"},
    {"abbr": "EP", "eng": "Estimated Position", "tr": "Tahmini Mevki"},
    {"abbr": "ERBL", "eng": "Electronic Range and Bearing Line", "tr": "Elektronik Mesafe ve Kerteriz Hattı"},
    {"abbr": "ETA", "eng": "Estimated Time of Arrival", "tr": "Tahmini Varış Zamanı"},
    {"abbr": "ETD", "eng": "Estimated Time of Departure", "tr": "Tahmini Kalkış Zamanı"},
    {"abbr": "GMT", "eng": "Greenwich Mean Time", "tr": "Greenwich Ortalama Zamanı"},
    {"abbr": "GZ", "eng": "Guard Zone", "tr": "Koruma Bölgesi"},
    {"abbr": "HDG", "eng": "Heading", "tr": "Pruva"},
    {"abbr": "LOG", "eng": "Log", "tr": "Parakete Cihazı"},
    {"abbr": "LOP", "eng": "Line of Position", "tr": "Mevki Hattı"},
    {"abbr": "N Up", "eng": "North Up", "tr": "Kuzey Yukarıda (Ekran Yönü)"},
    {"abbr": "POSN", "eng": "Position", "tr": "Mevki"},
    {"abbr": "PS", "eng": "Positioning System", "tr": "Mevkilendirme Sistemi"},
    {"abbr": "PTA", "eng": "Planning Time of Arrival", "tr": "Varış Zamanını Planlama"},
    {"abbr": "RAD", "eng": "Radius", "tr": "Yarı Çap (Dönüş Yarı Çapı)"},
    {"abbr": "RM", "eng": "Relative Motion", "tr": "Nispi Hareket"},
    {"abbr": "RNG", "eng": "Range", "tr": "Mesafe"},
    {"abbr": "ROT", "eng": "Rate of Turn", "tr": "Dönüş Hızı"},
    {"abbr": "SOG", "eng": "Speed Over Ground", "tr": "Yere Göre Sürat"},
    {"abbr": "Stand", "eng": "Standard", "tr": "Standart Gösterim"},
    {"abbr": "STG", "eng": "Speed To Go", "tr": "İhtiyaç Duyulan Sürat"},
    {"abbr": "STW", "eng": "Speed Through Water", "tr": "Suya Göre Sürat"},
    {"abbr": "TCPA", "eng": "Time to Closest Point of Approach", "tr": "Azami Yaklaşma Zamanı"},
    {"abbr": "TM", "eng": "True Motion", "tr": "Hakiki Hareket"},
    {"abbr": "TTG", "eng": "Time To Go", "tr": "Dönüş Yerine Kalan Zaman"},
    {"abbr": "VRM", "eng": "Variable Range Marker", "tr": "Değişken Mesafe İşaretleyicisi"},
    {"abbr": "WPT", "eng": "Waypoint", "tr": "Rota Bacağı Kesişim Noktası"},
    {"abbr": "XTD", "eng": "Cross Track Distance", "tr": "Rotadan Sapma Değeri"}
]

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Başar Teknik Eğitim - ECDIS Quiz", page_icon="⚓", layout="centered")

# --- STİL ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-size: 18px; margin-bottom: 10px; }
    .logo-text { font-size: 40px !important; font-weight: bold; color: #1E3A8A; text-align: center; border: 3px solid #1E3A8A; padding: 10px; border-radius: 15px; background: white; margin-bottom: 20px;}
    .question-box { background-color: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGO ---
st.markdown('<div class="logo-text">⚓ BAŞAR TEKNİK EĞİTİM</div>', unsafe_allow_html=True)

# --- SORU OLUŞTURMA FONKSİYONU ---
def create_questions(is_random):
    pool = data.copy()
    if is_random:
        random.shuffle(pool)
    
    # 50 soru sınırı (verimiz 44 adet, hepsini tekil kullanıyoruz)
    questions = []
    types = ["tr_to_abbr", "abbr_to_tr", "abbr_to_eng", "eng_to_abbr", "eng_to_tr", "tr_to_eng"]
    
    for i, item in enumerate(pool):
        q_type = types[i % len(types)]
        
        if q_type == "tr_to_abbr":
            q_text = f"'{item['tr']}' ifadesinin kısaltması nedir?"
            correct = item['abbr']
            options_pool = [x['abbr'] for x in data if x['abbr'] != correct]
        elif q_type == "abbr_to_tr":
            q_text = f"'{item['abbr']}' kısaltmasının Türkçe karşılığı nedir?"
            correct = item['tr']
            options_pool = [x['tr'] for x in data if x['tr'] != correct]
        elif q_type == "abbr_to_eng":
            q_text = f"'{item['abbr']}' kısaltmasının İngilizce açılımı nedir?"
            correct = item['eng']
            options_pool = [x['eng'] for x in data if x['eng'] != correct]
        elif q_type == "eng_to_abbr":
            q_text = f"'{item['eng']}' teriminin kısaltması nedir?"
            correct = item['abbr']
            options_pool = [x['abbr'] for x in data if x['abbr'] != correct]
        elif q_type == "eng_to_tr":
            q_text = f"'{item['eng']}' teriminin Türkçe karşılığı nedir?"
            correct = item['tr']
            options_pool = [x['tr'] for x in data if x['tr'] != correct]
        else: # tr_to_eng
            q_text = f"'{item['tr']}' ifadesinin İngilizce açılımı nedir?"
            correct = item['eng']
            options_pool = [x['eng'] for x in data if x['eng'] != correct]

        wrong_options = random.sample(options_pool, 3)
        options = wrong_options + [correct]
        random.shuffle(options)
        
        questions.append({
            "id": i+1,
            "question": q_text,
            "correct": correct,
            "options": options
        })
    return questions

# --- SESSION STATE YÖNETİMİ ---
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_q = 0
    st.session_state.answers = []
    st.session_state.score = 0

# --- GİRİŞ EKRANI ---
if not st.session_state.quiz_started:
    st.subheader("ECDIS Kısaltmaları Soru Bankası")
    mode = st.radio("Soru Modu Seçiniz:", ["Sabit (Her zaman aynı sıra)", "Değişken (Karışık sıra)"])
    
    if st.button("SINAVI BAŞLAT"):
        st.session_state.questions = create_questions(is_random=(mode == "Değişken"))
        st.session_state.quiz_started = True
        st.rerun()

# --- SORU EKRANI ---
elif st.session_state.quiz_started and st.session_state.current_q < len(st.session_state.questions):
    q_idx = st.session_state.current_q
    q = st.session_state.questions[q_idx]
    
    st.write(f"Soru {q_idx + 1} / {len(st.session_state.questions)}")
    st.progress((q_idx + 1) / len(st.session_state.questions))
    
    st.markdown(f'<div class="question-box"><h3>{q["question"]}</h3></div>', unsafe_allow_html=True)
    
    # Şık Harfleri
    labels = ["A", "B", "C", "D"]
    
    for i, option in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {option}", key=f"opt_{q_idx}_{i}"):
            # Cevabı Kaydet
            is_correct = (option == q["correct"])
            st.session_state.answers.append({
                "question": q["question"],
                "your_answer": option,
                "correct_answer": q["correct"],
                "is_correct": is_correct
            })
            if is_correct:
                st.session_state.score += 1
            
            # Sonraki Soruya Geç
            st.session_state.current_q += 1
            st.rerun()

# --- ANALİZ EKRANI ---
else:
    st.balloons()
    st.header("Sınav Sonuç Analizi")
    
    total = len(st.session_state.questions)
    percentage = (st.session_state.score / total) * 100
    
    col1, col2 = st.columns(2)
    col1.metric("Doğru Sayısı", f"{st.session_state.score} / {total}")
    col2.metric("Başarı Yüzdesi", f"%{percentage:.1f}")
    
    st.divider()
    
    st.subheader("Hatalı Sorular ve Çözümleri")
    for idx, ans in enumerate(st.session_state.answers):
        if not ans["is_correct"]:
            with st.expander(f"Soru {idx+1}: {ans['question']}"):
                st.error(f"Sizin Cevabınız: {ans['your_answer']}")
                st.success(f"Doğru Cevap: {ans['correct_answer']}")
        elif percentage == 100 and idx == 0:
            st.write("Tebrikler! Tüm soruları doğru yanıtladınız.")
            break

    if st.button("YENİDEN BAŞLAT"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()