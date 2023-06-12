from lib.string_builder import *

def test_str_is_blank_when_initialised():
    string_builder = StringBuilder()
    assert string_builder.size() == 0
    assert string_builder.output() == ""

def test_add_string_to_blank_returns_correctly():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    assert string_builder.size() == 5
    assert string_builder.output() == "Horse"

def test_add_string_to_existing_string_returns_correctly():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    string_builder.add(" ")
    string_builder.add("shoe")
    assert string_builder.size() == 10
    assert string_builder.output() == "Horse shoe"