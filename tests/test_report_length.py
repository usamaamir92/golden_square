from lib.report_length import *

def test_zero_character_length_returned_correctly():
    result = report_length('')
    assert result == 'This string was 0 characters long.'

def test_10_character_length_returned_correctly():
    result = report_length('Horse Dogg')
    assert result == 'This string was 10 characters long.'