#EN PYTHON NO EXISTEN LAS CONSTANTES (en c# o java si)
#pero para indicar que una variable es constante lo que hacemos es usar mayúsculas, así:
VERSION = 1.0 #con esto indicamos que esta variable se trate como una constante
# así, en ese formato solo se usaria con fines de lectura

print(VERSION) 
print(type(VERSION))

#ahora si quisiera cambiar el valor de la constante, solo lo cambio asÍ:

VERSION = 2.0
print(VERSION)
print(type(VERSION))
#sin embargo debemos evitar modificar sus valores

#EXPLAIN
"""  ¿Por qué Python no tiene constantes?
Python sigue el principio de "somos todos adultos responsables"
(We're all consenting adults). 
En lugar de imponer restricciones rígidas, 
confía en la disciplina del programador.
 Aunque técnicamente no existen constantes inmutables, 
 la convención de mayúsculas (CONSTANTE) 
 indica la intención de que el valor no debería modificarse. 
 
 ¿Por qué mayúsculas?
Convención: Las mayúsculas (PI = 3.1416) son una señal visual para otros 
programadores (y para ti mismo) de que el valor no debe
 cambiar. No es obligatorio:
 Es solo una convención, no una restricción del 
 lenguaje.
 
 . "Solo lectura" en este contexto significa:
Intención: El valor no debería ser modificado 
después de su definición. Z.B: 
TASA_IVA = 0.19  # Se espera que esto no cambie
TASA_IVA = 0.20  # ¡Código confuso! ¿Error o cambio intencional?


Diferencia entre variable y constante:
Variable: Valor que puede cambiar durante la ejecución (ej: contador = 0).
Constante: Valor que no debería cambiar (ej: GRAVEDAD_TIERRA = 9.81).

¿Por qué evitar modificar constantes?
Mantenibilidad: Si MAX_INTENTOS = 3 se usa en 10 lugares, cambiarlo podría romper la lógica.
Prevención de errores: Evita modificaciones accidentales.
Legibilidad: Clarifica la intención del código.
BUENO AMX, UNE EJEMPLO PRÁCTICO SERIA ESTE:

# Constantes (convención)
DIAS_SEMANA = 7
PRECIO_BASE = 100

# Variable (puede cambiar)
descuento = 0.1
precio_final = PRECIO_BASE * (1 - descuento)  # PRECIO_BASE no debería cambiar"""