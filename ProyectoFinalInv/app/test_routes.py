from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Item
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/dashboard')
def index():
    return '<h1>Corriendo en Modo de Prueba - Inventario Personal</h1>'

@main.route('/items', methods=['GET'])
@login_required
def listar_items():
    items = Item.query.filter_by(owner_id=current_user.id).all()
    data = [
        {
            'id': item.id,
            'nombre': item.nombre,
            'descripcion': item.descripcion,
            'categoria': item.categoria,
            'cantidad': item.cantidad,
            'precio_estimado': float(item.precio_estimado) if item.precio_estimado else None,
            'ubicacion': item.ubicacion,
            'fecha_adquisicion': item.fecha_adquisicion.strftime('%Y-%m-%d') if item.fecha_adquisicion else None,
            'owner_id': item.owner_id
        }
        for item in items
    ]
    return jsonify(data), 200

@main.route('/items/<int:id>', methods=['GET'])
@login_required
def listar_un_item(id):
    item = Item.query.get_or_404(id)
    if item.owner_id != current_user.id:
        return jsonify({'error': 'No tienes permiso para ver este ítem'}), 403
    data = {
        'id': item.id,
        'nombre': item.nombre,
        'descripcion': item.descripcion,
        'categoria': item.categoria,
        'cantidad': item.cantidad,
        'precio_estimado': float(item.precio_estimado) if item.precio_estimado else None,
        'ubicacion': item.ubicacion,
        'fecha_adquisicion': item.fecha_adquisicion.strftime('%Y-%m-%d') if item.fecha_adquisicion else None,
        'owner_id': item.owner_id
    }
    return jsonify(data), 200

@main.route('/items', methods=['POST'])
@login_required
def crear_item():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    fecha_adq = data.get('fecha_adquisicion')
    fecha_adq_date = None
    if fecha_adq:
        try:
            fecha_adq_date = datetime.strptime(fecha_adq, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Formato de fecha_adquisicion inválido. Use YYYY-MM-DD'}), 400

    item = Item(
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion', ''),
        categoria=data.get('categoria'),
        cantidad=data.get('cantidad', 0),
        precio_estimado=data.get('precio_estimado'),
        ubicacion=data.get('ubicacion'),
        fecha_adquisicion=fecha_adq_date,
        owner_id=current_user.id
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item creado', 'id': item.id}), 201

@main.route('/items/<int:id>', methods=['PUT'])
@login_required
def actualizar_item(id):
    item = Item.query.get_or_404(id)
    if item.owner_id != current_user.id:
        return jsonify({'error': 'No tienes permiso para editar este ítem'}), 403

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    fecha_adq = data.get('fecha_adquisicion')
    if fecha_adq:
        try:
            item.fecha_adquisicion = datetime.strptime(fecha_adq, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Formato de fecha_adquisicion inválido. Use YYYY-MM-DD'}), 400

    item.nombre = data.get('nombre', item.nombre)
    item.descripcion = data.get('descripcion', item.descripcion)
    item.categoria = data.get('categoria', item.categoria)
    item.cantidad = data.get('cantidad', item.cantidad)
    item.precio_estimado = data.get('precio_estimado', item.precio_estimado)
    item.ubicacion = data.get('ubicacion', item.ubicacion)

    db.session.commit()
    return jsonify({'message': 'Item actualizado', 'id': item.id}), 200

@main.route('/items/<int:id>', methods=['DELETE'])
@login_required
def eliminar_item(id):
    item = Item.query.get_or_404(id)
    if item.owner_id != current_user.id:
        return jsonify({'error': 'No tienes permiso para eliminar este ítem'}), 403

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item eliminado', 'id': item.id}), 200
