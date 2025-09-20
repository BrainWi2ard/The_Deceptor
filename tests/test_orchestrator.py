import requests

def test_orchestrate_flow():
    audio_file = open("tests/sample.wav", "rb")
    response = requests.post("http://localhost:8000/orchestrate/", files={"audio": audio_file})
    assert response.status_code == 200
    assert "transcription" in response.json()