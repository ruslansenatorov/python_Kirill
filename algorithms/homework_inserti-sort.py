from random import randint
a = []
for i in range(5):
    a.append(randint(1, 50))
print('start', a)
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list
print('sort', insertionSort(a))
