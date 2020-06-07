def merge(left_list, right_list):
sorted_list = []
left_list_index = 0
right_list_index = 0

left_list_length, right_list_length = len(left_list), len(right_list)

for _ in range(left_list_length + right_list_length):
if left_list_index < left_list_length and right_list_index < right_list_length:
# We check which value from the start of each list is smaller
# If the item at the beginning of the left list is smaller, add it to the sorted list
if left_list[left_list_index] <= right_list[right_list_index]:
sorted_list.append(left_list[left_list_index])
left_list_index += 1
# If the item at the beginning of the right list is smaller, add it
# to the sorted list
else:
sorted_list.append(right_list[right_list_index])
right_list_index += 1

# If we've reached the end of the of the left list, add the elements
# from the right list
elif left_list_index == left_list_length:
sorted_list.append(right_list[right_list_index])
right_list_index += 1
# If we've reached the end of the of the right list, add the elements
# from the left list
elif right_list_index == right_list_length:
sorted_list.append(left_list[left_list_index])
left_list_index += 1

return sorted_list