
#zad 1
points = 81
if points > 80:
    print("Passed the exam")
elif 50 <= points <= 80:
    print("Can improve result")
else:
    print("Must retake the exam")

#/////////////////////////////////////////////////////////////////////////////////////////
#Zad. 2

x = int(input("Insert x:"))
y = int(input("Insert y:"))
z = int(input("Insert z:"))

temp = 0

if x > y:
    temp = x
    x = y
    y = temp

if y > z:
    temp = y
    y = z
    z = temp

if x > y:
    temp = x
    x = y
    y = temp

print("Result:", x, y, z)

#///////////////////////////////////////////
#zad 3
Nazwa_pliku = 'Raport_maj.xlsx'
if Nazwa_pliku.endswith('.xlsx'):
    print('Tak')
else:
    print('Nie')

#/////////////////////////////////////////////
#zad 4
gol = int(input("Please enter total goals\n"))
bonus= int(0)
sum=int(0)
if gol > 5:
    bonus += 5
if gol > 10:
    bonus += 10
sum = sum + 10 * gol + bonus
print(sum)




#/////////////////////////////////////////////////
#zad5
try:
    with open('notwania_gieldowe.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error")

print("Adding new company")
print("---------------------")
try:
    with open('notwania_gieldowe.txt', 'a') as file:
        file.write("\nALR, 113")

    with open('notwania_gieldowe.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("Error")


#-------------------------------------------------
#zad6
letter = input("Enter a letter: ")
if letter.isupper():
    print("Letter is uppercase")
elif letter.islower():
    print("Letter is lowercase")
else:
    print("Not a letter")

#=============================================================
#zad7
Haslo = 'pk47!jy0893'
if len(Haslo) == 11 and '!' in Haslo:
    print("Haslo jest poprawne")
else:
    print("Haslo jest nie poprawne")


#======================================================================
#zad8
text = 'Studiuje-Informatykę'
first_three_chars = text[:3]
last_two_chars = text[-2:]
print("First three characters:", first_three_chars)
print("Last two characters:", last_two_chars)


#========================================================
#zad9
text = "It's me, Mario"
swapped_text = text.swapcase()
print(swapped_text)
