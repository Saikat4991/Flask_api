## Flask Introduction, Application, Open Link Flask, App Routing Flask Url Building Flask


from flask import Flask # import flask
from flask import request
# OBJECT
app = Flask(__name__) # name: parameter

# FUNCTION
@app.route("/")
def hello_world():
    return "Hello, World!" #to access : https://mango-mechanic-isuao.pwskills.app:5000/

@app.route("/hello1")
def hello_world1():
    return "Hello, World!1" #to access : https://mango-mechanic-isuao.pwskills.app:5000/hello1

@app.route("/hello2")
def hello_world2():
    return "Hello, World!2" #to access : https://mango-mechanic-isuao.pwskills.app:5000/hello2

@app.route('/test_fun')
def test():
    a = 5+6
    return "this is my 1st fun in flask {}".format(a) #https://mango-mechanic-isuao.pwskills.app:5000/test_fun


@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data) #https://mango-mechanic-isuao.pwskills.app:5000/input_url?x=data science

if __name__=="__main__":
    app.run(host="0.0.0.0")
