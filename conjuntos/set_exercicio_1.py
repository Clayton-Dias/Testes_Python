"""
Exercício 3: Criando e Manipulando Conjuntos

Crie um conjunto chamado letras contendo as vogais do alfabeto: "a", "e", "i", "o", "u".
Exiba na tela o tamanho do conjunto letras.
Adicione a consoante "b" ao conjunto letras.
Verifique se a vogal "i" está presente no conjunto letras.
Remova a consoante "b" do conjunto letras.
Crie um novo conjunto chamado consoantes contendo as consoantes: "b", "d", "f".
Verifique se o conjunto consoantes está contido no conjunto letras.
Exiba na tela a união dos conjuntos letras e consoantes (todos os elementos sem repetições).

Dicas:
Utilize a função set() para criar um conjunto.
A função len() retorna o tamanho do conjunto.
O método add() adiciona um elemento ao conjunto.
O operador in verifica se um elemento está presente no conjunto.
O método remove() remove um elemento do conjunto.
O operador | (união) retorna um novo conjunto com todos os elementos dos conjuntos originais, sem repetições.
O operador & (intersecção) retorna um novo conjunto com os elementos que estão presentes em ambos os conjuntos originais.
O operador - (diferença) retorna um novo conjunto com os elementos do primeiro conjunto que não estão presentes no segundo conjunto.
"""
#Criando um conjunto chamado letras contendo as vogais do alfabeto: "a", "e", "i", "o", "u".
letras = set(("a", "e", "i", "o", "u"))

#Exiba na tela o tamanho do conjunto letras.
print(f"O tamanho do conjunto de lteras é: {len(letras)}")

#Adicione a consoante "b" ao conjunto letras.
letras.add("b")
#print(letras)

#Verifique se a vogal "i" está presente no conjunto letras.
if "i" in letras:
    print("A vogal 'i' está em letras")
else:
    print("A vogal 'i' não está em letras")

#Remova a consoante "b" do conjunto letras.
letras.remove("b")

#Crie um novo conjunto chamado consoantes contendo as consoantes: "b", "d", "f".
consoantes = set(("b", "d", "f"))

#Verifique se o conjunto consoantes está contido no conjunto letras.
#print("O conjunto consoantes está contido no conjunto letras:", consoantes.issubset(letras))

if consoantes.issubset(letras) == True:
    print("O conjunto de consoantes está contido conjuntos de letras")
else:
    print("O conjunto de consoantes não está contido conjuntos de letras")


#Exiba na tela a união dos conjuntos letras e consoantes (todos os elementos sem repetições).
#uniao = letras.union(consoantes)
#uniao = letras|consoantes
#print(uniao)
print(f"União dos conjuntos letras e consoantes é: {letras|consoantes}")

