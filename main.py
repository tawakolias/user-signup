from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login.html',error = "")

@app.route("/welcome", methods = ['POST'])
def sign():
    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    if not username:
        error = "Username is Empty"
        return render_template('login.html', error = error)
    elif password != verify:
        error = "Password is not matching"
        return render_template('login.html', error = error)
    else:
        return render_template('welcome.html', username = username)
        





app.run()