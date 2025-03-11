import dash
from dash import html, dcc, callback, Output, Input, State
import dash_mantine_components as dmc
import requests

dash.register_page(__name__, path="/register", title="Register")

layout = dmc.Container([
    dmc.Center([
        dmc.Stack(
            [
                dmc.Title("Create an Account", order=2),
                dmc.TextInput(
                    label="User Name",
                    placeholder="Enter your username",
                    id="name-input",
                    required=True,
                    w=250,
                ),
                dmc.TextInput(
                    label="Email",
                    placeholder="Enter your email",
                    id="email-input",
                    required=True,
                    w=250,
                ),
                dmc.PasswordInput(
                    label="Password",
                    placeholder="Enter your password",
                    id="password-input",
                    required=True,
                    w=250,
                ),
                dmc.PasswordInput(
                    label="Confirm Password",
                    placeholder="Confirm your password",
                    id="confirm-password-input",
                    required=True,
                    w=250,
                ),
                dmc.Button("Register",
                           id="register-button",
                           fullWidth=True,
                           w=250,
                           color="blue"),
                html.Div(id="register-output"),
                dmc.Group(mt="sm",
                          children=[
                              dmc.Anchor("Already have an account? Login",
                                         href="/login",
                                         size="sm")
                          ])
            ],
            align="center",
        )
    ],
               style={"height": "80vh"})
])


@callback(Output("register-output", "children"),
          Input("register-button", "n_clicks"),
          State("name-input", "value"),
          State("email-input", "value"),
          State("password-input", "value"),
          State("confirm-password-input", "value"),
          prevent_initial_call=True)
def register(n_clicks, name, email, password, confirm_password):
    if n_clicks:
        if not name or not email or not password or not confirm_password:
            return "Please fill in all fields."

        if password != confirm_password:
            return "Passwords do not match."

        # TEMPORARY BACKEND API IMPLEMENTATION
        try:
            response = requests.post("http://localhost:8000/register",
                                     json={
                                         "username": name,
                                         "email": email,
                                         "password": password
                                     })

            if response.status_code == 201 or response.status_code == 200:
                # Registration successful
                return dmc.Group([
                    dmc.Text(
                        "Registration successful! Redirecting to login..."),
                    dcc.Location(pathname="/login", id="redirect-login")
                ])
            else:
                error_msg = response.json().get(
                    "detail", "Registration failed. Please try again.")
                return error_msg
        except Exception as e:
            # For development/testing purposes
            print(f"API connection error: {str(e)}")
            # Simulate successful registration
            return dmc.Group([
                dmc.Text("Registration successful! Redirecting to login...",
                         color="green"),
                dcc.Location(pathname="/login", id="redirect-login")
            ])
