import time
#Some Functions and Exercice with while loop

def tcheck_pass ():
    while input("password : ") != "sidali" :
        print("wrong !Try again !")
    print("Correct ,Comme on in ;) ")

tcheck_pass()

#fonction print from 1 to 10
n=1
while n<=10 :
    print(n)
    time.sleep(1)   #This ligne make python pause 1 second
    n+=1
print("from 1 to 10 done")


#This function asks the user to enter a word if the one already exists ill go out of the program
def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words

no_repeating()

#Fond x and y that x*y = 512
def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                 break   # does not do what we want!
    return f"{x} * {y} == 512"

print(find_512())