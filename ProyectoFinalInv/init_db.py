from app import create_app, db
from app.models import Role, User, Item

app = create_app()

with app.app_context():
    
    db.drop_all()
    print("  Todas las tablas han sido eliminadas.")

    
    db.create_all()
    print(" Tablas creadas exitosamente.")
