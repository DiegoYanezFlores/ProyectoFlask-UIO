#routes/libro_routes.py
from flask import Blueprint, jsonify, request
from repositories.libro_repository import LibroRepository
from services.libro_service import LibroService

# =========================================================
# Este archivo contiene las rutas HTTP del módulo libros.
#
# Aquí se definen los endpoints de la API:
#
# POST   /libros       -> Crear libro
# GET    /libros       -> Obtener todos los libros
# GET    /libros/<id>  -> Obtener un libro por ID
# PUT    /libros/<id>  -> Actualizar libro
# DELETE /libros/<id>  -> Eliminar libro
#
# RESPONSABILIDADES DE ESTE ARCHIVO:
# ✅ Recibir peticiones HTTP
# ✅ Leer datos JSON enviados por el cliente
# ✅ Llamar al service correspondiente
# ✅ Devolver respuestas JSON
# ✅ Manejar códigos HTTP
#
# ESTE ARCHIVO NO DEBE:
# ❌ Contener lógica de negocio
# ❌ Acceder directamente a SQLAlchemy
# ❌ Hacer consultas a la base de datos
#
# En arquitectura SOLID:
# Este archivo representa la CAPA DE PRESENTACIÓN.
# =========================================================


#Creacion de un blueprint
libros_bp = Blueprint('libros', __name__)

# ARQUITECTURA DE CAPAS: Instanciamos e Inyectamos la dependencia
_repo = LibroRepository()
libro_service = LibroService(_repo)

#CRUD de libros

# Crear un libro
@libros_bp.route('/libros', methods=['POST'])
def crear_libro():

    data = request.get_json()

    resultado = libro_service.crear_libro(data)

    # =====================================================
    # RESPUESTA EXITOSA
    # =====================================================
    if resultado['exito']:
        return jsonify({
            "mensaje": "Libro creado correctamente",
            "libro": resultado['libro'].to_dict_relacional()
        }), 201
    
    # =====================================================
    # RESPUESTA DE ERROR
    # =====================================================  
    else:
       return jsonify({
        "mensaje": "Error de validación", 
        "error": resultado['error']
    }), 400


# =========================================================
# OBTENER TODOS LOS LIBROS
# =========================================================
# Endpoint:
# GET /libros
#
# Devuelve todos los libros registrados.
# =========================================================

@libros_bp.route('/libros', methods=['GET'])
def obtener_libros():
    resultado = libro_service.obtener_libros()
    if resultado['exito']:
        # Retorna la lista con los diccionarios relacionales embebidos
        return jsonify({"libros": resultado['libros']}), 200
    return jsonify({
        "mensaje": "Error al obtener libros", 
        "error": resultado['error']
    }), 500

@libros_bp.route('/libros/<int:id>', methods=['GET'])
def obtener_libro(id):

    resultado = libro_service.obtener_libro_por_id(id)

    # =====================================================
    # RESPUESTA EXITOSA
    # =====================================================
    if resultado['exito']:
        return jsonify({"libro": resultado['libro'].to_dict_relacional()}), 200
    
    # =====================================================
    # RESPUESTA DE ERROR
    # =====================================================  
    else:
        return jsonify({
            "mensaje": "Libro no encontrado",
            "error": resultado['error']
        }), 404

# =========================================================
# ACTUALIZAR LIBRO
# =========================================================
# Endpoint:
# PUT /libros/<id>
#
# Permite modificar un libro existente.
# =========================================================
@libros_bp.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):

    # =====================================================
    # Obtener JSON enviado desde cliente (insomnia, postman...)
    # ====================================================
    data = request.get_json()

    # =====================================================
    # Enviar datos al service
    # =====================================================
    resultado = libro_service.actualizar_libro(id, data)

    # =====================================================
    # RESPUESTA EXITOSA
    # =====================================================
    if resultado['exito']:
        return jsonify({
            "mensaje": "Libro actualizado correctamente",
            "libro": resultado['libro'].to_dict()
        }), 200
    
    # =====================================================
    # RESPUESTA DE ERROR
    # =====================================================  
    else:
        return jsonify({
            "mensaje": "Error al actualizar el libro",
            "error": resultado['error']
        }), 404

# =========================================================
# ELIMINAR LIBRO
# =========================================================
# Endpoint:
# DELETE /libros/<id>
#
# Elimina un libro de PostgreSQL.
# =========================================================
@libros_bp.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    
    resultado = libro_service.eliminar_libro(id)

    # =====================================================
    # RESPUESTA EXITOSA
    # =====================================================
    if resultado['exito']:
        return jsonify({
            "mensaje": "Libro eliminado correctamente"
        }), 200

    # =====================================================
    # RESPUESTA DE ERROR
    # =====================================================    
    else:
        return jsonify({
            "mensaje": "Error al eliminar el libro",
            "error": resultado['error']
        }), 404
