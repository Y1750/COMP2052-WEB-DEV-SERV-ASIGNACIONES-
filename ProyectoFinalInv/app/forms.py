from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, IntegerField, DecimalField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField(
        'Role',
        choices=[('Admin', 'Admin'), ('Usuario', 'Usuario'), ('Owner', 'Owner')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Register')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')

class ItemForm(FlaskForm):
    nombre = StringField('Item name', validators=[DataRequired()])
    descripcion = TextAreaField('Description', validators=[DataRequired()])
    cantidad = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    categoria = SelectField('Category', choices=[
        ('Electronics', 'Electronics'),
        ('Furniture', 'Furniture'),
        ('Clothing', 'Clothing'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    precio_estimado = DecimalField('Estimated Price', validators=[DataRequired(), NumberRange(min=0)], places=2)
    ubicacion = StringField('Location', validators=[Optional()])
    fecha_adquisicion = DateField('Acquisition Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Save')
