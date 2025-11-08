# EVEN OR ODD
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

# SUM OF N
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

# SUM OF SQUARES
# def sum_of_sq(n):
#     if n == 1:
#         return 1
#     return (n-1) + n**2

# print(sum_of_sq(3))

# FIND CLOSEST TO N, DIVISIBLE BY M
# n = 13
# m = 4
# closest = 0

# for i in range(n, 0, -1): # 13 => 1
#     if i % m == 0: # 12, 8, 4, 0
#         closest = i
#         break

# print(closest)