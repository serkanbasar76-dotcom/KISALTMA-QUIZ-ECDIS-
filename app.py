import streamlit as st
import pandas as pd
import random

# --- VERİ SETİ ---
data = [
    {"abbr": "AIS", "eng": "Automatic Identification System", "tr": "Otomatik Kimliklendirme Sistemi"},
    {"abbr": "ARCS", "eng": "Admiralty Raster Chart Service", "tr": "Admiralty Raster Harita Servisi"},
    {"abbr": "ARPA", "eng": "Automatic Radar Plotting Aid", "tr": "Otomatik Radar Plotlama Yardımcısı"},
    {"abbr": "BRG", "eng": "Bearing", "tr": "Kerteriz"},
    {"abbr": "BTW", "eng": "Bearing to Waypoint", "tr": "Watpoint'e Kerteriz"},
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

st.set_page_config(page_title="Başar Teknik Eğitim", layout="centered")

# --- KAPSAMLI STİL (TÜM GÖRÜNÜRLÜK SORUNLARI İÇİN) ---
st.markdown("""
    <style>
    /* Genel metin renklerini siyah yap */
    html, body, [class*="st-"] {
        color: #1a1a1a !important;
    }
    
    .logo-text { 
        font-size: 32px !important; font-weight: bold; color: white !important; 
        text-align: center; background: #1E3A8A; padding: 20px; border-radius: 10px; margin-bottom: 20px;
    }

    .question-box { 
        background-color: white; padding: 25px; border-radius: 12px; 
        border: 2px solid #e0e0e0; margin-bottom: 15px;
    }

    /* Soru Sayacı Metni */
    .counter-text {
        font-size: 18px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px;
    }

    /* Analiz Sayfası Metinleri */
    .analysis-card {
        background-color: #ffffff; padding: 15px; border-radius: 8px;
        border: 1px solid #ddd; margin-bottom: 10px; color: #1a1a1a;
    }
    
    /* Butonlar */
    .stButton>button {
        height: 3.5em; font-size: 16px; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO ---
st.markdown('<div class="logo-text">⚓ BAŞAR TEKNİK EĞİTİM</div>', unsafe_allow_html=True)

# --- SORU OLUŞTURMA ---
def create_questions(is_random):
    pool = data.copy()
    if is_random: random.shuffle(pool)
    
    questions = []
    types = ["tr_to_abbr", "abbr_to_tr", "abbr_to_eng", "eng_to_abbr", "eng_to_tr", "tr_to_eng"]
    
    for i, item in enumerate(pool):
        q_type = types[i % len(types)]
        if "tr_to_abbr" in q_type: q_text, correct, o_key = f"'{item['tr']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif "abbr_to_tr" in q_type: q_text, correct, o_key = f"'{item['abbr']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        elif "abbr_to_eng" in q_type: q_text, correct, o_key = f"'{item['abbr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        elif "eng_to_abbr" in q_type: q_text, correct, o_key = f"'{item['eng']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif "eng_to_tr" in q_type: q_text, correct, o_key = f"'{item['eng']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        else: q_text, correct, o_key = f"'{item['tr']}' İngilizce açılımı nedir?", item['eng'], 'eng'

        options_pool = list(set([x[o_key] for x in data if x[o_key] != correct]))
        options = random.sample(options_pool, 3) + [correct]
        random.shuffle(options)
        
        questions.append({"id": i+1, "question": q_text, "correct": correct, "options": options})
    return questions[:50]

if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.current_q = 0
    st.session_state.answers = []
    st.session_state.score = 0

# --- GİRİŞ ---
if not st.session_state.quiz_started:
    st.markdown("<h2 style='text-align:center;'>ECDIS Eğitim Modülü</h2>", unsafe_allow_html=True)
    mode = st.selectbox("Soru Sıralaması", ["Sabit", "Değişken"])
    if st.button("SINAVI BAŞLAT"):
        st.session_state.questions = create_questions(is_random=(mode == "Değişken"))
        st.session_state.quiz_started = True
        st.rerun()

# --- SORU EKRANI ---
elif st.session_state.quiz_started and st.session_state.current_q < len(st.session_state.questions):
    q_idx = st.session_state.current_q
    q = st.session_state.questions[q_idx]
    
    # Soru Sayacı (Özel Stil ile)
    st.markdown(f'<p class="counter-text">Soru {q_idx + 1} / {len(st.session_state.questions)}</p>', unsafe_allow_html=True)
    st.progress((q_idx + 1) / len(st.session_state.questions))
    
    st.markdown(f'<div class="question-box"><h3 style="color:#1E3A8A;">{q["question"]}</h3></div>', unsafe_allow_html=True)
    
    cols = st.columns(1)
    labels = ["A", "B", "C", "D"]
    for i, option in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {option}", key=f"btn_{q_idx}_{i}"):
            is_correct = (option == q["correct"])
            st.session_state.answers.append({
                "question": q["question"], "user": option, "correct": q["correct"], "is_correct": is_correct
            })
            if is_correct: st.session_state.score += 1
            st.session_state.current_q += 1
            st.rerun()

# --- ANALİZ ---
else:
    st.markdown("<h2 style='color:#1E3A8A;'>Sınav Tamamlandı!</h2>", unsafe_allow_html=True)
    total = len(st.session_state.questions)
    percentage = (st.session_state.score / total) * 100
    
    st.metric("Başarı Oranı", f"%{percentage:.1f}", f"{st.session_state.score} Doğru")
    
    st.markdown("### Hata Analizi")
    for idx, ans in enumerate(st.session_state.answers):
        color = "#d4edda" if ans["is_correct"] else "#f8d7da"
        status = "✅ Doğru" if ans["is_correct"] else "❌ Yanlış"
        
        # Analiz kartlarını HTML ile görünür kılıyoruz
        st.markdown(f"""
            <div style="background-color:{color}; padding:15px; border-radius:10px; margin-bottom:10px; border:1px solid #ccc;">
                <b style="color:black;">Soru {idx+1}: {ans['question']}</b><br>
                <span style="color:black;">Durum: {status}</span><br>
                <span style="color:black;">Sizin Cevabınız: {ans['user']}</span><br>
                <span style="color:#155724; font-weight:bold;">Doğru Cevap: {ans['correct']}</span>
            </div>
        """, unsafe_allow_html=True)

    if st.button("YENİDEN BAŞLAT"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()
