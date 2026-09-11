# ============================================================
# AULA PRATICA 1
# ============================================================
#
# Objetivos:
#
# - Comandos basicos
# - Objetos
# - Vetores
# - Tabelas e Graficos
#
# ============================================================





# ============================================================
# 1. Calculadora
# ============================================================

# Rodar: Ctrl + Enter (com o cursor na linha que 
# voce quer rodar) (ou botao Run)

2 + 3

10 - 4

5 * 3

10 / 2

5^2

5**2


# ?

2 + 3 * 2


# ?

(2 + 3) * 2



# ============================================================
# EXERCICIO 1
# ============================================================

# Use o R para calcular:

# a) 15 + 7

# b) 20 dividido por 4

# c) 6 ao quadrado

# d) O dobro do resultado de 10 + 5



# ============================================================
# 2. OBJETOS
# ============================================================

# Objeto
#
# Recebe: <- ou =

idade <- 20
idade2 = 10

# ?

idade
idade2

# Podemos utilizar o objeto em operacoes

idade + 1

idade * 2

idade / 2


# Para alterar o valor guardado:

idade = 21

idade



# ============================================================
# EXERCICIO 2
# ============================================================

# Usando o R:

# a) Crie um objeto chamado peso com o valor 70

# b) Mostre o valor de peso

# c) Calcule o triplo do resultado de peso + 10


# ============================================================
# 3. VETORES
# ============================================================

# Concatenar: c() (ou combinar)

idades = c(18, 19, 20, 20, 21, 22)

idades


# ?

idades + 1


# ?

idades * 2

# somar vetores de mesmo tamanho

idades + c(1,2,3,4,5,6)

# Algumas funcoes

# media
mean(idades)

# mediana
median(idades)

min(idades)

max(idades)

# tamanho do vetor
length(idades)

# chr

nome = c("Joao","Joaquim","Julio")

nome

caracteres = c("1","a","4")

caracteres + 1

# ?

mean(nome)


# Selecionando um item do vetor

nome[2]


# ============================================================
# EXERCICIO 3
# ============================================================

notas = c(5, 7, 8, 6, 9, 10, 7)

# Usando o R, encontre:

# a) A media das notas # mean

# b) A mediana das notas # median

# c) A maior nota # max

# d) A menor nota # min

# e) O numero de alunos # length

# f) A nota na terceira posicao do vetor # []



# ============================================================
# 4. VARIAVEIS CATEGORICAS
# ============================================================

# Meio de transporte utilizado por 15 estudantes

transporte = c("Onibus","Onibus","Carro","Onibus","Bicicleta",
               "Carro","Onibus","Metro","Metro","Onibus",
               "Carro","Bicicleta","Onibus","Metro","Onibus")

transporte


# ============================================================
# 4.1 - TABELA DE DISTRIBUICAO DE FREQUENCIAS
# ============================================================

# Frequencia absoluta

table(transporte)


# ?

freq_abs_transporte = table(transporte)

freq_abs_transporte


# Frequencia relativa

prop.table(table(transporte))

# ou

prop.table(freq_abs_transporte)

# Novo objeto

freq_rel_transporte = prop.table(freq_abs_transporte)

freq_rel_transporte


# Frequencia relativa em porcentagem

100 * freq_rel_transporte



# ============================================================
# 4.2. GRAFICO DE BARRAS # barplot
# ============================================================

# Frequencia absoluta

freq_abs_transporte

barplot(freq_abs_transporte)

barplot(table(transporte))

# Frequencia relativa

barplot(freq_rel_transporte)

barplot(prop.table(table(transporte)))


# Personalizacao

barplot(freq_rel_transporte,
  main = "Meio de transporte",
  xlab = "Transporte",
  ylab = "Frequencia relativa")



# ============================================================
# 4.3. GRAFICO DE SETORES
# ============================================================

pie(freq_abs_transporte)


# Utilizando frequencias relativas

pie(freq_rel_transporte)

# Personalizacao

pie(freq_rel_transporte,
  main = "Meio de transporte")



# ============================================================
# EXERCICIO 4
# ============================================================

bebida = c("Cafe","Cafe","Cha","Cafe","Suco",
           "Cha","Cafe","Suco","Cafe","Cha")

# a) Identifique o tipo da variavel
# Categorica nominal, categorica ordinal, 
# numerica discreta ou numerica continua
# b) Construa a tabela de frequencia absoluta
# c) Construa a tabela de frequencia relativa
# d) Qual bebida foi mais frequente?
# e) Qual a porcentagem de pessoas que escolheram Cha?
# f) Construa um grafico de barras com
#    as frequencias relativas # barplot
# g) Construa um grafico de setores com
#    as frequencias relativas # pie




