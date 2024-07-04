import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
soma= numero_01 + numero_02
print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_01 = int(input("Inserir um numero inteiro: "))
resto_Divisao = numero_01 % 5
print(resto_Divisao)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
multiplicacao_01 =int(input("Insira o primeiro número "))
multiplicacao_02 =int(input("Insira o primeiro número "))
Multiplicacao = multiplicacao_01 * multiplicacao_02
print(Multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_01 = int(input("Inserir um numero inteiro: "))
Quadrado = numero_01**2
print(Quadrado)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
float1 = float(input("Inserir um numero inteiro: "))
float2 = float(input("Inserir um numero inteiro: "))
Soma = float1  + float2
print(Soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
float1 = float(input("Inserir um numero float: "))
float2 = float(input("Inserir um numero float: "))
Media = (float1 + float2) / 2
print(Media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = int(input("Inserir um numero base: "))
potencia = int(input("Inserir um numero expoente: "))
calculo = base**potencia
print(calculo)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Inserira temperatura: "))
conversao = (celsius * 1.8) + 32
print(conversao)


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.+
nome = str(input("Insiria aqui o seu nome: "))
maiuscula = nome.upper()
print(maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = str(input("Insiria aqui o seu nome: "))
espacos = nome.replace(" ","" )
print(espacos)



# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.





# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
from datetime import datetime , date

input_data = date.today()
print(input_data.month) 
print(input_data.year) 


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
String = str(input("Insira uma string: "))
String1 = str(input("Insira outra string: "))
Concatenar = String+String1
print(Concatenar)


# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação 
# AND entre elas.
string = str(input("Digite uma palavra: "))[0]
string1 = str(input("Digite outra palavra: "))[0]
Compara =  string.upper() =="K" and string1.upper() =="M"
print (Compara)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
string = str(input("Digite uma palavra: "))[0]
string1 = str(input("Digite outra palavra: "))[0]
Compara =  string.upper() =="K" or string1.upper() =="M"
print (Compara)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta 
# esse valor.
escolha = str(input("Insira a palavra True ou False: "))
if escolha == "True":
    print(False)
elif escolha == "False":
    print(True)
else:
    print("Digite uma das opçoes corretamente")
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
if numero_01 == numero_02:
    print("Numeros são iguais")
else:
    print("Numeros são diferentes")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
val_1 = float(input("Digite um número: "))
val_2 = float(input("Digite outro número: "))

print(val_1 != val_2 )
# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
phrase = input("Digite uma palavra ou frase: ")

if isinstance(phrase, str):
    formatted_phrase = phrase.replace(" ", "").lower()

    if formatted_phrase == formatted_phrase[::-1]:
        print(f"'{phrase}' é um palíndromo.")
    else:
        print(f"'{phrase}' não é um palíndromo.")

else:
    print("Insira uma palavra ou frase válida.")

# 23: Calculadora Simples
# 24: Classificador de Números
try:
    val = float(input("Digite um número: "))

    if val > 0:
        print(f"{val} é positivo.")
    elif val < 0:
        print(f"{val} é negativo.")
    else:
        print(f"{val} é igual a zero.")
    
    if val % 2 == 0:
        print(f"{val} é par.")
    else:
        print(f"{val} é ímpar.")

except ValueError as e:
    print("\nInsira um número válido.")
    print(f"[ERRO] {e}")

# 25: Conversão de Tipo com Validação
#   Crie um script que solicite ao usuário uma lista de números separados    #
#   por vírgula. O programa deve converter a string de entrada em uma        #
#   lista de números inteiros.                                               #
#                                                                            #
# * Utilize `try-except` para tratar a conversão de cada número e validar    #
#   que cada elemento da lista convertida é um inteiro.                      #
#                                                                            #
# * Se a conversão falhar ou um elemento não for um inteiro, imprima uma     #
#   mensagem de erro. Se a conversão for bem-sucedida para todos os          #
#   elementos, imprima a lista de inteiros.                                  #
#                                                                            #
##############################################################################

try:
    numbers_in = input("Digite números inteiros separados por vírgula: ")

    numbers = [int(number) for number in numbers_in.split(",")]
    print(f"Lista de números: {numbers}")

except ValueError as e:
    print("\nInsira apenas números inteiros válidos.")
    print(f"[ERRO] {e}")