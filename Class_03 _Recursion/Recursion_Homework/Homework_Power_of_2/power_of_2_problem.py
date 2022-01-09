# Given an integer n, return True if it is a power of 2. 
# An integer n is a power of two, if there exists an integer x such that n == 2^x

# Examples:

# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False


myInput = int(input("What number do you want to try? "))

def divide_by_two(num):

    num = num/2
    if num == 1 or num == 2:
        return True
    elif num % 2 != 0 :
        return False
    else :
        return divide_by_two(num)



isDivTwo = divide_by_two(myInput)
print(isDivTwo)