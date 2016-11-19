while True:
  try:
    number = int(input("Zadej cislo: "))
    break
  except ValueError:
    print("Spatne. Zadej to znovu!")

number = abs(number)

binary = ""

while number > 0:
    if (number % 2) == 1:
        binary = binary + str(1)
    else:
        binary = binary + str(0)

    number = number // 2

print("Binarni vysledek je: " + binary)  
