import pandas as pd
#creamos el dataframe
df=pd.read_excel("C:\\Users\\felip\\OneDrive\\Escritorio\\BD Turismo Post Pandemia.xlsx")
#comprobamos si tiene selvas vacias
vacios_columna=df.isnull().sum()
print(vacios_columna)
#al comprobar que existen celdas vacias entonces eliminamos las celdas vacias
df=df.dropna(how="all")
#vamos a comprobar si existen duplicados
duplicados=df[df.duplicated()]
print(duplicados)
#contamos la cantida de filas duplicadas
duplicados=df.duplicated().sum()
print(f"las celdas duplicadas son: {duplicados}")
#ya que existen filas duplicadas las eliminamos
df=df.drop_duplicates()