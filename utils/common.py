import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import dash_bootstrap_components as dbc

def build_navbar():
    return html.Div(
        id="banner",
        children=[
            html.Div(
                id="banner-text",
                className="banner",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(html.Div(html.H2("CBPM continuous monitoring on-line display")), width=11),
                            dbc.Col(
                                html.Div(
                                    id="banner-logo",
                                    children=[
                                        html.Button(
                                            id="learn-more-button", children="INFORMATION", n_clicks=0
                                        ),
                                    ],
                                ),
                            )
                        ],
                    ),
                ],
            ),
            html.Div(
                className="banner2",
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    daq.PowerButton(
                                        id='live_update_switch',
                                        on='True',
                                        size=50,
                                        color='#079407',
                                        # label='Label',
                                        # labelPosition='top'
                                    ),
                                    id='test_button',
                                    style={'padding': '10px 0px 0px 0px'},
                                ), width={"size": 1},
                            ),
                            dbc.Col(
                                html.Div(
                                    children=[
                                        html.H2("Live update is:"),
                                        html.H2(
                                            id='live_update_running',
                                            style={'margin-left': '1.0%', 'color': '#079407', 'font-weight': 'bold'},
                                        ),
                                        html.H2(
                                            id='live_update_paused',
                                            style={'margin-left': '0.5%', 'color': '#e0392a', 'font-weight': 'bold'},
                                        ),
                                    ],
                                ), #style={'padding': '0px 1000px 0px 0px'},
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        daq.Slider(
                                            id='time_window_slider',
                                            min=1,
                                            max=360,
                                            value=15,
                                            step=1,
                                            labelPosition='bottom',
                                            size=500,
                                            handleLabel={"label": "minute(s):", "showCurrentValue": True, },
                                            marks={'15': '15 minutes', '60': '1 hour', '120': '2 hours',
                                                   '180': '3 hours', '360': '6 hours'},
                                            color='blue'
                                        ),
                                    ], style={'railStyle': '10px', 'margin-right': '50%', 'padding': '20px 0px 0px 0px'}
                                ), width=4,
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id='demo-dropdown',
                                            options=[
                                                {'label': 'beam position', 'value': 'beam_position'},
                                                {'label': 'button readings', 'value': 'button_readings'},
                                            ],
                                            placeholder="Menu...",
                                        ),
                                    ]
                                ), width=2,
                            )
                            # dbc.Col(
                            #     html.Div(
                            #         daq.Slider(
                            #             className='columns',
                            #             id='time_window_slider',
                            #             min=1,
                            #             max=360,
                            #             value=15,
                            #             step=1,
                            #             labelPosition='bottom',
                            #             size=500,
                            #             handleLabel={"label": "minute(s):", "showCurrentValue": True, },
                            #             marks={'15': '15 minutes', '60': '1 hour', '120': '2 hours', '180': '3 hours',
                            #                    '360': '6 hours'},
                            #             color='blue'
                            #         ),
                            #         style={'width': '100%', 'stroke-width': '20px', 'padding': '20px 20px 100px 100px'}
                            #     ), width=6,
                            # ),
                            # dbc.Col(
                            #     html.Div(
                            #         daq.LEDDisplay(
                            #             id='my-daq-leddisplay',
                            #             value="17:10:01",
                            #             size=30
                            #         ), style={'padding': '5px 0px 0px 0px'},
                            #     )
                            # )
                        ], no_gutters=True, justify='start',
                    )
                ]
            )
        ],
    )

# def build_menus():
#     return html.Div
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


def generate_modal():
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                className="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Close",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton",
                        ),
                    ),
                    html.Div(
                        className="markdown-text",
                        children=dcc.Markdown(
                            children=(
                                """
                        ###### What is this mock app about?
                        This is a dashboard for monitoring real-time process quality along manufacture production line.
                        ###### What does this app shows
                        Click on buttons in `Parameter` column to visualize details of measurement trendlines on the bottom panel.
                        The sparkline on top panel and control chart on bottom panel show Shewhart process monitor using mock data.
                        The trend is updated every other second to simulate real-time measurements. Data falling outside of six-sigma control limit are signals indicating 'Out of Control(OOC)', and will
                        trigger alerts instantly for a detailed checkup.

                        Operators may stop measurement by clicking on `Stop` button, and edit specification parameters by clicking specification tab.
                    """
                            )
                        ),
                    ),
                ],
            )
        ),
    )