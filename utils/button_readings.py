# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
import pandas as pd
import plotly
import plotly.graph_objects as go

import utils.display as display

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


def build_layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id='cbpm_xpos')
                        ),
                        width=6
                    ),
                    dbc.Col(
                        html.Div(
                            children=[
                                dcc.Graph(id='cbpm_ypos'),

                            ]
                        ),
                        width=6
                    ),
                ], style={'margin-top': '-25px'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id='cbpm_xres')
                        ),
                        width=6
                    ),
                    dbc.Col(
                        html.Div(
                            children=[
                                dcc.Graph(id='cbpm_yres'),

                            ]
                        ),
                        width=6
                    ),
                ], style={'margin-top': '-5px'}
            ),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            table.DataTable(
                                id='table',
                                columns=[{"name": "<x>", "id": "x_avg"},
                                         {"name": "<y>", "id": "y_avg"},
                                         {"name": u"\u03c3(x)", "id": "sigmax_avg"},
                                         {"name": u"\u03c3(y)", "id": "sigmay_avg"},
                                         {"name": u"\u03c1(xy)", "id": "rho_xy"}],
                                # data=df.to_dict('records'),
                                style_cell={
                                    'text-align': 'center'
                                }
                            ), style={'margin-top': '100px'}
                        ),
                    )
                ]
            ),
        ]
    )