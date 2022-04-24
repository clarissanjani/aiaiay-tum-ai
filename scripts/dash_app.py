from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash
from dash.dependencies import Input, Output, State
import time
import base64
import os
import sys

workdir = os.path.dirname(os.path.dirname(__file__))
print(workdir)

sys.path.append(workdir)

from scripts.coordinate_helpers import coords_by_adress
from scripts.create_map import create_map

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.config.serve_locally = False

img_path = os.path.join(workdir, 'aiaiay-app/public/assets/bg.jpg')
# encoded_image = base64.b64encode(open('./Brightly.png', 'rb').read())
app.layout = html.Div(
    [
        html.Div(style = {'minHeight': '30vh','backgroundImage': f'url(./assets/Brightly.png)', 'backgroundRepeat': 'no-repeat',
                          'backgroundSize': 'cover'}),
        html.Br(),
        html.Br(),
        html.Div(
            [
                dcc.Input(id="input1", type="text", placeholder="Enter Adress", debounce=True,
                          style={'marginRight': '10px', 'justify-content': 'center'}),
                html.Button('Go', id='submit', style={'background-color': 'white', 'opacity': '0.5'})
            ], style={'width': '50%', 'padding-left': '25%', 'padding-right': '25%', 'padding-top': '10%'}),
        html.Br(),
        html.Br(),
        html.Div(html.Iframe(id='map', srcDoc=open('map.html', 'r').read(), width='100%', height=400),
                 style={'width': '80%', 'padding-left': '10%', 'padding-right': '10%'}),
        html.Br(),
        html.Br(),
        html.Div(html.Iframe(id='sunlight_map', srcDoc=open('sunlight_map.html', 'r').read(), width='100%', height=400),
                 style={'width': '80%', 'padding-left': '10%', 'padding-right': '10%'})
    ],
    style={
        'minHeight': '100vh',
        'backgroundImage': f'url(./assets/bg.jpg)',
        'backgroundRepeat': 'no-repeat',
        'backgroundSize': 'cover',
        'width': '100%',
    },
)


@app.callback(
    [Output("map", "srcDoc"),Output("sunlight_map", "srcDoc")],
    Input('submit', 'n_clicks'),
    State("input1", "value"),
)
def update_output(n_clicks, input1):
    if n_clicks:
        create_map(coords_by_adress(input1))
        # time.sleep()
        return open('map.html', 'r').read(), open('sunlight_map.html', 'r').read()
    else:
        return open('map.html', 'r').read(), open('sunlight_map.html', 'r').read()


if __name__ == '__main__':
    app.run_server(debug=True)

