import streamlit as st
from openai import OpenAI

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="RND-M Asistanı",
    page_icon="🌰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS: KURUMSAL VE PROFESYONEL TASARIM ---
st.markdown("""
    <style>
    /* ANA ARKAPLAN - Koyu Tema */
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }

    /* GİZLENECEK ÖGELER */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* YAN MENÜ */
    div[data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #2e7d32;
    }

    /* BAŞLIK VE METİNLER */
    h1, h2, h3 {
        color: #4ade80 !important;
        font-family: 'Courier New', monospace;
    }

    /* BİLGİ KUTUSU */
    .info-box {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #4ade80;
        border-radius: 10px;
        padding: 20px;
        color: #ecfdf5;
        font-family: 'Courier New', monospace;
        margin-bottom: 20px;
    }

    /* KULLANICI MESAJI */
    div[data-testid="stChatMessage"][data-testid="user"] {
        background-color: #064e3b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- YAN MENÜ: PROJE KÜNYESİ ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hazelnut.png", width=70)
    st.title("RND-M ")
    st.markdown("**Konumsal Veri Destekli Dijital Randıman Sistemi**")
    st.markdown("---")
    
    st.success("👨‍💻 **Geliştirici:** Giresun Fen Lisesi")
    st.info("📂 **Dal:** Coğrafya / Tarım Teknolojileri")
    
    with st.expander("📊 Proje İstatistikleri"):
        st.write("• **Analiz:** Farklı Randıman Türleri")
        st.write("• **Hata Payı:** %0 (Dijital)")
        st.write("• **Ekonomik Risk:** %1 Hata = Milyonlarca Dolar")
        
    st.caption("© 2025 RND-M Teknoloji")

# --- ANA EKRAN ---
col1, col2 = st.columns([1, 8])
with col1:
    st.write("")
with col2:
    st.title("RND-M Proje Asistanı")
    
    # Kullanıcıya Soru Önerileri
    st.markdown("""
    <div class="info-box">
        <b>🤖 SİSTEM HAZIR. ŞUNLARI SORABİLİRSİNİZ:</b><br><br>
        • <i>"Saha çalışmalarında ne tür fındıklar analiz edildi?"</i><br>
        • <i>"Manuel kırma yöntemi neden hatalı sonuç veriyor?"</i><br>
        • <i>"Cihazın çalışma prensibi ve formülü nedir?"</i><br>
        • <i>"Üreticilerin mevcut sisteme güveni ne durumda?"</i>
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

# --- SİSTEM ZEKASI (GÜNCELLENMİŞ BEYİN) ---
system_prompt = """
Sen RND-M (Randıman Analiz Sistemi) projesinin yapay zeka sözcüsü ve baş mühendisisin.

### 🆔 KİMLİK:
- **GELİŞTİRİCİ:** Giresun Fen Lisesi Öğrencileri.
- **PROJE ADI:** Doğu Karadeniz Fındık Ekonomisinde Şeffaflık ve Standardizasyon (RND-M).
- **ALAN:** Coğrafya / Tarım Teknolojileri.

### 🧠 GÜNCELLENMİŞ TEKNİK HAFIZA (BUNLARI KULLAN):

1. **SORUN ANALİZİ (MEVCUT DURUM):**
   - Randıman ölçümü hala manuel (çekiçle kırma, göz kararı ayıklama) yapılıyor.
   - Bu yöntem zaman alıcıdır ve güven sorunlarına yol açar.
   - 2.5 Milyar dolarlık ihracat ekonomisinde %1'lik ölçüm hatası, milyonlarca dolar kayıp demektir.
   - [cite_start]**Anket Sonucu:** Üreticilerin %90'ı mevcut manuel sisteme GÜVENMEMEKTEDİR[cite: 182].

2. **ÇÖZÜM VE DONANIM (RND-M CİHAZI):**
   - [cite_start]**Donanım:** Arduino Nano (İşlemci), Yük Hücresi/Load Cell (Hassas Tartım), HX711 Kartı, LCD Ekran[cite: 169].
   - **Yazılım:** "Standart Numune" prensibiyle çalışır.
   - [cite_start]**FORMÜL:** `(İç Ağırlık / 250) * 100`[cite: 171].
   - [cite_start]**Hız:** Manuel işlem dakikalar sürerken, dijital sistem saniyeler içinde sonuç verir[cite: 196].

3. **SAHA TEST SONUÇLARI (KANITLAR):**
   - [cite_start]**Kapsam:** Proje kapsamında **farklı randıman türlerine sahip fındıklar** analiz edilmiştir[cite: 123].
   - [cite_start]**Bulgu:** Farklı kalite ve türlerdeki (Levant, Giresun kalite vb.) fındıklar üzerinde yapılan testlerde, manuel yöntemin tutarsız olduğu ve aşağı/yukarı yuvarlama hataları yaptığı kanıtlanmıştır[cite: 132, 190].
   - Dijital sistem, fındığın türü veya randımanı ne olursa olsun %100 doğru ve standart sonuç vermiştir.

4. **GELECEK HEDEFİ:**
   - [cite_start]Cihaza Bluetooth/Wi-Fi eklenerek verilerin haritaya işlenmesi ve "Bölgesel Verim Haritası" oluşturulması[cite: 204].

### 🗣️ KONUŞMA KURALLARI:
- **Profesyonel ve Bilimsel Ol:** Asla "Kanka" deme. Bir mühendis ciddiyetiyle konuş.
- **Kanıt Göster:** Cevaplarında "Analiz sonuçlarımıza göre...", "Farklı randıman türlerinde yaptığımız testlere göre..." gibi ifadeler kullan.
- **Teknik Detay Ver:** Donanım sorulursa Arduino ve Load Cell'den bahset.
- **İngilizce Kodları Gizle:** Cevapta [/INST] gibi kodlar görürsen sil.
"""

# --- SOHBET GEÇMİŞİ ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Merhaba. RND-M projesi ve farklı randıman türleri üzerindeki analizlerimiz hakkında sorularınızı yanıtlamaya hazırım."}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- KULLANICI GİRİŞİ ---
if prompt := st.chat_input("Proje hakkında teknik soru sorun..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            stream = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free",
                messages=st.session_state.messages,
                stream=True,
                temperature=0.3,
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    part = chunk.choices[0].delta.content
                    clean_part = part.replace("[/INST]", "").replace("</s>", "")
                    full_response += clean_part
                    response_placeholder.markdown(full_response + "▌")
            
            final_response = full_response.replace("[/INST]", "").replace("</s>", "")
            response_placeholder.markdown(final_response)
        
        except Exception as e:
            st.error(f"Bağlantı hatası: {e}")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
