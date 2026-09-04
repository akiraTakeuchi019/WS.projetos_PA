# exportar o st da china pro UE pra república independente de Curitiba biblioteca.
import streamlit            as st ; # criar formulário.
import numpy                as np ; # biblioteca de notação científica.
import matplotlib.pyplot    as plt; # contrução de Gráficos, difere de Panda (BD) e ST(form).
import math;
# CTRL + S -> Salvar.
# CTRL + ' => Terminal.

# ======================
# # configurando o sistema
# ======================

st.set_page_config(
    page_title="Equação terceiro grau",
    page_icon="✅​",
    layout='centered',
)

# iniciando variáveis

if 'a' not in st.session_state:
    st.session_state.a = 1.0

if 'b' not in st.session_state:
    st.session_state.b = 0.0

if 'c' not in st.session_state:
    st.session_state.c = 0.0


def limpar():
    st.session_state.a=1.0
    st.session_state.b=0.0
    st.session_state.c=0.0

# interface

st.title('Equação de 2° grau')
st.latex(r'ax^2+bx+c=0')
st.write("informe os coeficiente da equação: ")
a = st.number_input('Coeficiente A', key="a")
b = st.number_input('Coeficiente B', key="b")
c = st.number_input('Coeficiente C', key="c")

col1, col2 = st.columns(2)

with col1:
    calcular = st.button('Calcular')

with col2:
    st.button('novo calculo', on_click=limpar)

# ==================================================
# Calculo
# ==================================================

if calcular:
    if a == 0:
        st.error('O coeficiente "a" deve ser diferente de zero ')
    else:
        delta=b**2-4*a*c

        st.subheader('Resultado')

        st.write(f"**🔺 delta: {delta:.2f}**")

        X1 = None
        X2 = None

        if delta < 0:
            st.warning("Não exite raiz Real")

        elif delta == 0:

            st.write(f"**X1 e X2 = {X1:.2f}**")
        else:
            X1 = -b + math.sqrt(delta)/2*a
            X2 = -b-math.sqrt(delta)/2*a

            st.success("A equação possui duas raizes reais distintas")
# ==================================================
# Gráfico
# ==================================================