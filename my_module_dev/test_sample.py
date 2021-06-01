# content of test_sample.py
from my_module import my_thing


def test_answer():
    assert my_thing.func(3) == 4
