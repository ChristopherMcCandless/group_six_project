import streamlit as st
from src.services.text_summary_service import TextSummaryService

@st.cache_data
def get_handler():
    handler = TextSummaryService()
    handler.setup()
    return handler

st.title('Выделение основных тезисов из вашего текста')
text = st.text_area(
    label='Текст',
    placeholder='Введите текст',
    key='target_text')

btn = st.button('Сформировать конспект', type='primary')

if btn and text:
    preparedText, summary = get_handler().handle(text)
    #TODO сделать нормальный вывод
    st.write(preparedText)
    st.write(summary)
    

    



