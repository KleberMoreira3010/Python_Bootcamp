import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
def soma_valores ( valor_1:int, valor_2:int) :
    soma=valor_1 + valor_2
    return print(soma)
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
def resto_divisao (valor:int):
    resto = valor % 5
    return resto

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
def multiplica_valores ( valor_1:int, valor_2:int) :
    multiplica=valor_1 * valor_2
    return print(multiplica)


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
def quadrado_valores ( valor_1:int) :
    quadrado=valor_1  * valor_1
    return print(quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

def soma_flutuantes(valor_1:float, valor_2:float):
    flutuantes=valor_1  + valor_2
    return print(flutuantes)



# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
def media (valor_1, valor_2):
    media =( valor_1 + valor_2) /2
    return media


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
def potencia (base, expoente ):
    calculo = base ** expoente
    return calculo

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação