#========================================================
# AULA 3: ASSIMETRIA E CURTOSE EXCESSIVA
#========================================================

#========================================================
# 1) FUNCOES "NA MAO"
#========================================================

# Assimetria amostral ajustada (tipo Fisher-Pearson)
assimetria = function(x) {
  x = x[is.finite(x)]
  n = length(x)
  
  if (n < 3) {
    stop("Sao necessarios pelo menos 3 valores.")
  }
  
  m = mean(x)
  s = sd(x)
  
  if (s == 0) {
    stop("Desvio padrao zero: assimetria indefinida.")
  }
  
  g1 = sum((x - m)^3) / n / (sqrt(sum((x - m)^2) / n)^3)
  
  # ajuste amostral
  G1 = sqrt(n * (n - 1)) / (n - 2) * g1
  
  return(G1)
}

# Curtose excessiva amostral ajustada
curtose_excess = function(x) {
  x = x[is.finite(x)]
  n = length(x)
  
  if (n < 4) {
    stop("São necessarios pelo menos 4 valores.")
  }
  
  m = mean(x)
  s2_n = sum((x - m)^2) / n
  
  if (s2_n == 0) {
    stop("Variancia zero: curtose indefinida.")
  }
  
  g2 = sum((x - m)^4) / n / (s2_n^2) - 3
  
  # ajuste amostral
  G2 = ((n - 1) / ((n - 2) * (n - 3))) * ((n + 1) * g2 + 6)
  
  return(G2)
}

#========================================================
# 2) ASSIMETRIA
#========================================================

# Objetivo:
# Comparar histograma + valor da medida de assimetria

#========================================================

set.seed(123)

# 1. Assimetria negativa
x_assim_neg <- 60 - rexp(3000, rate = 1/10)

# 2. Aproximadamente simetrica
x_simetrico <- rnorm(3000, mean = 50, sd = 10)

# 3. Assimetria positiva fraca
x_assim_pos_fraca <- rlnorm(3000, meanlog = log(50), sdlog = 0.2)

# 4. Assimetria positiva forte
x_assim_pos_forte <- rexp(3000, rate = 1/10) + 40


#========================================================
# 3) HISTOGRAMAS
#========================================================

par(mfrow = c(2, 2))

hist(x_assim_neg,
     breaks = 20,
     main = paste("Assimetria negativa\n",
                  "Valor:", round(assimetria(x_assim_neg), 2)),
     xlab = "Valores")

hist(x_simetrico,
     breaks = 20,
     main = paste("Quase simetrica\n",
                  "Valor:", round(assimetria(x_simetrico), 2)),
     xlab = "Valores")

hist(x_assim_pos_fraca,
     breaks = 20,
     main = paste("Assimetria positiva (fraca)\n",
                  "Valor:", round(assimetria(x_assim_pos_fraca), 2)),
     xlab = "Valores")

hist(x_assim_pos_forte,
     breaks = 20,
     main = paste("Assimetria positiva (forte)\n",
                  "Valor:", round(assimetria(x_assim_pos_forte), 2)),
     xlab = "Valores")

par(mfrow = c(1, 1))


#========================================================
# 4) COMENTARIOS
#========================================================

# Assimetria mede o GRAU DE INCLINACAO
# Se for perto de zero, a distribuicao e
# aproximadamente simetrica
# Se for positiva, a cauda e mais "alongada" a direita
# Se for negativa, a cauda e mais "alongada" a esquerda

# Importante:
# a assimetria NAO mede dispersão
# ela mede o DESEQUILIBRIO entre os lados


#========================================================
# 5) CURTOSE EXCESSIVA
#========================================================

set.seed(321)

# Referencia: normal
x_normal = rnorm(5000, mean = 0, sd = 1)

# Curtose excessiva positiva:
x_caudas_pesadas = rt(5000, df = 3)

# Curtose excessiva negativa:
x_achatada = runif(5000, min = -sqrt(3), max = sqrt(3))


#========================================================
# 6) HISTOGRAMAS
#========================================================

