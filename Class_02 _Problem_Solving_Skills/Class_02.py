#Count charachters in a string

sInput = input('What String Would You Like to Count?').lower()
oDictionary = {}

for char in sInput :
    if char != ' ':
        if char in oDictionary :
            oDictionary[char] += 1
        else :
            oDictionary[char] = 1

for k, v in oDictionary.items():
    print(k, ' ', v)
# print(oDictionary)