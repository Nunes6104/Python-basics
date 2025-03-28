a = int(input("Introduza um número para A: "))
b = int(input("Introduza um número para B: "))
if a > b:
    a, b = b, a
if a <= 9 or b <= 9:
    for i in range(a+1, b):
        if i % 10 != 0:
            print(i, end = ',')
    print("\b ")
else:
    print("Valores inválidos")