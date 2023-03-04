import random

alphabet = list("abcdefghijklmnopqrstuvwxyz") #converts the string into a list


del alphabet[3:5] #deletes d and e
alphabet.remove("z") #searches for, finds, and deletes z in the list
alphabet.insert(0,"1") #inserts the number 1 so that its index is 0
print(alphabet)

random.shuffle(alphabet) #shuffles items in a list randomly
for index, item in enumerate(alphabet): #allows the use of both index and value in a list with a loop
    print(alphabet[index],end="") #prints without newline character at the end, but with a blank nothingness instead
print()

alphabet.sort(key=str.lower) #sorts list alphabetically and numerically, with numbers further left than letters. Forces all letters to lowercase 
print(alphabet)              #so that the list does not sort, say lowercase a after uppercase Z

alphabet.sort(reverse = True, key=str.lower) #sorts list in reverse, with numbers further right than letters
print(alphabet)
#sorting can only be done with strings inside the array, not integers

random.shuffle(alphabet)
alphabet.reverse()
print(alphabet)

print(id("Howdy"))

