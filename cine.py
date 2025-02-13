from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, port=3000)
