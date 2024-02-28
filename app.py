from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import json
app=Flask(__name__,
          static_folder='public',
          static_url_path='/') # __name__: we are running the code from the current file 

app.secret_key='iamakey' # secret key for the session 

@app.route('/')
def index():
    return "hello hello m"

@app.route('/user/<username>')
def greet(username):
    return "hello"+username

@app.route('/getSum')
def getSum():
    print(request.headers.get('accept-language'))
    maxNumber=request.args.get("max", 10)
    maxNumber= int(maxNumber)
    result=0
    for n in range(1,maxNumber+1):
        print(n)
        result+=n
    return "sum:"+str(result)
@app.route('/getJson')
def getJson():
    return json.dumps({"name":"yenting", "age": 18})

@app.route('/redirect')
def redirectToGetJson():
    return redirect('/getJson')

@app.route('/dispalyTemplate')
def displayTemplate():
    return render_template("index.html")

@app.route('/hello')
def hello():
    name=request.args.get("name", "")
    session["username"]=name
    return "hello! "+name

@app.route('/talk')
def talk():
    name=session["username"]
    return "let's talk! "+name

@app.route('/show')
def show():
    input=request.args.get("input", "")
    return 'show me something: '+input

@app.route('/fate', methods=["POST"])
def fate():
    # number=int(request.args.get("number", 0))
    number=int(request.form["number"])
    if number % 2 == 0:
        return  render_template("fate.html", data="lucky")
    else:
        return render_template("fate.html", data="unlucky")

    




# update your port here
app.run(port=3000)