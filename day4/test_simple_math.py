from simple_math import simple_add, simple_div, simple_mult,simple_sub

def test_simple_add():
    assert simple_add(0,1) == 1

def test_simple_sub():
    assert simple_sub(5,3) == 2

def test_simple_div():
    assert simple_div(6,3) == 2

def test_simple_mult():
    assert simple_mult(5,3) == 15