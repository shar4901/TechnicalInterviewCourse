import time
import datetime
# def fibonacci (a, b, repTarget, rep) :
#     if rep == repTarget :
#         return a
#     else  :
#         a, b = b, a + b
#         rep += 1
#         return fibonacci(a, b, repTarget, rep)


# print(fibonacci(1, 1, 9, 1))


# def fibonacci (n) :
#     if n == 0 or n == 1:
#         return n
#     else : return fibonacci(n-1) + fibonacci(n-2)

# time_start = datetime.now()
# print(fibonacci(6))
# time_stop = datetime.now()
# total_time = time_start - time_stop
# print(total_time)

# def recursion (my_string) :
#     if my_string == "" :
#         return ""
    
#     return recursion(my_string[1:]) + (my_string[0])


# print(recursion('spencer'))

# def pal (my_string) :
#     if my_string[0] != my_string[-1] :
#         return False
#     elif len(my_string) <= 2 :
#         return True
    
#     return pal(my_string[1:-1])


# print(pal('abcfjklsdldcba'))

def sum_num(num) :
    if num == 0:
        return 0
    else :
        return (num -1) + (sum_num(num -1))


print(sum_num(5))





        
