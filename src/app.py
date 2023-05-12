from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def home():
    nav=['href=/trabalhos','Trabalhos',' ','Sobre mim', 'href=/contatos','Contato']
    title='Bem vindo!!'
    return render_template("index.html", title=title, nav=nav)

@app.route("/index")
def index():
    nav=['href=/trabalhos','Trabalhos',' ','Sobre mim', 'href=/contatos','Contato']
    title='Quem Sou'
    return render_template("index.html", title=title, nav=nav)

@app.route("/trabalhos")
def trabalhos():
    nav=['href=/index','Sobre mim', ' ','Trabalhos','href=/contatos','Contato']
    title="Trabalhos"
    return render_template("trabalhos.html", title=title, nav=nav)

@app.route("/contatos")
def contatos():
    nav=['href=/trabalhos','Trabalhos', '', 'Contato','href=/index','Sobre mim']
    title='Contatos'
    return render_template("contatos.html", title=title, nav=nav)