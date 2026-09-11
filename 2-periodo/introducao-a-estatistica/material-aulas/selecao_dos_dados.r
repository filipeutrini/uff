#--------------------------------------------------------
# LENDO OS DADOS
#--------------------------------------------------------

# Define o diretorio
# setwd("C:/...")
# setwd("~/Pasta Pública/INTRODUCAO A ESTATITICA (MAT)")

# Selecionando uma amostra

#### MODIFICAR NOME DOS DADOS

base_total = read.csv("Bank_Churn.csv", sep = ",")

# base_total_0 = read.csv("Bank_Churn.csv", sep = ",")
# base_total = base_total_0[,-c(2,5,6)] # Retira colunas (REMOVE VARIAVEIS)
# base_total = base_total_0[,c(2,5,6)] # Seleciona somente algumas colunas

total = nrow(base_total)


### VERIFICAR SE TEM NA
# base_total_com_na = read.csv("Bank_Churn.csv", sep = ",")
# base_total = na.omit(base_total_com_na)
# total = nrow(base_total)


# CALCULO PARA DEFINIR O TAMANHO DA AMOSTRA

# Definir variavel importante/alvo. 
# Exemplo: score de credito
variavel = base_total$CreditScore
mean(variavel)
var(variavel)

hist(base_total$CreditScore)

# SUGESTAO
# erro entre 1% e 10% do valor da media
0.01*mean(variavel)
0.10*mean(variavel)

erro = 15 # Estou disposta a errar em 15 o score de credito
# MUDAR A VARIAVEL E O ERRO
tamanho_da_amostra = ((1.96^2)*var(variavel))/(erro^2)

# fixar uma semente
set.seed(12345)
amostra = sample(1:total,tamanho_da_amostra)

# Selecionando a amostra
dados = base_total[amostra,]

# Exportar os dados para o computador
write.csv(dados,file="dados.csv")


#=================================================

# ALTERNATIVA PARA DEFINIR O DIRETORIO DE TRABALHO
# (Primeiro salvar o arquivo .R na MESMA PASTA que o dados.csv)
if (!require(rstudioapi)) install.packages("rstudioapi")
library(rstudioapi)
caminho <- rstudioapi::getActiveDocumentContext()$path
setwd(paste(unlist(strsplit(caminho,"/"))[1:(length(unlist(strsplit(caminho,"/")))-1)],collapse="/"))
