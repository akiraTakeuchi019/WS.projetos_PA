# WS.projetos_PA
Projetos de PA de 1-DS-A

import streamlit as st
import pandas as pd
import os
import datetime as date

# ==============================
# definir função novo cliente
# ==============================

def novo_cliente():
   st.session_state["nome"]= "" 
   st.session_state["endereco"]= "" 
   st.session_state["dt_nasc"]= date.today
   ()
   st.session_state["tipo_pessoa"]= 'pessoa fisica'

# ==============================
# titulo
# ==============================

st.title("cadastro de clientes")

# ==============================
# campo do cadastro
# ==============================

nome = st.text_input(
    "Digite o nome do Cliente",
    key="nome"
)

endereco = st.text_input(
    "Digite o endereco",
    key="endereco"
)

dt_nasc = st.date_input(
    "Digite o nome do Cliente",
    value= None,
    key="dt_nasc",
    format="DD/MM/YYYY",
    min_value = date.date(1900,1,1),
    max_value = date.date.today()
)

tipo_pessoa = st.selectbox(
    "selecione o tipo do cliente",
    ["pessoa fisica", "pessoa juridica"],
    key="tipo_pessoa"
)

# ==============================
# Botões
# ==============================

col1, col2 = st.columns(2)

with col1:
   cadastrar= st.button(
      "Cadastrar Cliente",
      use_container_width="True"
   )

with col2:
    novo = st.button(
      "novo cliente",
      on_click= novo_cliente
    )

# ==============================
# Cadastrar Cliente
# ==============================
if cadastrar:
    if nome.strip()=="":
        st.warning("O campor nome é obrigatorio")
    elif endereco.strip()=="":
        st.warning("O campor endereco é obrigatorio")
    elif tipo_pessoa.strip()=="":
        st.warning("O campor tipo de pessoas é obrigatorio")
    else:
        dt_nasc_formatada = dt_nasc.strftime
        ("%d/%m/%Y")

        with open(
            "cadCli.csv",
            "a",
            encoding="utf8",
        ) as cliente:
            cliente.write(
                f"{nome},{endereco,},{dt_nasc_formatada},{tipo_pessoa}\n"
            )
        st.success("registro salvo")
