print("========================")
print(" CALCULADORA MULTIUSOS ")				#By: Letalandroid pe 																																																																																																																																																																																																																																																																																																																																																				el día 11/01/2021
print("========================\n") 																																																																																																																																																																																																																																																																																																																																																												#By: Letalandroid pe el día 11/01/2021

print("""Elija la operación que desea realizar:
	
1. Suma.
2. Resta.
3. Multiplicación.
4. División Decimal.
5. División Entera.
6. Potenciación.
7. Radicación
8. Sacar el resto de una división.\n""") 																																																																																																																																																																																																																																																																																																																																																											#By: Letalandroid pe el día 11/01/2021
	
opcion = int(input("Elija la opción a desear: "))
	
if opcion == 1:
		print("Usted a elegido la opción: N° 1 ⇒ Suma.") 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_uno = int(input("Elija su primer número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_dos = int(input("Elija su segundo número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno + num_dos
		print("\nEl resultado de la suma entre: ", num_uno, " + ", num_dos, " es igual a ", resultado, ".")

if opcion == 2:
		print("Usted a elegido la opción: N° 2 ⇒ Resta.\n")
		num_uno = int(input("Elija su primer número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_dos = int(input("Elija su segundo número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno - num_dos
		print("\nEl resultado de la resta entre: ", num_uno, " - ", num_dos, " es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																										#By: Letalandroid pe el día 11/01/2021

if opcion == 3:
		print("Usted a elegido la opción: N° 3 ⇒ Multiplicación.\n")
		num_uno = int(input("Elija su primer número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_dos = int(input("Elija su segundo número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno * num_dos
		print("\nEl producto entre: ", num_uno, " multiplicado por ", num_dos, " es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																										#By: Letalandroid pe el día 11/01/2021

if opcion == 4:
		print("Usted a elegido la opción: N° 4 ⇒ División.\n")
		num_uno = float(input("Elija su primer número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_dos = float(input("Elija su segundo número: ")) 																																																																																																																																																																																																																																																																																																																																																						#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno / num_dos
		print("\nEl resultado entre: ", num_uno, " por ", num_dos, " es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																													#By: Letalandroid pe el día 11/01/2021

if opcion == 5:
		print("Usted a elegido la opción: N° 5 ⇒ División Entera.\n")
		num_uno = int(input("Elija su primer número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_dos = int(input("Elija su segundo número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno // num_dos
		print("\nEl resultado de la división entera entre: ", num_uno, " por ", num_dos, " es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		
if opcion == 6:
		print("Usted a elegido la opción: N° 6 ⇒ Potenciación.\n") 																																																																																																																																																																																																																																																																																																																																																					#By: Letalandroid pe el día 11/01/2021
		num_uno = int(input("Elija la base de su potencia: ")) 																																																																																																																																																																																																																																																																																																																																																						#By: Letalandroid pe el día 11/01/2021
		num_dos = int(input("Elija el exponente de su potencia: ")) 																																																																																																																																																																																																																																																																																																																																																				#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno ** num_dos
		print("\nEl resultado al elevar ", num_uno, " a la ", num_dos, " es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																												#By: Letalandroid pe el día 11/01/2021

if opcion == 7:
		import math
		print("Usted ha elegido la opción: Nº 7 ⇒ Radicación.\n")
		num_uno = float(input("Introduzca su número: "))
		opcion = input("¿Desea elevar al cuadrado?: ")
		opcion = opcion.lower()

		if opcion == "si":
			raiz = math.sqrt(num_uno)
			print("La raíz cuadrada de ", num_uno, " es ",raiz)
		if opcion == "no":
			num_dos = int(input("Introduzca el número a elevar: "))
			raiz_opcional = math.pow(num_uno, num_dos)
			print(num_uno,  " elevado a la ", num_dos, " es igual a ", raiz_opcional)



if opcion == 8:
		print("Usted a elegido la opción: N° 8: ⇒ Sacar el resto de uma división.\n")
		num_uno = int(input("Elija su primer número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		num_dos = int(input("Elija su segundo número: ")) 																																																																																																																																																																																																																																																																																																																																																							#By: Letalandroid pe el día 11/01/2021
		resultado = num_uno % num_dos

		if resultado == 0:
			print("\nLa división es exacta, osea que su resto es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																														#By: Letalandroid pe el día 11/01/2021
		
		else:
			print("""\nLa división es inexacta.
El resto que sale al dividir """, num_uno, " entre ", num_dos, " es igual a ", resultado, ".") 																																																																																																																																																																																																																																																																																																																																														#By: Letalandroid pe el día 11/01/2021

if opcion == 9:
	import math
	pi = math.pi
	print(pi)
if opcion == 10:
	import math
	e = math.e
	print(e)
if opcion == 11:
	import math
	tau = math.tau
	print(tau)

retorno = input("Quisiera volver a")

print("\nPvto el que lo lea\n") 																																																																																																																																																																																																																																																																																																																																																													#By: Letalandroid pe el día 11/01/2021