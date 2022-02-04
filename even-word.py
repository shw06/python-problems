#take input from user
word = input("enter a word\n")
#print original word
print("Original word is", word)

#convert str in a list 
x = list(word)
for i in x[0::2]:
    print(i)
             
