#repositories/libro_repository.py
from database import db
from database.models import Libro
from sqlalchemy.orm import joinedload

# =========================================================
# El repository SOLO se comunica con la base de datos.
#
# Aquí:
# ✅ usamos SQLAlchemy
# ✅ hacemos consultas SQL
# ✅ guardamos datos
#
# PERO:
# ❌ NO validamos negocio
# ❌ NO usamos Flask
# ❌ NO usamos jsonify
# =========================================================

class LibroRepository:

    
    def guardar_libro(libro):

        db.session.add(libro)
        db.session.commit()
        return libro


# =========================================================
# OBTENER TODOS LOS LIBROS
# =========================================================
    def obtener_libros():
    #OPTIMIZACIÓN PROFESIONAL: Trae los libros y sus relaciones de un solo golpe (Eager Loading)
        return Libro.query.options(
            joinedload(Libro.categoria), 
            joinedload(Libro.usuario)
        ).all()

# =========================================================
# OBTENER LIBRO POR ID
# =========================================================
    def obtener_por_id(id):

        #return Libro.query.get(id)
        return Libro.query.options(
            joinedload(Libro.categoria), 
            joinedload(Libro.usuario)
        ).get(id)

# =========================================================
# ACTUALIZAR LIBRO
# =========================================================
# SQLAlchemy detecta automáticamente los cambios
# realizados sobre el objeto.
#
# Solo necesitamos hacer commit().
# =========================================================
    def actualizar_libro():

        db.session.commit()

# =========================================================
# ELIMINAR LIBRO
# =========================================================
    def eliminar_libro(libro):

        db.session.delete(libro)

        db.session.commit()

    def obtener_todos_con_relaciones():
    # Carga de un solo golpe el libro junto a su categoría y usuario encargado
        return Libro.query.options(joinedload(Libro.categoria), joinedload(Libro.usuario)).all()