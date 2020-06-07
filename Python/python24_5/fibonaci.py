def fibonaci(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        result = fibonaci(n-1) + fibonaci(n-2)
        return result

user_input = int(input("Nhap mot so nao do va toi se cho ban ket qua :"))
print(fibonaci(user_input))

