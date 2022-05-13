import dash_bootstrap_components as dbc
from dash import dash_table
from dash import Dash, dcc, html, Input, Output, callback, State
import plotly.express as px
import plotly.figure_factory as ff
import plotly.io as pio
import pandas as pd
import dash_daq as daq
from wordcloud import WordCloud

wc = WordCloud(width=1500, height=700, min_font_size=10, background_color='gray')

df = pd.read_csv('spam.csv', encoding='cp1252')
df2 = pd.read_csv('transformed_df.csv')

options = ['Alpha_letters', 'Len_Of_Words', 'No_of_Chars', 'No_of_Sentences', 'No_of_digits', 'Num_chars',
           'Special_chars']
graph = dbc.Row([
    dbc.Col([
        html.H1('Exploratory Data Analysis',className='text-danger'),
        # About Data
        html.Div(id='null'),
        html.H4('Dataset Statistics'),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Total Records',className='text-warning'),
                        html.H1(id='records')
                    ]),
                ],color="primary"),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Total Features',className='text-warning'),
                        html.H1(id='features')
                    ]),
                ],color="primary"),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Target Labels',className='text-warning'),
                        html.H1(id='labels')
                    ]),
                ],color="primary"),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Imbalanced Data?',className='text-warning'),
                        html.H1(id='imbalance')
                    ]),
                ],color="primary"),
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.Row([
                        dbc.Label('Null Data',className='text-warning'),
                        html.H1(id='missing')
                    ]),
                ],color="primary"),
            ]),
        ]),

        # Data Table
        html.Br(),
        html.H2("Tabular Data", className='fs-5'),
        dcc.RadioItems(['Original Data', 'Transformed Data'], 'Original Data',inputStyle={"margin-left": "10px"}, id='table_radio'),
        html.Br(),
        dbc.Row(id='display_table'),
        # html.Br(),
        html.Br(),
        html.H2("Pie Chart: Target Data", className='fs-5'),
        dcc.Graph(id='pie'),

        html.Br(),
        html.Br(),

        # Histogram
        dbc.Label("Histogram", className='fs-5'),
        html.Br(),
        dcc.RadioItems(options, 'Alpha_letters',inputStyle={"margin-left": "10px"},id='data_radio'),
        html.Br(),
        dcc.Graph(id='histogram'),

        # KDE
        # html.Br(),
        html.Br(),
        dbc.Label("KDE Plot", className='fs-5'),
        dcc.RadioItems(['All', 'Spam', 'Not Spam'], 'All', inputStyle={"margin-left": "10px"},id='kde_filter'),
        dcc.Dropdown(options, ['Alpha_letters', 'Len_Of_Words'], id='kde_drop', multi=True,
                     style={'color': 'black'}),
        html.Br(),
        dcc.Graph(id='kde'),

        # scatter plot
        html.Br(),
        html.Br(),
        dbc.Label("Scatter Plot", className='fs-5'),

        dbc.Row([
            dbc.Col([
                html.Header('X- Axis'),
                dcc.Dropdown(options, 'No_of_Chars', id='xscat_drop', style={'color': 'black'})]),
            dbc.Col([
                html.Header('Y- Axis'),
                dcc.Dropdown(
                    options,
                    'Len_Of_Words', id='yscat_drop', style={'color': 'black'})]),

            dbc.Col([
                html.Header('Size'),
                dcc.Dropdown(
                    options,
                    'No_of_Sentences', id='size_scat_drop', style={'color': 'black'})]),
            dbc.Col([
                html.Header('Marginal_X'),
                dcc.Dropdown(['rug', 'box', 'violin', 'histogram'], None,
                             id='xmarg_drop', style={'color': 'black'})]),
            dbc.Col([
                html.Header('Marginal_Y'),
                dcc.Dropdown(['rug', 'box', 'violin', 'histogram'], None,
                             id='ymarg_drop', style={'color': 'black'})]),
            dbc.Col([
                daq.BooleanSwitch(
                    on=True, id='legend',
                    label="Legend", color="#9B51E0",
                    labelPosition="top")], width='auto'),
            dbc.Col([
                daq.BooleanSwitch(
                    on=True, id='tradeline',
                    label="Tradeline", color="#9B51E0",
                    labelPosition="top")], width='auto'),

        ]),

        html.Br(),
        dcc.Graph(id='scat_plot'),
        # Boxplot
        html.Br(),
        html.Br(),
        dbc.Label("Box Plot", className='fs-5'),
        dbc.Row([
            dbc.Col([
                dbc.Label('Features'),
                dcc.Dropdown(options, 'Alpha_letters', id='box_drop', multi=True,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                daq.BooleanSwitch(on=True, id='box_leg', label="Color", color="#9B51E0", labelPosition="top"),
            ], width='auto')
        ]),
        html.Br(),
        dcc.Graph(id='boxplot'),
# wordmap
        html.Br(),
        html.Br(),
        dbc.Label('WordMap of most used words'),
        dcc.RadioItems(['All', 'Spam', 'Not Spam'], 'All',inputStyle={"margin-left": "10px"},id='word_radio', className='fs-5'),
        html.Br(),
        dcc.Graph(id='wordmap'),

        # ECDF
        html.Br(),
        html.Br(),
        dbc.Label("Empirical Cumulative Distribution Plot", className='fs-5'),
        dbc.Row([
            dbc.Col([
                dbc.Label('Features'),
                dcc.Dropdown(options, 'Alpha_letters', id='ecdf_drop',
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                daq.BooleanSwitch(on=True, id='ecdf_leg', label="Color", color="#9B51E0", labelPosition="top"),
            ], width='auto')
        ]),
        html.Br(),
        dcc.Graph(id='ecdf'),

        # 3-D Scatter
        html.Br(),
        html.Br(),
        dbc.Label("3D Scatter Plot", className='fs-5'),
        dbc.Row([
            dbc.Col([
                dbc.Label('X-Axis'),
                dcc.Dropdown(options, 'Alpha_letters', id='x3d_drop', multi=False,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                dbc.Label('X-Axis'),
                dcc.Dropdown(options, 'Len_Of_Words', id='y3d_drop', multi=False,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                dbc.Label('X-Axis'),
                dcc.Dropdown(options, 'No_of_Chars', id='z3d_drop', multi=False,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                daq.BooleanSwitch(on=True, id='s_leg', label="Color", color="#9B51E0", labelPosition="top"),
            ], width='auto')
        ]),
        html.Br(),
        dcc.Graph(id='scatter3d'),

        # Polar Scatter
        html.Br(),
        html.Br(),
        dbc.Label("Polar Scatter Plot", className='fs-5'),
        dbc.Row([
            dbc.Col([
                dbc.Label('Value'),
                dcc.Dropdown(options, 'Alpha_letters', id='polar_drop', multi=False,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                dbc.Label('Theta'),
                dcc.Dropdown(options, 'Len_Of_Words', id='theta_drop', multi=False,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                dbc.Label('Size'),
                dcc.Dropdown(options, 'No_of_Chars', id='size_drop', multi=False,
                             style={'color': 'black'}),
            ]),
            dbc.Col([
                daq.BooleanSwitch(on=True, id='polar_leg', label="Color", color="#9B51E0", labelPosition="top"),
            ], width='auto')
        ]),
        html.Br(),
        dcc.Graph(id='polar_scatter'),

    ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
])


# display about data
@callback(
    Output('records', 'children'),
    Output('features', 'children'),
    Output('labels', 'children'),
    Output('imbalance', 'children'),
    Output('missing', 'children'),
    Output('pie', 'figure'),
    Input('null', 'children')
)
def update_records(x):
    fig = px.pie(df2, values=df2['Target'].value_counts().values, names=df2['Target'].value_counts().index,
                 template='plotly_dark')
    return df.shape[0], df.shape[1], df['Msg_Type'].nunique(), 'Yes', df.isnull().sum().sum(), fig


#  diplay table data
@callback(
    Output('display_table', 'children'),
    Input('table_radio', 'value')
)
def update(x):
    if x == 'Original Data':
        data1 = dash_table.DataTable(data=df.to_dict('records'), columns=[{'id': c, 'name': c} for c in df.columns],
                                     style_data={'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px',
                                                 'color': 'black', 'backgroundColor': 'white'},
                                     style_cell_conditional=[{'textAlign': 'left'}],
                                     style_header={'backgroundColor': 'rgb(74, 90, 232)', 'color': 'black',
                                                   'fontWeight': 'bold'}, page_size=5, )
        # print("Original data shown")
        return data1
    else:
        data2 = dash_table.DataTable(data=df2.to_dict('records'), columns=[{'id': c, 'name': c} for c in df2.columns],
                                     style_data={'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px',
                                                 'color': 'black', 'backgroundColor': 'white'},
                                     style_cell_conditional=[{'textAlign': 'center'}],
                                     style_header={'backgroundColor': 'rgb(74, 90, 232)', 'color': 'black',
                                                   'fontWeight': 'bold'}, page_size=5, )
        return data2


# display histogram
@callback(Output('histogram', 'figure'),
          Input('data_radio', 'value'))
def update_histogram(data_radio):
    fig = px.histogram(df2, x=data_radio, color='Target', labels={'x': data_radio, 'color': 'Msg type'},
                       template='plotly_dark')
    return fig


# display kde
@callback(Output('kde', 'figure'),
          Input('kde_filter', 'value'),
          Input('kde_drop', 'value'),
          )
def update_kde(kde_filter, kde_drop):
    kde_data = df2
    if kde_filter == 'Spam':
        kde_data = df2[df2['Target'] == 1]
    elif kde_filter == 'Not Spam':
        kde_data = df2[df2['Target'] == 0]
    data = []
    for i in kde_drop:
        data.append(kde_data[f'{i}'])
    pio.templates.default = "plotly_dark"
    fig = ff.create_distplot(data, kde_drop, show_hist=False)
    fig.update_layout(title_text='KDE Plot', title_x=0.5)
    return fig


# display scatter plot
@callback(
    Output('scat_plot', 'figure'),
    Input('xscat_drop', 'value'),
    Input('yscat_drop', 'value'),
    Input('size_scat_drop', 'value'),
    Input('xmarg_drop', 'value'),
    Input('ymarg_drop', 'value'),
    Input('legend', 'on'),
    Input('tradeline', 'on'),
)
def update_scatterplot(x, y, size, marg_x, marg_y, legend, td):
    lgd = None
    tradeline = None
    if legend != False:
        lgd = df2['Target'].astype(str)

    if td != False:
        tradeline = 'ols'
    fig = px.scatter(df2, x=x, y=y, color=lgd, trendline=tradeline,
                     size=size, marginal_x=marg_x, marginal_y=marg_y, template='plotly_dark',
                     labels={'color': 'Target'})
    return fig


@callback(
    Output('boxplot', 'figure'),
    Input('box_leg', 'on'),
    Input('box_drop', 'value'),
)
def update_box(x, y):
    leg = None
    if x:
        leg = df2['Target'].astype(str)
    fig = px.box(df2, y=y, color=leg, template='plotly_dark')
    return fig


@callback(
    Output('ecdf', 'figure'),
    Input('ecdf_leg', 'on'),
    Input('ecdf_drop', 'value'),
)
def update_ecdf(x, y):
    leg = None
    if x:
        leg = df2['Target'].astype(str)
    fig = px.ecdf(df2, x=y, color=leg, ecdfnorm=None, template='plotly_dark')
    return fig


@callback(
    Output('scatter3d', 'figure'),
    Input('s_leg', 'on'),
    Input('x3d_drop', 'value'),
    Input('y3d_drop', 'value'),
    Input('z3d_drop', 'value'),
)
def update_ecdf(s, x, y, z):
    leg = None
    if s:
        leg = df2['Target'].astype(str)
    fig = px.scatter_3d(df2, x=x, y=y, z=z, color=leg, template='plotly_dark')
    return fig


@callback(
    Output('polar_scatter', 'figure'),
    Input('polar_leg', 'on'),
    Input('polar_drop', 'value'),
    Input('theta_drop', 'value'),
    Input('size_drop', 'value'),
)
def update_ecdf(s, x, y, z):
    leg = None
    if s:
        leg = df2['Target'].astype(str)
    fig = px.scatter_polar(df2, r=x, theta=y, symbol='Target',
                           color=leg, size=z, template='plotly_dark'
                           )
    return fig


@callback(
    Output('wordmap', 'figure'),
    Input('word_radio', 'value')
)
def update_wordmap(x):
    if x == 'All':
        spam_wc = wc.generate(df2['Trf_Msg'].str.cat(sep=' '))  # object of words
        fig = px.imshow(spam_wc,template='plotly_dark')
        return fig
    elif x == 'Spam':
        spam_wc = wc.generate(df2[df2['Target'] == 1]['Trf_Msg'].str.cat(sep=' '))  # object of words
        fig = px.imshow(spam_wc,template='plotly_dark')
        return fig
    else:
        spam_wc = wc.generate(df2[df2['Target'] == 0]['Trf_Msg'].str.cat(sep=' '))  # object of words
        fig = px.imshow(spam_wc,template='plotly_dark')
        return fig
