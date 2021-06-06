import streamlit as st
import time as tm
import numpy as np
import spacy

def normalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punctuation_map))

def get_vector(s):
    return np.sum(np.array([model[i] for i in normalize(s)]), axis=0)

st.set_page_config(layout='wide',page_title=" 💬 QuizLIT 💬")
hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)
st.title('QuizLIT 💬✍️')
st.subheader('A Text Semantic Similarity Web App')
st.write('Created by Veeral Shah, Remi LeBlanc, Catie Cronister, Lucia Page-Harley, \nMin Che, Dashiell Brookhart, Joshua Majano, and Emre Okcular')
intro_text = "Hello and welcome! \n\nTo use QuizLIT (Patent Pending): \n \nPlease enter two text entries in the \nprovided text boxes and use the Analyze \nbutton to see your results."
st.sidebar.title('Directions:')
st.sidebar.text(intro_text)
st.sidebar.multiselect('Subjects:',['Biology','Chemistry','Physics','Calculus','Geometry','World History','U.S History'], ['Biology','Chemistry'])
st.sidebar.file_uploader('Student Answers File Input:')
col1, col2 = st.beta_columns(2)
CORRECT_ANSWER = col1.text_area('CORRECT ANSWER:', value='', height=15)
STUDENT_ANSWER = col2.text_area('STUDENT ANSWER:', value='', height=15)
button = st.button('Analyze💡')
nlp = spacy.load('en_core_web_sm')
doc1 = nlp(CORRECT_ANSWER)
doc2 = nlp(STUDENT_ANSWER)
if button and CORRECT_ANSWER and STUDENT_ANSWER:
    progress_bar = st.progress(0)
    status_text = st.empty()
    similarity = doc2.similarity(doc1)
    for i in range(100):
        # Update progress bar.
        progress_bar.progress(i + 1)
        if i<25:
            status_text.text('Loading sentence corpus...')           
        # Update status text.
        if i >= 25 and i<50:
            status_text.text(f'Deciphering text semantics of entries...')
        if i >= 50 and i<75:
            status_text.text(f'Analyzing differences...')
        if i >= 75:
            status_text.text(f'Compiling similarity scores...')
        tm.sleep(0.05)
    status_text.text('')      
    st.write(str(round(similarity*100,3))+'% Similar')
    
    


