print("🤖 Bot: Halo! Aku bot sederhana.")
print("Ketik 'keluar' untuk berhenti.")

while True:
    user = input("Kamu: ").lower()

    if user == "halo":
        print("🤖 Bot: Halo juga! Apa kabar?")
        
    elif user == "apa kabar":
        print("🤖 Bot: Aku baik! Makasih sudah tanya.")

    elif user == "siapa kamu":
        print("🤖 Bot: Aku bot Python yang dibuat di Termux.")

    elif user == "keluar":
        print("🤖 Bot: Oke, sampai jumpa!")
        break

    else:
        print("🤖 Bot: Maaf aku belum ngerti itu.") 
