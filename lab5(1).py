import math

def f(x):
    if x >= 3.7:
        return x + math.sqrt(x) + (4 * x + 7) ** (1/3)
    elif -1.5 < x < 3.7:
        return math.tan(x) + x**2
    elif x <= -1.5:
        return math.log(abs(x))
    
x = float(input("Введіть значення x: "))
print(f"f({x}) = {f(x)}")