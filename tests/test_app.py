# tests/test_app.py

from app import hello
from app.app import app


def test_hello_function(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hi\n"


def test_flask_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World from Flask CI/CD!" in response.data
