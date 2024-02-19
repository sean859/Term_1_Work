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

