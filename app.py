from flask import Flask

app = Flask(_name_)

menu = """
<a href="/">Página Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Olá, eu sou Ananda! Bem vinda ao meu site teste!"

app.route("/sobre")
def sobre():
  return menu +  "Este é meu site para a aula de Algoritmos de Automação"

app.route("/contato")
def contato():
  return menu + "meu contato é anandarduarte@gmail.com"
  
 
