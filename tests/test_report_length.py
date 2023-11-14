from lib.report_length import *

def test_length_1():
    result = report_length('Simon')
    assert result == "This string was 5 characters long."

def test_length_2():
    result = report_length('Makers')
    assert result == "This string was 6 characters long."

def test_length_3():
    result = report_length('Ahoy hoy me hearties')
    assert result == "This string was 20 characters long."