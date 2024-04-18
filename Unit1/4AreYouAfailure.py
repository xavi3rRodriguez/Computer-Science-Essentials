print("did you fail? calculator")
x = float(input('what was the total points posible: '))
print(x)
a = float(input('what did you get: '))
print(a)
c = float(a / x)*100
print(c)
if c < 60:
    print("fail")
else:
    print("pass")