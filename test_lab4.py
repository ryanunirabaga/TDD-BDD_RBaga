import pytest


class Calculator:
        def __init__(self, name):
            self.name = name
        
        def add(self, a, b):
            return a + b
        
        def subtract(self,a ,b):
            return  a - b
        
        def multiply(self,a ,b):
            return  a * b
        

@pytest.fixture

def base_calculator():
    return Calculator("Base Calculator")


def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True


def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True
    

calc = Calculator('my Calculator')

# test subtract
def test_subtract_a():
    assert calc.subtract(-1, -4) == 3


def test_subtract_b():
    assert calc.subtract(5, -4) == 9
    

def test_subtract_c():
    assert calc.subtract(0, -4) == 4


# test multiply
def test_multiply_a():
    assert calc.multiply(1, -2) == -2


def test_multiply_b():
    assert calc.multiply(-9, -2) == 18

    
def test_multiply_c():
    assert calc.multiply(0.5, -7) == -3.5
