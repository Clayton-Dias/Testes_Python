def hello(nome, idade):
    print(f"Olá {nome} !")
    if int(idade) > 17:
        print("Você deve se alistar !")
    else:
        print("Você ainda não pode se alistar !")

hello("João", 18)
hello("Luan", 15)
hello("Lucas", "20")
hello(idade = 14, nome = "Cicero")