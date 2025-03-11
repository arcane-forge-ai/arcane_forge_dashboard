import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, dcc, page_container, State

from components.header import create_header
from components.navbar import create_navbar, create_navbar_drawer


def create_appshell(data):
    return dmc.MantineProvider(
        id="m2d-mantine-provider",
        forceColorScheme="light",
        theme={
            # "primaryColor": "arcaneForge",
            "fontFamily": "'Inter', sans-serif",
            "components": {
                "Button": {
                    "defaultProps": {
                        "fw": 400
                    }
                },
                "Alert": {
                    "styles": {
                        "title": {
                            "fontWeight": 500
                        }
                    }
                },
                "AvatarGroup": {
                    "styles": {
                        "truncated": {
                            "fontWeight": 500
                        }
                    }
                },
                "Badge": {
                    "styles": {
                        "root": {
                            "fontWeight": 500
                        }
                    }
                },
                "Progress": {
                    "styles": {
                        "label": {
                            "fontWeight": 500
                        }
                    }
                },
                "RingProgress": {
                    "styles": {
                        "label": {
                            "fontWeight": 500
                        }
                    }
                },
                "CodeHighlightTabs": {
                    "styles": {
                        "file": {
                            "padding": 12
                        }
                    }
                },
                "Table": {
                    "defaultProps": {
                        "highlightOnHover": True,
                        "withTableBorder": True,
                        "verticalSpacing": "sm",
                        "horizontalSpacing": "md",
                    }
                },
            },
            "colors": {
                "arcaneForge": [
                    "#9EA1B6", "#888DAD", "#7379A6", "#5C65A4", "#4B559D",
                    "#3B4698", "#2B3895", "#303A7D", "#323969", "#32375A",
                    "#31344D", "#2E3143", "#2C2D3A"
                ]
            },
        },
        children=[
            dcc.Store(id="user-login-token", storage_type="session"),
            dcc.Store(id="user-info-store", storage_type="session"),
            dcc.Location(id="url", refresh="callback-nav"),
            dmc.NotificationProvider(zIndex=2000),
            dmc.AppShell(
                [
                    create_header(data),
                    create_navbar(data),
                    create_navbar_drawer(data),
                    dmc.AppShellMain(children=page_container),
                ],
                header={"height": 70},
                padding="xl",
                zIndex=1400,
                navbar={
                    "width": 300,
                    "breakpoint": "lg",
                    "collapsed": {
                        "mobile": True
                    },
                },
                aside={
                    "width": 300,
                    "breakpoint": "xl",
                    "collapsed": {
                        "desktop": False,
                        "mobile": True
                    },
                },
            ),
        ],
    )


clientside_callback(
    """
    function(n_clicks, theme) {        
        dash_clientside.set_props("m2d-mantine-provider", {
            forceColorScheme: theme === "dark" ? "light" : "dark"
        });
        return dash_clientside.no_update
    }
    """,
    Output("m2d-mantine-provider", "forceColorScheme"),
    Input("color-scheme-toggle", "n_clicks"),
    State("m2d-mantine-provider", "forceColorScheme"),
    prevent_initial_call=True,
)
