import requests

def test_romance_simulation():
    response = requests.post("http://localhost:8000/simulate", json={
        "scenario": "romance",
        "target": "target_user"
    })
    assert response.status_code == 200
    assert "report" in response.json()

def test_persona_upload():
    files = {'avatar': open('tests/avatar.jpg', 'rb')}
    response = requests.post("http://localhost:8020/upload_avatar", files=files)
    assert response.status_code == 200
    assert "persona_id" in response.json()
