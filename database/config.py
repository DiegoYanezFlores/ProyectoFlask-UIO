import _collections_abc
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()

class Config:

    # CONSTRUCCION DE URI 
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    # Configuración de Flask
    DEBUG = True  # EN DESARROLLO SIEMPRE TRUE PARA VER ERRORES
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
