import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # noqa: E402

from app import hello


def test_hello():
    assert hello() == "Hello, World from Flask CI/CD!"
