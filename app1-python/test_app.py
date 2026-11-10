from app import app


def test_index_returns_hello_world_1():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == "Hello World 1"


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"
