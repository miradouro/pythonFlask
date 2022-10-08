from flask import Flask, render_template, request
import urllib.request
import json


app = Flask(__name__)

frutas = []
registros = []


@app.route('/', methods=["GET", "POST"])
def principal():
    # frutas = ["Morango", "Uva", "laranja", "Mamao", "Pera", "Melao", "Abacaxi"]
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get('nota'):
            registros.append({"aluno": request.form.get('aluno'),
                              "nota": request.form.get('nota')})
    return render_template("sobre.html", registros=registros)


@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=9064c6b20e001de09c9440faa6d1f822"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=9064c6b20e001de09c9440faa6d1f822"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=9064c6b20e001de09c9440faa6d1f822"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2014&api_key=9064c6b20e001de09c9440faa6d1f822"
    elif propriedade == 'bradpitt':
        url = "https://api.themoviedb.org/3/discover/movie?with_people=287,819&sort_by=vote_average.desc&api_key=9064c6b20e001de09c9440faa6d1f822"

    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])


if __name__ == '__main__':
    app.run(debug=True)

