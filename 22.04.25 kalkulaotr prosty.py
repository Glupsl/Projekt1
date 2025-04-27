liczby = input("Podaj mi dwie liczby: ")
a_str, b_str = liczby.split()
a = float(a_str)
b = float(b_str)

operacja = input("Jakie działanie chcialbyś wykonać? + , - , * , / ")


if operacja == "+":
    wynik = a + b
    opis = "dodawanie"

elif operacja == "-":
    wynik = a - b
    opis = "odejmowanie"

elif operacja == "*":
    wynik = a * b
    opis = "mnozenie"

elif operacja == "/":
    wynik = a / b
    opis = "dzielenie"

else:
    print("Co ty klikosz???",operacja)
    exit()

print(f"Wynik: {opis}, liczby: {a} i {b}, wynik: {wynik}")