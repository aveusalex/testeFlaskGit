from flask import Flask, render_template, request


app = Flask(__name__, template_folder="view")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/autentica", methods=['POST'])
def


if __name__ == "__main__":
    app.run()