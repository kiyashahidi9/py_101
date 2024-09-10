# 1
# ask user for first int input
# ask user for second int input
# add the two numbers and set it to sum
# print the sum using an f string

# 2
# set a variable to a list of strings
# i think there is a <sep>.join() method
# display the join method

#strings = ['hello', 'world', 'crazy', 'world',]
#joined_strings = ' '.join(strings)
#print(joined_strings)

# 3
# set a variable to a list of integers
# set a iterable variable
# set a new list variable
# while the iterable variable is less than len of list
#   append the current index of the list to new list
#   add two to the iterable

# def every_other(list):
#    new_list = []
 #   iterable = 0

  #  while iterable < len(list):
   #     new_list.append(list[iterable])
    #    iterable += 2

  #  return new_list

#int_list = [3, 4, 5, 3, 6]
#print(every_other(int_list))

# 4
# function should define a list and char variable
# set an occurence variable
# set an index variable
# while the index variable is less than the len of list
#   if occurence is 3, return index
#   if the current index equals the char, occurence plus 1
#   index plus 1
#def third_occur(list, char):
#    occurence = 0
#    index = 0
#    while index < len(list):
#        if list[index] == char:
#            occurence += 1
#        if occurence == 3:
#            return index
#        
#        index += 1
#    return None
#print(third_occur('axbxdcxex', 'x'))

# 5
# set list1 and list2 variables to function
# set an even_list and an odd_list variable to empty set
# set a joined_list variable to list1 plus list2
# for every element in joined_list, 
#   if element is even, add even list
#   else add to odd list
# joined_list equals even_list plus odd_list