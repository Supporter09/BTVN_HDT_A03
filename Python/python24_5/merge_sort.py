list = [5,1,3,8,12,10]
result_array =[]
# def merge(list1,list2):
    
#     return result_array

# def merge_sort(nums):
#     # If the list is a single element, return it
#     if len(nums)<=1:
#         return nums
    
#     #  Use floor division to get midpoint, indices must be intergers
#     mid = len(nums)//2

#     # Sort and merge each half
#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])

#     # Merge the sorted lists into new one
#     i = j = k = 0
#         # Copy data to temp arrays L[] and R[] 
#     while i < len(left_list) and j < len(right_list): 
#         if left_list[i] < right_list[j]: 
#             result_array[k] = left_list[i] 
#             i+=1
#         else: 
#             result_array[k] = right_list[j] 
#             j+=1
#         k+=1
#         # Checking if any element was left 
#     while i < len(left_list): 
#         result_array[k] = left_list[i] 
#         i+=1
#         k+=1
#     while j < len(right_list): 
#         result_array[k] = right_list[j] 
#         j+=1
#     k+=1
#     # merge(left_list,right_list)
#     return result_array
#     # Xoa het phan tu array
    
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 

        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 

        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr



print(mergeSort(list))








