from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    nav=['href=/trabalhos','Trabalhos',' ','Home', 'href=/contatos','Contato']
    title='Bem vindo!!'
    return render_template("index.html", title=title, nav=nav, ensinoJson=fileJson('ensino'))

@app.route("/sobre")
def sobre():
    nav=['href=/trabalhos','Trabalhos',' ','Home', 'href=/contatos','Contato']
    title='Quem Sou'
    return render_template("index.html", title=title, nav=nav, ensinoJson=fileJson('ensino'), hobbiesJson=fileJson('hobbie'))

@app.route("/trabalhos")
def trabalhos():
    nav=['href=/sobre','Home', ' ','Trabalhos','href=/contatos','Contato']
    title="Trabalhos"
    return render_template("trabalhos.html", title=title, nav=nav, trabalhoJson=fileJson('trabalhos'), voluntariadoJson=fileJson('voluntariados'), projetoAPIJson=fileJson('projetosAPI'), projetoJson=fileJson('projetos'))

@app.route("/contatos")
def contatos():
    nav=['href=/trabalhos','Home', '', 'Contato','href=/sobre','Sobre mim']
    title='Contatos'
    return render_template("contatos.html", title=title, nav=nav)

import json
import codecs

def fileJson(title):
    with codecs.open(f"./src/static/json/{title}.json", "r", encoding="latin_1") as jsonFile:
        content = jsonFile.read()
        decoded_content = content.encode("latin_1").decode("utf-8")
    return json.loads(decoded_content)