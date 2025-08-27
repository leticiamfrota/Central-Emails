import streamlit as st
from pathlib import Path
from utilidades import *
from pagina_lista_email import *
from pagina_templates import *

def pag_config():
    st.markdown("# Configurações")
    email = st.text_input('Digite seu email: ')
    st.button('Salvar', key='salvar_email', 
                        on_click=_salvar_email, 
                        args=(email,))
    chave = st.text_input('Digite sua chave de e-mail: ')
    st.button('Salvar', key='salvar_chave', 
                        on_click=_salvar_chave, 
                        args=(chave,))

def _salvar_email(email):
    PASTA_CONFIGURACOES.mkdir(exist_ok=True)
    with open(PASTA_CONFIGURACOES / 'email_usuario.txt', 'w') as f:
        f.write(email)

def _salvar_chave(chave):
    PASTA_CONFIGURACOES.mkdir(exist_ok=True)
    with open(PASTA_CONFIGURACOES / 'chave.txt', 'w') as f:
        f.write(chave)

def ler_email_usuario():
    PASTA_CONFIGURACOES.mkdir(exist_ok=True)
    if (PASTA_CONFIGURACOES / 'email_usuario.txt').exists():
        with open(PASTA_CONFIGURACOES / 'email_usuario.txt', 'r') as f:
            return f.read()
    return ''

def ler_chave_usuario():
    PASTA_CONFIGURACOES.mkdir(exist_ok=True)
    if (PASTA_CONFIGURACOES / 'chave.txt').exists():
        with open(PASTA_CONFIGURACOES / 'chave.txt', 'r') as f:
            return f.read()
    return ''
