vowels = ['a','e','i','o','u'] #given vowels list

print("enter a character: \n")#ask for input

c = input()

#if character is in list vowels
#print vowel else print consonant
if c in vowels:
    print("Its a vowel")
else:
    print("its a consonant")
