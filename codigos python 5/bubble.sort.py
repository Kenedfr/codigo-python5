def bubbleSort(array):
    
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

import random

array = [random.randint(1, 100) for _ in range(15)]
print("Array não ordenado:")
print(array)

array_ordenado = bubbleSort(array)
print("\nArray ordenado utlizando bubblesort:")
print(array_ordenado)

import random

def bubblesort(array):
    
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
    return array

array = [random.randint(1, 100) for _ in range(15)]
print("Array não ordenado:")
print(array)

array_ordenado = bubbleSort(array)
print("\nArray ordenado utilizando bubbleSort:")
print(array_ordenado)