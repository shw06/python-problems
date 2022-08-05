import random
import array

from passlib.hash import pbkdf2_sha256

# give max length
max_length = 12

#give digits to choose from
digits = ['0','1','2','3','4','5','6','7','8','9']

#lower case and upper case characters to choose from
lower_case_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
upper_case_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
#symbols
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

combine_list = digits + lower_case_char + upper_case_char + symbols

#to randomly choose from lists
rand_digit = random.choice(digits)
rand_upper = random.choice(upper_case_char)
rand_lower = random.choice(lower_case_char)
rand_symbol = random.choice(symbols)

#dummy password which contains only 4 chars
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

#to get 12 characters we will minus these four from the max-len
#and then randomly shuffle again to get the rest chars

for i in range(max_length - 4):
    temp_pass = temp_pass + random.choice(combine_list)


    #now convert the password into an array
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

#now to append the array and form password
password = ""
for i in temp_pass_list:
    password = password + i

print(password)


hash_pass = input("Now do you want to hash this password in SHA: ")

if hash_pass == "yes" or hash_pass == "Yes" or hash_pass == "YES":
    password = pbkdf2_sha256.hash(password)
    print("Your hashed password is: \n", password)
elif hash_pass == "No" or hash_pass == "no":
    print("Okay congratulations")

