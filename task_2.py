print('xyz')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x == y) or ((z or y) <= x)) == 0:
                print(x, y, z)