'''
3) Escreva um programa que leia três pares ordenados e determine se formam os vértices de um triângulo.
'''

if __name__ == "__main__":
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))

    a = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
    b = ((x2 - x3)**2 + (y2 - y3)**2)**1/2
    c = ((x1 - x3)**2 + (y1 - y3)**2)**1/2

    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Os pontos formam um triângulo.")
    else:
        print("Os pontos não formam um triângulo.")