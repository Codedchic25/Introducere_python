raspuns = input("Ești de acord? (da/nu): ").strip().lower()
if raspuns == "da":
    print("Mulțumim!")
elif raspuns == "nu":
    print("Poate data viitoare.")
varsta = int(input("Vârstă validare: "))
if 0 < varsta <= 120:
    print("Vârstă validă.")
