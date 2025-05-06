# Correspondência multivariada - MCA

Dados: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-

![image](https://github.com/user-attachments/assets/b1d2670d-142f-4a85-a45c-1a1a063cdf0a)

O programa analisa um conjunto de dados simulados sobre hábitos estudantis e desempenho acadêmico, focando apenas nas variáveis qualitativas. Para cada par de variáveis categóricas, é construída uma tabela de contingência e aplicado o teste do qui-quadrado, verificando se existe associação estatisticamente significativa (p-valor ≤ 0,05). Em seguida, calcula-se a inércia total com base na quantidade de categorias e variáveis, bem como os autovalores (eigenvalues) das dimensões. Apenas os autovalores acima da média da inércia são considerados relevantes, pois indicam associações significativas entre as variáveis analisadas.
