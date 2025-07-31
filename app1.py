# app.py

import streamlit as st
import os
from rag_engine1 import load_docs, split_docs, create_vectorstore, get_chat_chain_with_memory

st.set_page_config(page_title="StudyBuddy 📚", layout="wide")
st.title("📄 Upload your PDF chapter")

if "chat_history_ui" not in st.session_state:
    st.session_state.chat_history_ui = []

uploaded_file = st.file_uploader("Upload your PDF chapter", type="pdf")

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if "chat_chain" not in st.session_state or st.session_state.get("current_file") != uploaded_file.name:
        with st.spinner("Processing PDF and initializing chatbot..."):
            docs = load_docs(file_path)
            splits = split_docs(docs)
            vectorstore = create_vectorstore(splits)
            chat_chain = get_chat_chain_with_memory(vectorstore)

            st.session_state.chat_chain = chat_chain
            st.session_state.chat_history_ui = []
            st.session_state.current_file = uploaded_file.name

        st.success("Document processed. You can now ask questions.")
    else:
        chat_chain = st.session_state.chat_chain
        st.success("Document already loaded. Ask more questions!")

    query = st.text_input("Ask a question about the chapter:")
    if query:
        with st.spinner("Thinking..."):
            response = chat_chain.invoke({"question": query})
            answer = response["answer"]

       
            st.session_state.chat_history_ui.append(("🧑 You", query))
            st.session_state.chat_history_ui.append(("🤖 Assistant", answer))

       
        for role, msg in st.session_state.chat_history_ui:
            st.markdown(f"**{role}:** {msg}")

if st.button(" Reset App"):
    st.session_state.clear()
    st.experimental_rerun()
