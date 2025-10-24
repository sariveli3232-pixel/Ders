V = input("Vise notunu sayı olarak giriniz: ")
V = int(V)

F = input("Final notunu sayı olarak giriniz: ")
F = int(F)

D = input("Devamsızlık gününü sayı olarak giriniz: ")
D = int(D)

A = '\033[92m'
B = '\033[91m'
zero = '\033[0m'

T = (V * 0.4) + (F * 0.6)

if F > 100 or F < 0:
    print("Final notu bu değerde olamaz")
elif V > 100 or V < 0:
    print("Vize notu bu değerde olamaz")
elif D < 0:
    print("Devamsızlık günü negatif olamaz")
elif D >= 28:
    print(f"Devamsızlıktan {B}kaldınız{zero}, not ortalamanız:", T)
elif T <= 60:
    print(f"Düşük puandan {B}kaldınız{zero}, not ortalamanız:", T)
else:
    print(f"{A}Geçtiniz{zero}, not ortalamanız:", T)