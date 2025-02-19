import streamlit as st
from streamlit_elements import elements, mui # type: ignore



def render_certifications():
    st.title("🎓 Seja bem-vindo à seção de certificados!")
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)


    #Dicionario de dados dos certificados
    certificados_fiap = [
        {
            "titulo": "🎓 Graduação em Bando de dados", 
            "data": "Dez/2023",
            "descricao": " FIAP: Curso superior de tecnologia em banco de dados .",
            "link": "https://drive.google.com/file/d/110X2qvel8qkV7t9_J3XXC2YR5--Qo8oR/view?usp=sharing"
        },
        {
            "titulo": "🎓 Banco de Dados e Analista BI",
            "data": "Dez/23",
            "descricao": "Administração de Banco de Dados e Analista de BI.",
            "link": "https://drive.google.com/file/d/1H_woD_A1j1_xBYaofoPxpdtqs4ldpvYC/view?usp=sharing"
        },
        {
            "titulo": "🎓 Infraestrutura de Banco de Dados",
            "data": "Dez/22",
            "descricao": "FIAP: Infraestrutura de Banco de Dados",
            "link": "https://drive.google.com/file/d/1OF8m7KxqL6ML4fNluxaCnIZWBQV8rF-3/view?usp=sharing"
        },
        {
            "titulo": "🎓 Suporte a Tomada de Decisões",
            "data": "jul/23",
            "descricao": "FIAP: Suporte a Tomada de Decisões",
            "link": "https://drive.google.com/file/d/1CnaS7-VlLlctmgabt1negLy-akptbnH2/view?usp=sharing"
        },
        {
            "titulo": "🎓 MATEMÁTICA",
            "data": "Out/24",
            "descricao": "FIAP: MATEMÁTICA",
            "link": "https://drive.google.com/file/d/1oo2_0urMGzoiWjUqylishiNg0u_3LmN_/view?usp=sharing"
        }]

    certificados_asimov=[      
        {
            "titulo": "🎓 Analise de dados com pandas e sql",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning ",
            "link": "https://drive.google.com/file/d/1d_J4HuCRHwTz3EwUFpIJDkEqPvrdkSiY/view?usp=sharing"
        },
        {
            "titulo": "🎓 Árvores de Decisão",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1js-u_iEl0fFnPcAgyphjPL3KSKgi0ArI/view?usp=sharing"
        },
        {
            "titulo": "🎓 Fundamentos de AI e ML",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1MzYP-dWr6TaDemP4k21QTuLG6AF_NeKe/view?usp=sharing"
        },
        {
            "titulo": "🎓 Matemática para Análise de Dados",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1-F8J1qxMj6rSmNABFd1zHZ7pY5T23GNe/view?usp=sharing"
        },        
        {
            "titulo": "🎓 Modelos de Class. e Regressão",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1c-1i2jaIODftUCpp9pkTfD0WozRw-Dxk/view?usp=sharing"
        },
        {
            "titulo": "🎓 Modelos Não Supervisionados",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1lkNvjfUw5y2iTPwFxj_UVHID3Ty8ZckW/view?usp=sharing"
        },
        {
            "titulo": "🎓 Python Starter",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1bqRXM-cSoMUFGEg9vduTyQoBuCNMTS49/view?usp=sharing"
        },
        {
            "titulo": "🎓 Visualização de Dados com Seaborn",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/10Qco9xO0OcyPDL7JJABXC3k5rvAOXb8h/view?usp=sharing"
        },
        {
            "titulo": "🎓 Visua. de Dados com Matplotlib",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1qh99P7Xr17ioq2y3d0YJzVkJiHaF966z/view?usp=sharing"
        },
        {
            "titulo": "🎓 Aplicativos Web com Streamlit",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Dashboards Interativos com Python",
            "link": "https://github.com/JONATHAN-ALMEIDA-MESQUITA/TravelTrendAnalysis"
        },
        {
            "titulo": "🎓 Data Science e machine learning",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Data Science e machine learning",
            "link": "https://drive.google.com/file/d/1HFh0jsm8sXcXjRCxMtlVrHeaZXhaaVad/view?usp=sharing"
        },
        {
            "titulo": "🎓 Gráficos Interativos com Plotly",
            "data": "Dez/24",
            "descricao": "ASIMOV - Trilha: Dashboards Interativos com Python",
            "link": "https://drive.google.com/file/d/1nbVnZ8JASi4HGPfIicCNLpazBMQH6unt/view?usp=sharing"
        }
]
    #Titulo para seleção dos certificados 
    st.markdown("**Selecione a instituição de ensino:**")
    
    col_cb1, col_cb2 = st.columns([1, 1])
    with col_cb1:
        fiap = st.checkbox("FIAP")
    with col_cb2:
        asimov = st.checkbox("ASIMOV Academy")

    # Layout das colunas para os cards
    col1, col2, col3 = st.columns([1, 1, 1])

    # Função para renderizar os cards
    def render_cards(certificados, prefix):
        column_count = 0
        for i, cert in enumerate(certificados):
            current_col = [col1, col2, col3][column_count]
            with current_col:
                with elements(f"{prefix}_card_{i}"):
                    with mui.Card(sx={"maxWidth": 400, "margin": "16px auto", "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)"}):
                        with mui.CardContent(sx={"backgroundColor": "#FFFF00", "color": "#000000", "padding": "12px"}):
                            mui.Typography(cert["titulo"], variant="h6", component="div", sx={"textAlign": "center"})

                        with mui.CardContent():
                            mui.Typography(cert["data"], color="text.secondary", variant="body2")
                            mui.Typography(cert["descricao"], variant="body2", sx={"marginTop": "8px"})

                        with mui.CardActions():
                            mui.Button("Visualizar Certificado 🔍", href=cert["link"], size="small", target="_blank", sx={"color": "#007bff"})
            column_count = (column_count + 1) % 3

    # Renderizar os certificados com base nos checkboxes
    if not fiap and not asimov:
        st.warning("Selecione pelo menos uma origem de certificados.")
    else:
        if fiap and certificados_fiap:
            render_cards(certificados_fiap, "fiap")
        if asimov and certificados_asimov:
            render_cards(certificados_asimov, "asimov")




