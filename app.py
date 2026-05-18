#app.py
import os
# pyrefly: ignore [missing-import]
from flask import Flask
from flask_cors import CORS

#1 IMPORTAMOS CONFIGURACION Y LA INICIALIZACION DE LA BASE DE DATOS
from database import init_db
from database.config import Config, config_dict

#IMPORTAR LOS BLUEPRINTS
from routes.libro_routes import libros_bp
from routes.main_routes import main_bp

def create_app():

    app = Flask(__name__)

    #A. HABILITAR CORS (COMUNICAICON ENTRE EL FRONT Y EL BACKEND
    CORS(app)

    #B. DETECTAR EL ENTORNO ACTUAL Y CARGAR CONFIGURACIÓN
    #Si no se define FLASK_ENV en el sistema, por defecto inicia en 'development'env = os.getenv('FLASK_ENV', 'development')
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config_dict[env])

    # C. Inicializamos la base de datos
    init_db(app)

    # D. Registro de Blueprints (Modularidad)
    # Registramos las rutas generales (Home, Health) en la raíz
    app.register_blueprint(main_bp)

    # Registramos las rutas de la API con un prefijo profesional
    # Todas las rutas de libros ahora empezarán con /api/libros
    app.register_blueprint(libros_bp, url_prefix='/api')

    return app

# INICIALIZAR EL SERVIDOR

if __name__ == '__main__':

    # Crear la aplicación
    app = create_app()

    # Imprimimos un mensaje de confirmación para los usuarios.
    print("\n========================================")
    print("🚀 Servidor Flask iniciado exitosamente")
    print("📍 URL Base: http://localhost:5000")
    print("📂 API Libros: http://localhost:5000/api/libros")
    print("========================================\n")
    
    app.run(debug=True)