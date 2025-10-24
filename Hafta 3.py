N = input("Sınav notunuzu giriniz: ")
N = int(N)

A = '\033[94m'
B = '\033[92m'
C = '\033[93m'
D = '\033[91m'
F = '\033[95m'
zero = '\033[0m'

if N >= 101 or N < 0:
    print("Hatalı giriş yaptınız.")
elif N >= 90:
    print(f"{A}A aldınız{zero}")
elif N >= 75:
    print(f"{B}B aldınız{zero}")
elif N >= 60:
    print(f"{C}C aldınız{zero}")
elif N >= 45:
    print(f"{D}D aldınız{zero}")
elif N >= 0:
    print(f"{F}F aldınız{zero}")