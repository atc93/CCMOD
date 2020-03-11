# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objects as go

from utils import display


def build_layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            dcc.Graph(id='button_amp')
                        ),
                        width=6
                    ),
                    dbc.Col(
                        html.Div(
                            children=[
                                dcc.Graph(id='button_std'),

                            ]
                        ),
                        width=6
                    ),
                ]
            )
        ]
    )

def update_plots(n, time, switch, cbpm_amp, cbpm_std):
    if switch:
        df = display.analyze(float(time))

        fig = []
        fig.append(plotly.subplots.make_subplots())
        fig.append(plotly.subplots.make_subplots())


        yaxis_label = ['Button reading amplitude [ADU]',
                       'Button reading width [ADU]']

        yaxis_data = ['top_in',
                      'top_out',
                      'bot_in',
                      'bot_out',
                      'top_in_std',
                      'top_out_std',
                      'bot_in_std',
                      'bot_out_std']

        names =['top_in', 'top_out', 'bot_in', 'bot_out']

        for i in range(2):

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

            for j in range(4):
                fig[i].add_trace(
                    go.Scatter(
                        x=df['timestamp'],
                        y=df[yaxis_data[i*4+j]],
                        name=names[j]
                    ),
                    secondary_y=False
                )

        return fig[0], fig[1]

    else:

        return cbpm_amp, cbpm_std
