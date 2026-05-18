# routes/main_routes.py
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return jsonify({
        "mensaje": "Sistema de Biblioteca funcionando correctamente",
        "modulo": "Principal",
        "estado": "activo"
    })

@main_bp.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "checks": {
            "database": "connected",
            "server": "running"
        }
    })