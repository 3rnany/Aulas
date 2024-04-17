import random

def jogo_de_aduvinhar():
    n_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True: 
        tentativa = int(input("Tente aduvinhá o numuro entre 1 e 100: "))
        tentativas +=1

        if tentativa < n_secreto:
            print("Tente um numuro maior")
        elif tentativa > n_secreto:
            print("Tente um numuro menor")
        else:
            print("Parabéns! Você acertou o numuro em {} tentativas!".format(tentativas))
            break

jogo_de_aduvinhar()

