def calculeaza_salariu(ore, plata_pe_ora=25):
    return ore * plata_pe_ora
def adauga_tva(pret): return pret * 1.19
print("Salariu brut:", calculeaza_salariu(160))
print("Preț cu TVA:", adauga_tva(100))
