"""
Crie uma lista chamada `minha_lista` que armazene os nomes de 4 frutas diferentes.
Exiba na tela o nome da fruta que está na segunda posição da lista.
Adicione um novo item à lista, inserindo o nome de outra fruta no final.
Mostre na tela a quantidade de frutas na lista.
Remova a última fruta da lista.

Dicas:
    Utilize a função print() para exibir os resultados na tela.
    Para acessar um elemento específico da lista, utilize o índice entre colchetes []. O primeiro índice é 0.
    Para adicionar um novo item ao final da lista, utilize o método append().
    Para obter a quantidade de elementos na lista, utilize a função len().
    Para remover um item da lista, utilize o método remove().

"""
#Crie uma lista chamada `minha_lista` que armazene os nomes de 4 frutas diferentes.
minha_lista = ["maçã", "laranja", "perâ", "melância"]

#Exiba na tela o nome da fruta que está na segunda posição da lista.
print(minha_lista[1])

#Adicione um novo item à lista, inserindo o nome de outra fruta no final.
minha_lista.append("jabuticaba")

#Mostre na tela a quantidade de frutas na lista.
print(len(minha_lista))

print(minha_lista)

#Remova a última fruta da lista.
minha_lista.remove("jabuticaba")
#minha_lista.pop() 
#pop() apagar o último item da lista, quando o index não é indicado, por exemplo pop(x)

#Mostrando o resultado final
print(minha_lista)



