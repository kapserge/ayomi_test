from fastapi.testclient import TestClient
from app.main import app
import pytest
from httpx import AsyncClient
client = TestClient(app)

def test_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API AYOMI is LIVE!!"}


"""
testing operation calcultrice
"""
def test_create_calcul():
    sample_payload = {
        
        "notation": "3 6 9 3 + -14 * / * 7 + 100 +",
        "resultat": "107",
        
    }
    response = client.post("api/Calculatrice/calcul/", json=sample_payload)
    assert response.status_code == 201
    

    

    