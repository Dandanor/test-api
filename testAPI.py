from flask import Flask,request,jsonify,render_template

app = Flask(__name__)


class person:
    def __init__(self,fname,lname,ID):
        self.fname=fname
        self.lname=lname
        self.ID=ID

p1=person("Dan","Peleg",123)
p2=person("Ron","Peleg",456)
p3=person("Orit","Peleg",789)

people=[p1,p2,p3]

@app.route("/") #creating API endpoint for homepage
def home():
    return "One Piece"

@app.route("/greet") #creating API endpoint for /greet
def welcome():
    name=request.args.get("name","strawhat") #making a get request to the server, args is waiting for an argument in the URL to assign values to keys (in this instance a value to "name". "strawhat" is the default value)
    return f"hello {name}"

@app.route("/ID")
def IDjson():
    user_ID=request.args.get("ID")
    try:
        user_ID=int(user_ID) #checks for input format 
    except ValueError:
        return jsonify({'Error':'Invalid User Format'})
    for i in people:
        if i.ID==user_ID:
            return jsonify(i.fname,i.lname,i.ID)
    return jsonify({"error":"user ID not found"})

@app.route("/mail")
def CreateMail():
    user_namemail=request.args.get("fname")
    if not user_namemail:
        return jsonify({'Error':'No Value Provided'})
    try:
        user_namemail=str(user_namemail)
    except ValueError:
        return jsonify({"Error":"Invalid User Format"})
    user_namemail=user_namemail.capitalize()
    for j in people:
            if j.fname==user_namemail:
                return (f'{j.fname}@gmail.com')
    return jsonify ({"Error":"Name not in database"})


if __name__== "__main__": #checks if I am executing this file directly- if imported as a module the following line will not execute
    app.run(debug=True, port=3000) #activate the server
