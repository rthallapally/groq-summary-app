import streamlit as st
from summarizer import summarize_text

st.title("📝 Text Summarizer with Groq")

input_text = st.text_area("Paste the text you want to summarize:")

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            result = summarize_text(input_text)
            st.markdown("### ✨ Summary")
            st.write(result)
