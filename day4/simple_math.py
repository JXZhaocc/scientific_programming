"""
A collection of simple math operations
"""

def simple_add(a,b):
    """ 
    Add two numbers together.
    
    Parameters
    ----------
    a: one input number
    b: one input number

    Returns
    ----------
    a + b : sum of the two numbers

    Examples
    ----------
    >>> simple_math.simple_add(2,3)
    5 
    
    """
    return a+b

def simple_sub(a,b):
    """ Subtract b from a"""
    return a-b

def simple_mult(a,b):
    """Multiply two numbers"""
    return a*b

def simple_div(a,b):
    """Divide two numbers"""
    return a/b

def poly_first(x, a0, a1):
    """ First order polynomial"""
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """ Second number polynomial"""
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
