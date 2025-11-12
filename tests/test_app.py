from app import hello

def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hi"
