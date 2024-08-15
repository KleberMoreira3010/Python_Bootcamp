import pandas as pd
import glob
import os


# Leitura dos arquivos Json
pasta = 'aula3\dados'
def extrair_dados (pasta: str) ->pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

    df_total = pd.concat(df_list, ignore_index=True)

    return df_total


# Transformacao
def transformar_dados ( df:pd.DataFrame) ->pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df



# Leitura em Json ou Parquet

if __name__ == "__main__":
    pasta_argumento = 'aula3\dados'
    dataframe=extrair_dados(pasta=pasta_argumento)
    print(transformar_dados(dataframe))
