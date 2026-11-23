from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = ""
    error = ""
    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])
            if not (10 <= nota1 <= 70 and
                    10 <= nota2 <= 70 and
                    10 <= nota3 <= 70 and
                    0 <= asistencia <= 100):
                error = "Ingresa notas entre 10 y 70 y asistencia entre 0 y 100."
            else:
                promedio = (nota1 + nota2 + nota3) / 3
                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
                promedio = round(promedio, 2)
        except (ValueError, KeyError):
            error = "Debes ingresar números válidos en todos los campos."
    return render_template("ejercicio1.html",
                           promedio=promedio,
                           estado=estado,
                           error=error)
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mayor = ""
    cantidad = None
    error = ""
    empate = False
    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()
        if not nombre1 or not nombre2 or not nombre3:
            error = "Debes ingresar los tres nombres."
        elif (nombre1.lower() == nombre2.lower() or
              nombre1.lower() == nombre3.lower() or
              nombre2.lower() == nombre3.lower()):
            error = "Los tres nombres deben ser diferentes."
        else:
            nombres = [nombre1, nombre2, nombre3]
            nombre_mayor = nombres[0]
            for nombre in nombres:
                if len(nombre) >= len(nombre_mayor):
                    nombre_mayor = nombre
            cantidad = len(nombre_mayor)
            empatados = 0
            for nombre in nombres:
                if len(nombre) == cantidad:
                    empatados += 1
            if empatados > 1:
                empate = True
    return render_template("ejercicio2.html",
                           nombre_mayor=nombre_mayor,
                           cantidad=cantidad,
                           error=error,
                           empate=empate)
if __name__ == "__main__":
    app.run(debug=True)
