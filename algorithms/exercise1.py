# 1) Пиши всё в этом файле.
# 2) Написать бинарный поиск
# 4) За какое время работает бинарный поиск? быстрее ли он простого?
# 6) Почему время выполнения алгоритма не измеряется в секундах?
# 7) В чём измеряется время выполнения алгоритма?
# 8) Как выражается время выполнения алгоритма?
# 9) К какому классу задач относиться задача о коммивояжере?

# 2
'''\бинарный поиск... чего то...'''
from random import randint

a = []
for i in range(20):
    a.append(randint(1, 50))
a.sort()
print(a)
find_int = int(input())

# счетчик для себя
k = 0

mid = len(a) // 2
low = 0
high = len(a) - 1
?
while a[mid] != find_int and low <= high:
    if find_int > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
    k = k + 1

if low > high:
    print("No find", k)
else:
    print("int", mid, k)
# 3
# Бинарный поимк работает за логарифмическое время, а простой поиск за линейное. Так что бинарный поиск быстрее простого )
# 6
# Мне кажется, что время работы алгоритма будет сильно привязанно к конкретному "железу" и высчитать точно вцполненин операции на раличных конфигурациях нельзя
# 7
# Время измеряется в шагах, оно ж количество операций?
# 8)
# Выражается через число О большое.
# 9) Задача о коммиявожоре относится к класу NP-трудных задач, т.е. нет оптимального решения до сих пор.
