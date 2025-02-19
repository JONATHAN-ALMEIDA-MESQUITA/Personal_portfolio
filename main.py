import streamlit as st
from about import render_about
from projects import render_projects
from certifications import render_certifications
# Configuração de pagina
st.set_page_config(layout="wide", page_title="Portifólio")


# Menu lateral "sidebar"
menu = st.sidebar.radio( 
    'Menu', 
    options=["About 🔍", "Projetcs 🚀", "Cerifications 🏆"])


# Dicionario para mapear o menus as funções de renderização
menu_functions = {
    "About 🔍": render_about, 
    "Projetcs 🚀": render_projects,
    "Cerifications 🏆" : render_certifications
}


# Renderiza a seção selecionada
menu_functions[menu]()