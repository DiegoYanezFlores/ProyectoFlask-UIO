#database/__init__.py
from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de la DB
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    # Creamos las tablas en la base de datos 
    with app.app_context():
        print("Inicializando BD...")  # DEBUG

        from .models import Usuario, Categoria, Libro, Prestamo, Cliente

        #Elimitar todas las tablas de la base de datos
        #db.drop_all()
        # Crear las tablas vacias en la base de datos
        db.create_all()

        print("Tablas creadas con éxito") # DEBUG
        