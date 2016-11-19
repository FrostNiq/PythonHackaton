while True:
  try:
    binary = str(input("Binarni cislo: "))

    check = True

    for char in binary:
      print(char)
      print(check)
      if int(char) != 0 and int(char) != 1:
        check = False

    if check == True:
      break
  except ValueError:
    print("Spatne. Zadej to znovu!")

number = 0

index = len(binary)
x = len(binary) - 1

for index in binary:
  number = number + (int(index) * pow(2, x))
  x = x - 1


print("Ciselny vysledek je: " + str(number))  
