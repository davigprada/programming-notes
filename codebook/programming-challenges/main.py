#Ejercicios de Funciones

#1
def saludo(n):
    return f'¡Hola, {n}!'
#print(saludo('david'))


#2 -Formas de obtener el factorial de un número
#1 Usando un ciclo For
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *=i
    return resultado

print(factorial(4))


#2 Usando recursividad
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

#Importando el modulo math
import math 

numero = 4
resultado = math.factorial(numero) 
print(resultado)



#3
def area_circulo(r):
    return math.pi * r**2

def volumen_cilindro(h, area_func):
    return h * area_func

total = volumen_cilindro(6, area_circulo(5))
resultado = round(total, 2)
#print(resultado) ###CODIGO MALO -> CORREGIR


#MI CODIGO INCORRECTO
numbers = [2, 5, 1, 6, 12, 59, 245, 995, 4]
def media():
    resultado = sum(numbers)/len(numbers)
    return resultado
print(resultado)

#CODIGO CORRECTO
def media(numbers):
    resultado = sum(numbers) / len(numbers)
    return resultado

numbers = [2, 5, 1, 6, 12, 59, 245, 995, 4]
resultado = media(numbers)
print(resultado)


#5
nnnnnnn = [2, 4, 5, 7, 10]
for i in nnnnnnn:
    print(i ** 2, end=' ')


def cuadrado(lista_numeros):
    lista = []
    for i in lista_numeros:
        lista.append(i ** 2)
    return lista

r = cuadrado([2, 4, 5, 6, 10 ])
print(r)


    
#Programa que pide la contraseña 
""" pw = 'David18964'
while True:
    pw_usuario = input('Digite la contraseña: ')
    if pw == pw_usuario:
        print('contraseña correcta')
        break
    else:
        print('contraseña incorrecta')
     """

#

cantidad_palabras = int(input('Dígame cuántas palabras tiene la lista: '))
palabras = []
if cantidad_palabras == 0:
    print('¡Imposible!')
else:
    for i in palabras:
        




#print(f'La lista creada es {lista_palabras}')

