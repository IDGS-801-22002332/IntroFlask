from flask import Flask, render_template, request

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


@app.route("/OperasBas")
def operaciones():
    return render_template("OperasBas.html")

@app.route("/resultado",methods=["GET","POST"])
def result():
    num1=request.form.get("num1")
    num2=request.form.get("num2")
    return "La multiplicacion de {} x {} es {}".format(num1,num2,str(int(num1) * int(num2)))


@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    resultado = ""  
    if request.method == "POST":
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            operacion = request.form["opcion"]  

            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                resultado = num1 / num2 

    return render_template("OperasBas.html", resultado=resultado)



if __name__ =="__main__":
    app.run(debug=True, port=3000) #Debug hace un reload