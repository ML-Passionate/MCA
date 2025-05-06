# Correspondência multivariada - MCA

Dados: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-

![image](https://github.com/user-attachments/assets/b1d2670d-142f-4a85-a45c-1a1a063cdf0a)


Seleciona apenas variáveis qualitativas
Faz a tabela de contingencia e submete ao modelo
Teste do ki^2. Se p-value <= 0,05, descartamos H0, ou seja, existe associação significativa. Fazemos o teste para cada par de variáveis.
Dimensoes = qtd de categorias - qta de variaveis
Inercia total = dimensoes / numero de variaveis
Média da inercia = inercia total / dimensoes
Eigenvalues = numero de dimensões, porém, so interessa eigenvalues > média da inercia, ou seja, sao esses que tem associação significativa
