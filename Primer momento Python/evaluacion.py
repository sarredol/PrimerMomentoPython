# 1. Crea Función Calcular Max y Min: recibe una lista de enteros y devuelve el máximo y el mínimo de los números guardados en la lista. Parámetros de entrada: lista de enteros Valores de salida: valor máximo y mínimo.

# def calcular_max_min(lista):
#     if not lista:
#         return None, None
#     max_val = max(lista)
#     min_val = min(lista)
#     return max_val, min_val

# numeros = [5, 10, -3, 45, 8, 0]
# maximo, minimo = calcular_max_min(numeros)
# print("Máximo:", maximo)
# print("Mínimo:", minimo)

# -------------------------------------------------------------

# 2. Usa la función MaxMin que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo creada anteriormente y crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior

# def main():
#     lista_numeros = []
    
#     while  lista_numeros != "fin":
#         entrada = input("Introduce números en la lista (escribe 'fin' para terminar):")
#         if entrada.lower() == 'fin':
#             break
#         try:
#             numero = int(entrada)
#             lista_numeros.append(numero)
#         except ValueError:
#             print("Por favor, introduce un número válido.")

#     if lista_numeros:
#         maximo, minimo = calcular_max_min(lista_numeros)
#         print(f"El valor máximo es: {maximo}")
#         print(f"El valor mínimo es: {minimo}")
#     else:
#         print("No se ingresaron números.")

# if __name__ == "__main__":
#     main()

#--------------------------------------------------------------

# 3. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@"

# def email_valido(email):
#     return "@" in email

# def main():
#     email = input("Introduce tu dirección de correo electrónico: ")
    
#     if email_valido(email):
#         print("La dirección de correo es válida.")
#     else:
#         print("La dirección de correo no es válida.")

# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------

# 4. Hacer una calculadora en Python usando el ciclo while o funciones, teniendo en cuentalo siguiente:
# - El usuario debe ingresar los datos a tener en cuenta en las operaciones.
# - La calculadora debe contener las siguientes opciones:
# o Suma
# o Resta
# o Multiplicación
# o División: para realizar esta operación debe tener una restricción que evite que el usuario ingrese 0 como divisor.
# o Potenciación
# o Factorial de un numero ingresado
# o Raíz cuadrada, debe especificar que el dato a ingresar debe ser entero positivo
# o Salir
# - Crear in código que arroje el resultado de la operación escogida por el usuario.
# Para la calculadora puede importar la librería math (import math) y utilizar las siguientes funciones:
# Math.sqrt(número): calcular raíz cuadrada de cualquier numero
# Math.isqrt(numero): calcular raíz cuadrada. Arroja resultado int
# Pow(a, b): utilizada para potenciación donde a es el número base y b seria el exponente.
# Math.factorial(n): calcula el factorial.

# import math

# def mostrar_menu():
#     print("\nCalculadora")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicación")
#     print("4. División")
#     print("5. Potenciación")
#     print("6. Factorial")
#     print("7. Raíz cuadrada")
#     print("8. Salir")

# def calcular():
#     while mostrar_menu != None:
#         mostrar_menu()
#         opcion = input("Selecciona una opción (1-8): ")
        
#         if opcion == '8':
#             print("Saliendo de la calculadora.")
#             break

#         if opcion in ['1', '2', '3', '4', '5']:
#             num1 = float(input("Ingresa el primer número: "))
#             num2 = float(input("Ingresa el segundo número: "))
        
#         if opcion == '1':
#             print(f"Resultado: {num1 + num2}")
#         elif opcion == '2':
#             print(f"Resultado: {num1 - num2}")
#         elif opcion == '3':
#             print(f"Resultado: {num1 * num2}")
#         elif opcion == '4':
#             if num2 == 0:
#                 print("Error: No se puede dividir entre 0.")
#             else:
#                 print(f"Resultado: {num1 / num2}")
#         elif opcion == '5':
#             print(f"Resultado: {pow(num1, num2)}")

#         elif opcion == '6':
#             num = int(input("Ingresa un número entero no negativo: "))
#             if num < 0:
#                 print("Error: El número debe ser no negativo.")
#             else:
#                 print(f"Resultado: {math.factorial(num)}")
        
#         elif opcion == '7':
#             num = int(input("Ingresa un número entero positivo: "))
#             if num < 0:
#                 print("Error: Debe ser un entero positivo.")
#             else:
#                 print(f"Resultado: {math.sqrt(num)}")
        
#         else:
#             print("Opción no válida. Por favor, selecciona una opción entre 1 y 8.")

# if __name__ == "__main__":
#     calcular()

# ----------------------------------------------------------------

# 5. Escriba un programa que muestre una partida de dados entre dos jugadores, se debe ingresar la cantidad de turnos que se van a jugar, cada jugador tira un dado. Si un jugador saca un valor mayor que el otro, gana los puntos de ambos dados. Si los dos jugadores sacan el mismo valor, ninguno recibe puntos. Si al finalizar la partida hay un
# empate, ninguno gana la partida. Debe mostrar quien gana la partida, quien gana cada turno y la puntuación acumulada por cada jugador.
# Para el examen pueden usar la librería random (import random) y utilizar el métodorandom.randint(desde, hasta) que toma números enteros de forma aleatorias según rango dado

# import random

# def jugar_turno(turno):
#     jugador1 = random.randint(1, 6)
#     jugador2 = random.randint(1, 6)

#     print(f"\nTurno {turno}: Jugador 1 tira {jugador1}, Jugador 2 tira {jugador2}")

#     if jugador1 > jugador2:
#         puntos = jugador1 + jugador2
#         print("¡Jugador 1 gana este turno!")
#         return puntos, 0
#     elif jugador2 > jugador1:
#         puntos = jugador1 + jugador2
#         print("¡Jugador 2 gana este turno!")
#         return 0, puntos
#     else:
#         print("Empate en este turno.")
#         return 0, 0

# def main():
#     turnos = int(input("Ingresa la cantidad de turnos a jugar: "))
#     puntuacion_jugador1 = 0
#     puntuacion_jugador2 = 0

#     for turno in range(1, turnos + 1):
#         puntos_jugador1, puntos_jugador2 = jugar_turno(turno)
#         puntuacion_jugador1 += puntos_jugador1
#         puntuacion_jugador2 += puntos_jugador2

#     print("\nResultado Final:")
#     print(f"Puntuación Jugador 1: {puntuacion_jugador1}")
#     print(f"Puntuación Jugador 2: {puntuacion_jugador2}")

#     if puntuacion_jugador1 > puntuacion_jugador2:
#         print("¡Jugador 1 gana la partida!")
#     elif puntuacion_jugador2 > puntuacion_jugador1:
#         print("¡Jugador 2 gana la partida!")
#     else:
#         print("La partida termina en empate.")

# if __name__ == "__main__":
#     main()