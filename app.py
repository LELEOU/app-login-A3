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
    erro = None
    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip()
        telefone = request.form["telefone"].strip()
        if len(nome) < 3 or len(email) < 10 or len(telefone) < 9:
            erro = "Preencha todos os campos corretamente!"
        else:
            cliente = {
                "nome": nome,
                "email": email,
                "telefone": telefone
            }
            clientes.append(cliente)
            return redirect(url_for('index')) # Evita duplicar a droga dos dados salvos no formulário
    return render_template_string(HTML + """
    {% if erro %}
      <p style="color:red;">{{ erro }}</p>
    {% endif %}
    """, clientes=clientes, erro=erro)

@app.route("/limpar", methods=["GET"]) # aqui limpa o formulari ora nao ficar cheio de coisas
def limpar():
    clientes.clear()
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run()
