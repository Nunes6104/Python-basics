l1 = int(input("Introduza o 1º lado do triângulo: "))
l2 = int(input("O 2º lado do triângulo: "))
l3 = int(input("O 3º lado do triângulo: "))

if l1 >= 0 and l2 >= 0 and l3 >= 0 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("O triângulo é equilátero")
    elif l1 != l2 != l3:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("Os Lados introduzidos não permitem formar um triângulo")