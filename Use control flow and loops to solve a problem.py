
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11] # initialize the LIST  of numbers in jumbled order

num_list.sort() # this sorts the list of numbers in ascending order
count = 0
for index, value in enumerate(num_list):# this iterates over the numbers in the var num_list
    # print(i)  this prints the iterated and sorted list of numbers
    if value == 36:
        count += 1
        print("Number and position found at: " , index , " ", value )
        break
    if value >= 45: #this checks if the number in the list  is over 45
        print("Over 45") #if a number is found to be under the number 45
        print(value)
    else:
        print("Under 45")
        print(value)
print(count)