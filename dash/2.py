import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
colors = {
    'background' : '#87D653',
    'text' : '#ff0033'
}

app.layout = html.Div(
    style = {'background' : colors['background']},
    children = [
        html.H1(
            children = 'Hello Dash',
            style = {
                'textAlign' : 'center',
                'color' : colors['text'],
            }
        ),
        html.Div(
            children = 'Dash hai ji', 
            style = {
                'textAlign' : 'center',
                'color' : colors['text']
            }
        ),

        dcc.Graph(
            id = 'eg2',

            figure = {
                'data': [
                    {'x' : [1,2,3], 'y' : [4,1,2], 'type' : 'bar', 'name' : 'Delhi'},
                ],
                'layout' :{
                    'plot_bgcolor' : colors['background'], 
                    'paper_bgcolor' : colors['background'],
                    'font': {
                        'color' : colors['text']
                    }
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug = True)