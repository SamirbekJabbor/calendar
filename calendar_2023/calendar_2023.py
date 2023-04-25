import calendar as c
y = int(input("yilni kiriting: "))
m = 0
while m < 12:
    m += 1
    print(c.month(y,m))
