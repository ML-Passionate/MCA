# Correspondência multivariada - MCA

Dados: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance

![image](https://github.com/user-attachments/assets/ab3c17fa-c6b8-4fbd-a833-a3d845d617c1)


Seleciona apenas variáveis qualitativas
Faz a tabela de contingencia e submete ao modelo
Teste do ki^2. Se p-value <= 0,05, descartamos H0, ou seja, existe associação significativa. Fazemos o teste para cada par de variáveis.
Dimensoes = qtd de categorias - qta de variaveis
Inercia total = dimensoes / numero de variaveis
Média da inercia = inercia total / dimensoes
Eigenvalues = numero de dimensões, porém, so interessa eigenvalues > média da inercia, ou seja, sao esses que tem associação significativa
