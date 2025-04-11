import pytest
import math
from calc import Calculator

calculator = Calculator()

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(0, 0) == 0
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, 1) == -2

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(0, 0) == 0
    assert calculator.multiply(-1, 1) == -1

def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(0, 5) == 0
    assert calculator.divide(-1, 1) == -1
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(0, 0) == 1
    assert calculator.power(-1, 2) == 1

def test_square_root():
    assert calculator.square_root(9) == 3
    assert calculator.square_root(0) == 0
    with pytest.raises(ValueError):
        calculator.square_root(-1)

def test_sin():
    assert math.isclose(calculator.sin(math.pi/2), 1, rel_tol=1e-9)

def test_cos():
    assert math.isclose(calculator.cos(0), 1, rel_tol=1e-9)

def test_tan():
    assert math.isclose(calculator.tan(math.pi/4), 1, rel_tol=1e-9)

def test_log():
    assert math.isclose(calculator.log(math.e), 1, rel_tol=1e-9)
    with pytest.raises(ValueError):
        calculator.log(0)
        calculator.log(-1)


