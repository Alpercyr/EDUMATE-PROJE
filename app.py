import streamlit as st
from openai import OpenAI

# --- SAYFA AYARLARI (TÜBİTAK/TEKNOFEST STANDARDI) ---
st.set_page_config(
    page_title="RND-M: Dijital Randıman Analiz Sistemi",
    page_icon="🌰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS İLE KURUMSAL TASARIM ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #2e7d32; /* Fındık Yeşili */
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    div[data-testid="stSidebar"] {
        background-color: #e8f5e9;
    }
    .info-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- YAN MENÜ (PROJE KÜNYESİ) ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hazelnut.png", width=70)
    st.title("RND-M Projesi")
    st.markdown("**Doğu Karadeniz Fındık Ekonomisinde Şeffaflık ve Standardizasyon**")
    st.markdown("---")
    
    st.subheader("👨‍💻 Geliştirici Ekip")
    st.success("**Giresun Fen Lisesi Öğrencileri**")
    
    st.subheader("📊 Proje Özeti")
    st.info("""
    Konumsal veri destekli, Arduino tabanlı,
    taşınabilir dijital randıman ölçüm cihazı.
    """)
    
    with st.expander("🏆 Proje Hedefi"):
        st.write("Milyarlarca dolarlık fındık ekonomisinde manuel ölçüm hatalarını bitirmek ve üreticinin hakkını korumak.")
    
    st.markdown("---")
    st.caption("© 2025 RND-M Teknoloji")

# --- ANA EKRAN ---
col1, col2 = st.columns([1, 8])
with col1:
    st.write("")
with col2:
    st.title("RND-M Asistanı")
    st.markdown("##### 🤖 Proje Teknik Sözcüsü ve Veri Analisti")
    
    # Kullanıcıya ipucu kutusu
    st.markdown("""
    <div class="info-box">
    <b>💡 Şunları sorabilirsiniz:</b><br>
    • <i>"Saha testlerinde ne gibi sonuçlar aldınız?"</i><br>
    • <i>"Cihazın içinde hangi donanımlar var?"</i><br>
    • <i>"Manuel yöntem neden hatalı?"</i>
    </div>
    """, unsafe_allow_html=True)

# --- API BAĞLANTISI (OpenRouter - Llama 3) ---
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"], 
    )
except Exception as e:
    st.error("⚠️ API Anahtarı Hatası: Lütfen Streamlit Secrets ayarlarını kontrol edin.")

# --- SİSTEM KİMLİĞİ (PROJE VERİLERİYLE EĞİTİLMİŞ BEYİN) ---
system_prompt = """
Sen RND-M (Randıman Analiz Sistemi) projesinin yapay zeka sözcüsü ve teknik mühendisisin.

### 🆔 GELİŞTİRİCİ BİLGİSİ (ÇOK ÖNEMLİ)
Seni kimin geliştirdiği sorulursa net ve gururlu bir şekilde şu cevabı ver:
👉 **"Beni, Giresun Fen Lisesi öğrencileri, Türk fındık ekonomisine değer katmak için geliştirdi."**

### 🧠 TEKNİK HAFIZA (RAPORDAN ALINAN VERİLER):

1. **SORUN (NEDEN BU PROJE?):**
   - Türkiye dünya fındık üretiminin %60-70'ini karşılar[cite: 25].
   - Ancak randıman ölçümü hala "çekiçle kırma" ve "göz kararı" ayıklama ile yapılıyor[cite: 33].
   - Bu manuel yöntem zaman alıcıdır ve güven sorununa yol açar.
   - 2 milyar dolarlık ihracatta %1'lik bir ölçüm hatası, milyonlarca dolar kayıp demektir[cite: 28, 31].

2. **ÇÖZÜM (DONANIM VE YAZILIM):**
   - **Cihaz:** Arduino Nano mikrodenetleyici tabanlıdır.
   - **Sensör:** Hassas ağırlık ölçümü için Yük Hücresi (Load Cell) ve HX711 kartı kullanıldı[cite: 57].
   - **Ekran:** Sonuçlar şeffaf bir LCD ekranda gösterilir.
   - **Yöntem:** Fındık piyasasında geçerli olan "Standart Numune (250gr)" formülünü kullanır: (İç Ağırlık / 250) * 100[cite: 58, 59].
   - **Hız:** Dakikalar süren işlemi saniyelere indirir[cite: 14].

3. **SAHA TESTLERİ VE KANITLAR:**
   - **Kapsam:** Giresun'da Sahil, Orta ve Yüksek Kol (rakım) dahil 5 farklı lokasyonda test yapıldı[cite: 12, 63].
   - **Bulgu 1:** Manuel yöntemin, özellikle 1. ve 3. lokasyonlarda "aşağı yuvarlama" eğiliminde olduğu ve üreticiye zarar ettirdiği tespit edildi.
   - **Bulgu 2:** RND-M cihazı %100 dijital doğrulukla, üreticinin hakkını teslim etti (Örn: Sahilde manuel %50 ölçerken, cihaz %50.4 ölçtü)[cite: 76, 85].
   - **Anket:** Üreticilerin %90'ı mevcut manuel sisteme güvenmediğini belirtti.

4. **GELECEK HEDEFİ:**
   - Cihaza Bluetooth/Wi-Fi eklenerek verilerin haritaya işlenmesi ve "Bölgesel Verim Haritası" oluşturulması[cite: 92].

### 🗣️ KONUŞMA TARZI:
- Bir TÜBİTAK proje sunumu yapar gibi **profesyonel, bilimsel ve ikna edici** konuş.
- Asla "Dostum", "Kanka" deme. "Sayın Kullanıcı" veya doğrudan cevap kullan.
- Sorulara cevap verirken yukarıdaki **sayısal verileri ve kanıtları** kullan.
"""

# --- SOHBET GEÇMİŞİ ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Merhaba. RND-M projesi ve saha test verilerimiz hakkında size nasıl yardımcı olabilirim?"}
    ]

# --- GEÇMİŞİ GÖSTER ---
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- KULLANICI GİRİŞİ ---
if prompt := st.chat_input("Sorunuzu buraya yazın..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- CEVAP ÜRETME ---
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Llama 3 Modeli (Stabil ve Ücretsiz)
            stream = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free",
                messages=st.session_state.messages,
                stream=True,
                temperature=0.3, # Ciddi ve tutarlı olması için düşük sıcaklık
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
        
        except Exception as e:
            st.error(f"Bağlantı hatası: {e}")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
