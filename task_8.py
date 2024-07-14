# В1 какой набор букв будет под номером 376?
# from itertools import *
# print([i for i in permutations(sorted('модест'))][376])



# В2 под каким номером стоит набор букв подходящий по условию задания?
# from itertools import *
# for i, w in enumerate(product(sorted('компьютер'), repeat=5), 1):
#     if i % 2 != 0 and w[0] != 'ь' and w.count('к') == 2:
#         print(i)



# В3 какое количество наборов букв будет подходящими по условию задания?
# from itertools import *
# k = 0
# for i, w in enumerate(product(sorted('дощгхимтэ'), repeat=5), 1):
#     if i % 2 == 0 and w[0] not in 'ми':
#         k += 1
# print(k)



# В4 какое количество наборов цифр будет подходящими по условию задания?
# from itertools import *
# k = 0
# for x in product('012345678', repeat=7):
#     if x[0] not in '026' and x[-2] != x[-1]:
#         k += 1
# print(k)



# В5 под каким номером стоит набор букв подходящий по условию задания?
# from itertools import *
# for i, w in enumerate(product(sorted('парус'), repeat = 3), 1):
#     if w[0] == 'с':
#         print(i)