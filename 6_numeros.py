#int
number = 10
result = number + 10
#para concatenar usamos la , así:
print("El resultado es: ", result)
#también podemos usar una resta como -10 o una multiplicación
#o una división, lo que sea 
#en el caso de las divisiones, en python siempre que
#usemos / el resultado será un float
""" por ejemplo si yo divido 10/2 el resultado será 5.0 (con un .0, siempre
aparecerán decimales si uso /, PEEERO si uso // el resultado será 5 (sin decimales))"""
#también podemos usar el % para obtener el residuo de una división
""" Entonces tenemos estos ejemplos para la clase:
División normal / (siempre devuelve float)
# División que siempre da resultado decimal
print(10 / 2)    # 5.0 (aunque es exacta, devuelve float)
print(7 / 2)     # 3.5
print(11 / 4)    # 2.75
print(5 / 3)     # 1.6666666666666667

División entera // (trunca el resultado)
# División que trunca el resultado al entero inferior
print(10 // 2)   # 5 (igual que / en este caso)
print(7 // 2)    # 3 (3.5 se trunca a 3)
print(11 // 4)   # 2 (2.75 se trunca a 2)
print(5 // 3)    # 1 (1.666... se trunca a 1)
print(-7 // 2)   # -4 (cuidado: va hacia abajo en la recta numérica)
""" 
#Comparación directa
a = 15
b = 4

print(f"{a} / {b} = {a / b}")    # 15 / 4 = 3.75
print(f"{a} // {b} = {a // b}")  # 15 // 4 = 3
print(f"Residuo: {a % b}")       # Residuo: 3
#Ahora tenemos un Ejemplo práctico: Conversión de segundos
segundos_totales = 5000

""" La f antes de las comillas en print(f"texto {variable}") 
es para los f-strings (formatted string literals), una característica de Python 3.6+ 
que hace que sea más fácil formatear cadenas. PILlA, POR EJEMPLO:

nombre = "Ana"
edad = 25

# Sin f-string (forma antigua)
print("Hola " + nombre + ", tienes " + str(edad) + " años")

# Con f-string (forma moderna)
print(f"Hola {nombre}, tienes {edad} años")
 OTROS EJEMPLOS:
 # Operaciones dentro de las llaves
print(f"En 5 años tendrás {edad + 5} años")

# Llamadas a funciones
print(f"Tu nombre en mayúsculas es {nombre.upper()}")

# Formateo de números
precio = 49.99
print(f"Precio: ${precio:.2f}")  # Muestra 2 decimales: $49.99
 """
# Convertir a horas, minutos y segundos
horas = segundos_totales // 3600
resto = segundos_totales % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}h {minutos}m {segundos}s")  # 1h 23m 20s


# Definir las variables primero
nombre = "Ana"  # Añade esta línea
edad = 25       # Añade esta línea

# Luego puedes usarlas
print(f"En 5 años tendrás {edad + 5} años")
print(f"Tu nombre en mayúsculas es {nombre.upper()}")

# Operaciones dentro de las llaves
print(f"En 5 años tendrás {edad + 5} años")

# Llamadas a funciones
print(f"Tu nombre en mayúsculas es {nombre.upper()}")

# Formateo de números
precio = 49.99
print(f"Precio: ${precio:.2f}")  # Muestra 2 decimales: $49.99

#CONTINUANDO CON LO DE LA f en el print:

# %-formatting (viejo estilo)
print("Hola %s" % nombre)

# .format() (estilo más nuevo)
print("Hola {}".format(nombre))

# f-strings (el más moderno y recomendado)
print(f"Hola {nombre}")