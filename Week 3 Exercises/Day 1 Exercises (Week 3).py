# Bubble Sort Algorithm

# Explained:
# This algortithm tasks an unsorted list and orders it in ascending value from lowest to highest
# by comparing values one and two then moving the highest value to the second position if not already present
# then switchs to values two and three moving the highest value to the second position, etc

# Code

def bubble(unsorted_list):
    unsorted_list_length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, unsorted_list_length):
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list

print(bubble([765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]))

# Extra List Code Results

# 1 = 0.363
# 2 = 0.406
# 3 = 0.4
# 4 = 0.374
# 5 = 0.377

# Insertion Sort Algorithm

# Explained:
# The way insertion sort works by taking a unsorted list and divide it into two lists 'sorted' and 'unsorted' by placing the first
# value into sorted once the algorithm starts its takes the value on the left most position in the unsorted list and moves it
# into the sorted list then compares that same value to the value on its left in the sorted list and if that value is smaller 
# it switchs positions with the value of left, this same value keeps getting compared with the value on the left and switching
# until it compares with a value smaller then it, in which case the value is now in its proper place on the list

# Code
def insertion(unsorted_list):
    unsorted_list_length = range(1, len(unsorted_list))
    for i in unsorted_list_length:
        value_to_sort = unsorted_list[i]

        while unsorted_list[i-1] > value_to_sort and i > 0:
            unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1], unsorted_list[i]
            i = i - 1
    return unsorted_list

print(insertion([765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]))

# Extra List Code Results

# 1 = 0.46
# 2 = 0.41
# 3 = 0.425
# 4 = 0.522
# 5 = 0.38