from flask import Flask, render_template

app=Flask(__name__)


@app.route("/hola")
def hola():
    return "<h1>Hola mundo hola</h1>"

@app.route("/user/<string:usuario>")
def user(usuario):
    return f"<h1<!Hola,{usuario}</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola, {username} Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}<h1>"

@app.route("/aperas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="name">ape Paterno:</label>
        <input type="text" id="paterno" name="name" required>
    </form>
        '''

@app.route("/")
def ejemplo1():
    titulo="IDGS801"
    lista=["Pedro","Juan","Luis"]
    return render_template('ejemplo.html', titulo=titulo, lista=lista)


if __name__ =="__main__":
    app.run(debug=True, port=3000) #Debug hace un reload