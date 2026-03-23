import random

angka_rahasia = random.randint(1, 10)

print("🎮 Game Tebak Angka")
print("Tebak angka dari 1 sampai 10")

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan == angka_rahasia:
        print("🎉 Benar! Kamu menebak dengan tepat!")
        break

    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")

    else:
        print("Terlalu besar!") 
