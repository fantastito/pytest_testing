from lib.greet   import *

def test_greet():
    result = greet('Simon')
    assert result == 'Hello, Simon!'