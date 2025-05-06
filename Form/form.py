from flask import Flask, render_template,redirect, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "hi"

@app.route("/form")
def form():
    return render_template("form.html")


def db(data):
    
    with open('db.txt',mode='a') as dbase:
        
        #Name = data["username"]
        #Email = data["email"]
        #Password = data["password"]
        file = dbase.write(f"\n{str(data)}")
        


@app.route("/submit_form", methods =  ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        name = data.get("username")
        db(data)
        print(data)
        return f"Thank You, {name}"
    else:
        return "Error"