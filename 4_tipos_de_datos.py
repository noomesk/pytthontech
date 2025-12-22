#Strings
#Integers
#Floats
#Booleans

#para el 1er tipo de variables, cadenas:
from calendar import firstweekday


first_name = "Angie" #comillas dobles
last_name = 'Pablo' #comillas simples

print(first_name, last_name) #ambas variables son tipo string
#ambas variables almacenan cadenas de caracteres
type(first_name)
print(type(first_name))
print(type(last_name))

#AHORA LOS ENTEROS
"""Los tipos de datos enteros, nos permiten representar
números enteros ya sea con o sin signo  """
age = 26
print(age)
print(type(age))
#ahora también lo podemos hacer con números neg
age_neg = -26
print(age_neg)
print(type(age_neg))

#ahora si vamos a usar números grandes podemos separarlos por un _ así:
number = 100_000_000 #asi es más facil de leer para los humanos
print(number)
print(type(number)) # en python usar _ para separar 
#números no supone ningun problema, mira: (ejecuto y sale normal el número
#eso es una buena práctica

#AHORA VAMOS CON LOS FLOTANTES:
""" igual que con los int representamos números
sólo que con los flotantes vamos a representar números
con punto décimal, por ejemplo:
"""
pi = 3.1416
print(pi)
print(type(pi)) #sale tipo float 

#AHORA VAMOS CON LOS BOLEANOS
""" Los datos de tipo boolean, nos permiten representar
verdadero (True) o falso(False).  """

anshi_es_real = True
print(anshi_es_real)
print(type(anshi_es_real)) #sale tipo bool
#de la misma manera si pusiera en vez de True, False
