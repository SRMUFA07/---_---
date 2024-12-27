# В1
# def duo(n):
#     digits = '0123456789AB'
#     if n < 12:
#         return digits[n]
#     return duo(n//12) + digits[n % 12]
    
# res = []
# for n in range(144, 10000):
#     s = duo(n)
#     if n % 12 == 0:
#         s += s[-3:]
#     else:
#         s = duo(n % 12 * 3) + s 
            
            
#     if int(s, 12) < 58000:
#         res.append((int(s, 12), n))
        
#     print(sorted(res, reverse = True)[0])



# ЦУ
# def find_min(target_result):
#     for num in range(10000, 100000):
#         str_num = str(num)
#         odd_sum = int(str_num[0]) + int(str_num[2]) + int(str_num[4])
#         even_sum = int(str_num[1]) + int(str_num[3])

#         result = ''.join(map(str, sorted([odd_sum, even_sum])))
#         if result == str(target_result):
#             return num

# print(find_min(621))



# Гриша 
# for N in range(1, 500):
#     N_bin = bin(N)[2:]
#     N_bin_str = str(N_bin)
    
#     for i in range(2):
#         if N_bin_str.count('1') > N_bin_str.count('0'):
#             N_bin_str += '0'
#         else:
#             N_bin_str = '11' + N_bin_str

#     R = int(N_bin_str, 2)
#     if R > 500:
#         print(N)
#         break



# №2
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему ново
# число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если число чётное, то к двоичной записи числа слева дописывается 10;
# б) если число нечётное, то к двоичной записи числа слева дописывается 1  и справ
# дописывается 01.
# Полученная таким образом запись является двоичной записью искомого числа R.
# 3. Результат переводится в десятичную систему и выводится на экран. 
# Укажите максимальное число R, которое может быть результатом работы данног
# алгоритма, при условии, что N не больше 12. В ответе запишите это число в десятично
# системе счисления.

result = []

for N in range(1, 123100):
    N_bin = bin(N)[2:]
    N_bin_str = str(N_bin)

    if N % 2 == 0:
        N_bin_str = '10' + N_bin_str
    else:
        N_bin_str = '1' + N_bin_str + '01'

    R = int(N_bin_str, 2)

    if not N > 12:
        result.append(R)

print(max(result))
