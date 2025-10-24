import random

hak = 10
tahmin = random.randint(1, 100)

A = '\033[92m'
B = '\033[91m'
zero = '\033[0m'

sayı = int(input("1 ile 100 arasında bir sayı tuttum. Bakalım bilebilecek misin? Lütfen tahmini sayıyı gir"))

while hak > 0:
    if sayı == tahmin:
        print(f"Tebrikler! {A}Bildin{zero}.")
        break
    elif sayı < 1 or sayı > 100:
        print("Lütfen 1 ile 100 arasında bir sayı gir.")
    elif sayı < tahmin:
        hak -= 1
        print("Daha büyük bir sayı söyle.")
        print(f"Kalan hakkın: {hak}")
    elif sayı > tahmin:
        hak -= 1
        print("Daha küçük bir sayı söyle.")
        print(f"Kalan hakkın: {hak}")

    if hak == 0:
     print(f"Üzgünüm, {B}hakkın bitti{zero}. Doğru sayı {tahmin} idi.")
     break
        
    sayı = int(input("Tekrar tahminini gir: "))
