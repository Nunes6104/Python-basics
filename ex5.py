a = int(input("Introduza limite superior a: "))
b = int(input("Introduza limite inferior b: "))
c = int(input("Introduza o incremento c: "))

if b > a:
    print("Limite inferior não pode ser maior que o limite superior")
else:
    for i in range(b, a, c):
        print(i, end=',')
    print("\b ")