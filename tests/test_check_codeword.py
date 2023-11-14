from lib.check_codeword import *

def test_check_codeword_1():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_2():
    result = check_codeword("hose")
    assert result == "Close, but nope."

def test_check_codeword_3():
    result = check_codeword('cowboy')
    assert result == "WRONG!"