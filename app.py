import streamlit as st
from utils.pdf_loader import load_multiple_pdfs
from utils.chunking import split_text
from utils.embeddings import create_embeddings, embed_query
from utils.vector_store import create_vector_store, search_vector_store
from utils.chatbot import ask_gemini
from utils.summary import summarize_document
from utils.pdf_generator import generate_summary_pdf
# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("🤖 AI Document Intelligence")

st.sidebar.markdown("""
### Features

✅ Multiple PDF Upload

✅ AI Summary

✅ Question Answering

✅ Semantic Search

✅ FAISS Vector Database

✅ Gemini AI
""")

# -----------------------------------
# Title
# -----------------------------------

st.title("📄 AI Document Intelligence Platform")

st.write(
    "Upload one or more PDF documents and ask questions about their content."
)

# -----------------------------------
# Upload PDFs
# -----------------------------------

uploaded_files = st.file_uploader(
    "📂 Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)
# -----------------------------------
# Process Uploaded PDFs
# -----------------------------------

if uploaded_files:

    st.success(f"✅ {len(uploaded_files)} PDF(s) uploaded successfully!")

    st.subheader(f"📁 Uploaded Files ({len(uploaded_files)})")

    for file in uploaded_files:
        st.write(f"📄 {file.name}")
    




    # -----------------------------------
    # Extract Text
    # -----------------------------------

    with st.spinner("Extracting text..."):

        text = load_multiple_pdfs(uploaded_files)
    st.write("Total Characters:", len(text))

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=250
    )

    # -----------------------------------
    # Split into Chunks
    # -----------------------------------

    chunks = split_text(text)

    # -----------------------------------
    # Create Embeddings
    # -----------------------------------

    embeddings = create_embeddings(chunks)
    st.subheader("🧠 Embedding Information")

    st.write("Embedding Shape:", embeddings.shape)
    # -----------------------------------
    # Create Vector Database
    # -----------------------------------

    vector_db = create_vector_store(embeddings)

    # -----------------------------------
    # Information
    # -----------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Chunks",
            len(chunks)
        )

    with col2:
        st.metric(
            "Vectors",
            vector_db.ntotal
        )

    st.divider()

    # ===================================
    # SUMMARY
    # ===================================

    st.header("📝 AI Document Summary")

    if st.button("Generate Summary"):

        with st.spinner("Generating summary..."):

            summary = summarize_document(text)

        st.success("Summary Generated Successfully!")

        st.markdown(summary)
        pdf_file = generate_summary_pdf(summary)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📥 Download Summary as PDF",
                data=file,
                file_name="AI_Document_Summary.pdf",
                mime="application/pdf"
            )
        st.divider()

    # ===================================
    # QUESTION ANSWERING
    # ===================================

    st.header("💬 Ask Questions")

    question = st.text_input(
        "Enter your question about the uploaded documents"
    )

    if question:

        with st.spinner("Searching documents..."):

            query_embedding = embed_query(question)

            indices = search_vector_store(
                vector_db,
                query_embedding,
                k=3
            )

            context = ""

            st.subheader("📚 Relevant Chunks")

            for idx in indices:

                if idx < len(chunks):

                    with st.expander(f"Chunk {idx+1}"):

                        st.write(chunks[idx])

                    context += chunks[idx] + "\n\n"

        with st.spinner("Generating answer..."):

            answer = ask_gemini(
                context,
                question
            )

        st.subheader("🤖 AI Answer")

        st.success(answer)

st.divider()

st.caption(
    "Built using Streamlit • FAISS • Sentence Transformers • Google Gemini"
)