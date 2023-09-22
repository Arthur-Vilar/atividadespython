produtos= []
valores= []

a= False

while (not a):
    nomeproduto= input("digite o nome do produto: ")
    valorproduto= input("digite o valor do produto: ")

    produtos.append(nomeproduto)
    valores.append(valorproduto)
    b=print("deseja inserir outro produto?(s/n) ")
    a= input() == "n"

print("segue abaixo os produtos digitados")
for i in range(len(produtos)):
    print(f"{produtos[i]} : R${valores[i]}")



