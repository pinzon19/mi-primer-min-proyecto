#creacion del proyecto 1
import pandas as pd
import plotly.express as px
import dash
from dash import dcc,html
#creamos el data frame
df=pd.read_csv("C:\\Users\\felip\\OneDrive\\Escritorio\\Automobile_data.csv")
#resumen estadistico del dataframe
resumen_estadistico=df.describe()
print(resumen_estadistico)
#creamoa la figura grafica(grafica de dispersion)
fig=px.scatter(df,x="wheel-base",y="length",title="analisis")
#inicializar la app dash
app=dash.Dash(__name__)
#layout del dashboard
app.layout=html.Div([
    html.H1("dashboard interactivo"),
    dcc.Graph(figure=fig),
    dcc.Dropdown(
        id="carros",
        options=[
            {"label":"norte","value":"norte"},
            {"label":"sur","value":"sur"},
            {"label":"este","value":"este"}
        ],
        value="Norte", #valro preterminado
    ),
])
#ejecutamos el servidor
if __name__ =="__main__":
    app.run_server(debug=True)