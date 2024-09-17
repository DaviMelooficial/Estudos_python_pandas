import sqlite3 
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = "index_name"
df_data.to_sql("Data", conn, index_label="index_name")

# Criando uma tabela
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Produtos
          ([product_id] INTEGER PRIMARY KEY, 
          [product_name] TEXT, 
          [price] INTEGER)""")

# Apagando uma tabela
c.execute('''DROP TABLE Produtos''')