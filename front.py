import streamlit as st
from back import fazer_consulta

st.set_page_config(page_title="Consulta CNPJ", layout='wide', page_icon='big-search-len.png')
st.title("Consultar informações de CNPJ's 🏢", anchor=False)

if "resultado" not in st.session_state:
    st.session_state.resultado = {
        "cnpj", "" ,
        "uf", "" ,
        "razao_social", "" ,
        "nome_fatatasia", "" ,
        "municipio", "" ,
        "logradouro", "" ,
        "natureza_juridica", "" ,
        "situacao_especial", "" ,
        "atividade_fiscal", "" ,
        "situacao_cadastral", "" ,
        "identificador_filial_matriz", "" 
    }

col1, col2, col3 = st.columns(3)
input = col1.text_input(label="", placeholder="Informe o CNPJ", autocomplete="0001", max_chars=14)

if input == "":
    col1.button(label="Pesquisar", icon="🔍", disabled=True)
elif len(input) < 14:
    col1.button(label="CNPJ incompleto", icon="⚠️", disabled=True)
elif not input.isdigit():
    col1.button(label="CNPJ não pode conter letras", icon="❌", disabled=True)
else:
    if col1.button(label="Pesquisar", icon="🔍"):
        resultado_consulta = fazer_consulta(input)
        if resultado_consulta:
            st.session_state.resultado.update(resultado_consulta)


with st.container():
    col1, col2, col3 = st.columns(3)

    col1.text_input(label="CNPJ:", disabled=True, value=st.session_state.resultado.get("cnpj", ""))
    col2.text_input(label="Razão Social:", disabled=True, value=st.session_state.resultado.get("razao_social", ""))
    col3.text_input(label="Nome Fantasia:", disabled=True, value=st.session_state.resultado.get("nome_fatatasia", ""))

    col1.text_input(label="Municipio:", disabled=True, value=st.session_state.resultado.get("municipio", ""))
    col2.text_input(label="Logradouro:", disabled=True, value=st.session_state.resultado.get("logradouro", ""))
    col3.text_input(label="Filial ou Matriz:", disabled=True, value=st.session_state.resultado.get("identificador_filial_matriz", ""))

    col1.divider()
    col2.divider()
    col3.divider()

    col1.text_input(label="Situação Especial:", disabled=True, value=st.session_state.resultado.get("situacao_especial", ""))
    col2.text_input(label="Situação Cadastral:", disabled=True, value=st.session_state.resultado.get("situacao_cadastral", ""))
    col3.text_input(label="Natureza Juridica:", disabled=True, value=st.session_state.resultado.get("natureza_juridica", ""))

col1, col2, col3 = st.columns(3)
col1.feedback(options='faces')