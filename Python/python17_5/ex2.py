# Tinh tong cac chu so trong so
def sum_digit(n):
    if n <10:
        result = n
    else:
        result = n%10 + sum_digit(n//10)
    return result

n = int(input("nhap so can tinh tong cac chu so: "))

print(sum_digit(n))