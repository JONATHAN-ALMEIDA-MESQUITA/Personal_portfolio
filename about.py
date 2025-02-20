import streamlit as st
from utils import get_image_as_base64


def render_about():
    col1, col2 = st.columns([1, 2])

    #Carregar a foto de perfil
    img_perfil = get_image_as_base64("assets/imagens/foto.png")

    #Renderizar foto de perfil
    
    col1.markdown(f"""
    <div style="display: flex; justify-content: center; margin-top: -20px;">
    <img src="data:image/png;base64,{img_perfil}" style="border-radius: 255px; width: 150px; height: 150px;">
    </div> <h4 style="text-align: center;margin-top: -1px;">Jonathan Mesquita</h4>
    """, unsafe_allow_html=True
    ),

    #Renderizar cargo, funções especificações

    col2.markdown(
    """
    <div style="margin-top: 20px;">
        <p>
            <strong>Profissão:</strong> Supervisor financeiro na BCD TRAVEL
        </p>
        <p>
            <strong>Responsabilidades:</strong> Gestão de pessoas | Gestão de processos | Desenvolvimento de projetos
        </p>
        <p>
            <strong>Habilidades:</strong> Análise de dados | Ciência de dados | Machine Learning | Power Apps | Power Automate
        </p>
    </div>
    """,
    unsafe_allow_html=True,
),
    
    #Renderizar e-mail de contato  link do linkedin
    
    col2.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px;">
                <a href="mailto:jonathan.mesquita@hotmail.com" style="text-decoration: none; font-size: 14px;">
                    📩 <b>jonathan.mesquita@hotmail.com</b>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        ),
    
    col2.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px;">
                <a href="https://www.linkedin.com/in/jonathan-mesquita-3049581b1" target="_blank" style="text-decoration: none; font-size: 14px;">
                    🌐 <b>LinkedIn: Jonathan Mesquita</b>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        ),


    
    #Renderizar texto sobre

    st.markdown("""
    <div style="margin-top: 100px;">
    </div>

    ### Sobre
    Oi, sou Jonathan Mesquita! Tenho uma trajetória consolidada no mercado como Analista e, atualmente, como Supervisor Financeiro. Durante essa jornada, 
    desenvolvi habilidades em gestão de pessoas, análise de dados e machine learning.
    Tenho paixão por transformar números em histórias e problemas complexos em soluções inteligentes. 
    Atualmente, estou me dedicando ao estudo de ciência de dados, onde já desenvolvi projetos que ampliaram meu conhecimento e trouxeram aplicabilidade prática ao meu dia a dia.
    <br>

    Sou entusiasta de tecnologia e acredito no poder da inovação. Meu objetivo não é apenas criar projetos complexos, mas também simplificar processos e otimizar 
    o tempo por meio de automações para tarefas repetitivas. Busco simplificar tarefas e melhorar a eficiência por meio de automações, utilizando Python e suas bibliotecas, além de plataformas low-code como Power Automate e Power Apps para soluções mais ágeis
    <br>
    Pronto para transformar dados em decisões inteligentes? Vamos juntos! 🚀


    """, unsafe_allow_html=True
    ),


    #Renderizar qualificações profissionais


    st.markdown("""
    <div style="margin-top: 100px;">
    </div>

    #### 💼 Qualificações

    <br>
                    
    🌍 **Idiomas:**
    + **Português:** Nativo
    + **Espanhol:** Básico
    + **Inglês:** Básico (em progresso)

    <br>

    🛠️ **Habilidades técnicas**: 
    + **SQL:** DML e DRS 
    + **Python:** Pandas, Numpy, Feature Engineering, Regressão, Modelos de Machine Learning 
    + **Bibliotecas de Visualização:** Matplotlib, Seaborn
    + **Ferramenta de análise de dados:** Excel
    + **Automação:** Power apps, Power Automate 

    <br>


    📋 **Qualificações Profissionais:** 
    + **Análise de dados:** Extração, limpeza, organização e mensuração de resultados;
    + **Dashboard:** Construção de KPIs, apresentação de resultados;
    + **Automação:** Melhoria de processos, desenvolvimento de fluxos e criação de regras de negócios;
    + **Gestão:** Habilidades de Autogerenciamento, controle de atividades e prazos, senso de urgência e priorização de atividades.

                
    <br>

    📜 **Histórico Profissional:** 
    + **BCD Travel turismo Brasil:** Supervisor Financeiro (CLT) (Ago/2015  presente)
        + Liderança de equipes e desenvolvimento de dashboards financeiros para análise e automação de processos.

    <br>
                
    + **Carlson Wagonlit Travel Brasil:** Assistente financeiro (CLT) - (Out/2011 a Ago/2015)
        + Responsável por relatórios financeiros e conciliações, buscando insights através da análise de dados.


                    
    """, unsafe_allow_html=True
    )
