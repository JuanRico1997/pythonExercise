
x = 1
y = 5
c = 0
j = 3
while (c<3):
    if (j%2 != 0):
        print("*" * y)
        x+=1
    elif(j%2==0):
        print(" " * (x+1))
        print("*" * y)
    x+= 1
    y-=2
    c+=1

