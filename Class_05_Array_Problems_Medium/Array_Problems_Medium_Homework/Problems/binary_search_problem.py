# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

#from sys import last_traceback


input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
# Output = 2


def binary_search(linput, n):
    lower = 0
    upper = len(linput) - 1

    while lower <= upper :
        mid = (upper + lower) // 2

        if linput[mid] == n :
            return mid 

        else :
            if linput[mid] < n :
                lower = mid + 1
            else :
                upper = mid - 1

    return -1

print(binary_search(input_array, input_target))
