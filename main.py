from flask import Flask, render_template,request
import forms


app=Flask(__name__)

@app.route("/")
def index():
    escuela="UTL!!!"
    alumnos=["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    nom=''
    apa=''
    ama=''
    alum_form=forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        print("Nombre : {} ".format(nom)) 
        print("Apellido paterno : {} ".format(apa))        
        print("Apelllido materno  : {} ".format(ama)) 
    
    return render_template("alumnos.html",form=alum_form,nom=nom)

@app.route("/maestros")
def maes():
    return render_template("maestros.html")

@app.route("/hola")
def saludo():
    return "<p><h1>Hola desde la funcion saludar<br> Y hola mundo</h1></p>"

''' http://127.0.0.1:5000/user/jose '''
@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola "+name


@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID {} Nombre {}".format(id,name)

#http://127.0.0.1:5000/suma/5.0/8.0
@app.route("/suma/<float:n1>/<float:n2>")
def funcSumar (n1,n2):
    return "El valor de {} + {} = {}".format(n1,n2,n1+n2)
    
@app.route("/default")
@app.route("/default/<string:ab>")
def fun(ab="UTL"):
    return "Hola " + ab

@app.route("/multiplicar",methods=["GET","POST"])
def multiplicar():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1>La multiplicación es: {} </h1>".format(str(int(num1)*int(num2)))
    else:
        return'''
        <form action="/multiplicar" method="POST">
            <label>N1:</labes>
            <input type="text" name="n1"/><br>
            <label>N2:</labes>
            <input type="text" name="n2"/><br>
            <input type="submit"/>
        </form>
        '''

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/opciones",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        if request.form.get('sum'):
            return "<h1>La Suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif request.form.get('res'):
            return "<h1>La Resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif request.form.get('mul'):
            return "<h1>La Multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
        else:
            return "<h1>La Division es: {} </h1>".format(str(int(num1)/int(num2)))

@app.route("/formulario2")
def form2():
    return render_template("formulario2.html")





'''
Aqui colocamos el motodo que iniciara la App
'''
if __name__=="__main__":
    app.run(debug=True)