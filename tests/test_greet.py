from lib.greet import *

def test_greet():
    result = greet("Usama")
    assert result == "Hello, Usama!"