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

st.set_page_config(page_title="Başar Eğitim Sistemi", layout="centered")

# --- KUVVETLİ KONTRAST VE TASARIM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6 !important; }
    html, body, [class*="st-"] { color: #001f3f !important; font-weight: 500; }

    .header-container {
        background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 30px; border-radius: 20px; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2); margin-bottom: 40px;
    }
    .anchor-circle {
        background: white; color: #1E3A8A; width: 50px; height: 50px;
        border-radius: 50%; display: inline-flex; align-items: center;
        justify-content: center; font-size: 24px; margin: 0 20px;
        vertical-align: middle; box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .title-text {
        color: white !important; font-size: 28px !important;
        font-weight: 900 !important; vertical-align: middle;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .question-box {
        background-color: white !important; color: #1E3A8A !important;
        padding: 25px; border-radius: 15px; border-left: 10px solid #1E3A8A;
        margin-bottom: 25px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    .stButton>button {
        background-color: white !important; color: #1E3A8A !important;
        border: 2px solid #1E3A8A !important; font-weight: bold !important;
        height: 4em !important; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1E3A8A !important; color: white !important; }

    .error-card {
        background-color: #ffffff !important; border: 2px solid #e53e3e !important;
        padding: 20px; border-radius: 12px; margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .question-number {
        background-color: #e53e3e; color: white; padding: 2px 10px;
        border-radius: 5px; font-size: 14px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO ALANI ---
st.markdown("""
    <div class="header-container">
        <div class="anchor-circle">⚓</div>
        <span class="title-text">BAŞAR EĞİTİM SİSTEMİ</span>
        <div class="anchor-circle">⚓</div>
    </div>
    """, unsafe_allow_html=True)

# --- FONKSİYONLAR ---
def get_quiz(shuffle):
    pool = data.copy()
    if shuffle: random.shuffle(pool)
    quiz = []
    types = ["tr-abbr", "abbr-tr", "abbr-eng", "eng-abbr", "eng-tr", "tr-eng"]
    for i, item in enumerate(pool[:50]):
        t = types[i % len(types)]
        if t == "tr-abbr": q, c, k = f"'{item['tr']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif t == "abbr-tr": q, c, k = f"'{item['abbr']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        elif t == "abbr-eng": q, c, k = f"'{item['abbr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        elif t == "eng-abbr": q, c, k = f"'{item['eng']}' kısaltması nedir?", item['abbr'], 'abbr'
        elif t == "eng-tr": q, c, k = f"'{item['eng']}' Türkçe karşılığı nedir?", item['tr'], 'tr'
        else: q, c, k = f"'{item['tr']}' İngilizce açılımı nedir?", item['eng'], 'eng'
        
        w_pool = list(set([x[k] for x in data if x[k] != c]))
        opts = random.sample(w_pool, 3) + [c]
        random.shuffle(opts)
        quiz.append({"q": q, "c": c, "opts": opts})
    return quiz

# --- STATE YÖNETİMİ ---
if 'pg' not in st.session_state:
    st.session_state.pg = "GIRIS"
    st.session_state.score = 0
    st.session_state.idx = 0
    st.session_state.log = []

# --- SAYFALAR ---
if st.session_state.pg == "GIRIS":
    st.markdown("<h3 style='text-align:center;'>ECDIS Eğitim Modülü</h3>", unsafe_allow_html=True)
    mode = st.radio("Soru Sıralaması:", ["Sabit (Sıralı)", "Değişken (Karışık)"], index=0, horizontal=True)
    
    if st.button("SINAVI BAŞLAT"):
        st.session_state.quiz = get_quiz(mode == "Değişken (Karışık)")
        st.session_state.pg = "SINAV"
        st.rerun()

elif st.session_state.pg == "SINAV":
    curr = st.session_state.quiz[st.session_state.idx]
    
    st.markdown(f"<p style='color:#1E3A8A; font-weight:bold;'>Soru {st.session_state.idx + 1} / {len(st.session_state.quiz)}</p>", unsafe_allow_html=True)
    st.progress((st.session_state.idx + 1) / len(st.session_state.quiz))
    
    st.markdown(f"<div class='question-box'><h3>{curr['q']}</h3></div>", unsafe_allow_html=True)
    
    L = ["A", "B", "C", "D"]
    for i, o in enumerate(curr['opts']):
        if st.button(f"{L[i]}) {o}", key=f"btn_{st.session_state.idx}_{i}"):
            is_correct = (o == curr['c'])
            if is_correct: st.session_state.score += 1
            # Log kaydına gerçek soru numarasını (idx+1) ekliyoruz
            st.session_state.log.append({
                "num": st.session_state.idx + 1,
                "q": curr['q'], 
                "u": o, 
                "c": curr['c'], 
                "is": is_correct
            })
            
            if st.session_state.idx + 1 < len(st.session_state.quiz):
                st.session_state.idx += 1
            else:
                st.session_state.pg = "ANALIZ"
            st.rerun()

else: # ANALIZ SAYFASI
    st.markdown("<h2 style='text-align:center; color:#1E3A8A;'>Sınav Analiz Raporu</h2>", unsafe_allow_html=True)
    total = len(st.session_state.quiz)
    perc = (st.session_state.score / total) * 100
    
    if perc >= 80:
        st.balloons()
        st.snow()
        st.success(f"TEBRİKLER! %{perc:.1f} Başarı ile Modülü Tamamladınız! ⚓🌟")
    
    c1, c2 = st.columns(2)
    c1.metric("Doğru Sayısı", f"{st.session_state.score} / {total}")
    c2.metric("Başarı Oranı", f"%{perc:.1f}")
    
    st.divider()
    st.markdown("<h4 style='color:#1E3A8A;'>Hatalı Soruların Detaylı Analizi:</h4>", unsafe_allow_html=True)
    
    errors = [x for x in st.session_state.log if not x["is"]]
    if not errors:
        st.success("Mükemmel! Hiç hata yapmadınız.")
    else:
        for err in errors:
            st.markdown(f"""
                <div class="error-card">
                    <span class="question-number">Soru {err['num']}</span><br><br>
                    <b style="color:#000; font-size:18px;">{err['q']}</b><br><br>
                    <div style="color:#000;">❌ Sizin Cevabınız: <span style="color:#e53e3e; font-weight:bold;">{err['u']}</span></div>
                    <div style="color:#000;">✅ Doğru Cevap: <span style="color:#38a169; font-weight:bold;">{err['c']}</span></div>
                </div>
            """, unsafe_allow_html=True)

    if st.button("ANA MENÜYE DÖN"):
        st.session_state.clear()
        st.rerun()
