''' 
Comentário: Na realização da função em comento, a soma de dois termos, a saber: A (num1) e B (num2), nisso, retorno é a soma desses termos que por fim gera o resultado. 
O print é a igualdade ou o resultado esperado entre a soma dos termos supracitados.
'''

def soma(num1, num2) :
    return num1 + num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = soma(num1, num2)
print("A soma dos números é: ", resultado)


