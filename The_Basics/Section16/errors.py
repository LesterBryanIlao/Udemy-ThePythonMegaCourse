x = int(input("x: "))
y = int(input("y: "))

try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)