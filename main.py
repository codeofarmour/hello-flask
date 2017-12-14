from flask import Flask

app = Flask(__name__) # app is the object, __name__ is the placeholder; whatever's in @app.route("/") will be passed to (__name__)
app.config['DEBUG'] = True

@app.route("/") # decorator/notation - tells application that this is the route
def index(): # named "index" bc it's the name of the page we're displaying, e.g. index.html. This tells app to go to decorator route
    return "Hello World"
'''
@app.route("/about")
def about():
    return "World"
'''
app.run()