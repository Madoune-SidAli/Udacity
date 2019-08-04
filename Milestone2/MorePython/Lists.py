list=["a","bc","d"]
nbr = len(list)

#Indexing
print(list[0]) #return a
print(list[0:2]) #return a , b

print(len(list))             #return 3 because we have 3 elements in our list

#List Methods
#append method allows us to add an item to the last of the list
list.append("e")
print(list)                  #return a ,bc ,d ,e


#The extend method adds the characters found in the given string in the end of the list
list.extend("fj")
print(list)                  #return a ,bc ,d ,e ,f ,j


#The reverce method reverce the list given => the first will be the last item
#NB : it's does'nt take paramatre
list.reverse()
print(list)


#The Sort method change list so that it's sorted in alphabetical order
list.sort()
print(list)

#This script about how join 2 list
first_list = [1, 2, 3]
second_list = [4, 5, 6]
for item in second_list:
    first_list.append(item)

print(first_list);


#this fun return number of characters found in the all of list
list2= ["1" ,"2" ,"3" ,"4"]
def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total

print(total_length(list2))