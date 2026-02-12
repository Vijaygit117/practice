from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/test", methods=["POST"])
def put_content():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    dept = data.get("dept")

    return jsonify({
        "name": name,
        "dept": dept
    })

@auth_bp.route("/test/<name>", methods=["GET"])
def get_name(name):
    return f'Hello {name}'

@auth_bp.route("/test", methods=["GET"])
def get_dept():
    name = request.args.get("name")

    return f'Hello {name}'
