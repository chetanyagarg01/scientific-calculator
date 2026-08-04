def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def expo(x, y): 
    return x ** y

def log(x, base):
    import math
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error! Logarithm undefined for given values."
def sqrt(x):
    import math
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Square root of negative number is undefined."
def factorial(x):
    import math
    if x >= 0 and int(x) == x:
        return math.factorial(int(x))
    else:
        return "Error! Factorial is undefined for negative numbers or non-integers."
def trig (a, b): 
    import math
    if a == 'sin':
        return math.sin(math.radians(b))
    elif a == 'cos':
        return math.cos(math.radians(b))
    elif a == 'tan':
        return math.tan(math.radians(b))
    else:
        return "Error! Invalid trigonometric function."
def percent(a, b):
    if b != 0:
        return (a / b) * 100
    else:
        return "Error! Division by zero."
def perm(a, b):
    import math
    if a >= 0 and b >= 0 and a >= b:
        return math.factorial(a) / math.factorial(a - b)
    else:
        return "Error! Invalid values for permutation."
def comb(a, b):
    import math
    if a >= 0 and b >= 0 and a >= b:
        return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))
    else:
        return "Error! Invalid values for combination."
def prime(a): 
    b = 0
    if a > 1: 
        for i in range ( 2, int(a/2) + 1): 
            if (a % i) == 0: 
                b = 1
                break
    if a <= 1:
        print("Error! Number must be greater than 1.")
    return b 
