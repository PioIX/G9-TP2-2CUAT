from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "clave"


@app.route('/')
def redireccionIndex():
    session["logueado"] = False
    session['nombre'] = ""
    session["aviso"] = False

    conn = sqlite3.connect("baseCulture.db")
    q = f"""SELECT nombreZapatilla, foto FROM Zapatillas"""
    resu = conn.execute(q)
    print(q)
    zapatillas = resu.fetchall()
    print(zapatillas)
  
    q = f"""SELECT nombrePantalon, foto FROM Pantalones"""
    resu = conn.execute(q)
    print(q)
    pantalones = resu.fetchall()
    print(pantalones)
 
    q = f"""SELECT nombreBuzo, foto FROM Buzos"""
    resu = conn.execute(q)
    print(q)
    buzos = resu.fetchall()
    print(buzos)


    q = f"""SELECT nombreRemera, foto FROM Remeras"""
    resu = conn.execute(q)
    print(q)
    remeras = resu.fetchall()
    print(remeras)
    return render_template('index.html', nombre = session['nombre'], logueado=session["logueado"], zapatillas = zapatillas, remeras = remeras, buzos = buzos, pantalones = pantalones)

@app.route('/Home')
def inicio():
    conn = sqlite3.connect("baseCulture.db")
    q = f"""SELECT nombreZapatilla, foto FROM Zapatillas"""
    resu = conn.execute(q)
    print(q)
    zapatillas = resu.fetchall()
    print(zapatillas)
  
    q = f"""SELECT nombrePantalon, foto FROM Pantalones"""
    resu = conn.execute(q)
    print(q)
    pantalones = resu.fetchall()
    print(pantalones)
 
    q = f"""SELECT nombreBuzo, foto FROM Buzos"""
    resu = conn.execute(q)
    print(q)
    buzos = resu.fetchall()
    print(buzos)


    q = f"""SELECT nombreRemera, foto FROM Remeras"""
    resu = conn.execute(q)
    print(q)
    remeras = resu.fetchall()
    print(remeras)
    return render_template('index.html', nombre = session['nombre'], logueado=session["logueado"], zapatillas = zapatillas, remeras = remeras, buzos = buzos, pantalones = pantalones)

@app.route('/Registro')
def redireccionRegistro():
    return render_template('Registro.html')

# ARREGLAR AVISO 
@app.route('/Login')
def redireccionLogin():
    print(session["aviso"])
    return render_template('Login.html', aviso=session["aviso"])


@app.route('/Logueado', methods=["GET", "POST"])
def cambioPagina():
    if request.method == "GET":
        return redirect('/Login')
    else:
        session['nombre'] = request.form['nombre']
        session['Mail'] = request.form['Mail']
        session['Contraseña'] = request.form['Contraseña']
        conn = sqlite3.connect("baseCulture.db")
        q = f"""SELECT Mail, Contraseña FROM Login WHERE Mail ='{session['Mail']}' and Contraseña ='{session['Contraseña']}'"""
        resu = conn.execute(q)
        print(q)
        if resu.fetchone():
            session["logueado"] = True
            return redirect('/Home')
        else:
            session["logueado"] = False
            session["aviso"] = True
            return redirect('/Login')


@app.route('/datosRegistrados', methods=["GET", "POST"])
def datosRegistrados():
  
    if request.method == "GET":
      return render_template('Registro.html')
    else:
      
      print(request.form['Mail'])
      print(request.form['Contraseña'])
      session['Mail'] = request.form['Mail']
      session['Contraseña'] = request.form['Contraseña']
      session['nombre'] = request.form['nombre']
      
      conn = sqlite3.connect('baseCulture.db')
      q = f"""INSERT INTO Login(Mail, Contraseña) VALUES('{session['Mail']}', '{session['Contraseña']}')"""
      conn.execute(q)
      conn.commit()
      conn.close()
      session["logueado"] = True
  
      return redirect('/Login')


@app.route('/producto', methods=['GET','POST'])
def redireccionProductos():
  if request.method == "POST":
    producto = request.form['producto']
    tipo = request.form['tipo']
    print(producto)
    print(tipo)

    if tipo == "zapatillas":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Zapatillas WHERE nombreZapatilla = '{producto}'"""
      print(q)
      resu = conn.execute(q)
      print("hola")
      producto = resu.fetchall()
      print(producto)

    if tipo == "pantalones":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Pantalones WHERE nombrePantalon = '{producto}'"""
      print(q)
      resu = conn.execute(q)
      print("hola")
      producto = resu.fetchall()
      print(producto)

    if tipo == "buzos":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Buzos WHERE nombreBuzo= '{producto}'"""
      resu = conn.execute(q)
      print("hola")
      print(q)
      producto = resu.fetchall()
      print(producto)

    if tipo == "remeras":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Remeras WHERE nombreRemera = '{producto}'"""
      resu = conn.execute(q)
      print("hola")
      print(q)
      producto = resu.fetchall()
      print(producto)
    
    
    return render_template('ProductoDefinitivo.html', variable=session["logueado"], nombre = session['nombre'], logueado=session["logueado"], foto=producto[0][11], nombrep=producto[0][0], precio=producto[0][2], linkGOAT=producto[0][5], linkStockx=producto[0][6], linkFarfetch=producto[0][7], codigo=producto[0][8], color=producto[0][3], retail=producto[0][9], release=producto[0][10], descripcion=producto[0][4])

  else:
    return render_template('ProductoDefinitivo.html', variable=session["logueado"], nombre = session['nombre'], logueado=session["logueado"])


@app.route('/ProductoDefinitivo', methods=['GET','POST'])
def redireccionProductoDefinitivo():
  if request.method == "POST":
    producto = request.form['producto']
    tipo = request.form['tipo']
    print(producto)
    print(tipo)

    if tipo == "zapatillas":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Zapatillas WHERE nombreZapatilla = '{producto}'"""
      print(q)
      resu = conn.execute(q)
      producto = resu.fetchall()
      print(producto)

    if tipo == "pantalones":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Pantalones WHERE nombrePantalon = '{producto}'"""
      print(q)
      resu = conn.execute(q)
      print(q)
      producto = resu.fetchall()
      print(producto)

    if tipo == "buzos":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Buzos WHERE nombreBuzo= '{producto}'"""
      resu = conn.execute(q)
      print(q)
      producto = resu.fetchall()
      print(producto)

    if tipo == "remeras":
      conn = sqlite3.connect("baseCulture.db")
      q = f"""SELECT * FROM Remeras WHERE nombreRemera = '{producto}'"""
      resu = conn.execute(q)
      print(q)
      producto = resu.fetchall()
      print(producto)
      
    return render_template('ProductoDefinitivo.html', variable=session["logueado"])
  

@app.route('/editarProducto')
def ingresoEditar():
    return render_template('Registro.html')

app.run(host='0.0.0.0', port=81)


