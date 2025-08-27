import streamlit as st
from pathlib import Path
from utilidades import *
from pagina_configuracoes import *
from pagina_lista_email import *
from pagina_templates import *


# ========== Home ==========

def home():
    destinatario_atual = st.session_state.destinatario_atual
    titulo_atual = st.session_state.titulo_atual
    corpo_atual = st.session_state.corpo_atual

    st.markdown("# Central de Emails")

    destinatario = st.text_input("Destinatários do Email:", value=destinatario_atual)
    titulo = st.text_input("Título do Email:", value=titulo_atual)
    corpo = st.text_area("Digite o Email:", height=400, value=corpo_atual)

    col1, col2, col3 = st.columns(3)
    col1.button('Enviar Email',use_container_width=True,
                                on_click=_enviar_email,
                                args=(destinatario, titulo, corpo))
    col3.button('Limpar', use_container_width=True, on_click=_limpar)

    st.session_state.destinatario_atual = destinatario
    st.session_state.titulo_atual = titulo
    st.session_state.corpo_atual = corpo

def _limpar():
    st.session_state.destinatario_atual = ''
    st.session_state.titulo_atual = ''
    st.session_state.corpo_atual = ''

def _enviar_email(destinatarios, titulo, corpo):
    email_usuario = ler_email_usuario()
    chave_usuario = ler_chave_usuario()
    if email_usuario == '':
        st.error('Adicione e-mail na página de configurações')
    elif chave_usuario == '':
        st.error('Adicione chave de e-mail na página de configurações')
    else:
        envia_email(email_usuario=email_usuario, 
                        destinatarios=destinatarios, 
                        titulo=titulo,
                        corpo=corpo,
                        senha_app=chave_usuario)

    
# ========== Main ==========

def main():

    inicializacao()

    st.sidebar.button("Central de Email", key='central_emails', use_container_width= True, on_click= mudar_pagina, args = ("home",))
    st.sidebar.button("Templates", key='templates', use_container_width= True, on_click=mudar_pagina, args = ("templates",))
    st.sidebar.button("Lista de Emails", key='lista_emails', use_container_width= True, on_click=mudar_pagina, args = ("lista_email",))
    st.sidebar.button("Configurações", key='configuracoes', use_container_width= True, on_click=mudar_pagina, args = ("configuracao",))
    
    if st.session_state.pagina_central_email == "home":
        home()
    elif st.session_state.pagina_central_email == "templates":
        pag_templates()
    elif st.session_state.pagina_central_email == "adicionar_novo_template":
        pag_adicionar_novo_template()
    elif st.session_state.pagina_central_email == "editar_template":
        nome_template_editar = st.session_state.nome_template_editar
        texto_template_editar = st.session_state.texto_template_editar
        pag_adicionar_novo_template(nome_template_editar, texto_template_editar)
    elif st.session_state.pagina_central_email == "lista_email":
        pag_lista_email()
    elif st.session_state.pagina_central_email == "adicionar_nova_lista":
        pag_adicionar_nova_lista()
    elif st.session_state.pagina_central_email == "editar_lista":
        nome_lista_editar = st.session_state.nome_lista_editar
        texto_lista_editar = st.session_state.texto_lista_editar
        pag_adicionar_nova_lista(nome_lista_editar, texto_lista_editar)
    elif st.session_state.pagina_central_email == "configuracao":
        pag_config()

main()