from flask import jsonify

def register_error_handlers(app):
    # Handle 404 Not Found
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not found"}), 404

    # Handle 500 Internal Server Error
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500

    # Handle other exceptions
    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({"error": str(error)}), 500
