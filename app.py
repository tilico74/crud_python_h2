from flask import Flask, render_template, request, redirect
import jpype
import jaydebeapi
import os

app = Flask(__name__)

h2_jar_path = os.path.abspath("lib/h2-2.3.232.jar")

if not jpype.isJVMStarted():
    jpype.startJVM(jpype.getDefaultJVMPath(), f"-Djava.class.path={h2_jar_path}")

def get_connection():
    return jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:./banco/crud_db",
        ["sa",""]
    )

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cliente (id IDENTITY PRIMARY KEY, nome VARCHAR(100));")
    cursor.execute("SELECT * FROM cliente;")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", clientes=clientes)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome_cliente = request.form['nome'].title()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cliente (nome) VALUES (?);", (nome_cliente,))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Erro ao inserir cliente: {e}"
    return redirect("/")

@app.route("/excluir/<int:id>")
def excluir(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE id= ?", (id,))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Erro ao deletar cliente: {e}"
    return redirect("/")

@app.route("/alterar/<int:id>")
def alterar(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id = ?", (id,))
        cliente = cursor.fetchone()
        cursor.close()
        conn.close()

        if cliente:
            return render_template("alterar.html", cliente=cliente)
        else:
            return f"Cliente com Id {id} não encontrado"
    except Exception as e:
        return f"Erro ao buscar cliente para eidção: {e}"

@app.route("/atualizar", methods = ["POST"])
def atualizar():
    id_cliente      = request.form['id']
    nome_cliente    = request.form['nome'].title()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE cliente SET nome= ?  WHERE id = ?", (nome_cliente, id_cliente))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Erro ao atualizar cliente: {e}"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)