par(mfrow = c(1, 3))

hist(x_normal,
     breaks = 20,
     main = paste("Normal\nExcess =", 
                  round(curtose_excess(x_normal), 3)),
     xlab = "Valores")

hist(x_caudas_pesadas,
     breaks = 20,
     main = paste("Caudas pesadas\nExcess =", 
                  round(curtose_excess(x_caudas_pesadas), 3)),
     xlab = "Valores",
     xlim = c(-6, 6))

hist(x_achatada,
     breaks = 20,
     main = paste("Mais achatada\nExcess =", 
                  round(curtose_excess(x_achatada), 3)),
     xlab = "Valores")

par(mfrow = c(1, 1))

#========================================================
# 7) COMENTARIOS
#========================================================

# Curtose excessiva compara o "peso das caudas" 
# e a concentracao dos valores em torno do centro 
# (em relacao a normal)

# Interpretacao:
# Curtose excessiva ~ 0: parecida com a normal
# Curtose excessiva > 0: caudas mais pesadas 
# (mais concentracao no centro)
# Curtose excessiva < 0: caudas mais leves 
# (formato mais achatado)


#========================================================
# 8) VARIANCIA x CURTOSE
#========================================================

# Variancia:
# Mede DISPERSAO (em torno da media)

# Curtose excessiva:
# Mede o comportamento das CAUDAS


#========================================================
# 9) EXEMPLO
#========================================================

set.seed(123)

# Normal com variancia ~ 1
a = rnorm(10000, mean = 0, sd = 1)
var(a)

# Uniforme com variancia ~ 1
b = runif(10000, min = -sqrt(3), max = sqrt(3))
var(b)

# t com variancia ~ 1
c = rt(10000, df = 5) / sqrt(5/3)
var(c)


#========================================================
# 10) HISTOGRAMAS: MESMA VARIANCIA, CURTOSE DIFERENTE
#========================================================

par(mfrow = c(1, 3))

hist(a,
     breaks = 10,
     main = paste("Normal\nVar =", round(var(a), 2),
                  "\nExcess =", round(curtose_excess(a), 2)),
     xlab = "Valores",
     xlim = c(-5, 5))

hist(b,
     breaks = 10,
     main = paste("Uniforme\nVar =", round(var(b), 2),
                  "\nExcess =", round(curtose_excess(b), 2)),
     xlab = "Valores",
     xlim = c(-5, 5))

hist(c,
     breaks = 10,
     main = paste("t ajustada\nVar =", round(var(c), 2),
                  "\nExcess =", round(curtose_excess(c), 2)),
     xlab = "Valores",
     xlim = c(-5, 5))

par(mfrow = c(1, 1))


#========================================================
# 11) EXEMPLO 2
#========================================================

par(mfrow = c(1, 2))

set.seed(123)

x1 = rnorm(1000, 0, 1)
boxplot(x1)

# Mistura: muitos valores perto de 0, 
# mas alguns valores extremos (outliers)
x2 = c(rnorm(950, 0, 0.7), rnorm(50, 0, 3))
boxplot(x2)


#========================================================
# 11) HISTOGRAMAS
#========================================================

par(mfrow = c(1, 2))

hist(x1,
     breaks = 20,
     main = paste("Normal\nVar =", round(var(x1), 2),
                  "\nExcess =", round(curtose_excess(x1), 2)),
     xlab = "Valores",
     xlim = c(-8, 8))

hist(x2,
     breaks = 20,
     main = paste("Mistura com extremos\nVar =", round(var(x2), 2),
                  "\nExcess =", round(curtose_excess(x2), 2)),
     xlab = "Valores",
     xlim = c(-8, 8))

par(mfrow = c(1, 1))

# Curtose "penaliza" MUITO MAIS valores extremos!


#========================================================
# 12) RESUMO
#========================================================

# ASSIMETRIA mede GRAU DE INCLINACAO
# VARIANCIA mede DISPERSAO
# CURTOSE excessiva mede o "peso das caudas"
# (e compara com a distribuicao normal)

