import pytest
import sys
import os

# Agregar la carpeta raíz al path de Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 404  # No hay ruta raíz definida

