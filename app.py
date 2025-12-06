import streamlit as st
from openai import OpenAI

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="RND-M Asistan",
    page_icon="🌰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS İLE TEMA ENTEGRASYONU (Senin Sitene Uydurma) ---
st.markdown("""
    <style>
    /* ANA ARKAPLAN - Senin sitenin koyu rengi (#0f172a) */
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }

    /* SIDEBAR (YAN MENÜ) TASARIMI */
    div[data-testid="stSidebar"] {
        background-color: #1e293b; /* Biraz daha açık koyu ton */
        border-right: 1px solid #2e7d32;
    }

    /* BAŞLIKLAR */
    h1, h2, h3 {
        color: #4ade80 !important; /* Parlak Yeşil */
        font-family: 'Courier New', monospace; /* Terminal havası */
    }

    /* BİLGİ KUTUSU (INFO BOX) TASARIMI - SANA ÖZEL */
    .info-box {
        background: rgba(30, 41, 59, 0.8); /* Yarı saydam koyu */
        border: 1px solid #4ade80; /* Yeşil Çerçeve */
        border-radius: 10px;
        padding: 20px;
        color: #ecfdf5;
        font-family: 'Courier New', monospace;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.1);
        margin-bottom: 20px;
    }

    .info-box i {
        color: #fbbf24; /* İkonlar sarı */
    }

    /* SOHBET BALONLARI */
    div[data-testid="stChatMessage"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
    }
    
    /* Kullanıcı Mesajı */
    div[data-testid="stChatMessage"][data-testid="user"] {
        background-color: #064e3b; /* Koyu yeşil arka plan */
    }

    </style>
    """, unsafe_allow_html=True)

# --- YAN MENÜ ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hazelnut.png", width=70)
    st.title("RND-M v1.0")
    st.markdown("---")
    st.info("**👨‍💻 Geliştirici: Giresun Fen Lisesi**")
    st.write("Doğu Karadeniz Fındık Ekonomisinde Dijital Dönüşüm Projesi.")
    st.caption("© 2025 RND-M Teknoloji")

# --- ANA EKRAN ---
col1, col2 = st.columns([1, 8])
with col1:
    st.write("")
with col2:
    st.title("RND-M Teknik Asistanı")
    
    # --- TASARIMA UYDURULMUŞ BİLGİ KUTUSU ---
    st.markdown("""
    <div class="info-box">
        <b>💡 SİSTEM HAZIR. ŞUNLARI SORABİLİRSİNİZ:</b><br><br>
        • <i>"Saha testlerinde (Sahil/Yüksek kol) ne sonuç aldınız?"</i><br>
        • <i>"Cihazın içindeki Arduino ve sensörler nasıl çalışıyor?"</i><br>
        • <i>"Manuel kırma yöntemi neden ekonomik zarar yaratıyor?"</i>
    </div>
    """, unsafe_allow_html=True)

# --- API BAĞLANTISI ---
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"], 
    )
except Exception:
    st.error("Sistem Hatası: API Anahtarı bulunamadı.")

# --- SİSTEM ZEKASI ---
system_prompt = """
Sen RND-M Projesinin Yapay Zeka Mühendisisin.
GELİŞTİRİCİ: Giresun Fen Lisesi Öğrencileri.
GÖREV: Proje raporundaki teknik verileri savunmak.

TEKNİK HAFIZA:
1. SORUN: Manuel randıman ölçümü (çekiçle) zaman kaybı ve hata dolu. %1 hata = Milyonlarca dolar kayıp.
2. ÇÖZÜM: RND-M Cihazı. Donanım: Arduino Nano, Load Cell, HX711, LCD Ekran. Yöntem: Standart 250gr numune.
3. KANIT: Giresun'da 5 lokasyonda test edildi. Manuel yöntemin üreticinin hakkını yediği (aşağı yuvarlama yaptığı) kanıtlandı.
4. SONUÇ: Cihaz saniyeler içinde %100 doğru sonuç veriyor. Üreticilerin %90'ı eski sisteme güvenmiyor.

KURALLAR:
- ASLA İngilizce teknik kodları (Örn: [/INST], </s>) cevapta gösterme.
- Profesyonel, ciddi ve teknik bir dil kullan. "Kanka" deme.
- Soruları Giresun'daki saha verilerine dayanarak cevapla.
"""

# --- SOHBET GEÇMİŞİ ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Sistem aktif. RND-M projesiyle ilgili teknik sorularınızı bekliyorum."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- KULLANICI GİRİŞİ VE FİLTRELEME ---
if prompt := st.chat_input("Komut giriniz..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Llama 3 veya Mistral (Ücretsiz Modeller)
            stream = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free",
                messages=st.session_state.messages,
                stream=True,
                temperature=0.3,
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    part = chunk.choices[0].delta.content
                    
                    # --- FİLTRELEME SİSTEMİ (ÇÖP TEMİZLİĞİ) ---
                    # Gelen parçada yasaklı kelime varsa onu boşlukla değiştir
                    part = part.replace("[/INST]", "").replace("</s>", "").replace("<s>", "")
                    
                    full_response += part
                    
                    # Ekrana basarken de son bir kontrol yap
                    clean_display = full_response.replace("[/INST]", "").replace("</s>", "")
                    response_placeholder.markdown(clean_display + "▌")
            
            # Son hali temiz bir şekilde yaz
            final_clean = full_response.replace("[/INST]", "").replace("</s>", "")
            response_placeholder.markdown(final_clean)
        
        except Exception as e:
            st.error(f"Bağlantı hatası: {e}")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
