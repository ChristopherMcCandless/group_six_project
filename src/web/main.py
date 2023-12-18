import streamlit as st
from src.services.text_summary_service import TextSummaryService

@st.cache_data
def get_handler():
    handler = TextSummaryService()
    return handler

st.title('Выделение основных тезисов из вашего текста')
text = st.text_area(
    label='',
    placeholder='Введите текст',
    key='target_text')

btn = st.button('Сформировать конспект', type='primary')

if btn and text:
    originalSummary, summary = get_handler().handle_ru(text)
    #TODO сделать нормальный вывод
    st.write('## Оригинальное саммари:', )
    st.write(originalSummary)
    st.write('## Итоговый конспект:')
    st.write(summary)
    
    



