nums =[16,2,4,2]

dictionary ={}
for index, item in enumerate(nums):
    number = item
    nums[index] = 0
    for index1, item1 in enumerate(nums):
        nums[index]=0
        dictionary[number] = [number,index,item1,index1]

for value in dictionary.values():
    print("result: {} - index {} and {}  - index {}".format(value[0],value[1], value[2],value[3] ))