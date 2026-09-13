import streamlit as st
from core.chatbot import ArtAdvisorBot

def configure_ui_styling():
    st.set_page_config(
        page_title="Galeria ArtAdvisor",
        layout="centered"
    )
    
    custom_css = """
    <style>
        .stApp {
            background-color: #FDFBF7;
        }
        
        header {
            visibility: hidden;
        }
        
        .title-text {
            color: #5C4033;
            text-align: center;
            font-family: 'Georgia', serif;
            font-weight: bold;
            font-size: 2.5rem;
            padding-top: 2rem;
            margin-bottom: 0rem;
        }
        
        .subtitle-text {
            color: #D4AF37;
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: 2rem;
        }
        
        .stChatMessage {
            border: 1px solid #C4A484 !important;
            border-radius: 8px;
            background-color: #FFFFFF !important;
        }
        
        .stChatMessage * {
            color: #334155 !important;
            line-height: 1.6 !important;
        }
        
        .stChatMessage table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            margin-bottom: 15px;
        }
        
        .stChatMessage th, .stChatMessage td {
            border: 1px solid #CBD5E1 !important;
            padding: 10px !important;
            text-align: left !important;
        }
        
        .stChatMessage th {
            background-color: #F8FAFC !important;
            font-weight: bold !important;
            color: #1E293B !important;
        }
        
        .stChatInputContainer * {
            color: #334155 !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def main():
    configure_ui_styling()

    st.markdown('<div class="title-text">Galeria ArtAdvisor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Asisten Kurator & Edukator Seni Rupa</div>', unsafe_allow_html=True)

    if "bot" not in st.session_state:
        st.session_state.bot = ArtAdvisorBot()
    
    if "ui_messages" not in st.session_state:
        st.session_state.ui_messages = []

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
                generator = bot.generate_response(result["messages"])
                response_text = st.write_stream(generator)
                
                st.session_state.ui_messages.append({"role": "assistant", "content": response_text})
                bot.save_assistant_response(response_text)
                
        elif result["action"] in ["continue", "exit"]:
            system_msg = result["message"]
            st.session_state.ui_messages.append({"role": "assistant", "content": system_msg})
            
            with st.chat_message("assistant"):
                st.markdown(system_msg, unsafe_allow_html=True)
                
            if result["action"] == "exit":
                st.stop()

if __name__ == "__main__":
    main()