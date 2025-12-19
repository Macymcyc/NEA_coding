from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
    vowels=None
    name = request.form.get("name","unknown")
    if name != "unknown":
        vowels=0
        for letter in name:
            if letter in ["a","e","i","o","u"]:
                vowels+=1
        #determine singular or plural
        if vowels == 0 or vowels > 1:
            vowels = f"{vowels} vowels."
        else:
            vowels = f"{vowels} vowel."
        #turn text input into proprt noun
        name=name.title()

    return render_template("index.html", name=name, vowels=vowels) 

if __name__ == "__main__":
    app.run(debug=True)