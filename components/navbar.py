from collections import defaultdict, OrderedDict
import yaml

import dash_mantine_components as dmc
from dash_iconify import DashIconify

from utils.constants import PRIMARY_COLOR

excluded_links = [
    "/404",
    "/getting-started",
    "/styles-api",
    "/style-props",
    "/dash-iconify",
    "/",
    "/migration",
    "/auth/callback",
    "/login",
    "/register",
]

# https://icon-sets.iconify.design/
category_data = {
    "Image Generation": {
        "icon": "mdi:image-outline"
    },
    "Audio Generation": {
        "icon": "mdi:audio-outline"
    },
    "Chat": {
        "icon": "mdi:chat-outline"
    },
    "Customized AI Tasks": {
        "icon": "mdi:cog-outline"
    },
    "Others": {
        "icon": "mdi:cog-outline"
    },
}


def create_main_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group([
            DashIconify(
                icon=icon,
                width=23,
                color=PRIMARY_COLOR,
            ),
            dmc.Text(label, size="sm"),
        ]),
        href=href,
        variant="text",
        mb=5,
        underline=False,
    )


def create_content(data):
    # First collect all links from registered pages
    links = defaultdict(list)
    for entry in data:
        if entry["path"] not in excluded_links:
            link = dmc.NavLink(
                label=entry["name"],
                href=entry["path"],
                h=32,
                className="navbar-link",
                pl=30,
            )
            links[entry["category"]].append(link)

    # Read product_config to get the correct order
    with open("product_config.yaml") as f:
        product_config = yaml.safe_load(f)
    
    body = []
    # Use product_config order to build the navbar
    for product in product_config["products"]:
        section = product["product_name"]
        if section in links:  # Only add sections that have registered pages
            body.append(
                dmc.Divider(
                    label=[
                        DashIconify(icon=category_data[section]["icon"],
                                    height=23),
                        dmc.Text(section, ml=5, size="sm"),
                    ],
                    labelPosition="left",
                    mt=40,
                    mb=10,
                ))
            body += links[section]

    return dmc.ScrollArea(
        offsetScrollbars=True,
        type="scroll",
        style={"height": "100%"},
        children=dmc.Stack(gap=0, children=[*body, dmc.Space(h=90)], px=25),
    )


def create_navbar(data):
    return dmc.AppShellNavbar(children=create_content(data))


def create_navbar_drawer(data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayProps={
            "opacity": 0.55,
            "blur": 3
        },
        zIndex=1500,
        offset=10,
        radius="md",
        withCloseButton=False,
        size="75%",
        children=create_content(data),
        trapFocus=False,
    )
