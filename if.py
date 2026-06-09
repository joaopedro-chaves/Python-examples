valor_trabalho = float(input("Digite o valor do trabalho: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))

if (horas_trabalhadas >= 100):
    bonus = 500.00
else:
    bonus = 0

salario = valor_trabalho * horas_trabalhadas + bonus
print(f"O salario total é de R${salario}")