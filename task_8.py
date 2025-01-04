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
# from itertools import *
# k = set() # создал множество чтобы исключить повторения
# for w in permutations('акарида'):
#     res = '' 
#     for i in w:
#         if i in 'аи':
#             res += 'г' # гласная
#         else:
#             res += 'с' # согласная
#     if 'гг' not in res and 'сс' not in res:
#         k.add(w)
# print(len(k))



# Из букв А, Д, М, Т составили всевозможные 5-буквенные слова. Полученные слова записали в алфавитном порядке. Запишите слово, которое стоит на 330-м месте от начала списка.
# from itertools import *
# print([i for i in product(sorted('адмт'), repeat=5)][329])



# Определите количество 12-ричных пятизначных чисел, в записи которых ровно однa цифра 7
# и не более трёх цифр с числовым значением, превышающим 8.
# def convert_to(number, base):
#     digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     if base > len(digits): return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result

# result = []
# for num in range(10000, 100000):
#     num_twelve = convert_to(num, 12)
#     num_twelve_str = str(num_twelve)

#     more_than_eight = 0
#     for i in num_twelve_str:
#         if i not in 'AB':
#             if int(i) > 8:
#                 more_than_eight += 1
#     if num_twelve.count('7') == 1 and more_than_eight <= 3:
#         result.append(num)
# print(len(result))



# Составляют 5-⁠буквенные слова из букв слова ПЯТНИЦА. Найти количество слов, которые не начинаются с Н и в которых есть только одна буква Я. Буквы в слове могут повторяться.
# from itertools import*
# count = 0
# for i in product('ПЯТНИЦА', repeat=5):
#     if i[0] != 'Н' and i.count('Я') == 1:
#         count += 1
# print(count)



# Все 5-⁠буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Запишите слово, которое стоит на 150-⁠м месте от начала списка.
# from itertools import*
# print([i for i in product(sorted("АКРУ"), repeat=5)][149])



# Олег составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. 
# В качестве кодовых слов Олег использует 4-⁠буквенные слова, в которых есть только буквы A, B, C, D, E, X, Z, причём буквы X и Z встречаются только на двух первых позициях, 
# а буквы A, B, C, D, E  — только на двух последних. Сколько различных кодовых слов может использовать Олег?
from itertools import*
count = 0
for i in product('ABCDEXZ', repeat=4):
    if (i[0] in 'XZ' and i[1] in 'XZ') and (i[2] in 'ABCDE' and i[3] in 'ABCDE'):
        count += 1
print(count)

    