# Tinh giai thua cua so nao do

def factorial(n):
    if n == 1:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

n = int(input("Nhap so can tinh giai thua: "))
print(factorial(n))