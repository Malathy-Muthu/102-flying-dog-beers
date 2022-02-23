import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
shopping=['Woodlands Mall', 'College Park Mall', 'Yogaworks Mall', 'Outlet Factory']
female_values=[30, 40, 25, 75]
male_values=[20,25, 4, 40]
color1='darkgreen'
color2='darkred'
mytitle='Visitor Counts'
tabtitle='Shopping'
myheading='Shopping Mall - Analytics'
label1='Female'
label2='Male'
githublink='https://github.com/Malathy-Muthu/102-flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
female_count = go.Bar(
    x=shopping,
    y=female_values,
    name=label1,
    marker={'color':color1}
)
male_count = go.Bar(
    x=shopping,
    y=male_values,
    name=label2,
    marker={'color':color2}
)

mall_data = [female_count, male_count]
mall_layout = go.Layout(
    barmode='group',
    title = mytitle
)

mall_fig = go.Figure(data=mall_data, layout=mall_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='Shopping',
        figure=mall_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
