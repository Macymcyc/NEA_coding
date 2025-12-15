from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/",method=["GET","POST"])
#@app.route("/<world>")

def index():#word="Welcome"
    name = request.args.form("name","unknown")
    return render_template("index.html", name=name) #f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)