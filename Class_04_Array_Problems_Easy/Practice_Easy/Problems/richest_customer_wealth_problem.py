# You are given an m x n integer grid accounts where accounts[i][j]
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

input_accounts = [[2,8,7],[7,1,3, 100],[1,9,5]]
# Output: 17
print(sum(input_accounts[0]))

def find_max (input_list) :

    max_networth = 0
    for person in input_list :
        temp_sum = 0
        for bank in person :
            temp_sum += bank
        if temp_sum > max_networth : max_networth = temp_sum

    return max_networth

print(find_max(input_accounts))

        



# def find_min_max (input_list):

#     #Initiate min and max variable
#     min = input_list[0]
#     max = input_list[0]

#     #loop through list
#     for val in input_list :

#         #if our variable > max, max = variable
#         if val > max : max = val

#         #if our vaiable < min, min = variable
#         if val < min : min = val

#     #return min and max
#     return min , max



# my_list = [1, 2, -1, 5, 10]


# print(find_min_max(my_list))


# def find_missing_value (input_list):
#     #loop through list
#     for i in range(len(input_list)) :
#         #see if value is equal to previous value - 1
#         if (input_list[i]) != (input_list[i + 1] - 1) :
#             return (input_list[i] + 1)


test_list = [10, 11, 12, 14, 15, 16]


# print(find_missing_value(test_list))
    

# def find_missing_value (input_list):

#     length_list = len(input_list)
#     found = False
#     cur_position = 0
#     min = input_list[0]
#     max = input_list[length_list - 1]

#     while found != True :
#         input_list[cur_position]

