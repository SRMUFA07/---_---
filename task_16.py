# №1
# def F(n):
#     if n <= 2:
#         return 2
#     if n > 2:
#         return F(n - 1) + 2 * F(n - 2)
# print(F(5))



# №2
# def F(n):
#     if n == 1:
#         return 2
#     if n >= 1:
#         return F(n - 1) * n
# print(F(5))



# №3
# def F(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return F(n // 2)
#     if n % 2 != 0:
#         return 1 + F(n - 1)
# print(len([n for n in range(1, 1001) if F(n) == 3]))



# №4
# import sys
# sys.setrecursionlimit(10**6) # повысил лемит на рекурсию, чтобы не возникало ошибки RecursionError
# def F(n):
#     if n < 11:
#         return 10
#     if n >= 11:
#         return n + F(n - 1)
# print(F(2022) - F(2019))



# №5
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n - 1) + n
# print(F(30))



# №6
# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + F(n - 1)
#     if n > 1 and n % 2 != 0:
#         return 2 * F(n - 2)
# print(F(26))




# №7
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3
#     if n > 2:
#         return F(n - 1) * n + F(n - 2) * (n - 1)
# print(F(5))


# №8
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n - 1) * (n + 2)
# print(F(5))


# №9
# import sys
# sys.setrecursionlimit(10**6)
# def F(n):
#     if n < 7:
#         return 7
#     if n >= 7:
#         return 2 * n + F(n - 1)
# print(F(2024) - F(2022))


# №10
# def F(n):
#     if n == 1:  
#         return 1
#     if n == 2:  
#         return 2
#     if n > 2:
#         return 2 * F(n - 1) + (n - 2) * F(n - 2)
# print(F(6))


def F(n):
    if n==1: 
        return 1
    if n==2:
        return 2
    if n>2:
        return 3 * F(n-1) - F(n-2)
print(F(8))