import streamlit as st
import json
from core.chatbot import ArtAdvisorBot

def configure_ui_styling():
    st.set_page_config(page_title="Galeria ArtAdvisor", layout="wide", initial_sidebar_state="expanded")
    
    custom_css = """
    <style>
        .stApp { background-color: #FDFBF7; }
        header { visibility: hidden; }
        .title-text { color: #5C4033; text-align: center; font-family: 'Georgia', serif; font-weight: bold; font-size: 2.5rem; padding-top: 1rem; margin-bottom: 0rem; }
        .subtitle-text { color: #D4AF37; text-align: center; font-family: 'Arial', sans-serif; font-size: 1.2rem; font-weight: 500; margin-bottom: 2rem; }
        .stChatMessage { border: 1px solid #C4A484 !important; border-radius: 8px; background-color: #FFFFFF !important; }
        .stChatMessage * { color: #334155 !important; line-height: 1.6 !important; }
        .stChatMessage table { width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 15px; }
        .stChatMessage th, .stChatMessage td { border: 1px solid #CBD5E1 !important; padding: 10px !important; text-align: left !important; }
        .stChatMessage th { background-color: #F8FAFC !important; font-weight: bold !important; color: #1E293B !important; }
        .stChatInputContainer * { color: #334155 !important; }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def main():
    configure_ui_styling()

    # --- INISIALISASI STATE ---
    if "bot" not in st.session_state:
        st.session_state.bot = ArtAdvisorBot()
    if "ui_messages" not in st.session_state:
        st.session_state.ui_messages = []

    # --- SIDEBAR (FITUR BONUS) ---
    with st.sidebar:
        st.markdown("### Kontrol Parameter")
        temperature = st.slider("Tingkat Kreativitas (Temperature)", min_value=0.0, max_value=1.0, value=0.3, step=0.1, help="0 = Kaku/Faktual, 1 = Kreatif/Ekspresif")
        max_tokens = st.slider("Panjang Jawaban (Max Tokens)", min_value=256, max_value=2048, value=1024, step=256)
        
        st.divider()
        st.markdown("### Statistik Sesi")
        stats = st.session_state.bot.history.get_statistics()
        st.write(f"**Total Pesan:** {stats['total']}")
        st.write(f"**Pesan Anda:** {stats['user']}")
        st.write(f"**Respon ArtAdvisor:** {stats['bot']}")

        st.divider()
        st.markdown("### Memori Obrolan")
        # Tombol Download
        export_data = st.session_state.bot.history.get_export_data()
        st.download_button(label="Unduh Riwayat (JSON)", data=export_data, file_name="artadvisor_history.json", mime="application/json", use_container_width=True)
        
        # Tombol Upload
        uploaded_file = st.file_uploader("unggah file .json untuk melanjutkan obrolan", type="json")
        if uploaded_file is not None:
            if st.button("Muat Data", use_container_width=True):
                try:
                    history_data = json.load(uploaded_file)
                    st.session_state.bot.history.import_from_data(history_data)
                    st.session_state.ui_messages = history_data.copy()
                    st.rerun()
                except Exception:
                    st.error("Format JSON tidak valid!")

    # --- UI UTAMA ---
    st.markdown('<div class="title-text">Galeria ArtAdvisor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Asisten Kurator & Edukator Seni Rupa</div>', unsafe_allow_html=True)

    for msg in st.session_state.ui_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"], unsafe_allow_html=True)

    user_input = st.chat_input("Tanyakan seputar karya seni, sejarah, atau panduan koleksi...")

    if user_input:
        if user_input.strip().lower() == "/clear":
            st.session_state.ui_messages.clear()

        st.session_state.ui_messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        bot = st.session_state.bot
        result = bot.process_input(user_input)

        if result["action"] == "chat":
            with st.chat_message("assistant"):
                # Menyelipkan parameter slider ke mesin LLM
                generator = bot.generate_response(result["messages"], temperature, max_tokens)
                response_text = st.write_stream(generator)
                
                st.session_state.ui_messages.append({"role": "assistant", "content": response_text})
                bot.save_assistant_response(response_text)
                st.rerun() # Memaksa sistem memperbarui angka statistik di Sidebar
                
        elif result["action"] in ["continue", "exit"]:
            system_msg = result["message"]
            st.session_state.ui_messages.append({"role": "assistant", "content": system_msg})
            with st.chat_message("assistant"):
                st.markdown(system_msg, unsafe_allow_html=True)
            if result["action"] == "exit":
                st.stop()

if __name__ == "__main__":
    main()