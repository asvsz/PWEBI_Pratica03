from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", titulo='Amanda')

@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html", titulo='Este é seu carrinho')


if __name__ == '__main__':
    app.run(debug=True)