'''
3) A regressão linear é uma técnica da estatística que busca ajustar uma equação linear $y = ax+b$ a um conjunto de dados $x$ e $y$. Dada uma coleção de dados, lida do console como pares consecutivos $(x,y)$, encontre os coeficientes a (inclinação) e b (interseção com y) da reta que minimiza o resíduo ε. (Fórmulas foram dadas na questão)
'''

if __name__ == "__main__":
    print("Regressão linear")
    soma_x = soma_y = soma_xy = soma_x2 = n = 0

    while True:
        x, y = input("Insira o par de valores (x,y) ou (e,e) para finalizar:").strip().removeprefix("(").removesuffix(")").split(",")
        if x == "e" and y == "e":
            break
        x = float(x)
        y = float(y)
        n += 1

        soma_x += x
        soma_y += y
        soma_xy += x*y
        soma_x2 += x**2

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    b = (soma_y - a * soma_x) / n

    print(f"a = {a:.3f}")
    print(f"b = {b:.3f}")
    print(f"y = {a:.3f}x + {b:.3f}")