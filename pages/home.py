import dash
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from utils.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR

dash.register_page(__name__,
                   "/",
                   title=PAGE_TITLE_PREFIX + "HOME",
                   description="The All-in-One AI Platform for Game Development")


def create_title(title, id):
    return dmc.Text(title, ta="center", fw=300, fz=30, id=id)


def create_heading(text):
    return dmc.Text(text, ta="center", mt=10, mb=20, mx=0)


def create_tile(icon, heading, description, href):
    return dmc.Card(
        radius="md",
        p="xl",
        withBorder=True,
        m=5,
        children=[
            DashIconify(
                icon=icon,
                height=20,
                color=PRIMARY_COLOR,
            ),
            dmc.Text(heading, size="lg", mt="md"),
            dmc.Text(description, size="sm", c="dimmed", mt="sm"),
        ],
    )


layout = html.Div([
    create_title(
        "Arcane Forge - AI for Game Development",
        id="features",
    ),
    dmc.Container(
        size="lg",
        px=0,
        py=0,
        my=40,
        children=[
            dmc.SimpleGrid(
                mt=80,
                cols={
                    "xs": 1,
                    "sm": 2,
                    "xl": 3
                },
                children=[
                    create_tile(
                        icon="mdi:image-outline",
                        heading="Image Generation",
                        description=
                        "Generate images from text prompts",
                        href="/image-generation",
                    ),
                    create_tile(
                        icon="mdi:audio-outline",
                        heading="Audio Generation",
                        description=
                        "Generate audio from text prompts",
                        href="/audio-generation",
                    ),
                    create_tile(
                        icon="mdi:chat-outline",
                        heading="Chat",
                        description=
                        "Chat with AI",
                        href="/chat",
                    ),
                    create_tile(
                        icon="mdi:cog-outline",
                        heading="Customized AI Tasks",
                        description=
                        "Customized AI Tasks",
                        href="/customized-ai-tasks",
                    ),
                ],
            )
        ],
    ),
])
