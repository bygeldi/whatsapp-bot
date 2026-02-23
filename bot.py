def cevap_ver(mesaj):
    mesaj = mesaj.lower()
    if "nasılsın" in mesaj:
        return "Bot olduğum için her zaman enerjik hissediyorum! Sen?"
    elif "kimsin" in mesaj:
        return "Ben senin yerime mesajlara bakan akıllı botunum."
    else:
        return "Bunu henüz öğrenmedim ama üzerinde çalışıyorum."

print("--- WhatsApp Botu Hazır! ---")
gelen = input("Gelen Mesaj: ")
print("Botun Cevabı:", cevap_ver(gelen))