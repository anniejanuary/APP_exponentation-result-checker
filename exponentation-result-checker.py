#podaj podstawę i wykładnik potęgi, z opcją np 5**0=1, podaj wynik i sprawdz czy jest dobry

#base of power - podstawa potęgi
print("Enter the base of power: ")
base=int(input())

#exponent - wykładnik potęgi
print("Enter the exponent: ")
exponent=int(input())

print("Enter the exponentation result: ")
result_input=int(input())

if result_input == base**exponent:
    print("Result correct")
else:
    print("Result incorrect")
