'''Escreva uma função chamada "maior_elemento" que receba uma lista de números como entrada e retorne o maior elemento da lista. Crie a lista e realize o teste, exibindo o resultado.
Comentário: Na função "maior_elemento", a lista de números possibilitou '''

def maior_elemento(lista):
    return max(lista)

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]

maior = maior_elemento(numeros)
print("O maior elemento da lista é: ", maior)

'''Digite uma lista de números separados por espaço: 1 2 3 4 6
O maior elemento da lista é: 6'''