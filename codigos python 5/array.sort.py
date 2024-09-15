import random

array_inteiros = [random.randint(1, 100) for _ in range(15)]
print("Array de inteiros não ordenados:")
print(array_inteiros)

array_inteiros.sort()
print("\nArray de inteiros ordenados de forma crescente:")
print(array_inteiros)

array_inteiros.sort(key=None, reverse=True)
print("\nArray de inteiros ordenados de forma decrescente:")
print(array_inteiros)

array_strings = ["nome", "dataNascimento", "cpf", "rg"]
array_strings += [f"Item {i}" for i in range(11)]
random.shuffle(array_strings)
print("\nArray de strings não ordenados:")
print(array_strings)

array_strings.sort()
print("\nArray de strings ordenados de forma crescente:")
print(array_strings)

array_strings.sort(key=None, reverse=True)
print("\nArray de strings ordenados de forma decrescente:")
print(array_strings)