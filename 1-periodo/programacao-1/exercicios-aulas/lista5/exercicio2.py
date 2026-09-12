'''
2) Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto, mandou digitar uma linha para cada mercadoria com nome, preço de compra e preço de venda das mesmas. Fazer um programa que:
    a) determine e escreva quantas mercadorias proporcionam:
        lucro < 10%
        10% <= lucro <= 20%
        lucro > 20 %
    b) determine e escreva o valor total de compra e de venda de todas as mercadorias, assim como o lucro total.
'''

if __name__ == "__main__":
    print("Análise do Comerciante")
    lucro_menor = lucro_medio = lucro_maior = 0

    total_compra = total_venda = 0.0

    total_mercadorias = int(input("Insira a quantidade de mercadorias: "))

    for i in range(total_mercadorias):
        nome = input("Nome da mercadoria: ")
        preco_compra = float(input("Preço de compra: R$"))
        preco_venda = float(input("Preço de venda: R$"))

        lucro = preco_venda - preco_compra
        percentual_lucro = (lucro / preco_compra) * 100

        if percentual_lucro < 10:
            lucro_menor += 1
        elif percentual_lucro <= 20:
            lucro_medio += 1
        else:
            lucro_maior += 1

        total_compra += preco_compra
        total_venda += preco_venda

    lucro_total = total_venda - total_compra

    print(f"\nLucro < 10%: {lucro_menor}")
    print(f"10% <= Lucro <= 20%: {lucro_medio}")
    print(f"Lucro > 20%: {lucro_maior}")

    print(f"Valor total de compra: R$ {total_compra:.2f}")
    print(f"Valor total de venda: R$ {total_venda:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")