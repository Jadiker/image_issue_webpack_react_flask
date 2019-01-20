# server.py
import random
from flask import Flask, render_template, send_from_directory

# app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
# app = Flask(__name__, static_folder="../static") # TemplateNotFound (index.html)
# app = Flask(__name__, root_path="../static") # TemplateNotFound (index.html)
app = Flask(__name__, static_folder="../static", template_folder="../static")

def get_hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
    return random.choice(greeting_list)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return get_hello()
    
# @app.route("/public/<path:path>")
# def get_public_file(path):
#     print("getting something from public: {}".format(path))
#     return send_from_directory("public", path)
# 
# @app.route("/dist/<path:path>")
# def get_dist_file(path):
#     print("getting something from dist: {}".format(path))
#     return send_from_directory("./dist", path)
    
@app.route('/<path:path>')
def static_file(path):
    print("getting static file {}".format(path))
    if path.startswith("public/"):
        path = "dist/" + path
        print("in public folder; path changed to: {}".format(path))
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run()
