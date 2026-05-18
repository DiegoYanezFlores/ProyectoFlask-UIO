#database/config.py
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Construcción URI 
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    """Configuración para el entorno de Desarrollo Local."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{Config.DB_USER}:{Config.DB_PASS}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
    )

class TestingConfig(Config):
    """Configuración para Pruebas Unitarias y de Integración."""
    DEBUG = True
    TESTING = True
    # Usamos una base de datos SQLite en memoria para tests ultra rápidos y aislados
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(Config):
    """Configuración para el entorno de Producción."""
    DEBUG = False
    # En producción se exige SSL/TLS para cifrar la conexión a la base de datos remota
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{Config.DB_USER}:{Config.DB_PASS}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}?sslmode=require"
    )

# Diccionario mapeador para facilitar la selección en el Application Factory
config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

    
