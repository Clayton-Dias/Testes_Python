"""
Exercício 1: Criando e Acessando Elementos de uma Tupla

Crie uma tupla chamada minha_tupla que armazene as cores do arco-íris: "vermelho", "laranja", "amarelo", "verde", "azul", "anil" e "violeta".
Exiba na tela a cor que está na quarta posição da tupla.
Tente modificar o valor da cor na quinta posição da tupla. (Isso deve gerar um erro, pois tuplas são imutáveis).
Crie uma nova tupla chamada cores_invertidas que seja a reversa da minha_tupla.
Mostre na tela a cores_invertidas.

Dicas:
Utilize a função print() para exibir os resultados na tela.
Para acessar um elemento específico da tupla, utilize o índice entre colchetes []. O primeiro índice é 0.
As tuplas são imutáveis, ou seja, seus valores não podem ser modificados após a criação.
Para criar uma nova tupla a partir de outra, você pode utilizar o fatiamento ou a função tuple().
"""
#Criando tupla ue armazene as cores do arco-íris
minha_tupla = tuple(("vermelho", "laranja", "amarelo", "verde", "azul", "anil","violeta"))
#minha_tupla = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil","violeta")
#print(minha_tupla)

#Mostrnado na tela a cor que está na quarta posição da tupla.
print(minha_tupla[3])

#Tentando modificar o valor da cor na quinta posição da tupla.
#minha_tupla[4] = "branco" #Gerar um erro, pois tuplas são imutáveis

#Criando uma nova tupla chamada cores_invertidas que seja a reversa da minha_tupla.
cores_invertidas = list(minha_tupla)
cores_invertidas.reverse()
cores_invertidas = tuple(cores_invertidas)

#Crie uma nova tupla chamada cores_invertidas que seja a reversa da minha_tupla usando fatiamento.
#cores_invertidas = minha_tupla[::-1]

#Mostrando na tela a cores_invertidas.
print(cores_invertidas)
#print(minha_tupla)