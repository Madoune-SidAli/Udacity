#Indexing
#NB : all the string start by index 0
print("Sid Ali"[0])
print("Madoune"[-1])

#Slicing
# the slice methis has 2 parametres => form the first index to the second one
print("Sid Ali"[0:3]) #return Sid
print("Sid Ali"[4:])  #return ALI

#Concatination
a = 5 + 5
print(a)
print("31" + "31")
#print(5+"51") this will case error because we  cant add string with an integer


#String Methods
#Startwith fonction return True Or False
print("madoune".startswith("mad")) #return True
print("madoune".startswith("sid")) #return True

#String to Integer
"""In this next exercise, your goal is to write a program that asks the user
for three numbers, adds those numbers up, and then prints a message saying what the sum is. """
n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
n3 = input("Enter a third number: ")
sum = int(n1) + int(n2) + int(n3)

#There are two  cases :
#The First One is :
print(f"{n1} + {n2} + {n3} = {sum}")

#The Second one is  :
print(n1 + ' + ' + n2 + ' + ' + n3 + ' = ' + str(sum))
