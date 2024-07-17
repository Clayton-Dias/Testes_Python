"""
Exercício 2: Combinando Tuplas e Verificando Elementos

Crie duas tuplas: frutas contendo ("banana", "maçã", "laranja") e legumes contendo ("tomate", "cenoura", "batata").
Crie uma nova tupla chamada mercado que combine as tuplas frutas e legumes.
Verifique se a fruta "laranja" está presente na tupla mercado.
Verifique se o legume "alface" está presente na tupla mercado.
Exiba na tela o último item da tupla mercado.

Dicas:
O operador + pode ser utilizado para concatenar tuplas.
Para verificar se um elemento existe em uma tupla, utilize o operador in.
O índice de um elemento em uma tupla pode ser obtido utilizando o método index().
"""
#Criando duas tuplas: frutas contendo ("banana", "maçã", "laranja") e legumes contendo ("tomate", "cenoura", "batata").
frutas = ("banana", "maçã", "laranja")
legumes = ("tomate", "cenoura", "batata")

#Criando uma nova tupla chamada mercado que combine as tuplas frutas e legumes.
mercado = frutas + legumes
#print(mercado)

#Verifique se a fruta "laranja" está presente na tupla mercado.
if "laranja" in mercado:
    print("Laranja está no mercado")
else:
    print("Laranja não está no mercado")

#Verifique se o legume "alface" está presente na tupla mercado.
if "alface" in mercado:
    print("Alface está no mercado")
else:
    print("Alface não está no mercado")

#Exiba na tela o último item da tupla mercado.
x = mercado.index("batata")
print(mercado[x])
#print(mercado[-1])
