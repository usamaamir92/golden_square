from lib.password_checker import *
import pytest

def test_password_length_is_greater_than_7():
    password = PasswordChecker()
    assert password.check("password") == True

def test_password_length_is_less_than_8():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("passwor")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."