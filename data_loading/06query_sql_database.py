import pandas as pd
import pymysql

conn = pymysql.connect(
    host='localhost',   # ✅ sem a porta
    port=3306,          # ✅ porta separada
    user='root',
    password='root',
    database='sample'
)

# Ler dados da tabela
dataframe = pd.read_sql("SELECT * FROM data", conn)

print(dataframe.head(2))
