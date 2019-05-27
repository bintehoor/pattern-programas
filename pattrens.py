# python pattrens programs assignment
print("------------------------(pattren 1)------------------------")
n =int(input("Enter Number of Rows: "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end="")
    print()


print("------------------------(pattren 2)------------------------")

n =int(input("Enter Number of Rows: "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row,end="")
    print()

print("------------------------(pattren 3)------------------------")

n =int(input("Enter Number of Rows: "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end="")
    print()

print("------------------------(pattren 4)------------------------")
a =int(input("Enter Number of Rows: "))
for i in range(1,a+1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range((a-1),0,-1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("------------------------(Dimond Pattren)------------------------")
a =int(input("Enter Number of Rows: "))
for i in range(1,a+1):
    print(' '*(a-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range((a-1),0,-1):
    print(' '*(a-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("------------------------(pattren 5)------------------------")

a =int(input("Enter Number of Rows: "))
for i in range(1,a+1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range((a-1),0,-1):
    print(' '*(a-i))
    for j in range(1,i+1):
        print(j,end=" ")
    print()

