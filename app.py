import streamlit as st
from src.helper import llm_pipeline
from PyPDF2 import PdfReader

# Streamlit App Configuration
st.title("📘 Gemini Minds - An Inteview Question Generator")
st.write("Upload a PDF and this app will generate questions and answers based on its content!")

# File uploader for the PDF
uploaded_pdf = st.file_uploader("📄 Upload a PDF file", type=["pdf"])

if uploaded_pdf:
    # Save the uploaded file to a temporary location
    temp_file_path = f"temp_{uploaded_pdf.name}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_pdf.getbuffer())
    
    # Check the number of pages in the uploaded PDF
    reader = PdfReader(temp_file_path)
    num_pages = len(reader.pages)

    if num_pages > 50:
        st.warning("⚠️ The uploaded PDF has more than 10 pages. Please upload a PDF with 50 or fewer pages.")
    else:
        st.write("✅ PDF uploaded successfully!")

        # Button to generate questions
        if st.button("🔍 Generate Questions"):
            st.write("🔍 Processing the uploaded PDF...")

            try:
                # Use the llm_pipeline from helper.py
                answer_generation_chain, questions_list = llm_pipeline(temp_file_path)

                if questions_list:
                    st.write("🎯 Generated Questions:")
                    for i, question in enumerate(questions_list, start=1):
                        st.markdown(f"**Q{i}: {question}**")
                        
                        # Generate answer for each question
                        result = answer_generation_chain.run(question)
                        st.markdown(f"*Answer: {result}*")
                else:
                    st.warning("⚠️ No questions were generated. Please try uploading a different PDF.")
            except Exception as e:
                st.error(f"An error occurred while processing the file: {e}")
else:
    st.write("📂 Please upload a PDF to begin.")

# Footer
st.markdown("---")
st.markdown("<div class='footer-container'><p class='footer'>🤖 Developed to help you ace your interviews! Good luck! 🍀</p></div>", unsafe_allow_html=True)

