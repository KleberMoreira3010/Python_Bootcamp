import math
from datetime import date, datetime

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
def temperatura (valor_1: float):
    Fahrenheit = (valor_1 *1.8)+32
    return (Fahrenheit)


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

def circulo ( ):
   raio_do_circulo = float(input("Digite o raio: "))
   area_do_circulo = math.pi * raio_do_circulo ** 2
   area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
   return print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
def maiuscula():
    palavra = str(input("Escreva uma palavra: "))
    transformacao = palavra.upper()
    return print(transformacao)


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def minuscula():
    palavra = str(input("Escreva uma palavra: "))
    transformacao = palavra.lower()
    return print(transformacao)


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, 
# imprima esta frase sem espaços em branco no início e no final.
def sem_espacos():
    frase =  str(input("Insira um frase: "))
    transformacao = frase.strip()
    return print(f"A frase sem espaços é: {transformacao} (Tamanho: {len(transformacao)})")


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" 
# e, em seguida, imprima o dia, o mês e o ano separadamente.
def converte_data ():
    input_data = input("Insira uma data no formato dd/mm/aaaa")
    data_convert = datetime.strptime(input_data, '%d/%m/%Y')
    return print(f"O dia é:  {data_convert.day}  o mês {data_convert.month} e o  ano {data_convert.year}" )


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

def concatena ():
    str1 = str(input("Escreva uma palavra: "))
    str2 = str(input("Escreva outra palavra: "))
    concatena = str1 + " " + " " + str2
    return print(concatena)

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário 
# e retorne o resultado da operação AND entre elas.
def validacao ():
    str1 = str(input("Escreva uma palavra: "))
    str2 = str(input("Escreva outra palavra: "))
    compara = str1==str2
    return ("Comparando as duas strings: ", compara)
        

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def validacao1 ():
    str1 = int(input("Escreva um numero: "))
    str2 = str(input("Escreva uma palavra: "))
    compara = str1>5
    compara1 = str2=='Kleber'
    return ("Comparando as duas strings: ", compara or compara1)




# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def bolle ():
    str1 = bool(input('Digite um booleano: True ou False'))
    if str1==True:
        str1==False
    else: str1== False
    return str1    


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

def val_num ():
    num1 = int(input("Escreva um numero: "))
    num2 = int(input("Escreva outro número: "))
    compara = num1==num2

    return ("Comparando os 2 números: ", compara)



# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

def val_num1 ():
    num1 = int(input("Escreva um numero: "))
    num2 = int(input("Escreva outro número: "))
    compara = num1!=num2

    return ("São diferentes?: ", compara)


# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
lista = [25,31,23,19,5,2,1,9999]

def ordena(list1: list):
    ordena=sorted(lista)
    return print(ordena)

# 25: Conversão de Tipo com Validação

