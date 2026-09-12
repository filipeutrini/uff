'''
Exercício 1: Implemente em Python programas que resolvam as seguintes operações
    a) Converter um número binário para decimal
    b) Converter um decimal para binário
    c) Converter um binário para hexadecimal
    d) Converter um hexadecimal para binário
Nos exercícios a e b, represente os números binários como números inteiros em base decimal formados somente pelos digitos 0 e 1.
Nos exercícios c e d, considere que os hexadecimais são representados por strings.
'''

def bin_to_dec(num: int):
    mult = 1
    dec = 0
    while num > 0:
        dec += (num%10) * mult
        num //= 10
        mult *= 2
    return dec

def dec_to_bin(num: int):
    binario = 0
    mult = 1

    while num > 0:
        binario = (num % 2) * mult + binario
        num = num // 2
        mult *= 10
    return binario

def bin_to_hex(num: int):
    hexa = ""

    while num > 0:
        dec = bin_to_dec(num%10000)
        if dec < 10:
            hexa = str(dec) + hexa
        else:
            hexa = chr(ord('A') + dec - 10) + hexa

        num //= 10000
    return hexa
    
def hex_to_bin(hexa: str):
    bin = 0
    for i in range(len(hexa)):
        bin *= 10000
        match hexa[i]:
            case "A":
                dec = 10
            case "B":
                dec = 11
            case "C":
                dec = 12
            case "D":
                dec = 13
            case "E":
                dec = 14
            case "F":
                dec = 15
            case _:
                dec = int(hexa[i])
        bin += dec_to_bin(dec)
    return bin

if __name__ == "__main__":
    # a)
    binario = int(input("Insira um número binário para converter para decimal: "))
    print(f"Equivalente decimal: {bin_to_dec(binario)}")

    # b)
    decimal = int(input("Insira um número decimal para converter para binário: "))
    print(f"Equivalente binário: {dec_to_bin(decimal)}")

    # c)
    binario2 = int(input("Insira um número binário para converter para hexadecimal: "))
    print(f"Equivalente hexadecimal: {bin_to_hex(binario2)}")

    # d)
    hexa = input("Insira um número hexadecimal para converter para binário: ")
    print(f"Equivalente binário: {hex_to_bin(hexa)}")