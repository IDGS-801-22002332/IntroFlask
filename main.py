from flask import Flask, render_template, request
from datetime import datetime
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash

app=Flask(__name__)
app.secret_key="este es una clave secreta"
csr=CSRFProtect()

@app.errorhandler(404)
def page_notfound(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    g.user="Mario"
    print("beforer1")
    
@app.after_request
def after_request(response):
    print("after1")
    return response

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
    nombre='None'
    titulo="IDGS801"
    lista=["Pedro","Juan","Luis"]
    nombre=g.user
    print("Index 2 {}".format(g.user))
    return render_template('ejemplo.html', titulo=titulo, nombre=nombre,lista=lista)


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

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    mat=0
    nom=''
    ape=''
    cor=''
    alumno_clas=forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        cor = alumno_clas.correo.data
        
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("Alumnos.html",form=alumno_clas,mat=mat,nom=nom,ape=ape,cor=cor)

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    total_pagar = None
    nombre = ""
    mensaje = ""
    
    if request.method == "POST":
        nombre = request.form["nombre"]
        cant_personas = int(request.form["cant_personas"])
        cant_boletos = int(request.form["cant_boletos"])
        cineco = request.form["cineco"]
        precio_boleto = 12
        
        cant_maxima = cant_personas * 7
        
        if cant_boletos > cant_maxima:
            mensaje = f"No puedes comprar más de {cant_maxima} boletos. Intenta de nuevo."
        else:
            total_pagar = cant_boletos * precio_boleto
            
            if cant_boletos > 5:
                total_pagar *= 0.85  
            
            if cineco == "si":
                total_pagar *= 0.90  
                
    return render_template("Cinepolis.html", total_pagar=total_pagar, nombre=nombre, mensaje=mensaje)

def calcularEdad(anio):
    anioActual = datetime.now().year
    return anioActual - anio

def obtenerSigno(dia, mes):
    signos = [
        ("Capricornio", 12, 22, 1, 19),
        ("Acuario", 1, 20, 2, 18),
        ("Piscis", 2, 19, 3, 20),
        ("Aries", 3, 21, 4, 19),
        ("Tauro", 4, 20, 5, 20),
        ("Géminis", 5, 21, 6, 20),
        ("Cáncer", 6, 21, 7, 22),
        ("Leo", 7, 23, 8, 22),
        ("Virgo", 8, 23, 9, 22),
        ("Libra", 9, 23, 10, 22),
        ("Escorpio", 10, 23, 11, 21),
        ("Sagitario", 11, 22, 12, 21),
    ]
    for signo, mesInicio, diaInicio, mesFin, diaFin in signos:
        if (mes == mesInicio and dia >= diaInicio) or (mes == mesFin and dia <= diaFin):
            return signo
    return "Desconocido"

def animalChino(anio):
    animales = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra"]
    return animales[anio % 12]

def imagen(animal):
    imagenes = {
        "Mono": "mono.webp",
        "Gallo": "gallo.webp",
        "Perro": "perro.webp",
        "Cerdo": "cerdo.webp",
        "Rata": "rata.webp",
        "Buey": "buey.webp",
        "Tigre": "tigre.webp",
        "Conejo": "conejo.webp",
        "Dragón": "dragon.webp",
        "Serpiente": "serpiente.webp",
        "Caballo": "caballo.webp",
        "Cabra": "cabra.webp"
    }
    return imagenes.get(animal, "default.png") 

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    signo = None
    animal = None
    edad = None
    mensaje = ""
    nombre = ""
    apaterno = ""
    amaterno = ""
    imagenAnimal = ""

    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            apaterno = request.form["apaterno"]
            amaterno = request.form["amaterno"]
            dia = int(request.form["dia"])
            mes = int(request.form["mes"])
            anio = int(request.form["anio"])

            signo = obtenerSigno(dia, mes)
            animal = animalChino(anio)
            edad = calcularEdad(anio)
            imagenAnimal = imagen(animal)

        except (ValueError, KeyError):
            mensaje = "Fecha inválida. Asegúrate de llenar todos los campos correctamente."

    return render_template("Zodiaco.html", signo=signo, animal=animal, edad=edad, mensaje=mensaje, nombre=nombre, apaterno=apaterno, amaterno=amaterno, imagenAnimal=imagenAnimal)


if __name__ =="__main__":
    csr.init_app(app)
    app.run(debug=True) #Debug hace un reload