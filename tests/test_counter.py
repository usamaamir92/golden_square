from lib.counter import *

def test_count_is_zero_when_initialised():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_number_is_added_correctly_to_count():
    counter = Counter()
    counter.add(15)
    assert counter.report() == "Counted to 15 so far."

def test_number_is_added_correctly_to_positive_count():
    counter = Counter()
    counter.add(25)
    counter.add(10)
    assert counter.report() == "Counted to 35 so far."