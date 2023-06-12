from lib.gratitudes import *

def test_list_is_empty_when_initialised():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_string_added_to_empty_list_returns_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("being on this course")
    assert gratitudes.format() == "Be grateful for: being on this course"

def test_string_added_to_list_returns_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("being on this course")
    gratitudes.add("the weather")
    gratitudes.add("whatever you like")    
    assert gratitudes.format() == "Be grateful for: being on this course, the weather, whatever you like"