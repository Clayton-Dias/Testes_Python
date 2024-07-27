"""
Crie uma função chamada calcula_media() que recebe um dicionário de notas como argumento e retorna a média das notas.
Crie um dicionário chamado alunos que armazene as notas de 3 alunos em 3 disciplinas: matemática, português e história.
Utilize dicionários aninhados para armazenar as notas de cada aluno em cada disciplina.
Utilize a função calcula_media() para calcular a média das notas de cada aluno em todas as disciplinas.
Exiba na tela o nome de cada aluno e sua média final.

Dicas: 
Funções permitem organizar o código em blocos reutilizáveis.
Dicionários aninhados são úteis para representar estruturas hierárquicas de dados.
A função sum() pode ser utilizada para calcular a soma de valores em um dicionário ou lista.
A divisão por len() fornece a média.
Exemplo de função `calcula_media():
    def calcula_media(notas):
        soma = sum(notas.values())
        media = soma / len(notas)
        return media
"""
#Crie uma função chamada calcula_media() que recebe um dicionário de notas como argumento e retorna a média das notas.
def calcula_media(notas):
        soma = sum(notas.values())
        media = soma / len(notas)
        return media

#Crie um dicionário chamado alunos que armazene as notas de 3 alunos em 3 disciplinas: matemática, português e história.
#Utilize dicionários aninhados para armazenar as notas de cada aluno em cada disciplina.
alunos = {
    "Isaac": {
        "matematica": 95,
        "portugues": 65, 
        "historia": 81
    },
    "Turin": {
        "matematica": 75, 
        "portugues": 85, 
        "historia": 80
    },
    "Newton": {
        "matematica": 80, 
        "portugues": 75, 
        "historia": 95
    }
}

#Utilize a função calcula_media() para calcular a média das notas de cada aluno em todas as disciplinas.
for aluno, notas in alunos.items():
    media = calcula_media(notas)
    print(f"O {aluno} tem a média de {media:.2f}") #Exiba na tela o nome de cada aluno e sua média final.

