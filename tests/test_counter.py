from lib.counter import *

def test_adds_to_counter_1():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_adds_to_counter_2():
    counter = Counter()
    counter.add(4)
    counter.add(9)
    result = counter.report()
    assert result == "Counted to 13 so far."