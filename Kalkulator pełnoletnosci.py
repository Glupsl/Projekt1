imie = input("Jak sie nazywasz?: ")

wiek = int(input("Ile masz lat?: "))

if wiek >= 18:
    print(f"Masz {wiek} lat, jesteś pełnoletni/a ;D")
elif wiek <= 0 or wiek > 120:
    print("Co ty wpisujesz downie!")
else:
    print(f"Masz {wiek} lat, nie jestes pelnoletni/a ;p")