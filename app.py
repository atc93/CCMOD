# -*- coding: utf-8 -*-
import time

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import utils.display as display

import plotly

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H2("CBPM continuous monitoring on-line display"),
                ],
            ),
        ],
    )

def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab1",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="tab-1",
                        label="Trend plots",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="tab-2",
                        label="Second tab",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="tab-3",
                        label="Third tab",
                        value="tab3",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )

def build_tab_1():
    return [
#        html.Div(
#            children=[
         html.Div(
             className="four columns",
             children=[
                html.P('\nSelect time window (in minutes) of last available data to display:')
             ],
         ),
         html.Div(
             className="four columns",
             children=[
                 dcc.Input(id='my-id', value='15', type='text'),
            ],
        ),
         html.Div(
             className="twelve columns",
             children=[
                 dcc.Graph(
                    id='live-update-graph',
                 ),
                 dcc.Interval(
                     id='interval-component',
                     interval=5*1000, # in ms
                     n_intervals = 1
                 )             
            ],
        ),
        html.Div(
            className="four columns",
            children=[
                html.P('Auto-update with fresh data switch:'),
                daq.BooleanSwitch(
                    id='my-daq-booleanswitch',
                    on=True,
                    label="Auto-update switch",
                    labelPosition="top"
                    )
            ],
        ),
        
    ]
#        )
#    ]

app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                # Main app
                html.Div(id="app-content"),
            ],
        ),
    ]
)

@app.callback(
    Output("app-content", "children"),
    [Input("app-tabs", "value")]
)
def render_tab_content(tab_switch):
#    print(tab_switch)
    if tab_switch == 'tab1':
        return build_tab_1()

#@app.callback(Output(component_id='data-window-selector', component_property='children'),
#                [Input(component_id='my-id', component_property='value')])
#def update_output_div(input_value):
#    return 'Enter time window (in minutes) for last available data: you have entered {} minutes'.format(input_value)



#app.layout = html.Div(children=[
#    html.Div(
#        [
#        html.H2(
#            "CBPM continuous monitoring on-line display",
#            id="title",
#            className="eight columns",
#            style={"margin-left": "3%"},
#            ),
#        daq.LEDDisplay(
#            id='my-LED-display',
#            label="Default",
#            value="15:17"
#            ),
#        ],
#        className="banner",
#        ),
#    html.Div(
#        children=[
#            html.Div(id='data-window-selector'),
#            dcc.Input(id='my-id', value='15', type='text')
#        ],
#        className="four columns",
#    ),
#    dcc.Graph(id='live-update-graph'),
#    dcc.Interval(
#        id='interval-component',
#        interval=5*1000, # in ms
#        n_intervals = 0
#    )
#])
#
#@app.callback(Output(component_id='data-window-selector', component_property='children'),
#                [Input(component_id='my-id', component_property='value')])
#def update_output_div(input_value):
#    return 'Enter time window (in minutes) for last available data: you have entered {} minutes'.format(input_value)
#
#
@app.callback(Output('live-update-graph', 'figure'),
                [Input('interval-component', 'n_intervals'),
                Input('my-id', 'value')],
                [State('my-daq-booleanswitch','on')])
def update(n, time, switch):


    if switch:
        df = display.analyze(int(time))

        fig = plotly.subplots.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
#        fig['layout']['margin'] = {'l': 30, 'r': 10, 'b': 30, 't': 10}
        fig['layout']['xaxis'].update(title='time')
        fig['layout']['yaxis'].update(title='vertical position [micron]')
        fig['layout']['plot_bgcolor'] = 'rgb(255, 255, 255)'
        fig.add_trace({
            'x': df['timestamp'],
            'y': df['ypos'],
        }, 1, 1)

        return fig

if __name__ == '__main__':
    app.run_server(debug=True)
