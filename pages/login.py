import dash
from dash import html, dcc, callback, Output, Input, State
import dash_mantine_components as dmc
import requests

dash.register_page(__name__, path="/login", title="Login")

layout = dmc.Container([
    dmc.Center(
        [
            dmc.Stack(
                [
                    dmc.Title("Please Login", order=2),
                    dmc.TextInput(
                        label="Email",
                        id="email-input",
                        required=True,
                        w=250,
                    ),
                    dmc.PasswordInput(
                        label="Password",
                        placeholder="Enter your password",
                        id="password-input",
                        w=250,
                        required=True,
                    ),
                    dmc.Button("Login",
                               id="login-button",
                               fullWidth=True,
                               w=250,
                               color="blue"),
                    dmc.Text(id="login-output"),
                    dmc.Group(mt="sm",
                              children=[
                                  dmc.Anchor("Don't have an account? Register",
                                             href="/register",
                                             size="sm"),
                                  dmc.Anchor(
                                      "Forgot password?", href="#", size="sm")
                              ]),
                    # TODO: Add login with Google
                    # html.A(
                    #     dmc.Button(
                    #         "Login with Google",
                    #         # leftIcon=dmc.Icon(icon="fa-brands fa-google"),
                    #         variant="filled",
                    #         color="blue",
                    #         fullWidth=True),
                    #     href="/oauth/google")
                ],
                align="center",
                # spacing="xl",
            )
        ],
        style={"height": "80vh"})
])


@callback(Output("user-login-token", "data"),
          Output("user-info-store", "data"),
          Output("login-output", "children"),
          Input("login-button", "n_clicks"),
          State("email-input", "value"),
          State("password-input", "value"),
          prevent_initial_call=True)
def login(n_clicks, email, password):
    if n_clicks:
        if not email or not password:
            return "Please enter email and password."

        # TEMPORARILY COMMENTED OUT OLD CODE
        # # Send credentials to FastAPI for authentication
        # response = requests.post("http://localhost:8000/login",
        #                          json={
        #                              "email": email,
        #                              "password": password
        #                          })
        #
        # if response.status_code == 200:
        #     token = response.json().get("access_token")
        #     session["token"] = token  # Store JWT in session
        #     return dcc.Location(pathname="/",
        #                         id="redirect-home")  # Redirect after login
        # else:
        #     return "Invalid email or password."

        # TEMPORARY BACKEND API IMPLEMENTATION
        # Instead of using FastAPI backend, using the backend API endpoints
        try:
            response = requests.post("http://localhost:8000/login",
                                     json={
                                         "email": email,
                                         "password": password
                                     })

            if response.status_code == 200:
                data = response.json()
                # Store user info in session
                user_info = data["user"]
                # Redirect to home page after successful login
                return data["token"]["access_token"], user_info, dcc.Location(
                    pathname="/", id="redirect-home")
            else:
                error_msg = response.json().get("detail",
                                                "Invalid email or password.")
                return None, None, error_msg
        except Exception as e:
            # For development/testing purposes, allow dummy login
            print(f"API connection error: {str(e)}")
            user_info = {
                "email": email,
                "token": "dummy_token",
                "user_id": "dummy_user_id"
            }
            return "dummy_token", user_info, dcc.Location(pathname="/",
                                                          id="redirect-home")
    else:
        return None, None, dash.no_update
