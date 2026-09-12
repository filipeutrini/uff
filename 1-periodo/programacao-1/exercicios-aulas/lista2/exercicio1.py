'''
Exercício 1: Cálculo do troco de uma compra em moedas
Dado um valor em reais, determine o total de moedas de 1 real, 50, 25, 10, 5 e 1 centavo.
'''

if __name__ == "__main__":
    print("Troco em Moedas")

    troco = float(input("Insira o troco em reais: R$"))
    centavos = int(round(troco*100))

    real1 = centavos50 = centavos25 = centavos10 = centavos5 = centavos1 = 0

    if centavos >= 100:
        real1 += centavos // 100
        centavos = centavos % 100
    if centavos >= 50:
        centavos50 += centavos // 50
        centavos = centavos % 50
    if centavos >= 25:
        centavos25 += centavos // 25
        centavos = centavos % 25
    if centavos >= 10:
        centavos10 += centavos // 10
        centavos = centavos % 10
    if centavos >= 5:
        centavos5 += centavos // 5
        centavos = centavos % 5
    if centavos >= 1:
        centavos1 = centavos // 1

    print("Quantidade de moedas:")
    print(f"1 real: {real1}")
    print(f"50 centavos: {centavos50}")
    print(f"25 centavos: {centavos25}")
    print(f"10 centavos: {centavos10}")
    print(f"5 centavos: {centavos5}")
    print(f"1 centavo: {centavos1}")
    print(f"Total: R${troco}")