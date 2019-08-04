list=["a","bc","d"]
nbr = len(list)


def affiche(list):
    for item in list :
     print(item)




#Indexing
print(list[0]) #return a
print(list[0:2]) #return a , b

print(len(list)) #return 3 because we have 3 elements in our list

#List Methods
#append method allows us to add an item to the last of the list
list.append("e")
print("est ",len(list)) #return a ,bc ,d ,e
affiche(list)
#The extend method adds the characters found in the given string in the end of the list
list.extend("fj")
affiche(list)      #return a ,bc ,d ,e ,f ,j
#The reverce method reverce the list given => the first will be the last item
#NB : it's does'nt take paramatre
list.reverse()

#The Sort method change list so that it's sorted in alphabetical order
list.sort()

#this fun return number of characters found in the all of list
def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total

print(total_length(list))