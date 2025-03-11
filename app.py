import os
from dotenv import load_dotenv
import dash
import dash_mantine_components as dmc
from dash import html, dcc, Input, Output, State, callback
from flask import Flask, session, redirect, url_for
from authlib.integrations.flask_client import OAuth

from components.appshell import create_appshell

# Load environment variables
dash._dash_renderer._set_react_version('18.2.0')
load_dotenv()

TITLE = os.getenv('TITLE')
URL_PREFIX = os.getenv('URL_PREFIX', '/ArcaneForge')

title = "Arcane Forge - AI for Game Development"
app = dash.Dash(TITLE, external_stylesheets=dmc.styles.ALL, use_pages=True)
app.title = TITLE
server = app.server

server.secret_key = os.urandom(24)

oauth = OAuth(server)
google = oauth.register(
    name='google',
    client_id=
    "394742476706-6nse37b6gtlfb04m9tu1cshk6r68nf5q.apps.googleusercontent.com",
    client_secret=None,
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    client_kwargs={
        'scope': 'openid email profile',
        'code_challenge_method': 'S256'  # PKCE prevents needing a secret
    },
    client_auth_method='none',
)


# Login route
@server.route('/oauth/google')
def login():
    redirect_uri = url_for('auth_callback', _external=True)
    print(redirect_uri)
    return google.authorize_redirect(redirect_uri)


# OAuth callback route
@server.route('/auth/callback')
def auth_callback():
    token = google.authorize_access_token(client_auth=None)
    user_info = google.parse_id_token(token)

    session['user'] = {
        'name': user_info['name'],
        'email': user_info['email'],
        'sub': user_info['sub']
    }
    return redirect('/')


# Logout route (optional but recommended)
@server.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


# def serve_layout():
#     if 'user' not in session:
#         return dcc.Location(pathname="/login", id="redirect-login")

#     # Authenticated layout:
#     return create_appshell(dash.page_registry.values())

app.layout = html.Div([
    # dcc.Location(id='url', refresh=True),
    create_appshell(dash.page_registry.values())
])


# Authentication protection
@app.callback(
    Output('url', 'pathname'),
    Input('url', 'pathname'),
    State('user-login-token', 'data'),
    State('user-info-store', 'data'),
)
def protect_routes(pathname, user_login_token, user_info_store):
    # List of public routes that don't require authentication
    public_routes = ['/login', '/register']

    if user_login_token is None and pathname not in public_routes:
        return '/login'
    return dash.no_update

# Logout callback
@callback(
    Output('user-login-token', 'data', allow_duplicate=True),
    Output('user-info-store', 'data', allow_duplicate=True),
    Output('url', 'pathname', allow_duplicate=True),
    Input('logout-button', 'n_clicks'),
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    if n_clicks is None:
        return dash.no_update, dash.no_update, dash.no_update
    
    # Clear the stored data and redirect to login page
    return None, None, '/login'


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
