#services/libro_service.py 

from repositories import libro_repository
from database.models import Libro

# =========================================================
# El service contiene la lógica del negocio.
#
# Aquí:
# ✅ validamos reglas
# ✅ tomamos decisiones
# ✅ coordinamos procesos
#
# PERO:
# ❌ NO manejamos HTTP
# ❌ NO usamos jsonify
# ❌ NO usamos request
# =========================================================

# =========================================================
# CREAR LIBRO (POST)
# =========================================================

class LibroService:
    def __init__(self, libro_repository):

        self.repo = libro_repository

    def crear_libro(data):

        # =================================================
        # VALIDACIÓN DE NEGOCIO
        # =================================================
        try:

            if data.get('stock', 0) < 0:
                return {
                    "exito": False,
                    "error": "El stock no puede ser negativo"
                }

        # =================================================
        # CREAR OBJETO LIBRO
        # =================================================
            nuevo_libro = Libro(
                titulo=data['titulo'],
                autor=data['autor'],
                editorial=data['editorial'],
                anio=data['anio'],
                isbn=data['isbn'],
                stock=data['stock'],
                categoria_id=data['categoria_id'],
                usuario_id=data['usuario_id']
            )

        # =================================================
        # GUARDAR EN REPOSITORY
        # =================================================
            libro_repository.guardar_libro(nuevo_libro)

        # =================================================
        # RESPUESTA EXITOSA
        # =================================================
            return {
                "exito": True,
                "libro": nuevo_libro
            }

        # =====================================================
        # MANEJO DE ERRORES (CREAR)
        # =====================================================
        except Exception as e:

            return {
                "exito": False,
                "error": str(e)
            }

# =========================================================
# OBTENER TODOS LOS LIBROS (GET)
# =========================================================

    def obtener_libros():

        try:

            libros = libro_repository.obtener_libros()

            return {
                "exito": True,
                "libros": [libro.to_dict() for libro in libros]
            }

        except Exception as e:

            return {
                "exito": False,
                "error": str(e)
            }

    # =========================================================
    # OBTENER LIBRO POR ID (GET)    
    # =========================================================
    def obtener_libro_por_id(id):
        
        # =====================================================
        # BUSCAR LIBRO
        # =====================================================

        libro = libro_repository.obtener_por_id(id)

        # =====================================================
        # VALIDAR EXISTENCIA
        # =====================================================

        if not libro: 
            return {
                "exito": False,
                "error": "Libro no encontrado"
            }
        
        # =====================================================
        # RESPUESTA EXITOSA
        # =====================================================
        else:
            return {

                "exito": True,

                "libro": libro

            }

    # =========================================================
    # ACTUALIZAR LIBRO
    # =========================================================
    def actualizar_libro(id, data):
        
        try:
            # =================================================
            # BUSCAR LIBRO EXISTENTE
            # =================================================
            libro = libro_repository.obtener_por_id(id)
            
            # =================================================
            # VALIDAR EXISTENCIA
            # =================================================
            if not libro:

                return {

                    "exito": False,

                    "error": "Libro no encontrado"

                }
            
            # =================================================
            # ACTUALIZAR DATOS
            # =================================================
            libro.titulo = data['titulo']
            libro.autor = data['autor']
            libro.editorial = data['editorial']
            libro.anio = data['anio']
            libro.isbn = data['isbn']
            libro.stock = data['stock']
            libro.categoria_id = data['categoria_id']
            libro.usuario_id = data['usuario_id']

            # =================================================
            # GUARDAR CAMBIOS
            # =================================================
            libro_repository.actualizar_libro()

            # =================================================
            # RESPUESTA EXITOSA
            # =================================================
            return {

                "exito": True,

                "libro": libro

            }
        
        # =================================================
        # MANEJO DE ERRORES (ACTUALIZAR)
        # =================================================
        except Exception as e:

            return {

                "exito": False,

                "error": str(e)

            }

    # =========================================================
    # ELIMINAR LIBRO
    # =========================================================
    def eliminar_libro(id):

        try: 
            # =====================================================
            # BUSCAR LIBRO
            # =====================================================
            libro = libro_repository.obtener_por_id(id)
            
            # =================================================
            # VALIDAR EXISTENCIA
            # =================================================
            if not libro:

                return {

                    "exito": False,

                    "error": "Libro no encontrado"

                }
            
            # =====================================================
            # ELIMINAR LIBRO
            # =====================================================
            libro_repository.eliminar_libro(libro)

            # =====================================================
            # RESPUESTA EXITOSA
            # =====================================================
            return {

                "exito": True,

                "mensaje": "Libro eliminado correctamente"

            }
        
        # =================================================
        # MANEJO DE ERRORES (DELETE)
        # =================================================
        except Exception as e:
            
            return {

                "exito": False,

                "error": str(e)

            }
