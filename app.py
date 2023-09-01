from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask('app')
app.secret_key = "CHANGE ME"

@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        #getting username and password 
        name = request.form["username"]
        password = request.form["password"]
        print(name)
    
    return render_template("index.html")

app.run(host='0.0.0.0', port=8080)