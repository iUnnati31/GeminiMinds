import streamlit as st
import random

# Function to extract questions and answers from the text file
def load_questions_and_answers(file_path):
    questions_and_answers = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Split the content by each question-answer section
    entries = content.split("Question:")
    for entry in entries[1:]:  
        parts = entry.split("Answer:")
        if len(parts) == 2:
            question = parts[0].strip()
            answer = parts[1].strip()
            questions_and_answers.append({"question": question, "answer": answer})
    
    return questions_and_answers

# Load questions and answers from the text file
file_path = 'F:\\Langchain\\Interview_Ques_Creator\\research\\answers.txt'
questions_and_answers = load_questions_and_answers(file_path)

# Streamlit App with background color styles
st.markdown(
    """
    <style>
        .title-container {
            background-color: #C6E7FF; 
            padding: 10px;
            border-radius: 10px;
        }
        .title {
            color: black;
            font-size: 40px; 
            text-align: center;
        }
        .subtitle-container {
            background-color: #4B0082; 
            border-radius: 10px;
            margin-top: 10px;
        }
        .subtitle {
            color: white;
            font-size: 18px;
            text-align: center;
        }
        .question-container {
            background-color: #ADD8E6;
            border-radius: 10px;
            margin-top: 20px;
        }
        .question {
            color: #133E87;
            font-size: 22px;
            font-weight: bold;
        }
        .answer-container {
            background-color: #98FB98;
            border-radius: 10px;
            margin-top: 10px;
        }
        .answer {
            color: #006400;
            font-size: 20px;
        }
        .footer-container {
            background-color: #A9A9A9;
            border-radius: 10px;
            margin-top: 20px;
        }
        .footer {
            color: white;
            font-size: 17px;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True
)

# Title and subtitle with custom background colors
st.markdown("<div class='title-container'><h1 class='title'>🎓 Interview Question Generator</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-container'><p class='subtitle'>Welcome! This app generates random interview questions for practice. Click the button below to test yourself and learn new insights! 🚀</p></div>", unsafe_allow_html=True)

# Button to generate questions
if st.button("🔍 Generate Question"):
    if questions_and_answers:
        qa = random.choice(questions_and_answers)
        st.markdown("<div class='question-container'><p class='question'>❓ Question:</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='question'>{qa['question']}</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='answer-container'><p class='answer'>💡 Answer:</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='answer'>{qa['answer']}</p></div>", unsafe_allow_html=True)
        st.write("🔄 Want another question? Click the button again!")
    else:
        st.write("⚠️ No questions found in the file. Please check the file path or contents.")
else:
    st.write("👆 Click 'Generate Question' to see a new question and answer.")

# Footer with background color
st.markdown("<div class='footer-container'><p class='footer'>🤖 Developed to help you ace your interviews! Good luck! 🍀</p></div>", unsafe_allow_html=True)
