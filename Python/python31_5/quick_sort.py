def partition(array,start,end):

    # left_index = 1
    # right_index = end
    # while left_index <= right_index: 
    #     while left_index <= pivot:
    #         if array[left_index] < pivot:
    #             left_index+=1
    #         elif array[left_index] > pivot:
    #             result1 = left_index

            
    #     while right_index >= pivot:
    #         if array[right_index] > pivot:
    #             right_index -=1
    #         elif array[right_index] < pivot:
    #             result2 = right_index
    #     array[result1],array[result2] = array[result2],array[result1]
    #     print(array)
    # return array.index(pivot)

    i = start+1         # index of smaller element 
    pivot = array[start]     # pivot 

    for j in range(start , end): 

        # If current element is smaller than or 
        # equal to pivot 
        if   array[j] <= pivot: 
            # increment index of smaller element 
            i = i+1 
            if i <= end:
                array[i],array[j] = array[j],array[i] 
    if i<7:
        array[i+1],array[end] = array[end],array[i+1] 
    return ( i+1 ) 



def quick_sort(array, start,end):
    if start >= end:
        return
    p= partition(array, start, end)
    quick_sort(array,start, p-1)
    quick_sort(array, p+1, end)

array = [5,4,2,9,7,8,3,6]
print(quick_sort(array,0, len(array)-1))