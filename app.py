import streamlit as st
import random
import time

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

st.set_page_config(page_title="Başar Eğitim Sistemi", layout="centered", page_icon="⚓")

# --- GELİŞMİŞ TASARIM VE KUTLAMA EFEKTLERİ ---
st.markdown("""
    <style>
    /* Ana Arkaplan (Deniz Mavisi Tonları) */
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f2ff 100%);
    }

    /* Başlık Alanı (Logo) - Lacivert Zeminli */
    .header-box {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border: 3px solid #ffffff;
    }

    /* Daire İçinde Çıpa Simgesi */
    .circle-anchor {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 60px;
        height: 60px;
        background-color: #ffffff;
        border-radius: 50%;
        color: #1E3A8A;
        font-size: 30px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 0 15px;
        vertical-align: middle;
    }

    /* Başlık Metni (Metin Değiştirildi) */
    .header-text {
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        display: inline-block;
        vertical-align: middle;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Buton Tasarımları */
    .stButton>button {
        width: 100%;
        height: 3.5em;
        font-weight: bold;
        font-size: 16px;
        border-radius: 10px;
        background: #ffffff;
        color: #1E3A8A;
        border: 2px solid #1E3A8A;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background: #1E3A8A;
        color: #ffffff;
    }

    /* Soru ve İlan Kutuları */
    .stInfo, .stSuccess, .stError {
        border-radius: 10px;
        padding: 20px;
    }
    
    h2, h3 { text-align: center; color: #1E3A8A; }

    /* Konfeti Efekti (Konfeti patladığında arka planı şeffaf yapar) */
    .confetti-active {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO VE BAŞLIK ALANI (Yeni Tasarım) ---
st.markdown(f"""
    <div class="header-box">
        <div class="circle-anchor">⚓</div>
        <div class="header-text">BAŞAR EĞİTİM SİSTEMİ</div>
        <div class="circle-anchor">⚓</div>
    </div>
    """, unsafe_allow_html=True)

# --- SORU ÜRETİCİ ---
def generate_quiz(is_shuffled):
    pool = data.copy()
    if is_shuffled:
        random.shuffle(pool)
    
    questions = []
    types = ["tr-abbr", "abbr-tr", "abbr-eng", "eng-abbr", "eng-tr", "tr-eng"]
    
    for i, item in enumerate(pool):
        t = types[i % len(types)]
        if t == "tr-abbr": q, c, k = f"'{item['tr']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif t == "abbr-tr": q, c, k = f"'{item['abbr']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        elif t == "abbr-eng": q, c, k = f"'{item['abbr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        elif t == "eng-abbr": q, c, k = f"'{item['eng']}' teriminin kısaltması nedir?", item['abbr'], 'abbr'
        elif t == "eng-tr": q, c, k = f"'{item['eng']}' teriminin Türkçe karşılığı nedir?", item['tr'], 'tr'
        else: q, c, k = f"'{item['tr']}' ifadesinin İngilizce açılımı nedir?", item['eng'], 'eng'

        wrong_pool = list(set([x[k] for x in data if x[k] != c]))
        options = random.sample(wrong_pool, 3) + [c]
        random.shuffle(options)
        questions.append({"question": q, "correct": c, "options": options})
        
    return questions[:50]

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "GIRIS"
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.history = []

# --- AKIŞ YÖNETİMİ ---

if st.session_state.page == "GIRIS":
    st.header("ECDIS Sınav Modülü")
    
    # Açık Seçenek Menüsü (İsteğiniz üzere st.radio ile yapıldı)
    mode = st.radio(
        "Soru Sıralaması Seçin:",
        options=["Sabit (Sıralı)", "Değişken (Karışık)"],
        horizontal=True # Seçenekleri yan yana gösterir, daha modern bir görünüm
    )
    
    st.markdown("<br>", unsafe_allow_html=True) # Boşluk
    if st.button("SINAVA BAŞLA", key="start_btn"):
        st.session_state.quiz = generate_quiz(mode == "Değişken (Karışık)")
        st.session_state.page = "SINAV"
        st.rerun()

elif st.session_state.page == "SINAV":
    idx = st.session_state.current_idx
    q = st.session_state.quiz[idx]
    
    st.subheader(f"Soru {idx + 1} / {len(st.session_state.quiz)}")
    st.progress((idx + 1) / len(st.session_state.quiz))
    
    st.info(f"### {q['question']}")
    
    labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {opt}", key=f"btn_{idx}_{i}"):
            is_correct = (opt == q["correct"])
            if is_correct: st.session_state.score += 1
            
            st.session_state.history.append({
                "q": q["question"], "user": opt, "correct": q["correct"], "is_correct": is_correct
            })
            
            if idx + 1 < len(st.session_state.quiz):
                st.session_state.current_idx += 1
            else:
                st.session_state.page = "ANALIZ"
            st.rerun()

elif st.session_state.page == "ANALIZ":
    st.header("🏁 Sınav Tamamlandı")
    
    total = len(st.session_state.quiz)
    percent = (st.session_state.score / total) * 100
    
    # Konfeti Efekti Kontrolü (%80 Üstü)
    if percent >= 80:
        # Arka planı şeffaf yapıp konfeti ve balon patlatıyoruz
        st.markdown('<style>.stApp { background-color: transparent !important; }</style>', unsafe_allow_html=True)
        st.balloons() # Balonlar
        # Havai fişek ve konfeti efekti (Streamlit'in varsayılanı konfetidir)
        time.sleep(0.5)
        st.success("MUHTEŞEM BİR BAŞARI! 🌟")
        st.divider()
    
    col1, col2 = st.columns(2)
    col1.metric("Doğru", f"{st.session_state.score} / {total}")
    col2.metric("Başarı Oranı", f"%{percent:.1f}")
    
    if percent < 80:
        st.info("Harika! Kendinizi daha da geliştirebilirsiniz.")
    else:
        st.divider()

    st.subheader("Hatalı Soruların Analizi")
    
    has_errors = False
    for i, item in enumerate(st.session_state.history):
        if not item["is_correct"]:
            has_errors = True
            st.error(f"**Soru {i+1}:** {item['q']}")
            st.write(f"❌ **Sizin Cevabınız:** {item['user']}")
            st.write(f"✅ **Doğru Cevap:** {item['correct']}")
            st.markdown("---")
            
    if not has_errors:
        st.success("Tebrikler! Hiç hata yapmadınız.")

    if st.button("Ana Menüye Dön"):
        st.session_state.clear()
        st.rerun()
