'''An example application to demonstrate Variable Rules in Routing
How to use it?

Step 1: run the application
Step 2: in the url: add '/cristobal' and you will see how the app changes

'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    '''View for the Home page of the website.'''
    return 'Welcome to the HomePage!'


@app.route('/<my_name>')
def greatings(my_name):
    '''View function to greet the user by name.'''
    return 'Welcome '+ my_name +'!'


if __name__ == '__main__':
    app.run(debug=True, port=3000)