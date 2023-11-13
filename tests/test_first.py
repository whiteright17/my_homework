import pytest
from src import my_func

def test_add_one():
    assert my_func.addition(3,4) == 7
def test_add_two():
    assert my_func.addition(5,5) == 10
@pytest.mark.skip('Negative test')
def test_add_three():
    assert my_func.addition(3,3) == 8

def test_sub_one():
    assert my_func.subtraction(10,2) == 8
def test_sub_two():
    assert my_func.subtraction(50,2) == 48
@pytest.mark.skip('Negative test')
def test_sub_three():
        assert my_func.subtraction(10, 2) == 5

def test_mul_one():
    assert my_func.multiplication(1,2) == 2
def test_mul_two():
    assert my_func.multiplication(3,2) == 6
@pytest.mark.skip('Negative test')
def test_mul_three():
    assert my_func.multiplication(3,2) == 8

def test_div_one():
    assert my_func.division(10,2) == 5
def test_div_two():
    assert my_func.division(100,2) == 50
@pytest.mark.skip('Negative test')
def test_div_three():
    assert my_func.division(5,0) == 'Division by zero is not allowed'
