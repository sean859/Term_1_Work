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
print(bubble([67, 12, 89, 43, 56, 34, 78, 23, 91, 45,
               18, 76, 39, 52, 87, 65, 29, 83, 16, 72,
                 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]))
