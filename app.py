import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
# nltk.data.path.append('nltk_data')

import prediction
import analysis

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True,
                prevent_initial_callbacks=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
server = app.server
app.title = 'SMS/Email Spam Detection'
app._favicon = "spam.png"


app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(html.A(
                [dbc.CardImg(src='assets/sk2.png', style={'width': '70px', 'height': '30px'}, className='mx-5 my-1')],
                href='https://isantosh-portfolio.herokuapp.com/')),
            dbc.NavItem(dbc.NavLink(
                html.A("Predict", href="/", className="me-1 text-decoration-none fs-5", id='predict_link',
                       n_clicks=0))),
            dbc.NavItem(dbc.NavLink(
                html.A("Analysis", href="model-report", className="me-1 text-decoration-none fs-5", id='model_link',
                       n_clicks=0))),
            dbc.NavItem(dbc.NavLink(html.A("Source Code", href="https://github.com/withusanty/SMS-SPAM-Classifier",
                                           className="me-1 text-decoration-none fs-5"))),
            dbc.NavItem(dbc.NavLink(html.A("Profile", href="https://isantosh-portfolio.herokuapp.com/",
                                           className="me-1 text-decoration-none fs-5"))),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Linkedin", href='https://www.linkedin.com/in/santy707/'),
                    dbc.DropdownMenuItem("Kaggle", href='https://www.kaggle.com/kuchhbhi'),
                    dbc.DropdownMenuItem("Github", href='https://github.com/withusanty'),
                    dbc.DropdownMenuItem(html.A("About", href='#about', className='me-1 text-decoration-none')),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ], fixed='top',
        brand="SMS/E-mail Spam Detection",
        brand_href="/",
        color="primary",
        dark=True,
        className='py-0'),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
        dcc.Location(id='url', refresh=True),
    ], id='display')

], fluid=True)

@app.callback(
    Output('display', 'children'),
    Input('url', 'pathname'))
def update(x):
    if x == '/':
        return prediction.spam_check_div
    elif x == '/model-report':
        return analysis.graph


if __name__ == '__main__':
    app.run_server(debug=True)
