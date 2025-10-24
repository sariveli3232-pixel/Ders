import random

rasgele_sayilar = []
for _ in range(100):
    rasgele_sayilar.append(random.randint(1, 1000))

print("--- Üretilen Rasgele Sayılar (İlk 100): ---")
print(rasgele_sayilar[:100], "...")

toplam = 0
for sayi in rasgele_sayilar:
    toplam += sayi
print(f"\n--- Hesaplamalar (Hazır Metot Kullanmadan) ---")
print(f"Toplam: {toplam}")

sayi_adedi = 100
ortalama = toplam / sayi_adedi
print(f"Ortalama: {ortalama:.2f}")

sirali_sayilar = sorted(rasgele_sayilar)

if sayi_adedi % 2 == 1:
    orta_index = sayi_adedi // 2
    medyan = sirali_sayilar[orta_index]
else:
    orta_index_1 = sayi_adedi // 2 - 1
    orta_index_2 = sayi_adedi // 2
    medyan = (sirali_sayilar[orta_index_1] + sirali_sayilar[orta_index_2]) / 2

print(f"Medyan (Ortanca): {medyan:.2f}")

minimum = rasgele_sayilar[0]
for sayi in rasgele_sayilar:
    if sayi < minimum:
        minimum = sayi
print(f"Minimum: {minimum}")

fark_kareleri_toplami = 0
for sayi in rasgele_sayilar:
    fark = sayi - ortalama
    fark_kare = fark * fark
    fark_kareleri_toplami += fark_kare

varyans = fark_kareleri_toplami / sayi_adedi

standart_sapma = varyans ** 0.5
print(f"Standart Sapma: {standart_sapma:.2f}")

sayi_sikliklari = {}
for sayi in rasgele_sayilar:
    if sayi in sayi_sikliklari:
        sayi_sikliklari[sayi] += 1
    else:
        sayi_sikliklari[sayi] = 1

en_yuksek_siklik = 0
modlar = []

for siklik in sayi_sikliklari.values():
    if siklik > en_yuksek_siklik:
        en_yuksek_siklik = siklik

for sayi, siklik in sayi_sikliklari.items():
    if siklik == en_yuksek_siklik:
        modlar.append(sayi)

if en_yuksek_siklik <= 1 and sayi_adedi > 0:
    print("Mod: Mod bulunamadı (Tüm sayılar eşit sayıda, veya birer kez geçti)")
else:
    print(f"Mod (Tepe Değer): {modlar} (Sıklık: {en_yuksek_siklik})")

def ters_secme_siralamasi(liste):
    n = len(liste)
    for i in range(n):
        en_buyuk_index = i
        for j in range(i + 1, n):
            if liste[j] > liste[en_buyuk_index]:
                en_buyuk_index = j

        liste[i], liste[en_buyuk_index] = liste[en_buyuk_index], liste[i]
    return liste

buyukten_kucuge_sirali = ters_secme_siralamasi(rasgele_sayilar.copy())

print(f"\n--- Rasgele Sayıların Büyükten Küçüğe Sıralanmış Hali (İlk 100): ---")
print(buyukten_kucuge_sirali[:100], "...")