from flask import Flask, render_template

app = Flask(__name__)


# route
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/users/<nome_users>")
def users(nome_users):
    return render_template("users.html",nome_users=nome_users)


if __name__=="__main__":
 app.run(debug=True)