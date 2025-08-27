## Central de Emails com Streamlit
Este projeto é uma aplicação web simples, desenvolvida com a biblioteca Streamlit, para gerenciar e enviar e-mails de forma eficiente. Ele permite que o usuário crie e use templates de e-mail, gerencie listas de destinatários e envie e-mails diretamente da interface do navegador.

### Como Rodar o Projeto
Siga estes passos para configurar e executar o projeto na sua máquina local:

1. Pré-requisitos \
Certifique-se de que você tem o Python 3.9 ou superior instalado. 

2. Clonar o Repositório \
git clone https://github.com/leticiamfrota/Central-Emails.git \
cd SEU-REPOSITORIO

3. Instalar as Dependências \
O projeto utiliza a biblioteca Streamlit e outras dependências. Instale-as usando o pip: \
pip install -r requirements.txt

4. Executar a Aplicação
Inicie a aplicação com o comando streamlit run: \
streamlit run central_emails.py \
A aplicação será aberta automaticamente no seu navegador padrão.

### Você também pode acessar o aplicativo no navegador, através do link: [Central de Emails](https://centralemails.streamlit.app/)

### Estrutura do Projeto
A estrutura de arquivos do projeto é organizada da seguinte forma:

. \
├── __pycache__/        &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Cache de execução do Python \
├── central_emails.py    &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Arquivo principal da aplicação Streamlit \
├── paginas/ \
│   ├── pagina_configuracoes.py \
│   ├── pagina_lista_email.py \
│   └── pagina_templates.py \
├── requirements.txt   &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Lista de dependências do projeto \
├── templates/         &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Pasta para templates de email em formato .txt \
├── lista_email/       &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Pasta para listas de email em formato .txt \
└── utilidades.py      &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;# Contém a função para enviar e-mails \




### Funcionalidades Principais
**Central de Emails**: Interface principal para escrever e enviar e-mails.

**Templates**: Crie, edite e use modelos de e-mail

**Listas de E-mails**: Salve e reutilize listas de destinatários para enviar e-mails em massa.

**Configurações**: Configure suas credenciais para o envio de e-mails. 
* Na área **Digite seu email** você adicionará o endereço de e-mail que será utilizado para enviar e-mails. 
* Na área **Digite sua chave de e-mail** você adicionará uma senha de aplicativo do Google. 

**Atenção**: Por questões de segurança, você deve utilizar uma senha de aplicativo do Google, e não a sua senha normal. 
* Ative a verificação em duas etapas na sua conta do Google. 
* Acesse Gerenciar senhas de app do Google. 
* Siga as instruções para gerar uma nova senha para o seu aplicativo. 


### Tecnologias Utilizadas
**Python**: Linguagem de programação. 

**Streamlit**: Framework de código aberto para criar aplicações web interativas com Python. 

**smtplib**: Biblioteca padrão do Python para o envio de e-mails usando o protocolo SMTP. 

**ssl**: Biblioteca padrão do Python para criar conexões seguras. 

### Autor
Letícia Frota - [Perfil no GitHub](https://github.com/leticiamfrota)
