from chalice import Chalice

app = Chalice(app_name='chalice_example')

@app.route('/')
def index():
    '''
    The view function returns {"hello": "world"}, whenever you make an HTTP GET request to "/"
    '''
    return {'hello': 'world'}


@app.route('/hello/{name}')
def hello_name(name):
    '''
    Returns a greeting with your name when you call "/hello/james"
    '''
    return {'hello': name}

@app.route('/users', methods=['POST'])
def create_user():
    '''
    Returns the user as JSON, when you post a user JSON structure
    in the post request. 
    '''
    user_as_json = app.current_request.json_body
    return {'user': user_as_json}

