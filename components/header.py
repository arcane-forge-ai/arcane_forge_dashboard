import dash_mantine_components as dmc
from dash_iconify import DashIconify


def create_header(data):
    return dmc.AppShellHeader(
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                h=70,
                children=dmc.Grid(
                    justify="space-between",
                    children=[
                        dmc.GridCol(
                            dmc.Group([
                                dmc.Anchor(
                                    dmc.Image(
                                        src="/assets/logo.webp",
                                        h=50,
                                    ),
                                    href="/",
                                    
                                ),
                            ]),
                            span="content",
                        ),
                        dmc.GridCol(
                            span="auto",
                            children=dmc.Group(
                                justify="flex-end",
                                h=64,
                                gap="xl",
                                children=[
                                    dmc.Button(
                                        "Logout",
                                        id="logout-button",
                                        # leftIcon=DashIconify(icon="radix-icons:exit", width=20),
                                        variant="outline",
                                        color="red",
                                        size="sm",
                                    ),
                                    dmc.ActionIcon(
                                        [
                                            DashIconify(
                                                icon="radix-icons:sun",
                                                width=64,
                                                id="light-theme-icon",
                                            ),
                                            DashIconify(
                                                icon="radix-icons:moon",
                                                width=64,
                                                id="dark-theme-icon",
                                            ),
                                        ],
                                        variant="transparent",
                                        color="arcaneForge",
                                        id="color-scheme-toggle",
                                        size="lg",
                                    ),
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="radix-icons:hamburger-menu",
                                            width=64,
                                        ),
                                        id="drawer-hamburger-button",
                                        variant="transparent",
                                        size="lg",
                                        hiddenFrom="sm",
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            )
        ],
    )
