from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "clave_super_secreta"


@app.route("/")
def index():
    
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/oferta')
def oferta():
    return render_template('ofertas.html')

@app.route('/carrito')
def carrito():
    juego = request.args.get('juego')
    imagen = ""
    if juego == "Elden Ring":
        imagen = "elden.jpg"
        descripcion=" Elden Ring es de los padres de Dark Souls llega este juego de mundo abierto, que presumiblemente sigue a rajatabla los mandamientos de la serie creada por Hidetaka Miyazaki, y que está ambientado en la fantasía oscura occidental y que proponen una mirada más profunda del RPG en tercera persona. Este videojuego insta a los jugadores a explorar un mapa grande y variado para descubrir todos los secretos que ocultan las Tierras Intermedias y descubrir cuál es el destino del misterioso Círculo de Elden."

    elif juego == "Mortal Kombat 1":
        imagen = "mortal.jpg"
        descripcion="Descubre un nuevo universo de Mortal Kombat™creado por Liu Kang, Dios del Fuego. ¡Mortal Kombat™ 1 abre paso a una nueva era de esta icónica saga con un nuevo sistema de kombate, modos de juego y fatalities!"
    else:
        juego =="Total War:Warhammer 3"
        imagen = "total.jpg"
        descripcion="El final cataclísmico de la trilogía de Total War™: WARHAMMER® ha llegado. Reagrupa a tus fuerzas y adéntrate en el Reino del Caos, una dimensión de terrores horripilantes en la que se decidirá el destino del mundo. ¿Conquistarás a tus demonios... o los dirigirás?"
    return render_template('carrito.html', juego=juego, imagen=imagen, descripcion=descripcion)

@app.route('/finalizar', methods=['POST'])
def finalizar():
    juego = request.form.get('juego')
    imagen = request.form.get('imagen')
    return render_template('finalizar.html', juego=juego, imagen=imagen)

@app.route('/confirmar', methods=['POST'])
def confirmar():
    juego = request.form.get('juego')
    imagen = request.form.get('imagen')
    return render_template('confirmar.html', juego=juego, imagen=imagen)

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "admin" and password == "1234":
            session["admin"] = True
            return redirect(url_for("admin_juegos"))
        else:
            return render_template("admin-login.html", error="Credenciales incorrectas")
    return render_template("admin-login.html")

@app.route("/admin/juegos")
def admin_juegos():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect("juegos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM juegos")
    juegos = cursor.fetchall()
    conn.close()

    return render_template("admin-juegos.html", juegos=juegos)

@app.route("/admin/nuevo", methods=["GET", "POST"])
def admin_nuevo():
    if not session.get("admin"):
        return redirect(url_for("admin-login"))

    if request.method == "POST":
        nombre = request.form["nombre"]
        imagen = request.form["imagen"]
        precio = request.form["precio"]

        conn = sqlite3.connect("juegos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO juegos (nombre, imagen, precio) VALUES (?, ?, ?)", (nombre, imagen, precio))
        conn.commit()
        conn.close()

        return redirect(url_for("admin_juegos"))

    return render_template("admin-nuevo.html")

@app.route("/admin/editar/<int:id>", methods=["GET", "POST"])
def admin_editar(id):
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect("juegos.db")
    cursor = conn.cursor()

    if request.method == "POST":
        nombre = request.form["nombre"]
        imagen = request.form["imagen"]
        precio = request.form["precio"]

        cursor.execute("UPDATE juegos SET nombre=?, imagen=?, precio=? WHERE id=?", (nombre, imagen, precio, id))
        conn.commit()
        conn.close()
        return redirect(url_for("admin_juegos"))

    cursor.execute("SELECT * FROM juegos WHERE id=?", (id,))
    juego = cursor.fetchone()
    conn.close()

    return render_template("admin-editar.html", juego=juego)

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("admin_login"))

if __name__ == '__main__':
    app.run(debug=True)