user_input = int(input("Nhap mot so nao do vao day: "))


def checkSNT(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,user_input // 2):
            if user_input % i == 0:
                return False
            else:
                return True

if checkSNT(user_input) == True:
    print("Day la so nguyen to")
else:
    print("Day ko la so nguyen to")            
        