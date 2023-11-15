import pytest
from src import my_func

@pytest.mark.parametrize("a, b, c", [(1, 2, 3)])
def test_add_one(a,b,c):
    assert my_func.addition(a,b) == c
def test_add_two():
    assert my_func.addition(5,5) == 10
@pytest.mark.skip('Negative test')
def test_add_three():
    assert my_func.addition(3,3) == 8

@pytest.mark.parametrize("a, b, c", [(5, 2, 3)])
def test_sub_one(a,b,c):
    assert my_func.subtraction(a,b) == c
def test_sub_two():
    assert my_func.subtraction(50,2) == 48
@pytest.mark.skip('Negative test')
def test_sub_three():
        assert my_func.subtraction(10, 2) == 5

@pytest.mark.parametrize("a, b, c", [(5, 2, 10)])
def test_mul_one(a,b,c):
    assert my_func.multiplication(a,b) == c
def test_mul_two():
    assert my_func.multiplication(3,2) == 6
@pytest.mark.skip('Negative test')
def test_mul_three():
    assert my_func.multiplication(3,2) == 8

@pytest.mark.parametrize("a, b, c", [(10, 2, 5)])
def test_div_one(a,b,c):
    assert my_func.division(a,b) == c
def test_div_two():
    assert my_func.division(100,2) == 50
@pytest.mark.skip('Negative test')
def test_div_three():
    assert my_func.division(5,0) == 'Division by zero is not allowed'
