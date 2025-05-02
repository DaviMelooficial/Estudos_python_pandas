import pandas as pd
import plotly.express as px

def gasolina_no_tempo(df):
    fig = px.line(df, x='DATA FINAL', y='PREÇO MÉDIO REVENDA', color='ESTADO',
                  title='Preço Médio da Gasolina ao Longo do Tempo',
                  labels={'DATA FINAL': 'Data', 'PREÇO MÉDIO REVENDA': 'Preço Médio (R$)', 'ESTADO': 'Estado'})
    return fig

def preco_medio_estado(df):
    avg_price = df.groupby('ESTADO')['PREÇO MÉDIO REVENDA'].mean().reset_index()
    fig = px.bar(avg_price, x='ESTADO', y='PREÇO MÉDIO REVENDA',
                  title='Preço Médio da Gasolina por Estado',
                  labels={'ESTADO': 'Estado', 'PREÇO MÉDIO REVENDA': 'Preço Médio (R$)'})
    return fig

def preco_distribuido(df):
    fig = px.box(df, x='PREÇO MÉDIO REVENDA', color='ESTADO',
                 title='Distribuição do Preço da Gasolina por Estado',
                 labels={'PREÇO MÉDIO REVENDA': 'Preço Médio (R$)', 'ESTADO': 'Estado'})
    return fig

def tendencia_preco(df, state):
    df_state = df[df['ESTADO'] == state]
    fig = px.line(df_state, x='DATA FINAL', y='PREÇO MÉDIO REVENDA',
                  title=f'Tendência de Preço da Gasolina em {state}',
                  labels={'DATA FINAL': 'Data', 'PREÇO MÉDIO REVENDA': 'Preço Médio (R$)'})
    return fig