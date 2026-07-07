import os
def afiseaza_tree(director_start, prefix=""):
    elemente = [e for e in os.listdir(director_start) if not e.startswith(('.', '__'))]
    elemente.sort()
    for i, element in enumerate(elemente):
        cale_completa = os.path.join(director_start, element)
        este_ultimul = (i == len(elemente) - 1)
        ramura = "└── " if este_ultimul else "├── "
        print(f"{prefix}{ramura}{element}")
        if os.path.isdir(cale_completa):
            urmatorul_prefix = prefix + ("    " if este_ultimul else "│   ")
            afiseaza_tree(cale_completa, urmatorul_prefix)
if __name__ == "__main__":
    dir_curent = os.path.dirname(os.path.abspath(__file__))
    print(f"\n📂 {os.path.basename(dir_curent)}/")
    afiseaza_tree(dir_curent)
    print("\n" + "="*50 + "\n[SUCCES] Structura si codul au fost generate complet!\n" + "="*50)
