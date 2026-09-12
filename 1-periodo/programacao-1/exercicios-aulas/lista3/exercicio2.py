'''
Exercício 2: Verificação da primalidade
Escreva um programa que verifique se um número inteiro k é primo.
'''

if __name__ == "__main__":
    print("Verificador de Primalidade")
    k = int(input("Insira um número: "))

    if k <= 1:
        print(f"O número {k} não é primo.")
    else:
        divisores = 0
        for i in range(2, k // 2 + 1):
            if k%i == 0:
                divisores += 1
            if divisores > 0:
                print(f"O número {k} não é primo.")
                break
        if divisores == 0:
            print(f"O número {k} é primo.")