import math

y = float(input("Introduza um valor para Y: "))
x = float(input("Introduza um valor para X: "))

z = (math.exp(y) + math.cos(x)) / math.log(y + 1)
print(f"Result: {z: .2f}")