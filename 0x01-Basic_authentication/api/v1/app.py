#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from flask_cors import (CORS, cross_origin)
import os


# Global
SECURED_PATHS = [
    '/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/'
]


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
auth_type = os.getenv('AUTH_TYPE')
if auth_type:
    if auth_type == 'auth':
        from api.v1.auth.auth import Auth
        auth = Auth()


@app.before_request
def authenticate_request():
    """Authenticates a request

    Checks whether the incoming request requires authentication
    to proceed

    Abort:
        (401): When autorization header not present
        (403): When user making request is not authorized
    """
    if auth is None:
        return
    if not auth.require_auth(request.path, SECURED_PATHS):
        return None
    auth_header = auth.authorization_header(request)
    if not auth_header:
        abort(401)
    current_user = auth.current_user(request)
    if not current_user:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Not forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
