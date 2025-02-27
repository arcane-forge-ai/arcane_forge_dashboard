import importlib
from typing import List, Optional

import dash
import dash_mantine_components as dmc
from pydantic import BaseModel, Field
import yaml
from dash import html


class ProductPageMeta(BaseModel):
    name: str = Field(
        description="Name of the product page. This would be shown on the menu"
    )
    # Type of the product page. Can be
    type: str = Field(
        description=
        "Type of the product page. Can be one of [embed, dash]. `embed` would be embed an IFrame of the URI into the dashboard; `dash` would be treated as a common dash page"
    )
    path: str = Field(description="Path of the product page.")
    uri: str = Field(
        description=
        "URI of the product page. If the product page is an `embed` type, then it should be a web URL (i.e. 'http://xxx.com'). If the product page is a `dash` type, then it should be a python module URI (i.e. modules.samples.timeline)"
    )


class ProductMeta(BaseModel):
    product_name: str = Field(
        "Name of the product. This would be shown on the menu")
    pages: List[ProductPageMeta] = Field(
        "List of all the pages that needs to be shown on the menu of the product"
    )


with open("product_config.yaml") as f:
    product_config = yaml.safe_load(f)

for product in product_config["products"]:
    product_meta = ProductMeta(**product)
    for product_page_meta in product_meta.pages:
        # add heading and description to the layout
        section = [
            dmc.Title(
                f"{product_meta.product_name} > {product_page_meta.name}",
                order=2,
                className="m2d-heading"),
            dmc.Divider(variant="solid", mb=16),
            # dmc.Text(metadata.description, className="m2d-paragraph"),
        ]
        if product_page_meta.type == "embed":
            dash.register_page(
                product_page_meta.name,
                product_page_meta.path,
                name=product_page_meta.name,
                layout=section + [
                    html.Div([
                        html.Div(
                            html.Iframe(
                                src=product_page_meta.uri,
                                id="content-iframe",
                                style={
                                    "border": "none",
                                    "width":
                                    "100%",  # Ensure the iframe takes 100% width of the parent
                                    "height":
                                    "100%"  # Ensure the iframe takes 100% height of the parent
                                }),
                            id="iframe-wrapper",
                            style={
                                "display":
                                "flex",  # Flexbox to ensure child elements stretch
                                "flexDirection":
                                "column",  # Make it a column layout
                                "height":
                                "100vh",  # Set the height to 100% of the viewport
                            })
                    ])
                ],
                category=product_meta.product_name,
            )
        elif product_page_meta.type == "dash":
            module = importlib.import_module(product_page_meta.uri)
            dash.register_page(
                product_page_meta.name,
                product_page_meta.path,
                name=product_page_meta.name,
                layout=section + [module.layout],
                category=product_meta.product_name,
            )
