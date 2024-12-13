from .....dio_bank.src.app import *

from flask import Blueprint, request, jsonify


username = Blueprint("username", __name__)


@username.route("/<string:username>", methods=["GET"])
def get_username(username):
    try:
        return jsonify({"username": username})
    except Exception as e:
        return jsonify({"error": str(e)}), 200
