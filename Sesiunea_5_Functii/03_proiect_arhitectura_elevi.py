elevi = []
def adauga_elev(nume, clasa, note): elevi.append({"nume": nume, "clasa": clasa, "note": note})
def calculeaza_media(note): return sum(note) / len(note)
def afiseaza_medii():
    for e in elevi:
        print(f"Elev: {e['nume']} - Medie: {calculeaza_media(e['note']):.2f}")
sys_test = [adauga_elev("Bogdan", 10, [9, 10, 8]), adauga_elev("Irina", 11, [10, 10, 10])]
afiseaza_medii()
