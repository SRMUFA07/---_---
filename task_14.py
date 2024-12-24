# №1
# def seven(num): # перевод в семеричную систему
#     digits = '0123456'
#     if n < 7:
#         return digits[num]
#     return seven(num // 7) + digits[num % 7]
# print(seven(6 * 343**5 + 5 * 49**7 - 50).count('6'))



# №5
# def three(num):
#     digits = '012'
#     if num < 3:
#         return digits[num]
#     return three(num // 3) + digits[num % 3]
# print(three(9**8 + 3**5 - 9).count('2'))



# №9
# def f(num):
#     digits = '012345'
#     if num < 6: # число тут говорит о том в какую сисиетму счисления я перевожу 
#         return digits[num]
#     return f(num // 6) + digits[num % 6]
# print(f(3 * 216**4 + 2 * 36**6 - 648).count('5'))



# №2
# for x in '0123456789AB':
#     for y in '0123456789AB':
#         exp = int(x + '231' + y, 12) + int('78' + x + '98' + y, 14)
#         if exp % 99 == 0:
#             print(exp // 99)
#             break



# №3
# for x in '0123456789': 
#     exp = int('3' + x + 'DA', 14) + int('5' + x + 'A6', 12) # выражение из условия, тут я и строю два числа int
#     if exp % 81 == 0:  # проверяю по условию, кратно ли 81
#         print(exp // 81)



# №7
# for x in '0123456789A':
#     for y in '0123456789A':
#         exp = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
#         if exp % 305 == 0:
#             print(exp // 305)



# №8
# for x in '0123456789': 
#     exp = int('8' + x + '71', 13) + int('3' + x + 'DF', 17)
#     if exp % 197 == 0:
#         print(exp // 197)



# №10
# for x in '0123456789': 
#     exp = int('1' + x + '563', 14) + int('871' + x + '3', 14)
#     if exp % 24 == 0:
#         print(exp // 24)



# №4
# def three(num):
#     digits = '012'
#     if num < 3:
#         return digits[num]
#     return three(num // 3) + digits[num % 3]

# for x in range(2031): 
#     if three(3**100 - x).count('0') == 2: # записываю выражение в троичной системе счисления, и проверяю количество нулей, нам нужно 2
#         print(x)
#         break



# №6
# В системе счисления с основанием p выполняется равенство zxyx7 + xy836  =  wzx64. 
# Буквами x, y, z и w обозначены некоторые цифры из алфавита системы счисления с
# основанием p. Определите значение числа xyzwp и запишите это значение в десятичной системе счисления.
# for p in range(1, 10): # система счисления p
#     for x in range(1, p):
#         for y in range (1, p):
#             for z in range (1, p):
#                 for w in range(1, p):
#                     exp1 = z*p**4 + x*p**3 + y*p**2 + x*p**1 + 7 # выражение 1
#                     exp2 = x*p**4 + y*p**3 + 8*p**2 + 3*p**1 + 6 # выражение 2
#                     exp3 = w*p**4 + z*p**3 + x*p**2 + 6*p**1 + 4 # выражение 3
#                     if exp1 + exp2 == exp3: # zxyx7 + xy836 = wzx64
#                         print(x*p**3 + y*p**2 + z*p**1 + w*p**0) # xyzwp


# Шаг 1: Вычисление выражения
result = 36**7 + 6**30 - 12

# Функция для перевода числа в систему счисления с основанием 6
def to_base_6(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % 6))
        n //= 6
    return ''.join(str(x) for x in digits[::-1])

# Переводим результат в систему счисления с основанием 6
base_6_result = to_base_6(result)

# Подсчёт цифр 5
count_5 = base_6_result.count('5')
print(count_5, base_6_result)