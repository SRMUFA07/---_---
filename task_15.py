# В1 числовая прямая
# A = set()
# def f(x, A):
#     return ((x in A) <= (x**2 <= 81)) and ((x**2 <= 36) <= (x in A))

# for x in range(-1000,1000):
#     if not f(x,A):
#         A.add(x)
# print(len(A) - 1)



# В2 ДЕЛ()
# def f(x, A):
#     # (A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 18)))
#     return (A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 18 != 0)))
    
#     # l1 = A < 50
#     # l2 = x % A != 0
#     # l3 = x % 10 == 0
#     # l4 = x % 18 != 0
#     # return l1 and (l2 <= (l3 <= l4))

# for A in range (1, 300): # диапазон можно менять 
#     flag = True
#     for x in range (1, 300): # диапазон можно менять 
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)

# В2.1
# def f(x, A):
#     return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

# for A in range (1, 300):
#     flag = True
#     for x in range (1, 300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)



# В3 с тремя аргументами
# def f(x, y, A):
#     return (x < A) or (y < A) or (x + 2*y > 50)

# for A in range (300):
#     flag = True
#     for x in range (300):
#         for y in range (300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# В4
# def f(x, A):
#     return (x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))

# for A in range (300):
#     flag = True
#     for x in range (300):
#         if not f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)
#         break


# №5
# def f(x, y, A):
#     return (x + 2*y > 16) or (x + y <= A)
# for A in range (300):
#     flag = True
#     for x in range (300):
#         for y in range (300):
#             if not f(x, y, A):
#                 flag = False
#                 break
#     if flag:
#         print(A)
#         break



# №6 Для какого наибольшего целого неотрицательного числа A выражение
# (x > A) ∨ (y > x) ∨ (2y + x < 110)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?

for A in range(300, -1, -1):
    k = 0 
    for x in range(300):
        for y in range(300):
            if (x > A) or (y > x) or (2 * y + x < 110):
                k += 1
    if k == 300**2:
        print(A)
        break