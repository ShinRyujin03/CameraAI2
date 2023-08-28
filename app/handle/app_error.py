from flask import jsonify

class InputError(Exception):
    def __init__(self, message):
        self.message = message

def handle_input_error(e):
    response = {'error': str(e)}
    return jsonify(response), 400

def handle_generic_error(e):
    response = {'error': 'An error occurred'}
    return jsonify(response), 500
