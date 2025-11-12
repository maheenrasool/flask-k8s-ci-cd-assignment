# tests/test_app.py.

from app import hello


def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hi\n"
