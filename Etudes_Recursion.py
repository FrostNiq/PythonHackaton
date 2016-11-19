#Faktorial
while True:
  try:
    number = int(input("Zadej cislo pro vypocet faktorialu: "))
    break
  except ValueError:
    print("Spatne. Zadej to znovu!")

print(number)
faktorial = 1

for i in range(1, number + 1):
  faktorial *= i

print("Faktorial je: " + str(faktorial))

#Fibbonaciho
while True:
  try:
    number = int(input("Zadej cislo pro Fibbonaciho posloupnost: "))
    break
  except ValueError:
    print("Spatne. Zadej to znovu!")

print(number)

Fibbonaciho = []
Fibbonaciho.insert(0,0)
Fibbonaciho.insert(1,1)

for i in range(2, number):
  Fibbonaciho.append(Fibbonaciho[i-1] + Fibbonaciho[i-2])

print(str(number) + ". prvek Fibbonaciho posloupnosti je: " + str(Fibbonaciho[number-1]))

#Find Greatest common diversion
while True:
  try:
    a = int(input("Zadej cislo a: "))
    b = int(input("Zadej cislo b: "))
    break
  except ValueError:
    print("Spatne. Zadej to znovu!")

rest = a % b

while rest != 0:
  a = b
  b = rest
  rest = a % b


print("Nejvetsi spolecny delitel je: " + str(b))
