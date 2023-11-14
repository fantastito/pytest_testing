import pytest
from lib.password_checker import *

def test_check_password_length1():
    password = PasswordChecker()
    result = password.check('P12345678')
    assert result == True

def test_check_password_length2():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('123')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

#1. is password long enough, yes
#2. is password long enough, not, returns error