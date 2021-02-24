print("===============================================================")
print(" Saber si una división entre dos números, es exacta o inexacta ") #By: Letalandroid
print("===============================================================\n")

import time

numero_uno = int(input("Coloque su primer número: "))
numero_dos = int(input("Coloque su segundo número: "))

resultado = numero_uno % numero_dos

if resultado == 0:
    print("La división es exacta.")
    print("El resto de esta división es 0 por ser exacta.")

else:
    print("La división es inexacta")
    print("El resto es de: ", resultado)

time.sleep(3)

print("Este programa se cerrará en:")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Bye xd")
time.sleep(2)