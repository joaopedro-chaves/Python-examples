# If e Else / Se e Senão

#definição de variáveis input
valor_trabalho = float(input("Digite o valor do trabalho: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))

# Tomada de decisão (decisão baseada no valor da variável horas_trabalhadas)
if (horas_trabalhadas >= 100):
    bonus = 500.00
elif (horas_trabalhadas >= 50): # elif / Senão Se
    bonus = 250.00
else:
    bonus = 0

# Soma o valor do trabalho com as horas trabalhadas e soma o bônus
salario = valor_trabalho * horas_trabalhadas + bonus

# Exibição do resultado no formato moeda brasileira
print(f"O salario total é de R${salario}")