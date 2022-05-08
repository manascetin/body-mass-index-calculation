#VÜCUT KÜTLE İNDEKSİ HESAPLAMA

kilo = float(input("Kilonuzu Kg Cinsinden Giriniz: "))
boy = float(input("Boyunuzu Metre Cinsinden Giriniz: "))

index = (kilo) / (boy **2)

if(index < 18.5):
    print("Zayıfsınız. Kütle İndeksiniz: ", index)
elif(18.5 < index < 24.9):
    print("Normal Kilolusunuz. Kütle İndeksiniz: ", index)
elif(25 < index < 29.9):
    print("Fazla Kilolusunuz. Kütle İndeksiniz: ", index)
elif(30 < index < 39.9):
    print("Obezsiniz. Kütle İndeksiniz: ", index)
elif(index > 40):
    print("İleri Derecede Obezsiniz. Kütle İndeksiniz: ", index)
else:
    print("Bilgileriniz Yanlış.")
