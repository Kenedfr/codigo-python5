with open('loremipsum.txt', 'r') as file:
    conteudo = file.read()

print("Conteúdo do arquivo:")
print(conteudo) 

print("\nPrimeira linha do arquivo:")
print(conteudo.splitlines()[0])

print("\nPrimeiros 3 caracteres do arquivo:")
print(conteudo[:3])

with open('loremipsum.txt', 'r') as file:
    conteudo = file.read()
    print("Conteudo do arquivo:")
    print(conteudo)
