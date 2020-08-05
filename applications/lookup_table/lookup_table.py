# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y) # power exponents -- x to the power of y
    v = math.factorial(v) # factorial is 1 * 2 * 3 * 4 * ...n-1 * n (or v)
    v //= (x + y) # take factorial number, floor divide by (x+y) and reassign
    v %= 982451653 # newest v modulo by this number

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    cache = {
        "x": x,
        "y": y
    }
    
    if (x, y) not in cache:
        cache["x"] = x
        cache["y"] =y
    
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y) 
    v %= 982451653

    return v



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
