'''
Escreva um programa em Python que leia um arquivo texto e gere uma análise do arquivo que deve ser salva em outro arquivo de tipo texto.
Na análise deve ser impresso para cada linha:
a) número da linha
b) conteúdo da linha
c) número de caracteres da linha
d) número de espaços em branco na linha
e) número de palavras da linha
f) número de letras da linha
Ao final da análise deve ser impresso o total global de cada um dos itens da análise por linha. Além disso, deve ser gerado um terceiro arquivo contendo o conjunto de todas as palavras encontradas no texto em ordem (sem usar o sort da linguagem).
Para casa: modifique sua solução para que o dicionário também contenha as linhas e as posições em que cada palavra ocorreu no texto, criando desta forma um glossário. Procure limpar as palavras de forma que não tenha caracteres de pontuação como ":", ",", ".", e etc.
'''

import string

def limpar_palavra(palavra):
    return palavra.strip(string.punctuation).lower()


def insercao_ordenada(lista, palavra):
    if palavra in lista:
        return
    index = 0
    while index < len(lista) and lista[index] < palavra:
        index += 1
    lista.insert(index, palavra)


def analisar_texto(
    texto,
    analise,
    palavras_ord,
    glossario_arq,
):
    with open(texto, "r", encoding="utf-8") as t:
        linhas = t.readlines()

    total_linhas = len(linhas)
    total_caracteres = 0
    total_espacos = 0
    total_palavras = 0
    total_letras = 0

    palavras_ordenadas = []
    glossario = (
        {}
    )

    with open(analise, "w", encoding="utf-8") as f_out:
        for num_linha, linha in enumerate(linhas, start=1):
            conteudo = linha.rstrip("\r\n")

            num_caracteres = len(conteudo)
            num_espacos = conteudo.count(" ")

            palavras = conteudo.split()
            num_palavras = len(palavras)

            num_letras = sum(1 for c in conteudo if c.isalpha())

            total_caracteres += num_caracteres
            total_espacos += num_espacos
            total_palavras += num_palavras
            total_letras += num_letras

            f_out.write(f"L{num_linha}: {conteudo}; {num_caracteres} caracteres; {num_espacos} espaços em branco; {num_palavras} palavras; {num_letras} letras\n")

            for pos_palavra, p in enumerate(palavras, start=1):
                p_limpa = limpar_palavra(p)
                if p_limpa:
                    insercao_ordenada(palavras_ordenadas, p_limpa)
                    if p_limpa not in glossario:
                        glossario[p_limpa] = []
                    glossario[p_limpa].append((num_linha, pos_palavra))

        f_out.write("-" * 50 + "\n")
        f_out.write(f"Total de linhas: {total_linhas}\n")
        f_out.write(f"Total de caracteres: {total_caracteres}\n")
        f_out.write(f"Total de espaços em branco: {total_espacos}\n")
        f_out.write(f"Total de palavras: {total_palavras}\n")
        f_out.write(f"Total de letras: {total_letras}\n")

    with open(
        palavras_ord, "w", encoding="utf-8"
    ) as f_palavras:
        for palavra in palavras_ordenadas:
            f_palavras.write(f"{palavra}\n")

    with open(glossario_arq, "w", encoding="utf-8") as f_glossario:
        f_glossario.write(
            "Palavra -> [(Linha, Posição da Palavra na Linha), ...]\n\n"
        )
        for palavra in palavras_ordenadas:
            ocorrencias = glossario[palavra]
            locais_str = ", ".join(
                [f"(Linha {l}, Pos {p})" for l, p in ocorrencias]
            )
            f_glossario.write(f"{palavra}: {locais_str}\n")



if __name__ == "__main__":
    texto = "texto.txt"
    analise = "analise.txt"
    palavras_ord = "palavras_ordenadas.txt"
    glossario = "glossario.txt"

    analisar_texto(
        texto,
        analise,
        palavras_ord,
        glossario,
    )