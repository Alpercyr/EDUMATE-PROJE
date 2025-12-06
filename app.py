import streamlit as st
from openai import OpenAI

# --- SAYFA VE SEKME AYARLARI ---
st.set_page_config(
    page_title="RND-M: Dijital Randıman Sistemi",
    page_icon="🌰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS İLE GÖRSEL DÜZENLEMELER (Profesyonel Görünüm) ---
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    h1 {
        color: #2e7d32; /* Fındık Yeşili */
    }
    </style>
    """, unsafe_allow_html=True)

# --- YAN MENÜ (SIDEBAR) - PROJE KÜNYESİ ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hazelnut.png", width=80) # Fındık İkonu
    st.title("RND-M Projesi")
    st.markdown("---")
    st.subheader("👨‍💻 Geliştirici Ekip")
    st.info("**Giresun Fen Lisesi Öğrencileri**")
    
    st.subheader("📂 Proje Hakkında")
    st.caption("""
    Doğu Karadeniz Fındık Ekonomisinde Şeffaflık ve Standardizasyon için geliştirilmiş;
    Konumsal Veri Destekli Dijital Randıman Analiz Sistemi.
    """)
    st.markdown("---")
    st.write("© 2025 RND-M Teknoloji")

# --- ANA BAŞLIK ---
col1, col2 = st.columns([1, 5])
with col1:
    st.write("") # Boşluk
with col2:
    st.title("RND-M Asistanı")
    st.markdown("**Dijital Tarım ve Randıman Analiz Uzmanı**")

# --- API KURULUMU (OpenRouter) ---
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"], 
    )
except Exception as e:
    st.error("API Anahtarı hatası. Lütfen ayarlardan kontrol ediniz.")

# --- SİSTEM KİMLİĞİ (PROFESYONEL PERSONA) ---
system_prompt = """
Sen RND-M (Randıman Analiz Sistemi) projesinin yapay zeka sözcüsü ve teknik uzmanısın.

### 🆔 KİMLİK VE KÜNYE
- **GELİŞTİRİCİ:** Seni Giresun Fen Lisesi öğrencileri geliştirdi. (Bunu sorarlarsa gururla söyle).
- **PROJE ADI:** RND-M (Konumsal Veri Destekli Dijital Randıman Analiz Sistemi).

### 🧠 TEKNİK BİLGİ BANKAN (Rapor Verileri):
1. **SORUN:** Mevcut randıman ölçümü manuel (çekiçle) yapılıyor. Bu durum zaman kaybına, %1'e varan ölçüm hatalarına ve milyonlarca dolar ekonomik kayba yol açıyor.
2. **DONANIM:** Sistemde Arduino Nano mikrodenetleyici, ağırlık ölçümü için Yük Hücresi (Load Cell), veri dönüştürücü olarak HX711 kartı ve sonuç ekranı için LCD panel kullanılmıştır.
3. **YÖNTEM:** Fındık piyasasında geçerli olan 'Standart Numune (250gr)' yöntemini dijitalleştirir. Formül: (İç Ağırlık / 250) * 100.
4. **KANIT:** Giresun'da 5 farklı coğrafi lokasyonda (Sahil, Orta, Yüksek kol) saha testleri yapılmış, manuel yöntemin tutarsızlığı kanıtlanmıştır.
5. **AVANTAJ:** İşlem süresini dakikalardan saniyelere indirir, insan hatasını sıfırlar, şeffaflık sağlar.

### 🗣️ İLETİŞİM DİLİ VE KURALLAR:
- **Profesyonel Ol:** "Kanka", "Dostum" gibi ifadeler YASAK. "Sayın Kullanıcı" veya doğrudan hitap kullan.
- **Teknik ve Bilimsel Konuş:** Bir mühendis veya akademisyen ciddiyetiyle cevap ver.
- **İkna Edici Ol:** Projenin gerekliliğini savun.
- **Türkçe:** Sadece kusursuz İstanbul Türkçesi kullan.
"""

# --- SOHBET GEÇMİŞİ ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Merhaba. RND-M Dijital Randıman Sistemi hakkında size nasıl teknik destek sağlayabilirim?"}
    ]

# --- GEÇMİŞİ GÖSTERME ---
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- KULLANICI GİRİŞİ ---
if prompt := st.chat_input("Projenin teknik detayları veya amacı hakkında soru sorunuz..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- YAPAY ZEKA CEVABI ---
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Model Seçimi: Llama 3 veya Mistral (Ücretsiz ve Stabil)
            stream = client.chat.completions.create(
                model="meta-llama/llama-3-8b-instruct:free", 
                messages=st.session_state.messages,
                stream=True,
                temperature=0.3, # Daha ciddi ve tutarlı olması için düşük sıcaklık
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
        
        except Exception as e:
            st.error(f"Sistem bağlantısında bir hata oluştu: {e}")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
