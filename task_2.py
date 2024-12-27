# №1
# print('xyz')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if ((x == y) or ((z or y) <= x)) == 0:
#                 print(x, y, z)



# №2
print('xyzw')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((w <= y) <= x) or not z) == 0:
                    print(x, y, z, w)