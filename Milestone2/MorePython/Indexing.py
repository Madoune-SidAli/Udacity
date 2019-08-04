""" a function called start_K that checks whether a string starts with the letter K.

If the string starts with K, the function should return True. If it doesn't, the function should return False."""


def start_K(s):
    if s[0] == "K":
        return True
    else:
        return False
# A function call like this should return True:
print("For Kelly it will be :" , start_K("Kelly"))

# And one like this should return False:
print("For Abe it will be :" , start_K("Abe"))