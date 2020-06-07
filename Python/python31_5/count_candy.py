money = int(input("Nhap so tien ban co"))
candy_price = int(input("Nhap gia tien cua keo"))
candy_shell_trade = int(input("Nhap so vo keo can de lay mot cai keo"))

# def check_candy_shell(candy_shell,candy_shell_trade):
#     if candy_shell > candy_shell_trade:
#         return False
#     else:
#         return True
# def trade_candy(money,candy_price,candy_shell_trade):
#     candy = money // candy_price
#     candy_shell = candy
#     while check_candy_shell(candy_shell, candy_shell_trade) == False:
#         candy += candy_shell // candy_shell_trade
#         candy_shell = candy
#     check_candy_shell(candy_shell,candy_shell_trade)
#     return candy
    
    

# print(trade_candy(money,candy_price,candy_shell_trade))

def count_remain(choc,wrap):
    if (choc<wrap):
        return 0
    new_choc = choc // wrap
    return new_choc + count_remain(new_choc + choc%wrap, wrap)

def count_max_choco(money, price, wrap):
    choc = money // price
    return choc + count_remain(choc,wrap)

