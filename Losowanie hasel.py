import random
import string
losuj = input("Z ilu liczb ma sie skadal twoje haslo:  ")

znaki = string.ascii_letters
haslo = ""

for i in range(int(losuj)):
    haslo += random.choice(znaki)
print(haslo)