import streamlit as st

st.set_page_config(page_title="DeckBrain", page_icon="🧠")
st.title("🧠 DeckBrain - File Upload")

# Upload multiple files
uploaded_files = st.file_uploader(
    "Upload your solution decks (PDF, DOCX, XLSX, PPTX)",
    type=["pdf", "docx", "xlsx", "pptx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.subheader("Uploaded Files")
    for f in uploaded_files:
        st.write(f"📂 {f.name} ({round(len(f.getvalue())/1024,2)} KB)")
