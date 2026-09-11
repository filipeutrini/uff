# ============================================================
# AULA PRATICA 1
# ============================================================
#
# Objetivos:
#
# - Ler base de dados no R
# - Frequencias acumuladas
# - Medidas de posicao e dispersao
# - Personalizar graficos
# - Trabalho
#
# ============================================================





# ============================================================
# 1. LENDO OS DADOS
# ============================================================

# Define o diretorio
# setwd("C:/...")
setwd("~/Pasta Pública/INTRODUCAO A ESTATITICA (MAT)")


read.csv("dados.csv")
read.csv("dados.csv",sep=";")


# Le os dados e coloca no objeto "dados"
dados = read.csv("dados.csv",sep=";") # dec = ","
dados


# Verificar o separador entre colunas, normalmente ";" ou ","
# e o separador decimal, normalmente "," ou "."









# ============================================================
# 2. VARIAVEL
# ============================================================

# $

dados$idade

dados$genero

# ?

# Variavel salario?

dados$salario



# ============================================================
# 3. TABELAS DE FREQUENCIA
# ============================================================

table(dados$grau_de_instrucao)

freq_abs_grau_de_instrucao = table(dados$grau_de_instrucao)

freq_abs_grau_de_instrucao

prop.table(freq_abs_grau_de_instrucao)


# ============================================================
# 3.1 FREQUENCIA ACUMULADA # cumsum()
# ============================================================

# Como fazer a frequencia absoluta acumulada?
# O argumento sao as frequencias absolutas

cumsum(freq_abs_grau_de_instrucao)

# Como fazer a fequencia relativa acumulada?
# O argumento sao as frequencias relativas

# prop.table(freq_abs_grau_de_instrucao)

freq_rel_grau_de_instrucao = prop.table(table(dados$grau_de_instrucao))

cumsum(freq_rel_grau_de_instrucao)


# Colocando em objetos:

freq_abs_acumulada_grau_de_instrucao = cumsum(freq_abs_grau_de_instrucao)

freq_abs_acumulada_grau_de_instrucao

# ?

# frequencia relativa acumulada

freq_rel_acumulada_grau_de_instrucao = cumsum(prop.table(table(dados$grau_de_instrucao)))

freq_rel_acumulada_grau_de_instrucao

# ?

# Quantas pessoas possuem grau de instrucao 
# menor ou igual a Graduacao?




# ============================================================
# 3.2 MONTANDO A TABELA DE DISTRIBUICAO DE FREQUENCIAS # data.frame()
# ============================================================


data.frame(
  a = c(3,2,1),
  b = c(2,3,4)
)


# Tabela de distribuicao de frequencias


# grau de inst
# ens med
# grad
# pos


data.frame(
  grau_de_instrucao = c("Ens med","Grad","Pos grad")
)


# nomes dos graus de instrucao
names(freq_abs_acumulada_grau_de_instrucao)

as.numeric(freq_abs_grau_de_instrucao)

tabela_grau_de_instrucao = data.frame(
  grau_de_instrucao = names(freq_abs_grau_de_instrucao),
  ni = as.numeric(freq_abs_grau_de_instrucao),
  fi = as.numeric(freq_rel_grau_de_instrucao),
  Ni = as.numeric(freq_abs_acumulada_grau_de_instrucao),
  Fi = as.numeric(freq_rel_acumulada_grau_de_instrucao)
)

tabela_grau_de_instrucao




# ============================================================
# 4. MEDIDAS
# ============================================================

# ============================================================
# 4.1 MEDIA
# ============================================================

mean(dados$idade)


# ============================================================
# 4.2 MEDIANA
# ============================================================

median(dados$idade)


# ============================================================
# 4.3 QUARTIS
# ============================================================

quantile(dados$idade)


# Por padrao, o R apresenta:
# minimo
# primeiro quartil
# mediana
# terceiro quartil
# maximo


# ============================================================
# 4.4. VARIANCIA
# ============================================================

var(dados$idade)


# ============================================================
# 4.5 DESVIO PADRAO
# ============================================================

sd(dados$idade)


# ============================================================
# 4.6 DISTANCIA INTERQUARTILICA
# ============================================================

IQR(dados$idade)


# ?

# Calcule a media, mediana e desvio padrao 
# da variavel salario

mean(dados$salario)
median(dados$salario)
sd(dados$salario)


# ============================================================
# 5. GRAFICOS - MODIFICACOES
# ============================================================

# ============================================================
# 5.1 GRAFICO DE BARRAS
# ============================================================

freq_abs_genero = table(dados$genero)
freq_rel_genero = prop.table(freq_abs_genero)

barplot(freq_rel_genero)

# Modificacoes ultima aula:

barplot(freq_rel_genero,
  main = "Grafico de barras
  de genero",                      # TITULO
  xlab = "Genero",                 # EIXO X                
  ylab = "Frequencia relativa"     # EIXO Y
)

# Outras modificacoes:

barplot(freq_rel_genero,
  main = "Grafico de barras
  de Genero",
  xlab = "Genero",
  ylab = "Frequencia relativa",
  col = c("lightblue", "lightpink"),   # CORES
  ylim = c(0,1)                        # LIMITE
)


# ============================================================
# 5.2 HISTOGRAMA
# ============================================================

hist(dados$salario)


hist(dados$salario,freq = FALSE,
  main = "Histograma de Salario",
  xlab = "Salario",
  ylab = "Densidade de frequencia",
  col = "lightblue"
)


# ============================================================
# 5.3 BOXPLOT
# ============================================================

boxplot(dados$salario)


boxplot(dados$salario,
  main = "Boxplot de Salario",
  ylab = "Salario",
  col = "lightblue"
)



# ============================================================
# 6. LEGENDA
# ============================================================

# Barras

barplot(freq_rel_genero,
  main = "Grafico de barras de Genero",
  xlab = "Genero",
  ylab = "Frequencia relativa",
  col = c("lightpink", "lightblue")
)

legend(
  "topright",
  legend = c("Feminino", "Masculino"),
  fill = c("lightpink", "lightblue")
)

# Setores

pie(freq_rel_genero,
        main = "Grafico de setores de Genero",
        col = c("lightpink", "lightblue")
)

legend("topright",
  legend = paste(100*round(freq_rel_genero,2),"%"),
  fill = c("lightpink", "lightblue")
)



# ============================================================
# 7. TRABALHO
# ============================================================

# PASSO 1
# Encontre uma base de dados no Kaggle
# que atenda os requisitos

banco = read.csv("Bank_Churn.csv",sep=",")
banco$Gender

barplot(prop.table(table(banco$Gender)))

# Duvidas sobre o trabalho

# Alternativa 
# (Primeiro salvar o arquivo .R 
# na MESMA PASTA que o dados.csv)
if (!require(rstudioapi)) install.packages("rstudioapi")
library(rstudioapi)
caminho = rstudioapi::getActiveDocumentContext()$path
setwd(paste(unlist(strsplit(caminho,"/"))[1:(length(unlist(strsplit(caminho,"/")))-1)],collapse="/"))

