import requests

def test_get_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    
    assert response.status_code == 200
    
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

def test_create_user():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post("https://reqres.in/api/users", json=payload)
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "morpheus"
    assert "id" in data