from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
  nome = "Monica"
  dados = {"profissao":"Professora", "company":"Majete Edtech" }
  return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
  return render_template('contato.html')

@app.route('/projetos')
def projetos():
  return render_template('projetos.html')