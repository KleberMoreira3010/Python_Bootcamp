import pandas as pd
import glob
import os


# Leitura dos arquivos Json
pasta = 'dados'

arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

df_total = pd.concat(df_list, ignore_index=True)

print(df_total)


# Transformacao



# Leitura em Json ou Parquet