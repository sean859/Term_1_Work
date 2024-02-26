# Linear Search Algorithm

# Explained:
# Linear search is a basic search engine where the user can input a number or word, that will be considered the 'search' value, then the algorithm will take that 'search' value and compare to every value in the list
# using a loop where it compares the 'search' value to a value in the list, if it dosen't match it goes to the next value, however if it does match then the loop breaks using a 'break' keyword and then the results
# can be printed to clarify

# Code
def linear_search(search_list, search_value):
    i = 0
    found = False

    while i < len(search_list):
        if search_list[i] == search_value:
            found = True
            value_location = i + 1
            break
        i = i + 1
    if found == True:
        print("The Value Was Found At", value_location)
    else:
        print("Value Was Not Found")
linear_search([3, 4, 6, 7, 12, 15, 9, 12], 85)


# Binary Search Algorithm

# Explained:
# The binary search takes a sorted list and creates a 'midpoint' being the number in the very middle of the list, and compares it to the 'search' number if they don't match it then creates a sublist filled with
# either lower or higher values then the 'midpoint' value if the 'search' value is higher or lower then the 'midpoint' basically if the number you searched is higher then the 'midpoint' it creates a sublist
# filled the values that are higher then the 'midpoint' and vice versa if its lower, then with this new sublist it repeats the process, making a 'midpoint' with the middle most number comparing it the 'search'
# value and if its lower or higher creates a new sublist with lower or higher values depending on the search, then it keeps repeating until the 'midpoint' is equal to the 'search' value and the cycle breaks

# Code
def binary_search(search_list, search_value):
    begin = 0
    end = len(search_list) -1

    while begin <= end:
        midpoint = begin + (end - begin) // 2
        midpoint_value = search_list[midpoint]
        if midpoint_value == search_value:
            return midpoint
        elif search_value < midpoint_value:
            end = midpoint - 1
        else:
            begin = midpoint + 1
    return "Value Not Found"
print(binary_search([12, 24, 30, 42, 55, 63, 75, 82, 91, 99], 12))



