# Pandas:

# Pandas is a library used in python for different data sets including Selection, Merge, Quick, etc.
# With functions including analyzing, cleaning, exploring, and manipulating data, also the name 'Pandas' refers to 
# both 'Panel Data' (Pan), and 'Python Data Analysis' (das) 

# PIP:

# Pip is a package manager for Python packages allowing the user to install and manage additional packages or modules
# that are not part of the standard python library, with packages almost being a box with all the files you need for a 
# specific module, well modules are python code libraries you can include in your project

# Venv 

# Allows the user to mangae separate package installations for different projects, being installed with Python 3, so basically 
# a folder that can be used to contain all your seperate packages for easy use later


# Selection sort

# Explained:
# Selection sort will take the first value's number and compare it every other values number on the right, till
# it gets compared to a smaller number in which case the smaller numb,,,er will become which number gets compared 
# with others, once its compared all the numbers, it should have the minimum number, now the number gets put
# into a sorted list on the left and now the others numbers are placed into a unsorted list at the end of
# an interation, then at the start of the next interation it takes the first value's number in the unsorted
# list and repeats the process till the all numbers are sorted in the sorted list from lowest to highest

# Code

def selection_sort(unsorted_list):
    list_length = range(0, len(unsorted_list)-1)

    for i in list_length:
        min_value = i

        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_value]:
                min_value = j
        
        if min_value != i:
            unsorted_list[min_value], unsorted_list[i], unsorted_list[i], unsorted_list[min_value]
    
    return unsorted_list
print(selection_sort([15, 16, 18, 3, 6, 9]))

# Merge Sort

# Explained:
# Merge sort is a conquer and divide algorithm by that it means that is breaks down a list given to it into smaller list called sub
# list then breaks those sub lists into even more sub lists until the sublist contains only one value then to sort it merges 
# two sub list together into one placing the lower number on the left and the higher on the right, then once all sub lists contain
# two values it merges those list into lists of 4, again putting the lowest value on the left side and continues from lowest to highest
# then it keeps repeating this process untill all sublists have merged into one sorted list with the numbers going from lowest to 
# highest 

# Code

def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result
def mergesort(lst):
    if(len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)
print(mergesort([67, 12, 89, 43, 56, 34, 78, 23, 91, 
                 45, 18, 76, 39, 52, 87, 65, 29, 83, 
                 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]))
