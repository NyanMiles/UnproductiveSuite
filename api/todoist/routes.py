from flask import Blueprint, jsonify
from .tasks import obtener_datos_ejemplo


todoist_bp = Blueprint('todoist', __name__, url_prefix='/todoist')


@todoist_bp.route('/tasks', methods=['GET'])
def tareas():
    data = obtener_datos_ejemplo()
    return jsonify(data)