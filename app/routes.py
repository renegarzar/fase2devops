from flask import Blueprint, request, jsonify
from app.database import DB_FILE
import sqlite3

cliente_routes = Blueprint("clientes", __name__)

@cliente_routes.route("/clientes", methods=["POST"])
def crear_cliente():
    data = request.json
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, correo, telefono) VALUES (?, ?, ?)",
                   (data["nombre"], data["correo"], data["telefono"]))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Cliente creado"}), 201

@cliente_routes.route("/clientes/<int:id>", methods=["PUT"])
def modificar_cliente(id):
    data = request.json
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nombre=?, correo=?, telefono=? WHERE id=?",
                   (data["nombre"], data["correo"], data["telefono"], id))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Cliente actualizado"}), 200

@cliente_routes.route("/clientes/<int:id>", methods=["GET"])
def obtener_cliente(id):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    cliente = cursor.fetchone()
    conn.close()
    if cliente:
        return jsonify({"id": cliente[0], "nombre": cliente[1], "correo": cliente[2], "telefono": cliente[3]}), 200
    return jsonify({"mensaje": "Cliente no encontrado"}), 404
