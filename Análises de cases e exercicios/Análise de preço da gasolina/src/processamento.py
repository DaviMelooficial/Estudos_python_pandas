import pandas as pd

def carregar_data(file_2000, file_2010):
    df_2000 = pd.read_csv(file_2000, index_col=0)
    df_2010 = pd.read_csv(file_2010, index_col=0, low_memory=False)
    return pd.concat([df_2000, df_2010])

def transformar_data(df):
    df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
    df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])
    df['ANO_MES'] = df['DATA FINAL'].apply(lambda x: '{}-{:02d}'.format(x.year, x.month))
    return df

def filtro_gasolina(df):
    return df[df['PRODUTO'] == 'GASOLINA COMUM']