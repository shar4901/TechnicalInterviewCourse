# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 4]
# Output = True


#first try
def duplicates (input_array) :
    duplicates = []
    for i in range(0, len(input_array)) :
        for j in range(0, len(input_array)) :
            if i != j and input_array[i] == input_array[j] :
                return True
    return False


    


#optimized try
def opt_duplicates (input_array) :
    num_count = {}
    for num in input_array :
        if num in num_count : return True
        else : num_count[num] = True
    return False


#antoher optimized try
def duplicates_sort (input_array):
    input_array.sort()
    for i in range(0, len(input_array)) :
        try:
            if input_array[i] == input_array[i + 1] : return True
        except:
            return False



