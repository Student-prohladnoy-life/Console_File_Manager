import math


def test_math_pi():
    assert round(math.pi, 2) == 3.14, 'Test failed!!!'

def test_math_sgrt():
    assert math.sqrt(4) == 4 ** (0.5), 'Test failed!!!'
    assert math.sqrt(16) == 4, 'Test failed!!!'

def test_math_pow():
    assert math.pow(4, 0.5) == 4 ** 0.5, 'Test failed!!!'
    assert math.pow(3, 3) == 27, 'Test failed!!!'
    assert math.pow(4, -1) == 0.25, 'Test failed!!!'
    assert math.pow(4, -0.5) == 0.5, 'Test failed!!!'

def test_math_hypot():
    assert math.hypot(2, 4) == (2 ** 2 + 4 ** 2) ** 0.5, 'Test failed!!!'
    assert math.hypot(-2, 0) == 2, 'Test failed!!!'
    assert math.hypot(0, 2) == 2, 'Test failed!!!'

def test_sorted():
    assert sorted([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9], 'Test failed!!!'
    assert sorted([8,4,9,2,5], reverse=True) == [9, 8, 5, 4, 2], 'Test failed!!!'


def test_map():
    assert list(map(lambda x: x ** 4, [2, 4, 8])) == [16, 256, 4096], 'Test failed!!!'
    assert list(map(int, ['1', '5', '9'])) == [1, 5, 9], 'Test failed!!!'

def test_filter():
    assert list(filter(lambda x: x > 0, [-96, -5, -2, 0, 2, 5, 86])) == [2, 5, 86], 'Test failed!!!'
    assert list(filter(lambda x: -2 < x < 4, [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6,])) == [-1, 0, 1, 2, 3], 'Test failed!!!'