import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from datetime import date

app = dash.Dash(__name__)
colours = {'text': '#0000FF', 'background':'#FFFFFF'}
text_size = {'H1':48,'H2':40,'text':36}

app.layout = html.Div(style={'backgroundColor':colours['background'],'fontFamily':'calibri'}, children=[

    html.H1(children='Room Temperature',
        style = {'textAlign': 'center',
                 'color':colours['text'],
                 'fontSize':text_size['H1']}),

    html.H2(children='A simple dashboard exercise',
            style = {'textAlign': 'center','color':colours['text'],'fontSize':text_size['H2']}),

    html.Div(children=[
            html.Div(children = [
                    dcc.DatePickerRange(
                        id='date_picker',
                        min_date_allowed = date(2021,9,1),
                        max_date_allowed = date.today(),
                        initial_visible_month = date.today(),
                        end_date = date.today()
                    ),
                    html.Div(id = 'date_picker_html')
                ],
                style = {'textAlign': 'left','color':colours['text'],'fontSize':text_size['text']}
            ),
            
            html.Div(children = [
                        html.Label("Stats",style = {'textAlign': 'right','color':colours['text'],'fontSize':text_size['text']}),

                        dcc.RadioItems(
                            options=[
                                {'label': 'max','value':'max'},
                                {'label': 'min','value':'min'},
                                {'label': 'mean','value':'mean'},
                                {'label': 'describe','value':'describe'}
                            ]
                        )
                    ], style = {'textAlign': 'right','color':colours['text'],'fontSize':text_size['text']}
            )
        ],style = {'width':'100%','display':'inline-block'}
    ),


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