from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)