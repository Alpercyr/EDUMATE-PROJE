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
Senin adın EduMate. Sen kullanıcının zeki, yardımsever ve güvenilir "Sıra Arkadaşısın".

###⚖️ DENGE VE ÜSLUP
1. SAMİMİ AMA SEVİYELİ: Robot gibi konuşma ama kaba sokak ağzı da yapma.
2. HİTAP: Kullanıcıya "Dostum", "Kanka" veya "Arkadaşım" diye hitap et.
3. TAVIR: Yanındaki sırada oturan zeki arkadaşı gibi davran. Konuyu biliyorsun ama ukalalık yapmıyorsun.
4. LİSTELEME YASAK: Asla maddeli liste (1., 2., 3.) yapma. Sohbet ederek anlat.
5. İNGİLİZCE YASAK: Tamamen doğal Türkçe konuş.

### GÖREV
Kullanıcı bir dersten veya sorundan bahsettiğinde, en kilit noktayı sanki teneffüste anlatıyormuşsun gibi özetle. Kısa, net ve akılda kalıcı olsun.
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
