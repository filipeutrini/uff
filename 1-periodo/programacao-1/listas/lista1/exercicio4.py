'''
4) Escreva um programa que leia um inteiro n e imprima os padrões abaixo.
'''

if __name__ == "__main__":
    n = int(input("Insira um número: "))

    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

    print()

    for i in range(n):
        for j in range(n):
            if j < i:
                print("-", end=" ")
            else:
                print("*", end=" ")
        print()
    print()

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print("-", end=" ")
        print()

    print()

    for i in range(n):
        for j in range(n):
            dist = min(i, j, n - 1 - i, n - 1 - j)
            
            if dist % 2 == 0:
                print("*", end=" ")
            else:
                print("-", end=" ")
        print()