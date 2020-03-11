# -*- coding: utf-8 -*-
import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output, State
import dash_table as table
import numpy
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


import utils.display as display
import utils.xymotion as xymotion
import utils.common as common
import utils.button_readings as button_readings

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder="./assets")
app.config.suppress_callback_exceptions = True

# row = html.Div(
#     [
#         daq.Slider(
#             id='time_window_slider',
#             min=1,
#             max=360,
#             value=15,
#             step=1,
#             labelPosition='bottom',
#             size=500,
#             handleLabel={"label": "minute(s):", "showCurrentValue": True,},
#             marks={'15': '15 minutes', '60': '1 hour', '120': '2 hours', '180': '3 hours', '360': '6 hours'},
#             color='blue'
#         ),
#     ], style={'railStyle': '10px', 'margin-left': '37%', 'padding': '20px 0px 0px 0px'}
# )



app.layout = html.Div(
    [
        common.build_navbar(),
        common.generate_modal(),
        # row,
        dbc.Container(
            [
                dcc.Interval(
                    id='interval-component',
                    interval=5 * 1000,  # in ms
                ),
                html.Div(
                    id="app-container",
                    children=[
                        html.Div(id="app-content")
                    ]
                )
            ],
            # fluid=True,
        ),
    ],
    style={'backgroundColor':'white'}
)

@app.callback(
    Output("app-content", "children"),
    [Input("demo-dropdown", 'value')]
)
def render_menus(menu_name):
    if menu_name == "beam_position":
        return xymotion.build_layout()
    elif menu_name == "button_readings":
        return button_readings.build_layout()

# @app.callback(
#     Output("app-content", "children"),
#     [Input("app-tabs", "value")]
# )
# def render_tab_content(tab_switch):
# #    print(tab_switch)
#     if tab_switch == 'tab1':
#         return build_tab_1()

@app.callback(
    [Output(component_id='live_update_running', component_property='children'),
    Output(component_id='live_update_paused', component_property='children')],
    [Input('live_update_switch', 'on')]
)
def change_live_text_status(switch):
    if switch:
        return ("RUNNING", "")
    elif not switch:
        return ("", "PAUSED")


@app.callback([Output('cbpm_xpos', 'figure'),
               Output('cbpm_ypos', 'figure'),
               Output('cbpm_xres', 'figure'),
               Output('cbpm_yres', 'figure')],
              [Input('time_window_slider', 'value'),
               Input('interval-component', 'n_intervals'),
               Input('live_update_switch', 'on')],
              [State('cbpm_xpos', 'figure'),
               State('cbpm_ypos', 'figure'),
               State('cbpm_xres', 'figure'),
               State('cbpm_yres', 'figure')])
def call_back_xymotion(time, n, switch, cbpm_xpos, cbpm_ypos, cbpm_xres, cbpm_yres):
    # print(n, time, switch)
    return xymotion.update(n, time, switch, cbpm_xpos, cbpm_ypos, cbpm_xres, cbpm_yres)

@app.callback([Output('button_amp', 'figure'),
               Output('button_std', 'figure')],
              [Input('time_window_slider', 'value'),
               Input('interval-component', 'n_intervals'),
               Input('live_update_switch', 'on')],
              [State('button_amp', 'figure'),
               State('button_std', 'figure')])
def call_back_button_readings(time, n, switch, button_amp, button_std):
    # print(n, time, switch)
    return button_readings.update_plots(n, time, switch, button_amp, button_std)

# ======= Callbacks for modal popup =======
@app.callback(
    Output("markdown", "style"),
    [Input("learn-more-button", "n_clicks"), Input("markdown_close", "n_clicks")],
)
def update_click_output(button_click, close_click):
    ctx = dash.callback_context

    if ctx.triggered:
        prop_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if prop_id == "learn-more-button":
            return {"display": "block"}

    return {"display": "none"}

if __name__ == '__main__':
    app.run_server(debug=True)
