import streamlit as st
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

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Başar Teknik Eğitim", page_icon="⚓")

# CSS: En güvenli hale getirildi (Karanlık Mod uyumlu ama lacivert ağırlıklı)
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; color: #1E3A8A; }
    .logo-header { background-color: #1E3A8A; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px; }
    .logo-header h1 { color: white !important; margin: 0; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; font-weight: bold; }
    div[data-testid="stExpander"] { background-color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO ---
st.markdown('<div class="logo-header"><h1>⚓ BAŞAR TEKNİK EĞİTİM</h1></div>', unsafe_allow_html=True)

# --- SORU ÜRETİCİ ---
def generate_questions(shuffle_mode):
    temp_data = data.copy()
    if shuffle_mode:
        random.shuffle(temp_data)
    
    quiz = []
    formats = ["tr-abbr", "abbr-tr", "abbr-eng", "eng-abbr", "eng-tr", "tr-eng"]
    
    for i, item in enumerate(temp_data):
        fmt = formats[i % len(formats)]
        if fmt == "tr-abbr": q, c, k = f"'{item['tr']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif fmt == "abbr-tr": q, c, k = f"'{item['abbr']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        elif fmt == "abbr-eng": q, c, k = f"'{item['abbr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        elif fmt == "eng-abbr": q, c, k = f"'{item['eng']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif fmt == "eng-tr": q, c, k = f"'{item['eng']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        else: q, c, k = f"'{item['tr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        
        wrong_pool = list(set([x[k] for x in data if x[k] != c]))
        options = random.sample(wrong_pool, 3) + [c]
        random.shuffle(options)
        quiz.append({"q": q, "c": c, "options": options})
    return quiz[:50]

# --- STATE ---
if 'step' not in st.session_state:
    st.session_state.step = "GIRIS"
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.user_answers = []

# --- AKIŞ ---
if st.session_state.step == "GIRIS":
    st.write("### ECDIS Kısaltmaları Sınavına Hoş Geldiniz")
    mode = st.radio("Soru Düzeni:", ["Sabit", "Değişken"])
    if st.button("SINAVA BAŞLAT"):
        st.session_state.questions = generate_questions(mode == "Değişken")
        st.session_state.step = "SINAV"
        st.rerun()

elif st.session_state.step == "SINAV":
    idx = st.session_state.current_idx
    total = len(st.session_state.questions)
    q_data = st.session_state.questions[idx]
    
    # Soru Sayacı
    st.info(f"Soru: {idx + 1} / {total}")
    st.progress((idx + 1) / total)
    
    # Soru Metni
    st.markdown(f"### {q_data['q']}")
    
    # Şıklar
    for opt in q_data['options']:
        if st.button(opt, key=f"btn_{idx}_{opt}"):
            is_correct = (opt == q_data['c'])
            if is_correct: st.session_state.score += 1
            st.session_state.user_answers.append({
                "question": q_data['q'],
                "user": opt,
                "correct": q_data['c'],
                "is_correct": is_correct
            })
            
            if idx + 1 < total:
                st.session_state.current_idx += 1
            else:
                st.session_state.step = "ANALIZ"
            st.rerun()

elif st.session_state.step == "ANALIZ":
    st.success("## Sınav Tamamlandı!")
    total_q = len(st.session_state.questions)
    perc = (st.session_state.score / total_q) * 100
    
    st.subheader(f"Başarı Oranı: %{perc:.1f}")
    st.write(f"Toplam {total_q} soruda {st.session_state.score} doğru yaptınız.")
    
    st.divider()
    st.write("### Hatalı Soruların Analizi")
    
    for i, ans in enumerate(st.session_state.user_answers):
        if not ans["is_correct"]:
            with st.expander(f"Soru {i+1} (Hatalı): {ans['question']}"):
                st.write(f"**Sizin Cevabınız:** :red[{ans['user']}]")
                st.write(f"**Doğru Cevap:** :green[{ans['correct']}]")
        else:
            # Doğru cevapları da istersen buraya ekleyebiliriz ama şimdilik sadece hataları gösteriyorum
            pass

    if st.button("YENİDEN DENE"):
        st.session_state.clear()
        st.rerun()
