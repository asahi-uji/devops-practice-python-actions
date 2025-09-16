import importlib
m = importlib.import_module("main")

def test_compute_sum_basic():
    assert m.compute_sum(2, 3) == 5

def test_compute_sum_zero():
    assert m.compute_sum(0, 0) == 0

def test_compute_sum_negative():
    assert m.compute_sum(-5, 10) == 5
