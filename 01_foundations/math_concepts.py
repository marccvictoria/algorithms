import math

# 1. EVEN OR ODD
# n = 2

# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# MULTIPLICATION TABLE
# n = 10
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end="\t")
#     print()

# 2. SUM OF N
# n = 3
# sum = 0

# for i in range(1, n + 1):
#     sum += i

# print(sum)

# recursion method

# def sum(n):
#     if n == 1:
#         return 1
#     return sum(n-1) + n

# print(sum(3))

# 3. SUM OF SQUARES
# def sum_of_sq(n):
#     if n == 1:
#         return 1
#     return (n-1) + n**2

# print(sum_of_sq(3))

# 4. FIND CLOSEST TO N, DIVISIBLE BY M
# n = 13
# m = 4
# closest = 0

# for i in range(n, 0, -1): # 13 => 1
#     if i % m == 0: # 12, 8, 4, 0
#         closest = i
#         break

# print(closest)

# 5. THE DICE PROBLEM
# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. 
# The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, 
# your task is to guess the number on the opposite face of the cube.

# Observe: Opposite sides equal to 7

# side = 4 # given
# opposite_side = 7 - side

# print(opposite_side) # 3

# 6. Nth term of AP from First Two Terms
# Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series. 

# a1 = 2
# a2 = 3
# n = 4 # find the value at 4th term

# diff = a2 - a1

# an = a1 + (n - 1) * diff

# print(an)


# 7. SUM OF DIGITS
# n = 687 # 6 + 8 + 7 = 21
# sum = 0

# while True:
#     sum += n % 10 # Extract the last digit
#     n = n // 10 # Remove the last digit

#     if n == 0:
#         break

# print(sum)


# 8. PRIME TESTING
# n = 11 # prime
# isPrime = True

# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         isPrime = False
#         break

# print(isPrime)

# 9. DISTANCE BETWEEN TWO POINTS
# You are given two coordinates (x1, y1) and (x2, y2) of a two-dimensional graph. Find the distance between them.

# x1, y1 = (3, 4)
# x2, y2 = (4, 3)

# dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# print(dist)

# 10. Check whether triangle is valid or not if sides are given
# a = 7 
# b = 10
# c = 5 

# if (a + b  <= c) or (a + c <= b) or (b + c <= a):
#     print("valid")
# else:
#     print("invalid")

# 11. Factorial
# iterative approach
# n = 10
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial) 

# # recursive approach
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(10))

# 12. Pair Cube Count
# Given n, count all 'a' and 'b' that satisfy the condition a^3 + b^3 = n. 
# Where (a, b) and (b, a) are considered two different pairs
# n = 9 # output: 2
# count = 0

# for a in range(n):
#     for b in range(n):
#         if n == a**3 + b**3:
#             count += 1

# print(count)

# another approach
# def countPairs(n):
#     count = 0
#     # Check for each number 1 to cbrt(n)
#     for i in range(1, int(math.pow(n, 1/3)) + 1):
#         # Store cube of a number
#         cb = i * i * i
#         # Subtract the cube from given n
#         diff = n - cb
#         # Check if the difference is also a perfect cube
#         cbrt_diff = round(diff ** (1/3))
#         # If yes, then increment count
#         if cbrt_diff * cbrt_diff * cbrt_diff == diff:
#             count += 1

#     return count

# if __name__ == "__main__":
#   n = 2
#   print(countPairs(n))