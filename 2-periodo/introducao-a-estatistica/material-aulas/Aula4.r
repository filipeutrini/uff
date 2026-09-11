#----------------------------------------------------------
# Investigando relacoes entre 2 variaveis
#----------------------------------------------------------

# 2 categoricas: 
# Tabela de contingencia
# Proporcoes OBSERVADAS (probabilidade condicional)
# Medida Qui-quadrado

#----------------------------------------------------------
# Dados
#----------------------------------------------------------

if (!require(rstudioapi)) install.packages("rstudioapi")
library(rstudioapi)
caminho <- rstudioapi::getActiveDocumentContext()$path
setwd(paste(unlist(strsplit(caminho,"/"))[1:(length(unlist(strsplit(caminho,"/")))-1)],collapse="/"))

# Lendo os dados

dados = read.csv("dados.csv", sep = ";")

#----------------------------------------------------------
# VARIAVEIS
#----------------------------------------------------------

# individuo -> id
# idade -> variavel numerica continua
# genero -> variavel categorica nominal
# grau_de_instrucao -> variavel categorica ordinal
# quantidade_de_filhos -> variavel numerica discreta
# salario -> variavel numerica continua

#----------------------------------------------------------
# 1. RELACAO ENTRE 2 VARIAVEIS CATEGORICAS
#----------------------------------------------------------

# Exemplo:
# genero e grau_de_instrucao

# Pergunta:
# Existe relacao entre genero e grau de instrucao?
# POR EXEMPLO:
# No grupo das mulheres parece haver uma distribuicao
# de grau de instrucao diferente do grupo dos homens?

#----------------------------------------------------------
# TABELA DE CONTINGENCIA
#----------------------------------------------------------

table(dados$genero,
      dados$grau_de_instrucao)

tabela_genero_instrucao = table(dados$genero,
                                dados$grau_de_instrucao)

tabela_genero_instrucao

#----------------------------------------------------------
# PROPORCOES
#----------------------------------------------------------

prop.table(tabela_genero_instrucao)

prop.table(tabela_genero_instrucao,
           margin = 1)

prop.table(tabela_genero_instrucao,
           margin = 2)


# %
round(prop.table(tabela_genero_instrucao,
                 margin = 1) * 100, 1)

#----------------------------------------------------------
# TESTE QUI-QUADRADO
#----------------------------------------------------------

# H0: nao existe relacao
# H1: existe relacao

# Medida qui-quadrado (explicando as contas)

qui <- chisq.test(tabela_genero_instrucao)

qui

qui$expected

qui$p.value

# INTERPRETAR O P-VALOR

# H0: nao existe relacao
# H1: existe relacao

# Considerando nivel de significancia:
# alpha = 0,05 (FIXAR)
# Se p-valor < 0,05 -> Rejeitar H0 (Temos indicios de que ha relacao)
# Se p-valor >= 0,05 -> Não rejeitar H0 (Nao temos indicios de que haja relacao)

# VISUALIZACAO DO PVALOR

{p_valor <- qui$p.value
gl = qui[2]$parameter
x <- seq(0, qchisq(0.999, df = gl), length.out = 500)
y <- dchisq(x, df = gl)
plot(x, y,
     type = "l",
     lwd = 2,
     xlab = expression(chi^2),
     ylab = "Densidade",
     main = paste("Distribuicao Qui-quadrado (gl =", gl, ")"))
abline(v = qui$statistic, lty = 2, col = "red", lwd = 2)
polygon(c(qui$statistic, x[x >= qui$statistic], max(x)),
        c(0, y[x >= qui$statistic], 0),
        col = rgb(1, 0, 0, 0.3),
        border = NA)}

#----------------------------------------------------------
# GRAFICO
#----------------------------------------------------------

barplot(prop.table(table(dados$genero,
                         dados$grau_de_instrucao),
                   margin = 2), # margin = 1 ou margin = 2
        beside = TRUE,
        legend = TRUE,
        ylim = c(0,1),
        main = "Grau de instrucao por genero",
        ylab = "Proporcao")

# OU

barplot(prop.table(table(dados$grau_de_instrucao,
                         dados$genero),
                   margin = 2),
        beside = TRUE,
        legend = TRUE,
        ylim = c(0,1),
        main = "Grau de instrucao por genero",
        ylab = "Proporcao")
