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


def update(n, time, switch, cbpm_xpos, cbpm_ypos, cbpm_xres, cbpm_yres):
    if switch:
        df = display.analyze(float(time))

        fig = []
        fig.append(plotly.subplots.make_subplots())
        fig.append(plotly.subplots.make_subplots())
        fig.append(plotly.subplots.make_subplots())
        fig.append(plotly.subplots.make_subplots())

        yaxis_label = ['Horizontal position [micron]',
                       'Vertical position [micron]',
                       'Horizontal "resolution" [micron]',
                       'Vertical "resolution" [micron]']

        yaxis_data = ['cbpm_x',
                      'cbpm_y',
                      'cpbm_xres',
                      'cbpm_yres']

        for i in range(4):

            fig[i].update_layout(
                height=500,
                template='plotly_white'
            )

            # fig[i]['layout']['xaxis'].update(title='Time [hh:mm:ss]', title_font=dict(size=25), tickfont=dict(size=18))
            # fig[i]['layout']['xaxis'].update(gridcolor='grey', showline=True, linewidth=2, linecolor='grey', mirror=True)
            fig[i].update_xaxes(
                title='Time [hh:mm:ss]',
                title_font=dict(size=20),
                tickfont=dict(size=18),
                gridcolor='grey',
                showline=True,
                linewidth=2,
                linecolor='grey',
                mirror=True
            )

            fig[i].update_yaxes(
                title=yaxis_label[i],
                title_font=dict(size=20),
                tickfont=dict(size=18),
                gridcolor='grey',
                showline=True,
                linewidth=2,
                linecolor='grey',
                mirror=True,
                zeroline=True,
                zerolinecolor='grey',
                zerolinewidth=1,
                # automargin=True
            )

            # fig[i]['layout']['plot_bgcolor'] = 'rgb(0, 0, 0, 0)'
            # fig[i]['layout']['paper_bgcolor'] = 'rgb(0, 0, 0, 333)'

            fig[i].add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df[yaxis_data[i]],
                    name="position"
                ),
                secondary_y=False
            )

        return fig[0], fig[1], fig[2], fig[3]

    else:

        return cbpm_xpos, cbpm_ypos, cbpm_xres, cbpm_yres
