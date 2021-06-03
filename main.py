from flask import Flask, Blueprint, redirect, url_for, render_template, request

#app = Blueprint("app", __name__, static_folder ="static", template_folder= "templates")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)