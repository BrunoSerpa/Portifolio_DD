from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def home():
    nav=['href=/trabalhos','Trabalhos',' ','Sobre mim', 'href=/contatos','Contato']
    title='Bem vindo!!'
    return render_template("index.html", title=title, nav=nav, ensinoJson=fileJson('ensino'))

@app.route("/sobre")
def sobre():
    nav=['href=/trabalhos','Trabalhos',' ','Sobre mim', 'href=/contatos','Contato']
    title='Quem Sou'
    return render_template("index.html", title=title, nav=nav, ensinoJson=fileJson('ensino'))

@app.route("/trabalhos")
def trabalhos():
    nav=['href=/sobre','Sobre mim', ' ','Trabalhos','href=/contatos','Contato']
    title="Trabalhos"
    return render_template("trabalhos.html", title=title, nav=nav, trabalhoJson=fileJson('trabalhos'), voluntariadoJson=fileJson('voluntariados'), projetoJson=fileJson('projetos'))

@app.route("/contatos")
def contatos():
    nav=['href=/trabalhos','Trabalhos', '', 'Contato','href=/sobre','Sobre mim']
    title='Contatos'
    return render_template("contatos.html", title=title, nav=nav)

import json
def fileJson(title):
    with open(f"static/json/{title}.json") as openFile:
        jsonFile=openFile.read()
        return json.loads(jsonFile.encode("latin_1").decode("utf-8"))