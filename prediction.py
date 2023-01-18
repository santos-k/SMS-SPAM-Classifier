import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback, State
import pickle
import nltk
nltk.download('wordnet')
nltk.download('punkt')

transform_text = pickle.load(open('transform_text.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def text_prep(text):
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    text = text.lower()
    # tokenization
    text = nltk.word_tokenize(text)
    # removing special chars
    ls = []
    for i in text:
        if i.isalnum():
            ls.append(i)
    ls2 = []
    # remove stopwords
    for i in ls:
        if i not in stopwords.words('english'):
            ls2.append(i)
    ls3 = []
    # apply stemming
    for i in ls2:
        ls3.append(ps.stem(i))

    return " ".join(ls3)


# Spam Check div

spam_check_div = dbc.Row([
    dbc.Col([
        dbc.Label("Check Spam SMS/Email", className='fs-5'),
        dbc.Textarea(placeholder='Enter your message or email here', id='msg_input', size='lg'),
        html.Br(),
        dbc.Button('Check', id='btn', n_clicks=0),
        html.Br(),
        html.Br(),
        html.Div(id='result')
    ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
])


@callback(
    Output('result', 'children'),
    Input('btn', 'n_clicks'),
    State('msg_input', 'value')
)
def result(x, y):
    if x == 0:
        return ''
    else:
        if y is None or y == '':
            return 'Pls enter message first'
        else:
            if len(y) > 10:
                try:
                    prep_msg = text_prep(y)
                    trf_msg = transform_text.transform([prep_msg]).toarray()
                    pred = model.predict(trf_msg)
                    if pred == 0:
                        return 'This is not SPAM'
                    else:
                        return 'This is SPAM'
                except Exception as e:
                    return e
            else:
                return 'Oops..!! Input must be greater then 10 characters.'

