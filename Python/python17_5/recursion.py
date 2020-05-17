# Ha noi tower

user_num_input = int(input("Nhap so dia vao day thang cho:"))

def hannoi_tower_recursion(n):
    if n == 1: 
        result =1 
    else:
        result = 2 * (hannoi_tower_recursion(n-1)) +1
    return result
print(hannoi_tower_recursion(user_num_input))

# Cach giai deo dung de qui :