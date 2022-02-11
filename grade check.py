print("Enter your obtained markes")
sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())
sub6 = int(input())


total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
avg = total/6

if avg >= 91 and avg <= 100:
    print("You got A+")
elif avg >= 81 and avg <= 91:
    print("You got A")
elif avg >= 71 and avg <= 81:
    print("You got B+")
elif avg >= 61 and avg <= 71:
    print("You got B")
elif avg >= 51 and avg <= 61:
    print("You got C+")
elif avg >= 41 and avg <= 51:
    print("You got C")
elif avg >= 31 and avg <= 41:
    print("You got D+")
elif avg >= 21 and avg <= 31:
    print("You got D")
elif avg >= 0 and avg <= 21:
    print("You got E+")
else:
    print("Invalid input!")
