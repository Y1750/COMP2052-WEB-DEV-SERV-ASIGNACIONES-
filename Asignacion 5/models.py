from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, username, password, role="user"):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Creación de algunos usuarios de prueba
users = {
    "admin": User(id=1, username="admin", password="admin123", role="admin"),
    "user": User(id=2, username="user", password="user123", role="user")
}
