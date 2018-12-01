import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

df_names = pd.read_csv('OH.TXT', names=[
                       'state', 'sex', 'year', 'name', 'occurance'])

app = dash.Dash(__name__)

app.layout = html.Div([dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i, "deletable": True}
             for i in df_names.columns],
    data=df_names.to_dict("rows"),
    filtering=True,

), html.Div(id='datatable-filter-container'),

dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': {year.year for year in data},
                    'y': df_names['occurance'], 'type': 'line', 'name': 'Occurance'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
])


@app.callback(
    Output('datatable-filter-container', 'children'),
    [Input('table', "data")])
def update_graph(rows):
    if rows is None:
        dff=df_names
    else:
        dff=pd.DataFrame(rows)

    return html.Div()


if __name__ == '__main__':
    app.run_server(debug=True)
