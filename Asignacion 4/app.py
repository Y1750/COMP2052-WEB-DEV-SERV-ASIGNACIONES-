from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_para_formularios'

@app.route("/")
def home():
    return "Servidor activo: Proyecto Capstone Formulario."

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        correo = form.correo.data
        # Aquí puedes guardar los datos si tuvieras base de datos
        flash(f'Usuario {nombre} registrado exitosamente!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
