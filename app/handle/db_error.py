from flask import jsonify

class DatabaseError(Exception):
    def __init__(self, message):
        self.message = message

    def handle_database_error(e):
        response = {'error': 'Database error'}
        return jsonify(response), 500

    def handle_generic_error(e):
        response = {'error': 'An error occurred'}
        return jsonify(response), 500