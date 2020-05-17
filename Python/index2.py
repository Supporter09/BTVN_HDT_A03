array = [1,3,4,16,32,8,64,4,128,2,256,32]

for i in range(len(array)):
    for j in range(1,len(array)):
        if i != j :
            tich = array[i] * array[j]
        
            if tich == 256:
                    print(array[i],'va',array[j],'o vi tri so',i,'va',j)
                    array[i]=0
                    array[j]=0
                
                