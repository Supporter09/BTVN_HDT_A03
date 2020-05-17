from math import sqrt

print("Day la mot pt bac 2 tong quat: ax^2 + bx +c =0")
print("nhap cac so a,b,c vo day thang cho: ")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

def Quadro(a,b,c):
    delta = pow(b,2) - 4*(a*c)
    if delta < 0:
        print("Pt deo co nghiem")
    elif delta == 0:
        root = -b/(2*a)
        return root
    elif a>0:
        root1 = (-b + sqrt(delta))/(2*a)
        root2 = (-b - sqrt(delta))/(2*a)
        return root1,root2

print(Quadro(a,b,c))