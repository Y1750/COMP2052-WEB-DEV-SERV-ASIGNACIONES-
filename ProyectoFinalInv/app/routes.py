from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import ItemForm, ChangePasswordForm
from app.models import db, Item, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            flash('Contraseña actual incorrecta.')
            return render_template('cambiar_password.html', form=form)
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('✅ Contraseña actualizada correctamente.')
        return redirect(url_for('main.dashboard'))
    return render_template('cambiar_password.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role.name == 'Admin':
        items = Item.query.all()
    else:
        items = Item.query.filter_by(owner_id=current_user.id).all()
    return render_template('dashboard.html', items=items)

@main.route('/items', methods=['GET', 'POST'])
@login_required
def crear_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            cantidad=form.cantidad.data,
            categoria=form.categoria.data,
            precio_estimado=form.precio_estimado.data,
            ubicacion=form.ubicacion.data,
            fecha_adquisicion=form.fecha_adquisicion.data,
            owner_id=current_user.id
        )
        db.session.add(item)
        db.session.commit()
        flash("Ítem agregado correctamente.")
        return redirect(url_for('main.dashboard'))
    return render_template('item_form.html', form=form)

@main.route('/items/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_item(id):
    item = Item.query.get_or_404(id)
    if item.owner_id != current_user.id and current_user.role.name != 'Admin':
        flash('No tienes permiso para editar este ítem.')
        return redirect(url_for('main.dashboard'))
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.nombre = form.nombre.data
        item.descripcion = form.descripcion.data
        item.cantidad = form.cantidad.data
        item.categoria = form.categoria.data
        item.precio_estimado = form.precio_estimado.data
        item.ubicacion = form.ubicacion.data
        item.fecha_adquisicion = form.fecha_adquisicion.data
        db.session.commit()
        flash("Ítem actualizado correctamente.")
        return redirect(url_for('main.dashboard'))
    return render_template('item_form.html', form=form, editar=True)

@main.route('/items/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_item(id):
    item = Item.query.get_or_404(id)
    if item.owner_id != current_user.id and current_user.role.name != 'Admin':
        flash('No tienes permiso para eliminar este ítem.')
        return redirect(url_for('main.dashboard'))
    db.session.delete(item)
    db.session.commit()
    flash("Ítem eliminado correctamente.")
    return redirect(url_for('main.dashboard'))

@main.route('/usuarios')
@login_required
def listar_usuarios():
    if current_user.role.name != 'Admin':
        flash("No tienes permiso para ver esta página.")
        return redirect(url_for('main.dashboard'))
    usuarios = User.query.join(User.role).all()
    return render_template('usuarios.html', usuarios=usuarios)
