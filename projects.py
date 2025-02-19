import streamlit as st
from streamlit_elements import elements, mui 
from utils import get_image_as_base64


# Função para renderizar os cards dos projetos
def render_projects():
    st.title("Seja bem vindo seção projetos! 🚀")
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)

    #Carregar projetos
    projects = [
        {
            "imagem": get_image_as_base64("assets/imagens/estimativa_de_precos_de_Imoveis.png"),
            "titulo": "🏠 Estimativa de preços de imóveis",
            "data": "Nov/2024",
            "descricao": "Previsão de preços baseada em dados públicos de locação de imóveis para viagens.",
            "link": "https://aplicativo-web-predictive-analysis.amslmd.easypanel.host/"
        },
        {
            "imagem": get_image_as_base64("assets/imagens/analise_de_tendencias_de_viagem.png"),
            "titulo": "🛒 Analise de vendas E-commerce",
            "data": "Set/24",
            "descricao": "Previsão de vendas baseada em dados de e-commerce para análise de desempenho futuro.",
            "link": "https://github.com/JONATHAN-ALMEIDA-MESQUITA/E-commerce_sales_analysis"
        },
        {
            "imagem": get_image_as_base64("assets/imagens/analise_de_vendas_ecommerce.png"),
            "titulo": "✈️ Análise de tendências de viagem",
            "data": "Jun/24",
            "descricao": "Modelo de análise de dados para previsão e insights sobre tendências de viagens e viajantes.",
            "link": "https://github.com/JONATHAN-ALMEIDA-MESQUITA/TravelTrendAnalysis"
        },
        {
            "imagem": get_image_as_base64("assets/imagens/open_health-ai.png"),
            "titulo": "🏥 Prevenção de problemas de saúde",
            "data": "Nov/23",
            "descricao": "Challenge-FIAP---Global_Solutions, modelo de análise de dados para previsão de problemas de saude..",
            "link": "https://github.com/JONATHAN-ALMEIDA-MESQUITA/Challenge-FIAP---Global_Solutions_Open_Health-AI"
        },
        {
            "imagem": get_image_as_base64("assets/imagens/potifolio.png"),
            "titulo": "💼 Portilio de projetos",
            "data": "Dez/24" ,
            "descricao":"Este projeto reflete minha evolução em estudos e projetos, além de inspirar outros colegas a criarem seus proprios portifólios. ",
            "link": ""
        },
        {
            "imagem": get_image_as_base64("assets/imagens/rpa_email.png"),
            "titulo": "📩 RPA envio de e-mails em massa",
            "data": "Julo/23" ,
            "descricao":"Projeto desenvolvido em Power automate para aumentar a produtividade de envio de e-mails para diversos remetentes. ",
            "link": ""
        },
        {
            "imagem": get_image_as_base64("assets/imagens/controle_de_despesa.png"),
            "titulo": "🖥️ Aplicativo controle de pagamentos",
            "data": "Jun/24" ,
            "descricao":"Projeto desenvolvido para em Power apps para melhorar o fluxo de envio de pagamentos e aprovações. ",
            "link": ""
        }
]

    #Renderizar os projetos (cards) em colunas
    col1, col2, col3 = st.columns([1, 1, 1])
    for i, project in enumerate(projects):
        current_col = [col1, col2, col3][i % 3]
        with current_col:
            with elements(f"projeto_card_{i}"):
                 #Construção do card, configuração de tamanho e cor
                with mui.Card(sx={"maxWidth": 700, "margin": "16px auto", "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)"}):

                    #Titulo card
                    with mui.CardContent():
                         mui.Typography(project['titulo'], variant='h6', component='div')

                        #Imagem do card
                    mui.CardMedia(
                        component="img",
                        height="300",
                        image=f"data:image/png;base64,{project['imagem']}",
                        alt=project['titulo']
                        )
                        
                    with mui.CardContent():
                        mui.Typography(project["data"], color="text.secondary", variant="body2")
                        mui.Typography(project["descricao"], variant="body2", sx={"marginTop": "8px"})

                        # Ações do Card
                        with mui.CardActions():
                            mui.Button("Learn More", href=project["link"], size="small", target="_blank")
                            mui.IconButton(mui.icon.Favorite())



