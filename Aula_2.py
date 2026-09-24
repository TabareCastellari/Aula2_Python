from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <h1>Meu primeiro Flask!</h1>
    <p>Bem-vindo ao meu site.</p>
    <a href="/usuario/Tabare">Ver usuário</a>
    """


@app.route("/usuario/<nome>")
def usuario(nome):
    return f"""
    <h1>Olá, {nome}!</h1>
    <p>Você está vendo uma página dinâmica.</p>
    <a href="/">Voltar</a>
    """


if __name__ == "__main__":
    app.run(debug=True)