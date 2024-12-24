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
N_array = []

for N in range(1, 500):
    N_bin = bin(N)[2:]
    N_bin_str = str(N_bin)
    
    for i in range(2):
        if N_bin_str.count('1') > N_bin_str.count('0'):
            N_bin_str += '0'
        else:
            N_bin_str = '11' + N_bin_str

    R = int(N_bin_str, 2)
    if R > 500:
        print(N)
        break

    