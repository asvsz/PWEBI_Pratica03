from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("paginas/home.html")

@app.route("/carrinho")
def carrinho():
    return render_template("paginas/carrinho.html")

@app.route("/sobre")
def sobre():
    return render_template("paginas/sobre.html")

@app.route("/perfil")
def perfil():
    return render_template("paginas/perfil.html")

@app.route("/combos")
def combos():
    return render_template("paginas/combos.html")

@app.route("/pizzas")
def pizzas():
    return render_template("paginas/pizzas.html")

@app.route("/bebidas")
def bebidas():
    return render_template("paginas/bebidas.html")

if __name__ == '__main__':
    app.run(debug=True)