def flatten_and_sort(array):  # Define the function
    arr = []  # Initialize an empty list to collect flattened items
    for item in array:  # Loop through each element in the outer array
        for i in item:  # Loop through each element in nested lists
            arr.append(i)  # Add each element to the flattened list
    return sorted(arr)  # Return the sorted flattened list

print(flatten_and_sort([["c"], ["d"], ["e", "f"], ["l"]]))


'''
# How does this solution ensure data immutability?
    # creates a new list arr and does not modify the input array

# Is this solution a pure function? Why or why not?
    # Yes, it only depends on its input array and returns the same output every time for the same input

# Is this solution a higher order function? Why or why not?
    # No because it doesnt take any functions as arguments or return a function 

# Would it have been easier to solve this problem using a different programming style?
    # Depends on the pregrammer?

# Why in particular is functional programming a helpful paradigm when solving this problem?
    # Functional programming helps in creating predictable and reliable code
'''
