produto = {} # criou-se o dicionario

print("Registro de produtos") #msg para o usuario

produto["nome"] = input("Nome do produto: ") # comando para inserir 'items' no dicionario.
produto["preco"] = float(input("Preço do produto: ")) # outro comando para inserir valor.

print("Produto resgistrado: ")
print("-"*20) # colocar os prints entre tracinhos
print(f"Nome: {produto['nome']}")
print(f"Preço: {produto['preco']}")
print("-"*20) # colocar os prints entre tracinhos
