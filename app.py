from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def PaginaInicio ():
    return render_template('inicio.html')


@app.route("/contacto",methods=['GET','POST'])
def contacto():
   if request.method =='POST':
   #Viene del formulario
      nombre =request.form.get('nombre')
      correo=request.form.get('correo')
      mensaje=request.form.get('mensaje')

      return render_template("mostrarcontacto.html",nombre=nombre,correo=correo,mensaje=mensaje)
   return render_template("contacto.html")


if __name__ == '__main__':
    app.run(debug=True)