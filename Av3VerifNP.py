def verifica_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    return pares

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]

pares = verifica_pares(numeros)
print("Os números pares da lista são: ", pares)

'''Digite uma lista de números separados por espaço: 1 3 4 6 8 4
Os números pares da lista são: [4, 6, 8, 4]'''

