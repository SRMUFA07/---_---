# Обозначим через P(N) – произведение 5 наименьших различных нетривиальных делителей
# натурального числа N (не считая единицы и самого числа). Если у числа N меньше 5 таких
# делителей, то P(N) считается равным нулю. Найдите 5 наименьших натуральных чисел,
# превышающих 400 000 000, для которых P(N) оканчивается на 17 и не превышает N. В ответе для
# каждого найденного числа запишите сначала значение P(N), а затем – наибольший делитель,
# вошедший в произведение P(N).
# 185


# zn=[]
# for x in range(400000001, 400000100):
#     de = set()  
#     for d in range(1, round(x**0.5) + 1):
#         if x % d == 0:
#             de.add(d)
#             de.add(x//d)
#     if len(de) > 5:
#         de=sorted(de)
#         p = de[5] * de[1] * de[2] * de[3] * de[4]
#         if p < x:
#             zn.append(p)
# print((zn)[:5])



# import math

# def find_divisors(n):
#     divisors = set()
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n // i)
#         if len(divisors) > 5:
#             break
#     return sorted(divisors)

# def find_numbers(limit, count):
#     result = []
#     n = limit + 1
#     while len(result) < count:
#         divisors = find_divisors(n)
#         if len(divisors) >= 5:
#             product = divisors[0] * divisors[1] * divisors[2] * divisors[3] * divisors[4]
#             if product % 100 == 17 and product <= n:
#                 result.append((product, divisors[4], n))
#         n += 1
#     return result

# limit = 400_000_000
# count = 5
# numbers = find_numbers(limit, count)

# for product, largest_divisor, number in numbers:
#     print(f"P(N) = {product}, наибольший делитель = {largest_divisor}, число N = {number}")




# 10 дз Поляков
def find_numbers_with_four_divisors(start, end):
    # Проходим по всем числам в диапазоне
    for num in range(start, end + 1):
        divisors = []

        # Ищем все делители числа
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
                    
        # Проверяем, есть ли у числа ровно 4 делителя
        if len(divisors) == 4:
            divisors.sort()
            print(divisors)

# Значения по условию
find_numbers_with_four_divisors(338472, 338494)