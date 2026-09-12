'''
10) Escreva um programa em Python que calcule o fatorial de um inteiro n.
'''

if __name__ == "__main__":
    print("Calculadora de Fatorial")
    n = int(input("Insira um número n: "))

    if n < 0:
        print("Não existe fatorial de números negativos.")
    else:
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        print(f"{n}! = {fatorial}")