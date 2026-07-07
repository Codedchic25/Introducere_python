nota = int(input("Ce notă ai luat? "))
print("Promovat" if nota >= 5 else "Picat")
user = input("Utilizator: ")
parola = input("Parolă: ")
if (user == "admin" and parola == "1234") or (user == "guest" and parola == "guest"):
    print("Acces permis.")
else:
    print("Acces respins.")
