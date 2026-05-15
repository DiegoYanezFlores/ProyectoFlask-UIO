#app.py
from flask import Flask
from flask_cors import CORS

#1 IMPORTAMOS CONFIGURACION Y LA INICIALIZACION DE LA BASE DE DATOS
from database import init_db
from database.config import Config

#IMPORTAR LOS BLUEPRINTS
from routes.libro_routes import libros_bp
from routes.main_routes import main_bp

def create_app():

    app = Flask(__name__)

    #A. HABILITAR CORS (COMUNICAICON ENTRE EL FRONT Y EL BACKEND
    CORS(app)

    # B. Cargar configuración centralizada
    # Leemos todo desde el objeto Config en database/config.py
    app.config.from_object(Config)

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
    # Imprimimos un mensaje de confirmación para los alumnos
    print("\n========================================")
    print("🚀 Servidor Flask iniciado exitosamente")
    print("📍 URL Base: http://localhost:5000")
    print("📂 API Libros: http://localhost:5000/api/libros")
    print("========================================\n")
    
    app.run(debug=True)
