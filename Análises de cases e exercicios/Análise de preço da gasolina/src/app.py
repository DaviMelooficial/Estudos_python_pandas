import streamlit as st
from processamento import carregar_data, transformar_data, filtro_gasolina
from visualizacao import gasolina_no_tempo, preco_medio_estado, tendencia_preco
import streamlit.components.v1 as components

# Ajustar o layout para ocupar toda a largura da tela
st.set_page_config(layout="wide")

def main():
    st.title("Análise de Preços da Gasolina no Brasil")
    
    # Carregar e processar os dados
    df = carregar_data('gasolina_2000+.csv', 'gasolina_2010+.csv')
    df = transformar_data(df)
    df = filtro_gasolina(df)
    
    # Filtro por estados
    estados = df['ESTADO'].unique()
    estados_selecionados = st.multiselect("Selecione os estados:", estados, default=estados[:3])
    
    # Filtrar o DataFrame pelos estados selecionados
    df_filtrado = df[df['ESTADO'].isin(estados_selecionados)]
    
    # Gráfico de tendências de preços
    st.subheader(f"Tendências de Preços da Gasolina")
    st.plotly_chart(gasolina_no_tempo(df_filtrado), use_container_width=True)
    
    # Gráfico de preço médio por estado
    st.subheader("Preço Médio da Gasolina por Estado")
    st.plotly_chart(preco_medio_estado(df_filtrado), use_container_width=True)

    # Exibir dados filtrados
    st.subheader("Dados da Gasolina")
    st.write(df_filtrado.head())  # Exibe apenas os dados filtrados
    
if __name__ == "__main__":
    main()