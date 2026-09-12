'''
9) Escreva um programa em Python que leia dois inteiros n e m e calcule MDC(m,n).
'''

if __name__ == "__main__":
    m = int(input("Insira o número m: "))
    n = int(input("Insira o número n: "))

    a, b = abs(m), abs(n)
    while b != 0:
        a, b = b, a % b

    print(f"MDC({m}, {n}) = {a}")