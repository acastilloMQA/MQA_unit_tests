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
