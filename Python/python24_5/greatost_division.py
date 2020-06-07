import random
def check_division(num):
    division_array =[]
    for i in range(1,num):
        check = num%i
        if check == 0:
            division_array.append(i)
    return division_array




def greatost_division(num1,num2):
    check_array=[]
    num1_division_array = check_division(num1)
    num2_division_array = check_division(num2)
    
    for n in range(len(num1_division_array)):
        if num1_division_array[n] == num2_division_array[n]:
            check_array.append(num1_division_array[n])
    return max(check_array)

print(greatost_division(6,8))



# FIXXXXXXXX USING RECURSION

def greatest_division(a,b):
    if a ==b:
        result = a
    elif a>b:
        result = greatest_division(b,a-b)
    else:
        result = greatest_division(a,b-a)
    return result
print(greatest_division(random.randint(100000000, 9999999999),random.randint(100000000000000000000000000000000, 9999999999999999999999999999999999999999999999999999999999)))