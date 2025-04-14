from flask import Flask, render_template_string

app = Flask(__name__)

# Layout base simples
base_html = """
<!doctype html>
<html>
<head>
    <title>{{title}}</title>
    <style>
        nav { background: #f0f0f0; padding: 10px; }
        nav a { margin-right: 15px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/sobre">Sobre</a>
        <a href="/contatos">Contatos</a>
    </nav>
    <h1>{{heading}}</h1>
    <p>{{content}}</p>
</body>
</html>
"""

# Rotas principais
@app.route("/")
def home():
    return render_template_string(
        base_html,
        title="Página Inicial",
        heading="Bem-vindo!",
        content="Esta é a página inicial do site."
    )

@app.route("/sobre")
def sobre():
    return render_template_string(
        base_html,
        title="Sobre Nós",
        heading="Sobre",
        content="Informações sobre nossa empresa."
    )

@app.route("/contatos")
def contatos():
    return render_template_string(
        base_html,
        title="Contatos",
        heading="Fale Conosco",
        content="Email: contato@exemplo.com | Tel: (11) 1234-5678"
    )

# Rota dinâmica simples
@app.route("/user/<nome>")
def usuario(nome):
    return render_template_string(
        base_html,
        title=f"Página de {nome}",
        heading=f"Olá, {nome}!",
        content=f"Esta é a página pessoal de {nome}."
    )