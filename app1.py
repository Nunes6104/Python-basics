nome = input("Qual é o teu nome? ")
print("Olá,", nome)
numero = int(input("Digite um numero: "))
print(f"O numero é: {numero}")

dia = int(input("Qual o dia de nascimento: "))
mes = int(input("Qual o mes de nascimento: "))
ano = int(input("Qual o ano de nascimento: "))

diasDeVida = ((2025 - ano)*365) + ((12 - mes)* 30) + (31 - dia)
print(f"O {nome} tu viveste {diasDeVida} dias")