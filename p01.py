lista = []

for i in range(3):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)

lista.sort()

lista.reverse()

for num in lista:
    print(num, end=', ')

print()
