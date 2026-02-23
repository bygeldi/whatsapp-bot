import random

def cevap_ver(mesaj):
    mesaj = mesaj.lower()
    
    selamlar = ["Selam! Bugün harika görünüyorsun.", "Merhaba, botun emrine amade!", "Ooo hoş geldin!"]
    nasilsin_cevaplar = ["Süperim, devrelerim pırıl pırıl!", "Biraz ısındım ama iyiyim.", "Robotik bir neşe içindeyim!"]

    if "selam" in mesaj:
        return random.choice(selamlar)
    elif "nasılsın" in mesaj:
        return random.choice(nasilsin_cevaplar)
    elif "kimsin" in mesaj:
        return "Ben senin kişisel asistan botunum."
    else:
        return "Bunu henüz öğrenmedim ama not alıyorum!"

print("--- WhatsApp Botu 2.0 Hazır! ---")
while True: # Bu satır botun kapanmadan sürekli soru sormasını sağlar
    gelen = input("Gelen Mesaj (Çıkmak için 'q'): ")
    if gelen.lower() == 'q':
        break
    print("Botun Cevabı:", cevap_ver(gelen))