# ============================================================
# 5. VARIAVEL NUMERICA DISCRETA
# ============================================================

# Numero de filhos de 20 pessoas

filhos = c(0, 0, 1, 0, 2,
  1, 0, 1, 2, 0,
  3, 1, 0, 2, 1,
  0, 1, 2, 0, 1)


filhos


# ?

table(filhos)


# ?

prop.table(table(filhos))


# Frequencia absoluta

freq_abs_filhos = table(filhos)

freq_abs_filhos

freq_rel_filhos = prop.table(freq_abs_filhos)

# ============================================================
# 5.1. GRAFICO DE LINHAS # plot
# ============================================================

# Frequencia absoluta

plot(freq_abs_filhos)

# Frequencia relativa # FACAM ESSE

plot(freq_rel_filhos)


# Personalizacao

plot(freq_rel_filhos,
  main = "Numero de filhos",
  xlab = "Numero de filhos",
  ylab = "Frequencia relativa")



# OBSERVACAO IMPORTANTE: Se uma variavel numerica discreta
# assumir MUITOS VALORES DIFERENTES, faremos graficos que
# usamos para variaveis numericas continuas

# ============================================================
# EXERCICIO 5
# ============================================================

# Quantidade de pares de sapatos

sapatos = c(0, 1, 2, 1, 0,
  1, 3, 0, 2, 1,
  1, 0, 2, 1, 4)

# a) Identifique o tipo da variavel
# b) Construa a tabela de frequencias absolutas
# c) Construa a tabela de frequencias relativas
# d) Construa um grafico de linhas # plot



# ============================================================
# 6. VARIAVEL NUMERICA CONTINUA
# ============================================================

idades = c(18, 18, 19, 19, 19,
  20, 20, 20, 21, 21,
  22, 22, 23, 24, 25,
  27, 29, 31, 35, 42)

idades


# ?

table(idades) # NAO FAZER


# Para variaveis numericas continuas,
# quase sempre temos muitos valores diferentes

# USAMOS INTERVALOS


# ============================================================
# 6.1. HISTOGRAMA # hist
# ============================================================

hist(idades)


# Alterando o numero de classes

# ?

hist(idades, breaks = 5)

# ?

hist(idades,breaks = 10)


hist(idades, freq = TRUE) # Frequencia absoluta

# FAZER DESSA FORMA:

hist(idades, freq = FALSE) # Densidade de frequencia


# Personalizacao

hist(idades, freq = FALSE,
    main = "Histograma das idades",
    xlab = "Idade",
    ylab = "Densidade de frequencia")


# Grafico de barras:
# as barras representam categorias

# Histograma:
# as barras representam intervalos de valores



# ============================================================
# EXERCICIO 6
# ============================================================

# Tempo que alunos demoram pra chegar a faculdade

tempo = c(50, 35, 12, 25, 95, 22, 
          31, 42, 25, 35, 15, 25)

# a) Identifique o tipo da variavel
# b) Construa um histograma # hist
# c) Construa um histograma com 10 classes # breaks


# ============================================================
# 6.2. BOXPLOT
# ============================================================

salarios = c(1800, 1900, 2000, 2100, 2200,
  2300, 2400, 2500, 2600, 2800,
  3000, 3200, 3400, 3600, 4000,
  4300, 4700, 5200, 6000, 12000)

salarios

boxplot(salarios)


# Versao horizontal

boxplot(salarios,
  horizontal = TRUE,
  main = "Boxplot dos salarios",
  xlab = "Salario")



# ============================================================
# VALORES EXTREMOS
# ============================================================

salarios2 = c(1800, 1900, 2000, 2100, 2200,
  2300, 2400, 2500, 2600, 2800,
  3000, 3200, 3400, 3600, 4000,
  4300, 4700, 5200, 6000)

boxplot(salarios2)

c(salarios2, 20000)

# ?

boxplot(c(salarios2, 20000))


# ?

mean(salarios2)
mean(c(salarios2, 20000))

# ?

median(salarios2)
median(c(salarios2, 20000))

# OBSERVACAO: A mediana e mais ROBUSTA do que a media
# com relacao a valores extremos

# ============================================================
# EXERCICIO 7
# ============================================================

x = c(10, 112, 114, 121, 126, 130, 135, 
      144, 147, 150, 220)


# Antes de executar:

# a) Observe os valores e tente prever 
# como sera o boxplot

# b) Construa o boxplot do vetor x


# ============================================================
# EXERCICIO 8 - nao precisa entregar
# ============================================================

# TEMPO

tempo = c(50, 35, 12, 25, 95, 22, 
          31, 42, 25, 35, 15, 25)

tempo

# a) Construa o histograma de tempo
# b) Construa o boxplot de tempo


