from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_eda_summary_valid(): 
    response = client.get("/eda/summary", params={"feature":"SalePrice"})
    assert response.status_code == 200
    data = response.status_code == 200
    data = response.json()
    assert data["feature"] == "SalePrice"
    assert "mean" in data 
    assert "median" in data

def test_eda_summary_invalid(): 
    response = client.get("eda/summary", params={"feature": "Unknow"})
    assert response.status_code == 404

#Comprobar que la api rechaza variables categoricas cuando solicitamos estadisticas
def test_eda_sumary_categorical(): 
    response = client.get("eda/summary", params={"feature": "Neighborhood"})
    assert response.status_code==400
    data = response.json()
    assert "not numerical" in data["detail"]
