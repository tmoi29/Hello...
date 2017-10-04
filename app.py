#Team Hello...
#Tiffany Moi and Alessandro Cauthon
#SoftDev1 pd7
#HW07 -- Do I Know You?
#2017-10-05
from flask import Flask, render_template, request, session
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def hi():
    return render_template('login.html', message = "")

@app.route("/auth", methods = ["POST"])
def process():
    person = request.form["User"]
    pw = request.form["Pass"]
    reqmeth = request.method
    if (person == "KenM"):
        if (pw == "1234"):  
            session["username"] = person
            return render_template('welcome.html', name = person, method = reqmeth)
        else:
            return render_template('login.html', message = "Invalid Password")
    else:
        return render_template('login.html', message = "Invalid Username")

@app.route("/logout")
def logout():
    session.pop("username")
    return render_template('login.html', message = "Successfully logged out!")

if __name__ == "__main__":
    app.debug = True
    app.run()
