# 1) Insira o seu nome (INPUT)
nome=input("Por favor, digite o seu nome: ")

# 2) Entre com o valor do salario
salario = 1000

# 3) Percentual do bonus
percentual= float(input("Insira qual será o percentual do Bônus sobre o salário: "))

# 4) Cálculo final
bonus = float((salario * percentual) + salario )

# 5) Print do resultad de uma mensagem personalizada

print(f" {nome}, valor do seu Bônus será de {bonus}.")
      


