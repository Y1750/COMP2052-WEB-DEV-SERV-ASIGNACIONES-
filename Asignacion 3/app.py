from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    lista_productos = [
        {'id': 1, 'nombre': 'Laptop', 'precio': 1200},
        {'id': 2, 'nombre': 'Smartphone', 'precio': 800},
        {'id': 3, 'nombre': 'Auriculares', 'precio': 150}
    ]
    return render_template('productos.html', productos=lista_productos)

@app.route('/usuarios')
def usuarios():
    lista_usuarios = [
        {'id': 1, 'nombre': 'Ana', 'correo': 'ana@email.com'},
        {'id': 2, 'nombre': 'Luis', 'correo': 'luis@email.com'},
        {'id': 3, 'nombre': 'María', 'correo': 'maria@email.com'}
    ]
    return render_template('usuarios.html', usuarios=lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
