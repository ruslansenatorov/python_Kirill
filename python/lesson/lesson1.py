# Задание 1

# Напиши программу, которая создает список:
#
# из чисел от -3 до 9 (включая 9);
# каждое второе число из последовательности от 20 до -1 (не включая -1);
# каждое десятое число от -500 до 80 (включая 80);
# нечетные числа -40 до 5.
# Вход
#
# Нет входных данных.
#
# Выход
#
# Решение задачи.


# Задание 2
# Создай словарь, в котором ключами будут четные числа, которые есть на промежутке 1 от 10, а значениями словаря будут кубы соотвествующих ключей.
#
# Вход
#
# Нет входных данных.
#
# Выход
#
# Решение задачи.
#

# Задание 3
# Напиши программу, которая конвертирует строковые значения данного словаря nums в числа, там, где это применимо.
#
# Вход
#
# Нет.
#
# Выход
#
# Решение задачи.
#
# Пример
#
# ### Тест 1
#
# Выход:
#
# { 'x': 10 , 'y': 20 , 'z': 30, 'p': 40, 'q': 50, 'r': 60}

# nums ={ 'x':'10' , 'y':'20' , 'z':'30', 'p':'40', 'q':'50', 'r':'60'}
# код здесь



# Задание 4
# Напиши функцию pretty_print, которая прнимает на вход неограниченное число аргументов и выводит пару аргумент-значение построчно.
#
# Пример
#
# ### Тест 1
#
# pretty_print(title="The Matrix", director="Wachowski", year=1999)
#
# Выход:
#
#     title: The Matrix
#     director: Wachowski
#     year: 1999
#
#
#
# ### Тест 2
#
# pretty_print(name="Anna", surname ="Delvey")
#
#
# Выход:
#
#     name: Anna
#     surname: Delvey



# Задание 5
# Два слова являются анаграммами, если состоят из одинаковых букв. Напишите функцию, которая принимает на вход два словами и считает, являеются эти слова анаграммами.
#
# ###  Тест 1
# print(is_anagrams("binary", "brainy"))
#
# Выход:
#
# True


# Задание 6
# Напиши функцию для определения количества гласных в строке (выдача - словарь). Функция должна поддерживать как кириллицу, так и латиницу.
#
# ### Тест 1
# our_function('Hello! How are you today?')
#
# Выход:
#
# {'a': 2, 'e': 2, 'i': 0, 'o': 4, 'u': 1}


# Задание 7
# Напиши функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
#
# Параметры функции:
#
# size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
# value — значение элементов списка (по-умолчанию 0).
# ### Тест 1
#
# result = make_matrix(3)
#
# Выход:
#
# result = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
#
# ### Тест 2
#
# result = make_matrix((4, 2), 1)
#
# Выход:
#
# result = [
#     [1, 1, 1, 1],
#     [1, 1, 1, 1]
# ]