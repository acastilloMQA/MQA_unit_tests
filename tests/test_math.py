import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    expected = 3

    assert a + b == expected

def test_pass():
    pass

def test_multiply_two_positive_ints():
    assert 2 * 3 == 6

def test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0


datos = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 100, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, resultado', datos)
def test_multiplication(a, b, resultado):
    assert a * b == resultado
