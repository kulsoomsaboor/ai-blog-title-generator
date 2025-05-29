from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_titles_valid_input():
    response = client.post("/generate-titles", json={"prompt": "Benefits of morning exercise"})
    assert response.status_code == 200
    assert "titles" in response.json()
    assert isinstance(response.json()["titles"], list)
