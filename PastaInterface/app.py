from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])



def home():
    mensagem = None

    if request.method == "POST":
        nome = request.form.get("nome")
        if nome:
            mensagem = f"Olá, {nome}! Seja bem-vindo ao site!"

    return render_template("index.html", mensagem=mensagem)



if __name__ == "__main__":
    app.run(debug=True)