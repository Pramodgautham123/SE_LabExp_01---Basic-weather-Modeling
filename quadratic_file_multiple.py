import math
with open("input.txt", "r") as file:
    for line in file:
        a, b, c = map(float, line.strip().split())
        D = b**2 - 4*a*c
        print(f"\nEquation: {a}x² + {b}x + {c} = 0")
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print("Roots are real and distinct:", x1, x2)
        elif D == 0:
            x = -b / (2*a)
            print("Roots are real and equal:", x)
        else:
            print("No real roots")
