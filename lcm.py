def calculate_lcm(x,y): #define function
    #decide which is a great number
    if x > y: 
        greater = x
    else:
        greater = y
    while(True): 
        if((greater % x == 0) and (greater % y == 0)):  #if num1/num2 % x is 0 and num1/num2 % y is 0 then lcm is the greater number
            lcm = greater
            break
        greater += 1  #if greater is not one of them then do greater + 1 to get the lcm
    return lcm

num1 = int(input("enter first number: "))
num2 = int(input("enter another number: "))
print("lcm is : ",calculate_lcm(num1,num2))
           
