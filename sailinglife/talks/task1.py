#create a program that writes to output 1st fifty odd numbers

licznik = 0
number = 0
oddns = []
while (licznik < 50):

    if number % 2 == 1:
        oddns.append (number)
        licznik = licznik + 1
    number = number + 1

print (oddns)
