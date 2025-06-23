from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
clientes = []

HTML = """
<!doctype html>
<title>Cadastro de Clientes</title>
<h2>Cadastro de Clientes</h2>
<form method="POST">
  Nome: <input type="text" name="nome"><br>
  Email: <input type="email" name="email"><br>
  Telefone: <input type="text" name="telefone"><br>
  <input type="submit" value="Salvar">
</form>

<h3>Clientes Cadastrados:</h3>
<ul>
{% for c in clientes %}
  <li>{{ c['nome'] }} - {{ c['email'] }} - {{ c['telefone'] }}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cliente = {
            "nome": request.form["nome"],
            "email": request.form["email"],
            "telefone": request.form["telefone"]
        }
        clientes.append(cliente)
        return redirect(url_for('index'))  # Evita duplicar a droga dos dados salvos no formulário
    return render_template_string(HTML, clientes=clientes)

if __name__ == "__main__":
    app.run()
