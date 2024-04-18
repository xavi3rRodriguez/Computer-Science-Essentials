print("did you fail? calculator")
x = float(input('what was the total points posible: '))
print(x)
a = float(input('what did you get: '))
print(a)
c = float(a / x)*100
print(c)
if c >= 90:
    print("A")
elif c >= 80:
    print("B")
elif c >= 70:
    print("C")
elif c >= 60:
    print("D")
if c < 60:
    print("F")