from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def home():
    title='Bem vindo!!'
    return render_template("index.html", title=title)

@app.route("/index")
def index():
    title='Quem Sou'
    return render_template("index.html", title=title)

@app.route("/trabalhos")
def quemsomos():
    title="Trabalhos"
    return render_template("trabalhos.html", title=title)

@app.route("/contatos")
def contatos():
    title='Contatos'
    return render_template("contatos.html", title=title)