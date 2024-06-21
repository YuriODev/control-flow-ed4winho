import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The roots are: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"The root is: {root}"
    else:
        return "No real roots exist."

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

print(find_roots(a, b, c))
