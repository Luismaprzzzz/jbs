from flask import Flask, render_template


app = Flask('name', static_url_path="/static")

@app.route("/")
def Pagina():
    return render_template("Page.html")

@app.route("/iniciar")
def iniciar():
    return render_template("Login.html")
@app.route("/Formulario")
def Formulario():
    return render_template("Registro.html")

@app.route("/Perfil")
def Perfil():
    return render_template("/Pantalla.html")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
