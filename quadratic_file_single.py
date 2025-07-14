with open("input.txt", "r") as file:
    line = file.readline()
    a, b, c = map(float, line.split())

D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots:", x1, x2)
else:
    print("No real roots")
