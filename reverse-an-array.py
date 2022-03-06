# Write a program to reverse an array or string

# iterative approach

def reverseList(A, start, end):
    while start < end: #as long as start is less than end
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

A =[1,2,3,4,5,6]
print(A)
reverseList(A, 0, 5)
print("reverseed list is: ")
print(A)


#recursive approach

def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# using list slicing


def reverseList(A):
  print( A[::-1])
     
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseList(A) 