from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "clave"

@app.route('/')
def redireccionIndex():
    session["Logueado"] = True
    return render_template('index.html')

@app.route('/Registro')
def redireccionRegistro():
  return render_template('Registro.html')

#hacer approute home
@app.route('/Login') 
def redireccionLogin():
  return render_template('Login.html')
  
@app.route('/Logueado' , methods = ["GET", "POST"])
def Logueado():
  if request.method == "GET":
    return redirect('/Login')
  else:
    session['Mail'] = request.form['Mail']
    session['Contraseña'] = request.form['Contraseña']
    conn = sqlite3.connect("baseCulture.db")
    q = f"""SELECT Mail, Contraseña FROM Login WHERE Mail ='{session['Mail']}' Contraseña ='{session['Contraseña']}'"""
    resu = conn.execute(q)
    print(q)
    if resu.fetchone():
      session["Logueado"] = True
      return redirect('/Home')
    
@app.route('/Producto')
def redireccionProducto():
  return render_template('Producto.html', variable = session["Logueado"])



  
app.run(host='0.0.0.0', port=81)