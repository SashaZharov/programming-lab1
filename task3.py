Num = [1, 3, 6, 2, 4, 5, 10, 16, 11, 12, 15, 18, 30, 64, 59, 40, 39]

# Сортировка пузырьком
def BubleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                n = array[j]
                array[j] = array[j+1]
                array[j+1] = n
    print(array)

# Пирамидальная сортировка
def HeapSort(array):

    def heapify(array, heap_size, index):

        Max = index
        left = (2 * index) + 1
        right = (2 * index) + 2

        if left < heap_size and array[left] > array[Max]:
            Max = left
        if right < heap_size and array[right] > array[Max]:
            Max = right
        if Max != index:
            array[index], array[Max] = array[Max], array[index]
            heapify(array, heap_size, Max)

    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    print(array)

# Гномья сортировка
def GnomSort(array):
    i = 1
    while i < len(array):
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    print(array)

# Блочная сортировка
def BlockSort(array):
    blocks = []
    answ = []
    maxArr = max(array)
    size = maxArr // len(array)
    i = 0
    print(size, maxArr)

    while i < maxArr:
        blocks.append([])
        i += 1
    print(blocks)

    for i in array:
        blocks[i//size].append(i)
        print(i, i//size)
    for i in blocks:
        i = sorted(i)
        answ += i
    print(answ)

HeapSort(Num)
# BubleSort(Num)
# GnomSort(Num)
#BlockSort(Num)
