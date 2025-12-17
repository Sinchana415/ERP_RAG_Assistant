import streamlit as st
from rag import answer_question

st.set_page_config(page_title="ERP RAG Assistant")

st.title("📘 ERP Manual Q&A Assistant")

query = st.text_input("Ask a question about ERP policies")

if query:
    with st.spinner("Searching ERP manuals..."):
        answer, sources = answer_question(query)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Source Documents")
    for src in set(sources):
        st.write(f"- {src}")

