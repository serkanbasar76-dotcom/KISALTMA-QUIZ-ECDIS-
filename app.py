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

st.set_page_config(page_title="Başar Teknik Eğitim", layout="centered")

# Minimal ve Garanti Stil
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 3.5em; font-weight: bold; margin-bottom: 5px; }
    h1, h2, h3 { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Logo Alanı
st.title("⚓ BAŞAR TEKNİK EĞİTİM")
st.divider()

# --- SORU ÜRETİCİ ---
def generate_quiz(is_shuffled):
    pool = data.copy()
    if is_shuffled:
        random.shuffle(pool)
    
    questions = []
    # 6 farklı kombinasyon türü
    types = ["tr-abbr", "abbr-tr", "abbr-eng", "eng-abbr", "eng-tr", "tr-eng"]
    
    for i, item in enumerate(pool):
        t = types[i % len(types)]
        if t == "tr-abbr": q, c, k = f"'{item['tr']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif t == "abbr-tr": q, c, k = f"'{item['abbr']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        elif t == "abbr-eng": q, c, k = f"'{item['abbr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        elif t == "eng-abbr": q, c, k = f"'{item['eng']}' teriminin kısaltması nedir?", item['abbr'], 'abbr'
        elif t == "eng-tr": q, c, k = f"'{item['eng']}' teriminin Türkçe karşılığı nedir?", item['tr'], 'tr'
        else: q, c, k = f"'{item['tr']}' ifadesinin İngilizce açılımı nedir?", item['eng'], 'eng'

        # Yanlış seçenekleri al
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
    order = st.selectbox("Soru Sıralaması Seçin:", ["Sabit", "Değişken"])
    if st.button("SINAVA BAŞLA"):
        st.session_state.quiz = generate_quiz(order == "Değişken")
        st.session_state.page = "SINAV"
        st.rerun()

elif st.session_state.page == "SINAV":
    idx = st.session_state.current_idx
    q = st.session_state.quiz[idx]
    
    # Soru Bilgisi
    st.subheader(f"Soru {idx + 1} / {len(st.session_state.quiz)}")
    st.progress((idx + 1) / len(st.session_state.quiz))
    
    st.info(q["question"])
    
    # Şıklar (A, B, C, D eklenmiş hali)
    labels = ["A", "B", "C", "D"]
    for i, opt in enumerate(q["options"]):
        if st.button(f"{labels[i]}) {opt}", key=f"btn_{idx}_{i}"):
            is_correct = (opt == q["correct"])
            if is_correct: st.session_state.score += 1
            
            st.session_state.history.append({
                "q": q["question"],
                "user": opt,
                "correct": q["correct"],
                "is_correct": is_correct
            })
            
            if idx + 1 < len(st.session_state.quiz):
                st.session_state.current_idx += 1
            else:
                st.session_state.page = "ANALIZ"
            st.rerun()

elif st.session_state.page == "ANALIZ":
    st.header("🏁 Sınav Sonucu")
    
    total = len(st.session_state.quiz)
    percent = (st.session_state.score / total) * 100
    
    col1, col2 = st.columns(2)
    col1.metric("Doğru", f"{st.session_state.score} / {total}")
    col2.metric("Başarı", f"%{percent:.1f}")
    
    st.divider()
    st.subheader("Hatalı Soruların Analizi")
    
    # Analiz Sayfası - Okunabilirlik Garantili (Markdown kullanarak)
    for i, item in enumerate(st.session_state.history):
        if not item["is_correct"]:
            # st.error kullanarak hem zemin rengini hem yazı rengini sistemin yönetmesini sağlıyoruz
            st.error(f"**Soru {i+1}:** {item['q']}")
            st.write(f"❌ **Sizin Cevabınız:** {item['user']}")
            st.write(f"✅ **Doğru Cevap:** {item['correct']}")
            st.markdown("---")
            
    if st.button("Ana Menüye Dön"):
        st.session_state.clear()
        st.rerun()
