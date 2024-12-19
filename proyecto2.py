import pandas as pd
import plotly.express as px
import dash
from dash import dcc,html
#creamos el dataframe y lo decodificamos con latin1 ya que no es un archivo que lee utf-8
df=pd.read_csv("C:\\Users\\felip\\OneDrive\\Escritorio\\valenciahoteles.csv",encoding="latin1")
estadistica=df.describe()
#print(estadistica)
#comprobar si hay columnas vacias

"""vacias_columnas=df.isnull().sum()
print(vacias_columnas)"""
#ya no existe columnas vacias

#comprobamos si existe duplicados
duplicados=df[df.duplicated()]
#print(duplicados)
#ahora que si existe duplicados
#elmininamos los duplicados
df_limpio=df.drop_duplicates()
#creamos las diferentens figuras que existen en el libreria de plotly

#grafica de linea
fig_line=px.line(df_limpio,x="Número de comentarios",y="Valoración",title="numero de comentarios vs valoracion")
#fig.show()

#grafica de dispercion
fig_dis=px.scatter(df_limpio,x="Fecha",y="Número de comentarios",title="fecha vs numero de comentarios")
#fig.show()

#grafico de barras
fig_bar=px.bar(df_limpio,x="Valoración",y="Precio",title="precio vs valoracion")
#fig.show()

#graficas de barras apiladas
fig_api=px.bar(df_limpio,x="Valoración",y="Precio",title="VALORACION VS PRECIO",barmode="stack")
#fig.show()

#grafico de cajas
fig_caj=px.box(df_limpio,x="Número de comentarios",y="CP",title="numero de comentarios vs cp")
#fig.show()

#grafica de violin
fig_vi=px.violin(df_limpio,x="Valoración",y="CP",box=True,title="valoracion vs cp")
#fig.show()

#grafico de area
fig_are=px.area(df_limpio,x="Fecha",y="Valoración",title="valacion en funcion del tiempo")
#fig.show()

#grafico circular
fig_cir=px.pie(df_limpio,names="Valoración",values="Precio",title="valoracion precio")
#fig.show()

#grafica de mapas
fig_map=px.scatter_mapbox(df_limpio,lat="lat",
                      lon="long",
                      hover_name="Nombre",
                      title="lat vs long",
                      color="Nombre")
fig_map.update_layout(mapbox_style="carto-positron", mapbox_accesstoken="open-street-map")
#fig.show()

#inicializar la  app dash
app=dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div([
    # Título del dashboard
    html.H1("Dashboard de Hoteles en Valencia", style={"text-align": "center"}),

    # Contenedor de gráficos
    html.Div(   [
        # Fila de gráficos de líneas y dispersión
        html.Div([
            dcc.Graph(figure=fig_line, style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(figure=fig_dis, style={'display': 'inline-block', 'width': '48%'})
        ], style={'display': 'flex', 'justify-content': 'space-between'}),

        # Fila de gráficos de barras y apiladas
        html.Div([
            dcc.Graph(figure=fig_bar, style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(figure=fig_api, style={'display': 'inline-block', 'width': '48%'})
        ], style={'display': 'flex', 'justify-content': 'space-between'}),

        # Fila de gráficos de caja y violín
        html.Div([
            dcc.Graph(figure=fig_caj, style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(figure=fig_vi, style={'display': 'inline-block', 'width': '48%'})
        ], style={'display': 'flex', 'justify-content': 'space-between'}),

        # Fila de gráficos de área y circularpqwerty
        html.Div([
            dcc.Graph(figure=fig_are, style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(figure=fig_cir, style={'display': 'inline-block', 'width': '48%'})
        ], style={'display': 'flex', 'justify-content': 'space-between'}),

        # Mapa de dispersión
        html.Div([
            dcc.Graph(figure=fig_map)
        ], style={'padding-top': '20px'})
    ], style={'padding': '20px'})
])

# Ejecutar la aplicación Dash
if __name__ == '__main__':
    app.run_server(debug=True)