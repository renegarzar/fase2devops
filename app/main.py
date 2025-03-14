from flask import Flask
from app import database
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from app.routes import cliente_routes

app = Flask(__name__)
database.init_db()

# Registrar rutas
app.register_blueprint(cliente_routes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
