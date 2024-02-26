# Linear Search Algoithm

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


