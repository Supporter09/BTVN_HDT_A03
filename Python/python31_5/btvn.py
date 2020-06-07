def minTiles(n,m):
    if n == 0 and m ==0:
        return 0
    
    elif n%2 == 0 and m %2==0:
        return minTiles(int(n/2), int(m/2))
    
    elif n%2 == 0 and m % 2== 1:
        return(n + minTiles(int(n/2), int(m/2)))

    elif  n%2 == 1 and m%2 ==0 :
        return ( m + minTiles(int(n/2), int(m/2)))

    else:
        return(n +m -1 + minTiles(int(n/2), int(m/2)))

print(minTiles(4,5))