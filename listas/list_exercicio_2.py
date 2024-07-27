"""
Crie uma lista chamada numeros utilizando a função range() para gerar uma sequência de números de 1 a 10 (inclusivo).
Exiba na tela os números pares da lista.
Crie uma nova lista chamada pares que contenha apenas os números pares da lista numeros.
Mostre na tela a lista pares.
Insira o número 15 na lista pares na terceira posição.

Dicas:
A função range() gera uma sequência de números. Utilize range(inicio, fim, passo) para definir o intervalo e o passo da sequência.
Para verificar se um número é par, utilize o operador % (resto da divisão). Se o resto for 0, o número é par.
O fatiamento permite obter sublistas de uma lista original. Utilize lista[inicio:fim:passo]. Se omitir o inicio ou fim, utilize : para pegar desde o início ou até o final da lista, respectivamente.
Para inserir um elemento em uma lista em uma posição específica, utilize o índice entre colchetes [] e atribua o valor desejado.
"""
#Crie uma lista chamada números utilizando a função range() para gerar uma sequência de números de 1 a 10 (inclusivo).
numeros = list(range(1, 11))
print(numeros) 

#Exiba na tela os números pares da lista.
"""
for varNumero in numeros:
    if varNumero % 2 == 0:
        print(varnumero)
"""

print(numeros[1::2]) 
#O fatiamento permite obter sublistas de uma lista original. 
#Utilize lista[inicio:fim:passo]. Se omitir o inicio ou fim, utilize "::" para pegar desde o início ou até o final da lista, respectivamente.


#Crie uma nova lista chamada pares que contenha apenas os números pares da lista números.
numeros_pares = list(range(2, 11, 2))
#numeros_pares = numeros[1::2]      #Fatiamento para obter uma sublista com os números pares.

#Mostre na tela a lista pares.
print(numeros_pares)

#Atribua o número 15 na lista pares na terceira posição.
numeros_pares[2] = 15

#Mostrando o resultado após atribuir o número 15 na lista pares na terceira posição.
print(numeros_pares)