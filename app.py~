from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hi():
    return render_template('form.html')

@app.route("/auth")
def process():
    person = request.args["Name"]
    pref = request.args["Type"]
    reqmeth = request.method
    return render_template('auth.html', name = person, fry = pref, method = reqmeth)

if __name__ == "__main__":
    app.debug = True
    app.run()
