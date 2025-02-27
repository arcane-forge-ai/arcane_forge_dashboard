import os
from dotenv import load_dotenv
import dash
import dash_mantine_components as dmc

from components.appshell import create_appshell

# Load environment variables
dash._dash_renderer._set_react_version('18.2.0')
load_dotenv()

TITLE = os.getenv('TITLE')
URL_PREFIX = os.getenv('URL_PREFIX', '/ArcaneForge')

title = "Arcane Forge - AI for Game Development"
app = dash.Dash(
    TITLE,
    external_stylesheets=dmc.styles.ALL,
    use_pages=True
)
app.title = TITLE
server = app.server

# Define the layout with AppShell
app.layout = create_appshell(dash.page_registry.values())

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
