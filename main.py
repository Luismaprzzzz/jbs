from flask import Flask, render_template


app = Flask('__name__')

@app.route("/")
def Page():
    return render_template("/Page.html")

@app.route("/iniciar")
def iniciar():
    return render_template("/Login.html")
@app.route("/Formulario")
def Formulario():
    return render_template("/Registro.html")

@app.route("/Perfil")
def Perfil():
    return render_template("/Pantalla.html")


if __name__ == '__main__':
    app.run(debug=True)
