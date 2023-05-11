from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("paginas/home.html")

@app.route("/carrinho")
def carrinho():
    return render_template("paginas/carrinho.html", titulo='Este é seu carrinho')

@app.route("/sobre")
def sobre():
    return render_template("paginas/sobre.html", titulo='Este é seu sobre')

@app.route("/perfil")
def perfil():
    return render_template("paginas/perfil.html", titulo='Este é seu perfil')

@app.route("/atendimento")
def atendimento():
    return render_template("paginas/atendimento.html", titulo='Este é seu atendimento')

if __name__ == '__main__':
    app.run(debug=True)