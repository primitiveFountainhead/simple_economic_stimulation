import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children =[
    html.H1(children = 'Hello Dash'),
    html.Div(children = '''Dash Framework'''),
    dcc.Graph(
    id = 'eg-graph', 
    figure = {
        'data': [
            {'x' : [1,2,3], 'y' : [4,1,2], 'type' : 'bar', 'name' : 'Farzeenkaka'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Mumbai'},
        ],
        'layout' : {
            'title' : 'Dash Visual'
        }
    }
)])



if __name__ == '__main__':
   app.run_server(debug=True)