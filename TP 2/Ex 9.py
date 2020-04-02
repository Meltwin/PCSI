a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if (a >= b):
    if (b>=c):
        print("A >= B >= C")
    else:
        if (a>=c):
            print("A >= C >= B")
        else:
            print("C >= A >= B")
else:
    if (b>=c):
        if (a>=c):
            print("B >= A >= C")
        else:
            print("B >= C >= A")
    else:
        print("C >= B >= A")