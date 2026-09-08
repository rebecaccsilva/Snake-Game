import streamlit as st

COLS = 5
ROWS = 5

if "snake" not in st.session_state:
    st.session_state.snake= [(0,1),(0,2),(0,3)]
snake_set=set(st.session_state.snake)

st.title("Snake II 🐍")

grid_html = '<div style="display:grid; grid-template-columns:repeat(5, 30px); gap:2px;">'
for linhas in range(ROWS):
    for coluna in range(COLS):
        if (coluna,linhas) in snake_set:
            cor="green"
        else:
            cor="#333"
        grid_html += f'<div style="width:30px; height:30px; background:{cor};"></div>'
grid_html += '</div>'

st.markdown(grid_html, unsafe_allow_html=True)

st.text_input("teste")