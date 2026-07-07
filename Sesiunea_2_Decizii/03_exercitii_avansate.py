a, b, c = 5, 12, 9
if a > b and a > c: print("a e cel mai mare")
elif b > c: print("b e cel mai mare")
else: print("c e cel mai mare")
an = int(input("An: "))
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print("An bisect")
else:
    print("Nu e an bisect")
