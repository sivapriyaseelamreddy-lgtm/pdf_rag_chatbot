import streamlit as st
from pdf_loader import load_pdf
from rag import get_answer

st.set_page_config(page_title="PDF RAG Chatbot", page_icon="📚")

st.title("📚 PDF RAG Chatbot")

# Green button CSS
st.markdown("""
<style>

/* Full page background */
.stApp {
    background-color: black;
    color: white;
}

/* Title and text */
h1, h2, h3, p, label {
    color: white !important;
}

/* Text input box */
.stTextInput input {
    background-color: #222222;
    color: white;
}

/* Upload box */
[data-testid="stFileUploader"] {
    color: white;
}

/* Green Ask Button */
div.stButton > button {
    background-color: green;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
}

</style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF Loaded Successfully!")

    pdf_text = load_pdf(file_path)

    question = st.text_input("Ask question from PDF")

    if st.button("🔍 Ask"):
        if question:
            answer = get_answer(pdf_text, question)

            st.write("### 🤖 Answer:")
            st.write(answer)

        else:
            st.warning("⚠ Please enter a question")