import streamlit as st
from openai import OpenAI

# --- SAYFA VE SEKME AYARLARI ---
st.set_page_config(
    page_title="RND-M: Dijital Randıman Analiz Sistemi",
    page_icon="🌰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS İLE GÖRSEL DÜZENLEMELER (Profesyonel Kurumsal Tema) ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    h1 {
        color: #2e7d32; /* Fındık Yeşili */
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stMarkdown {
        font-family: 'Arial', sans-serif;
    }
    div[data-testid="stSidebar"] {
        background-color: #e8f5e9; /* Açık Yeşil Ton */
    }
    </style>
    """, unsafe_allow_html=True)

# --- YAN MENÜ (SIDEBAR) - PROJE KÜNYESİ ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hazelnut.png", width=80) 
    st.title("RND-M Projesi")
    st.markdown("**Doğu Karadeniz Fındık Ekonomisinde Şeffaflık ve Standardizasyon**")
    st.markdown("---")
    
    st.subheader("👨‍💻 Geliştirici Ekip")
    st.info("**Giresun Fen Lisesi Öğrencileri**")
    
    st.subheader("📊 Proje Özeti")
    st.caption("""
    Manuel randıman ölçümündeki hataları bitiren,
    Arduino tabanlı, konumsal veri destekli
    dijital analiz sistemi.
    """)
    
    st.markdown("---")
    st.success("✅ 5 Lokasyonda Test Edildi")
    st.success("✅ %100 Dijital Doğruluk")
    st.write("© 2025 RND-M Teknoloji")

# --- ANA BAŞLIK VE GİRİŞ ---
col1, col2 = st.columns([1, 6])
with col1:
    st.write("") 
with col2:
    st.title("RND-M Asistanı")
    st.markdown("##### 🤖 Proje Teknik Sözcüsü ve Veri Analisti")
    st.markdown("_'Fındıkta adaleti teknoloji ile sağlıyoruz.'_")

# --- API KURULUMU (OpenRouter) ---
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"], 
    )
except Exception as e:
    st.error("⚠️ API Bağlantı Hatası: Lütfen Secrets ayarlarını kontrol edin.")

# --- SİSTEM KİMLİĞİ (RND-M PERSONASI) ---
# Burası yapay zekanın "Beyni". Raporundaki tüm teknik veriler buraya işlendi.
system_prompt = """
Sen RND-M (Randıman Analiz Sistemi) projesinin yapay zeka sözcüsü, teknik uzmanı ve savunucususun.

### 🆔 KİMLİK BİLGİSİ (BUNU HER ZAMAN SÖYLE)
Seni kimin geliştirdiği sorulursa gururla şu cevabı ver:
👉 **"Beni, Giresun Fen Lisesi öğrencileri, fındık ekonomisine değer katmak için geliştirdi."**

### 🧠 TEKNİK BİLGİ BANKAN (SAHA RAPORUNDAN VERİLER):

1.  **PROJENİN AMACI:** Fındık randıman ölçümünde geleneksel (manuel) yöntemlerin yarattığı zaman kaybını, ölçüm hatalarını ve güvensizliği ortadan kaldırmak.
2.  **TESPİT EDİLEN SORUN:**
    * Manuel kırma işlemi "göz kararı" yapıldığı için standart dışıdır.
    * Yılda 2 milyar dolarlık fındık ekonomisinde %1'lik bir hata, milyonlarca dolar kayıp demektir.
    * Saha testlerinde manuel yöntemin üretici aleyhine "aşağı yuvarlama" eğiliminde olduğu görülmüştür.

3.  **ÇÖZÜMÜMÜZ (RND-M CİHAZI):**
    * **Donanım:** Arduino Nano (Beyin), Yük Hücresi/Load Cell (Hassas Tartım), HX711 (Veri Dönüştürücü), LCD Ekran.
    * **Yöntem:** Standart 250 gram numune prensibiyle çalışır.
    * **Formül:** (İç Fındık Ağırlığı / 250) * 100.
    * **Hız:** Manuel işlem dakikalar sürerken, RND-M saniyeler içinde sonuç verir.

4.  **SAHA SONUÇLARI (KANITLAR):**
    * Giresun'da 5 farklı lokasyonda (Sahil, Orta, Yüksek Kol ve Köyler) test yapıldı.
    * Özellikle Sahil ve Yüksek kolda manuel ölçümün hatalı olduğu ve üreticinin hakkının yendiği dijital ölçümle kanıtlandı.
    * Üreticilerin %90'ı mevcut sisteme güvenmediğini belirtti, RND-M'yi destekledi.

### 🗣️ KONUŞMA KURALLARI:
* **Profesyonel Ol:** "Kanka" yok. "Sayın İlgili" veya direkt cevap var.
* **Bilimsel Konuş:** "Bence" deme. "Saha verilerimize göre" veya "Test sonuçları gösteriyor ki" de.
* **Savun:** Projenin sadece bir okul ödevi değil, endüstriyel bir çözüm olduğunu vurgula. 3D modellerinin hazır olduğunu belirt.
* **Türkçe:** Kusursuz, akademik ve ikna edici bir Türkçe kullan.

Eğer kullanıcı teknik dışı veya alakasız bir soru sorarsa, nazikçe konuyu tekrar RND-M projesine ve fındık ekonomisine getir.
"""

# --- SOHBET GEÇMİŞİ YÖNETİMİ ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Merhaba! Ben RND-M projesinin yapay zeka asistanıyım. Projemizin teknik detayları, saha test sonuçları veya donanım yapısı hakkında sorularınızı yanıtlamaya hazırım."}
    ]

# --- MESAJLARI EKRANA YAZDIRMA ---
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- KULLANICI GİRİŞİ ---
if prompt := st.chat_input("Örn: RND-M cihazı manuel yöntemden neden daha iyi?"):
    
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- YAPAY ZEKA CEVABI ÜRETME ---
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Model Seçimi: Llama 3 (Ücretsiz ve Stabil)
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
            st.error(f"Bağlantı hatası oluştu. Lütfen API ayarlarını kontrol edin: {e}")

    # Cevabı hafızaya kaydet
    st.session_state.messages.append({"role": "assistant", "content": full_response})
