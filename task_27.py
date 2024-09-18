# пример
# file_array = open('27-B.txt')
# read_line = int(file_array.readline())
# a = [int(s) for s in file_array]
# amounts = []

# for i in range(read_line):
#     for j in range(i + 1, read_line):
#         for k in range(j + 1, read_line):
#             amount = a[i] + a[j] + a[k]
#             if amount % 105 == 0:
#                 amounts.append(amount)

# print(max(amounts))



f = open('27-B.txt')
n = int(f.readline())
a = [int(s) for s in f]
summi = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            summa = a[i] + a[j] + a[k]
            if summa % 105 == 0:
                summi.append(summa)
print(max(summi))