print("========================================")
print(" Piedra, papel o tijeras 100% imposible ") 			#By: Letalandroid
print("========================================\n")

piedra_papel_tijeras = input("¿Qué elijes: Piedra, Papel o Tijeras?: ")
piedra_papel_tijeras = piedra_papel_tijeras.lower()

if piedra_papel_tijeras == "piedra":
    print("Yo elijo papel.")
    print("Gané.")

if piedra_papel_tijeras == "papel":
    print("Yo elijo tijeras.")
    print("Gané.")

if piedra_papel_tijeras == "tijeras":
    print("Yo elijo piedra.")
    print("Gané.")


