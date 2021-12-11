import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from datetime import date

app = dash.Dash(__name__)
colours = {'text': '#0000FF', 'background':'#FFFFFF'}
# font = {'font'}

app.layout = html.Div(style={'backgroundColor':colours['background'],'fontFamily':'calibri'}, children=[

    html.H1(children='Room Temperature',
        style = {'textAlign': 'center',
                 'color':colours['text']}),

    html.H2(children='A simple dashboard exercise',
            style = {'textAlign': 'center','color':colours['text']}),

    html.Div(children=[
        html.Label("Stats"),
        dcc.RadioItems(
            options=[
                {'label': 'max','value':'max'},
                {'label': 'min','value':'min'},
                {'label': 'mean','value':'mean'},
                {'label': 'describe','value':'describe'}
            ]
        )
    ],style = {'color':colours['text']}),

    html.Br(),

    html.Div([
        dcc.DatePickerRange(
            id='date_picker',
            min_date_allowed = date(2021,9,1),
            max_date_allowed = date.today(),
            initial_visible_month = date.today(),
            end_date = date.today()
        ),
        html.Div(id = 'date_picker_html')
    ]),

    html.Br(),
    html.Br(),

    html.Div([
        dcc.RangeSlider(
            id = 'range_slider',
            min = 0,
            max = 23,
            step = 1,
            value = [0,23],
            allowCross = False,
            tooltip = {'placement':'bottom','always_visible':True}
        ),
        html.Div(id='out_range_slider')
    ])


    # dcc.Graph(
    #     id='example-graph',
    #     figure=None
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)