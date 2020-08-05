# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y) # power exponents -- x to the power of y
    v = math.factorial(v) # factorial is 1 * 2 * 3 * 4 * ...n-1 * n (or v)
    v //= (x + y) # take factorial number, floor divide by (x+y) and reassign
    v %= 982451653 # newest v modulo by this number

    return v

cache = {
    "powEx": 0,
    "factor": 0,
    "divide": 0,
    "modulo": 0
}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    powEx2 = math.pow(x, y)
    cache["powEx"] = int(powEx2)
    factorial2 = math.factorial(powEx2)
    cache["factorial"] = int(factorial2)
    divide2 = factorial2 // (x+y)
    cache["divide"] = int(divide2)
    mod2 = divide2 % 982451653
    return mod2
    
    print(f'powEx: {cache["powEx"]}')
    print(f'factorial2: {factorial2}')


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
