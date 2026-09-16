import requests

def test_api_smoke():
    response = requests.get("https://example.com/api/health")
    assert response.status_code == 200