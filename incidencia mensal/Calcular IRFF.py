import streamlit as st

st.set_page_config(
    page_title = "Calculador de incidencia mensal",
    layout = 'centered',
)

st.title ("Calcular imposto de renda")
st.subheader ("Coloque seu salário e calcularemos seu IRFF")

salario = st.number_input('Seu Salario', key="a")
if 'a' not in st.session_state:
    st.session_state.a = 0.0


desconto = None
if   2428.80 >= salario :
    desconto = None
elif 2826.65 >= salario > 2428.80:
    desconto = 0.075
elif 3751.05 >= salario > 2826.65:
    desconto= 0.15
elif 4664.68 >= salario > 3751.05:
    desconto = 0.225
else:
    desconto = 0.275


col1 , col2 = st.columns(2)

with col1:
    calcular = st.button('Calcular')


def limpar():
    st.session_state.a=0.0

with col2:
    limpar = st.button('apagar', on_click=limpar)


if calcular:

    if salario == 0:
        st.error("coloque um valor")
    elif desconto == None:
        st.success('Você está isento (pobre)')
    else:
        st.write(f'você recebera uma alíquota de: {desconto}')
        st.success(f'será descontado: {salario*desconto:.2f}R$ do seu salário')

