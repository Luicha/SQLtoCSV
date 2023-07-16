import pandas as pd
import sqlite3
import csv

conn = sqlite3.connect('fafa.db')
query = "SELECT id, palabra, tipoPalabra FROM palabras"

df = pd.read_sql_query(query, conn)

df['palabra'] = df['palabra'].apply(lambda x: f'{x}')
df['tipoPalabra'] = df['tipoPalabra'].apply(lambda x: f'{x}')


df.to_csv('resultado.csv', index=False, quotechar='"', encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)
