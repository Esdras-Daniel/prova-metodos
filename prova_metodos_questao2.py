import numpy as np

# Armazena os valores atuais dos pontos
pontos = np.zeros(3)
# Armazena os últimos valores dos pontos
pontos_anterior = []
pontos_anterior_comparacao = []
iteracao = 1

# Preenche os valores iniciais dos pontos anteriores, no caso todos = 0
pontos_anterior = pontos
for i in range(len(pontos)):
    pontos_anterior_comparacao.append(pontos[i])

print("Valor inicial: ", pontos)

while iteracao <= 4:
    # Altera cada valor da lista pontos em função dos pontos anteriores
    pontos[0] = (9 - pontos_anterior[1] - pontos_anterior[2])/3
    pontos[1] = (1 - pontos_anterior[0] + pontos_anterior[2])/5
    pontos[2] = (35 - (2*pontos_anterior[0]) - pontos_anterior[1])/6

    # Altera o valor dos pontos anteriores para os pontos atuais 
    for i in range(len(pontos)):
        pontos_anterior_comparacao[i] = pontos[i]

    print("\nIteração", iteracao, ":")
    print("Pontos: ", pontos)

    iteracao += 1

erro = []
pontos_exatos = [0.842, 1.105, 5.368]

for i in range(len(pontos)):
    erro.append(pontos_exatos[i]-pontos[i])

print("Norma dos erros: ", np.linalg.norm(erro))
print("Norma dos pontos exatos: ", np.linalg.norm(pontos_exatos))
print("Erro relativo: ", np.linalg.norm(erro)/np.linalg.norm(pontos_exatos))
