import sys
import os
from app import hello


def test_hello():
    assert hello() == "Hello, World from Flask CI/CD!"
