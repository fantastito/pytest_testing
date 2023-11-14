from lib.string_builder import *

def test_string_build_len():
    string_build = StringBuilder()
    string_build.add("Hello")
    result = string_build.size()
    assert result == 5

def test_string_build_output():
    string_build = StringBuilder()
    string_build.add('Simon')
    result = string_build.output()
    assert result == 'Simon'

def test_string_build_add_2():
    string_build = StringBuilder()
    string_build.add('Ahoy')
    string_build.add('Hoy')
    result = string_build.output()
    assert result == 'AhoyHoy'