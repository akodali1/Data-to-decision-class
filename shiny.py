#Installing the required packages
! pip install -q dash jupyter_dash

#Importing the required 
import dash
from jupyter_dash import JupyterDash  # pip install dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

#Reading the csv file from the github
df = pd.read_csv(
    'https://raw.githubusercontent.com/akodali1/Data-to-decision-class/main/shiny_data.csv')

#Assining the Jupyterdash as app
app = JupyterDash()

#Designing the app layout
app.layout = html.Div([
            html.H1("Population by year for Different Nationalities"), #Heading
            dcc.Graph(id='my-graph'),#ID for output/graph
            dcc.Dropdown(
                id='fm_nationality',#ID for dropdown
                options=[{'label': x, 'value': x} for x in df.sort_values('fm_nationality')['fm_nationality'].unique() ],#Selecting the options
                value=df.sort_values('fm_nationality')['fm_nationality'].unique(),#Assigning the values to dropdown
                multi=True#Selecting multi nationalities at a single time
                
            )
        ],
        style={'width': '100%', 'display': 'inline-block'})#Different styles of the layout

#Calling the app which has one input and output
@app.callback(
    Output('my-graph', 'figure'),
    Input('fm_nationality', 'value'))

#Defining a fuction for getting the lineplot for population of different nationalities over the years
def update_figure(fm_nationality):
    dff=df[df['fm_nationality'].isin(fm_nationality)]
    fig = px.line(dff, x='year', y='population_by_year', color='fm_nationality', height=600,markers=True)
    fig.update_layout(yaxis={'title':'Total Population'})
    #fig.update_layout(showlegend=False)
    return fig
    

#Running the app in external mode 
if __name__ =='__main__':
    app.run_server(mode='external')
