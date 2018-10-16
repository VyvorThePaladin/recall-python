# Accepts n by n matrix from user and
# computes the absolute diagonal difference

# Enter value of n and then enter the matrix
print(abs(sum((lambda arr: int(arr[x]) - int(arr[len(arr) - x - 1]))
              (input().split()) for x in range(int(input())))))
