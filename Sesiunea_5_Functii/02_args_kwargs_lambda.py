def suma_infinit(*numere): return sum(numere)
print("Suma args:", suma_infinit(10, 20, 30, 40))
numere = [1, 2, 3, 4, 5]
patrate = list(map(lambda x: x**2, numere))
pare = list(filter(lambda x: x % 2 == 0, numere))
print("Pătrate:", patrate)
print("Numere Pare:", pare)
