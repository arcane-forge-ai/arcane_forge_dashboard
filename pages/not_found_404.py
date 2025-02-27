import dash
import dash_mantine_components as dmc

from utils.constants import PAGE_TITLE_PREFIX

dash.register_page(__name__, title=PAGE_TITLE_PREFIX + "404", path="/404")

layout = dmc.Stack(
    align="center",
    children=[
        dmc.Text(
            [
                "If you think this page should exist, create an issue ",
                dmc.Anchor(
                    "here",
                    underline=False,
                    target="_blank",
                    href="https://github.com/dagondagon666/arcane_forge_dashboard/issues",
                ),
                ".",
            ]
        ),
        dmc.Anchor("Go back to home", href="/", underline=False),
    ],
    mt=100,
)
