from lib.present import *
import pytest

def test_wrap_on_empty_contents_does_not_error():
    present = Present()
    present.wrap('A')
    assert present.contents == 'A'

def test_wrap_on_not_empty_contents_errors():
    present = Present()
    present.wrap('A')
    with pytest.raises(Exception) as e:
        present.wrap('B')
    error_messsage = str(e.value)
    assert error_messsage == 'A contents has already been wrapped.'
    assert present.contents == 'A'

def test_unwrap_on_empty_contents_does_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_messsage = str(e.value)
    assert error_messsage == "No contents have been wrapped."

def test_unwrap_on_not_empty_contents_does_not_error():
    present = Present()
    present.wrap('C')
    assert present.unwrap() == 'C'
    





