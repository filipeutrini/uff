'''
11) Escreva um programa que calcule a combinação Cₙ﹐ₖ dados dois inteiros n e k.
'''

def fatorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

if __name__ == "__main__":
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))

    if k < 0 or k > n:
        print("Valores inválidos. 0 <= k <= n.")
    else:
        combinacao = fatorial(n) // (fatorial(k) * fatorial(n - k))
        print(f"C({n}, {k}) = {combinacao}")