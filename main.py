from flask import Flask, render_template
from flask import request
from pytest import main

from TuclaseExamen import arithmetic_arranger


app = Flask(__name__)
listaNum =[]


@app.route("/operaciones",methods=["GET"])
def operaciones():
    listaNum.clear()
    return render_template("operaciones.html")


@app.route("/operaciones",methods=["POST"])
def ResultadoCine():
    operandor1 = request.form.get("txtNum1")
    operando = request.form.get("cmbOperador")
    operandor2 = request.form.get("txtNum2")

    operacion = str(operandor1) + ' ' + str(operando) + ' ' + str(operandor2)
    
    listaNum.append(operacion)

    respuesta = arithmetic_arranger(listaNum, True)

    main(['-vv'])

    return render_template("operaciones.html",res=respuesta)


if __name__ =="__main__":
    app.run(debug=True, port=3000)
