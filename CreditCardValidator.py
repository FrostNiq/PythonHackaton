#The credit card number we want to validate. This program works with *most* credit card numbers.

#card_number = str(input("Enter credit card number you want to check: "))
card_number = '4012888888881881'

# Reverse the credit card number and take the digits in the odd positions and then the digits in the even positions
#
# Add up all the digits in the odd positions into a total.
#
# Multiply every even-positioned digit by two;
#   if the product is greater than 9 (e.g. 8 * 2 = 16),
#      then subtract 9 and add the result to the total.
#   Otherwise add the multiplication product to the total.
#
# If the total is divisible by 10 (the remainder after division by 10 is equal to 0 or the number ends in a zero);
#   then the credit card number is valid.

card_number = input("Enter credit card number you want to check: ")

card_number = card_number[::-1]

oddCardNumber = card_number[::2]

evenCardNumber = card_number[1::2]

sumOddCardNumber = 0

for number in oddCardNumber:
  sumOddCardNumber += int(number)

multipliedEvenCardNumber = 0

for number in evenCardNumber:
  mp_number = int(number) * 2
  if mp_number > 9 :
    multipliedEvenCardNumber += (mp_number - 9)
  else:
    multipliedEvenCardNumber += mp_number

finalCheck = multipliedEvenCardNumber + sumOddCardNumber

if (finalCheck % 10 ) == 0 :
  print("Credit Card is valid")
else:
  print("Credit card is not valid")
