"""
Crie um conjunto chamado numeros1 contendo os números pares de 1 a 10: {2, 4, 6, 8, 10}.
Crie um conjunto chamado numeros2 contendo os números ímpares de 1 a 9: {1, 3, 5, 7, 9}.
Exiba na tela a união dos conjuntos numeros1 e numeros2 (todos os números de 1 a 10, sem repetições).
Mostre na tela a intersecção dos conjuntos numeros1 e numeros2 (apenas os números pares ímpares: {2, 8}).
Exiba na tela a diferença do conjunto numeros1 em relação ao conjunto numeros2 (todos os números pares que não são ímpares: {4, 6, 10}).
Verifique se os conjuntos numeros1 e numeros2 são iguais.
Crie um conjunto chamado primos contendo os números primos menores que 10: {2, 3, 5, 7}.
Verifique se o conjunto primos é um subconjunto do conjunto numeros1 (todos os primos presentes nos pares de 1 a 10).

Dicas :

Utilize as mesmas dicas do Exercício 1 para as operações com conjuntos.
O operador == verifica se dois conjuntos são iguais (contêm os mesmos elementos).
O operador <= verifica se um conjunto é um subconjunto do outro (todos os elementos do primeiro conjunto estão presentes no segundo).
O operador >= verifica se um conjunto é um superconjunto do outro (contém todos os elementos do outro conjunto e possivelmente mais).
"""

#Crie um conjunto chamado numeros1 contendo os números pares de 1 a 10: {2, 4, 6, 8, 10}.
numeros1 = set(("2", "4", "6", "8", "10"))
#numeros1 = {2, 4, 6, 8, 10}

#Crie um conjunto chamado numeros2 contendo os números ímpares de 1 a 9: {1, 3, 5, 7, 9}.
numeros2 = set(('1', '3', '5', '7', '9'))
#numeros2 = {1, 3, 5, 7, 9}

#Exiba na tela a união dos conjuntos numeros1 e numeros2 (todos os números de 1 a 10, sem repetições).
print(f"A união dos conjuntos é: {numeros1.union(numeros2)}")

#Mostre na tela a intersecção dos conjuntos numeros1 e numeros2 (apenas os números pares ímpares: {2, 8}).
print(f"A intersecção dos conjuntos é: {numeros1.intersection(numeros2)}")

#Exiba na tela a diferença do conjunto numeros1 em relação ao conjunto numeros2 (todos os números pares que não são ímpares: {4, 6, 10}).
print(f"A diferença dos conjuntos é: {numeros1.difference(numeros2)}")

#Verifique se os conjuntos numeros1 e numeros2 são iguais.
if numeros1 == numeros2:
    print(f"O conjunto numeros1 é igual ao conjunto numeros2.")
else:
    print(f"O conjunto numeros1  não é igual ao conjunto numeros2.")

#Crie um conjunto chamado primos contendo os números primos menores que 10: {2, 3, 5, 7}.
primos = set(("2","3","5","7"))

#Verifique se o conjunto primos é um subconjunto do conjunto numeros1 (todos os primos presentes nos pares de 1 a 10).
if primos.issubset(numeros1) == True:
    print("O conjunto de primos é um subconjunto do conjunto numeros1")
else:
    print("O conjunto de primos não é um subconjunto do conjunto numeros1")