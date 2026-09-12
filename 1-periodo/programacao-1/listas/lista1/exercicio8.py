'''
8) Escreva um programa em Python que leia um inteiro n e imprima todos os primos de 1 a n.
'''

if __name__ == "__main__":
    print("Primos no Intervalo")
    n = int(input("Insira um número: "))

    if n <= 0:
        print(f"O número deve ser maior do que 0.")
    else:
        for i in range(2, n+1):
            divisores = 0
            for j in range(2, i // 2 + 1):
                if i%j == 0:
                    divisores += 1
                if divisores > 0:
                    break
            if divisores == 0:
                print(i, end=" ")
    print("")