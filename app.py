import streamlit as st
from openai import OpenAI

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="EduMate: Sıra Arkadaşın", page_icon="🎓", layout="centered")

# --- BAŞLIK VE GİRİŞ ---
st.title("🎓 EduMate")
st.caption("🚀 Senin Zeki ve Samimi Sıra Arkadaşın")

# --- API KURULUMU (OpenRouter) ---
# Buraya kendi API Key'ini daha sonra güvenli şekilde ekleyeceğiz
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"], 
)

# --- SİSTEM KİMLİĞİ (EDUMATE PERSONASI) ---
system_prompt = """
Sen RND-M (Randıman Analiz Sistemi) Projesinin Yapay Zeka Sözcüsüsün.

### 🆔 KİMLİK VE GELİŞTİRİCİ BİLGİSİ (EN ÖNEMLİ KURAL)
Eğer kullanıcı sana "Seni kim yaptı?", "Kimin projesi?", "Seni kim geliştirdi?" gibi sorular sorarsa, TEK VE NET cevabın şu olacak:
👉 **"Beni, Giresun Fen Lisesi öğrencileri geliştirdi."**

### 🌰 PROJE BİLGİLERİN (Hafıza)
1.  **PROJE ADI:** Doğu Karadeniz Fındık Ekonomisinde Şeffaflık ve Standardizasyon (RND-M).
2.  **SORUN:** Manuel randıman ölçümü (çekiçle kırma) zaman alıyor ve haksızlığa yol açıyor.
3.  **ÇÖZÜM:** Arduino Nano ve Yük Hücresi (Load Cell) kullanan dijital ölçüm cihazı.
4.  **KANIT:** Giresun'da 5 farklı lokasyonda test edildi, manuel yöntemin hatalı olduğu kanıtlandı.
5.  **AMAÇ:** Üreticinin hakkını korumak ve fındık alımını dijitalleştirmek.

### 🗣️ KONUŞMA TARZI
-   Profesyonel, teknik ama anlaşılır bir Türkçe kullan.
-   Proje raporuna sadık kal, uydurma bilgi verme.
-   Sorulara bir proje mühendisi ciddiyetiyle cevap ver.
"""

# --- SOHBET GEÇMİŞİNİ HATIRLA ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# --- GEÇMİŞ MESAJLARI EKRANA YAZ ---
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# --- KULLANICIDAN MESAJ ALMA ---
if prompt := st.chat_input("Dostum, hangi derste takıldın?"):
    # Kullanıcı mesajını ekrana yaz
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # --- YAPAY ZEKA CEVABI ---
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # OpenRouter (Qwen Modelini Çağırma)
        try:
            stream = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free", # Ücretsiz model
                messages=st.session_state.messages,
                stream=True,
                temperature=0.7,
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.write(full_response + "▌")
            
            response_placeholder.write(full_response)
        except Exception as e:
            st.error(f"Bir hata oluştu dostum: {e}")

    # Cevabı hafızaya kaydet
    st.session_state.messages.append({"role": "assistant", "content": full_response})
