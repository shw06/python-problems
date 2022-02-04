print("Printing curren number and previous number sum in range (10)")

previous_num = 0

for i in range(1,11):
      x_sum = previous_num + i
      print("current number", i,"previous number ",previous_num, "sum: ", previous_num + i)

      previous_num = i
