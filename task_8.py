# В1 какой набор букв будет под номером 376?
# from itertools import *
# print([i for i in permutations(sorted('модест'))][376])



# В2 под каким номером стоит набор букв подходящий по условию задания?
# from itertools import *
# for i, w in enumerate(product(sorted('компьютер'), repeat=5), 1): # еденица нужна чтобы список шел с одного, как в задании
#     if i % 2 != 0 and w[0] != 'ь' and w.count('к') == 2:
#         print(i)



# В3 какое количество наборов букв будет подходящими по условию задания?
# from itertools import *
# k = 0
# for i, w in enumerate(product(sorted('дощгхимтэ'), repeat=5), 1):
#     if i % 2 == 0 and w[0] not in 'ми':
#         k += 1
# print(k)



# В4 какое количество наборов цифр будет подходящими по условию задания (девятеричная система счисления)?
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



# В6 сколько различных кодов можно составить с неким условием, нет ограничения на использование букв.
# from itertools import *
# k = 0
# for w in product('ваяющий', repeat = 4):
#     if w[0] != 'й' and ('а' in w or 'я' in w or 'ю' in w or 'и' in w):
#         k += 1
# print(k)



# В7 сколько различных кодов можно составить с неким условием, каждую букву можно использовать единожды.
# from itertools import *
# k = 0
# for w in permutations('пайщик'):
#     word = ''.join(w) # объеденил сторку чтобы проверить по условию задания
#     if w[0] != 'й' and 'иа' not in word:
#         k += 1
# print(k)



# В8 сколько различных кодов можно составить с условием, что в коде не должны стоять рядом две гласные и две согласные буквы.
from itertools import *
k = set() # создал множество чтобы исключить повторения
for w in permutations('акарида'):
    res = '' 
    for i in w:
        if i in 'аи':
            res += 'г' # гласная
        else:
            res += 'с' # согласная
    if 'гг' not in res and 'сс' not in res:
        k.add(w)
print(len(k))