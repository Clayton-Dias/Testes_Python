"""
Crie um dicionário chamado agenda para armazenar informações de contato de seus amigos:
    Chave: nome do amigo (string)
    Valor: dicionário com informações de contato (telefone, email)
Adicione 3 amigos à sua agenda, cada um com nome, telefone e email.
Exiba na tela o telefone do primeiro amigo da agenda.
Modifique o email do segundo amigo para um novo endereço.
Adicione uma nova chave "cidade" ao dicionário de informações do terceiro amigo, com o valor correspondente à sua cidade natal.
Exiba na tela todas as chaves e valores do dicionário do terceiro amigo.

Dicas:
Utilize a função dict() para criar um dicionário.
Para acessar um valor específico no dicionário, utilize a chave entre colchetes [].
Para adicionar um novo par chave-valor, utilize a atribuição dentro dos colchetes.
Para iterar sobre as chaves de um dicionário, utilize o loop for.
Para iterar sobre os pares chave-valor de um dicionário, utilize o loop for com a função items().
"""
#Crie um dicionário chamado agenda para armazenar informações de contato de seus amigos:
#Chave: nome do amigo (string)
#Valor: dicionário com informações de contato (telefone, email)
agenda = {}

#Adicione 3 amigos à sua agenda, cada um com nome, telefone e email.
#Utilize a função dict() para criar um dicionário.
agenda = dict(
    Ana=dict(
        telefone="1234-5678",
        email="ana@email.com",
    ),
    Brian=dict(
        telefone="9876-5432",
        email="brian@email.com",
    ),
    Diana=dict(
        telefone="9137-8426",
        email="diana@email.com",
    )
)

#Exiba na tela o telefone do primeiro amigo da agenda.
primeiro_amigo =  list(agenda.keys()) #Obtendo a lista de amigos
primeiro_amigo = primeiro_amigo[0]  #Obtendo o nome do primeiro amigo da lista

print(f"O telefone do primeiro amigo da agenda, que é a {primeiro_amigo}, é {agenda[primeiro_amigo]["telefone"]}.")

#Modifique o email do segundo amigo para um novo endereço.
agenda["Brian"]["email"] = "brian@email.br"
#print(agenda["Brian"]["email"])

#Adicione uma nova chave "cidade" ao dicionário de informações do terceiro amigo, com o valor correspondente à sua cidade natal.
agenda["Diana"]["cidade"] = "Natal"
#print(agenda["Diana"]["cidade"])

#Exiba na tela todas as chaves e valores do dicionário do terceiro amigo.
print("Dados do terceiro amigo da agenda: ")
for x, y in agenda["Diana"].items():
    print(f"{x}: {y}")


"""
#Dica do professor :
# Imprimindo do dicionário completo e formatado usando a biblioteca `pprint`.
import pprint
pprint.pprint(agenda)

# Imprimindo do dicionário completo e formatado usando a biblioteca `json`.
import json
print(json.dumps(agenda, indent=4, ensure_ascii=False))
"""