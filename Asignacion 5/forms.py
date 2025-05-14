from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(message="Usuario requerido.")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida.")])
    submit = SubmitField('Iniciar sesión')
