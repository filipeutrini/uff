'''
2) Escreva um programa em Python que leia três números reais a, b e c e imprima-os em ordem crescente.
'''

if __name__ == "__main__":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))

    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    print(a, b, c)