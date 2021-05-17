import os

kelimeler={
    "get":["Almak","Edinmek","Olmak","Elde Etmek"],
    "break":["Mola","Ara","Kırmak","Fren"],
    "winner":["Kazanan","Galip","Birinci"]
}

def kelimeEkle(kelime,kelimeler):
    if kontrol(kelime,kelimeler):
        mevcut_anlamlar=set(kelimeler[kelime])
        yeni_giris=input("Kelime zaten mevcut. Girdiginiz kelimenin kayıtlı anlamları : {}\n Yeni bir Anlam girmek ister misiniz?(E/H)".format(mevcut_anlamlar))
        if yeni_giris.lower()=="e":
            yeni_anlamlar=input("Girmek istediğiniz anlamları aralarına virgül koyarak yazınız : ")
            yeni_anlamlar_bolunmus=set(yeni_anlamlar.split(","))
            kelimeler[kelime]=list(mevcut_anlamlar | yeni_anlamlar_bolunmus)
            print("Girdiğiniz anlamlar Kaydedildi. Anlamlar Listesinin son hali : ",kelimeler[kelime])
        elif yeni_giris.lower()=="h":
            pass
    else:
        yeni_anlamlar = input("Girmek istediğiniz anlamları aralarına virgül koyarak yazınız : ")
        yeni_anlamlar_bolunmus = set(yeni_anlamlar.split(","))
        kelimeler[kelime] = list(yeni_anlamlar_bolunmus)
        print("Girdiğiniz anlamlar Kaydedildi. Anlamlar Listesinin son hali : ", kelimeler[kelime])
    input("Devam etmek için bir tuşa basın.")



def kelimeCevir(kelime,kelimeler):
    if kontrol(kelime,kelimeler):
        print("{}  kelimesinin anlamları ".format(kelime),end=": ")
        print(*kelimeler[kelime])
    else:
        print("Girdiğiniz kelime mevcut değildir")
    input("Devam etmek için bir tuşa basın.")

def kontrol(kelime,kelimeler):
    if kelime in kelimeler:
        return True
    else:
        return False

def kelimeriListele():
    for no,kelime in enumerate(kelimeler,1):
        print("{} . {}".format(no,kelime))
    input("Devam etmek için bir tuşa basın.")


# kelimeEkle("benefit",kelimeler)
# kelimeCevir("get",kelimeler)
# kelimeriListele()


secenekler= """
            [1] Kelime Ekle
            [2] Kelime Çevir
            [3] Kelimeleri Listele
            """
while True:
    temizle=("cls" if os.name == "nt" else "clear")
    os.system(temizle)
    print(secenekler)
    secenekler=int(input("Seçiminizi yapın : "))

    if secenekler==1:
        kelime=input("Eklenecek İngilizce Kelimeyi girin   :  ")
        kelimeEkle(kelime,kelimeler)
    elif secenekler==2:
        kelime=input("Anlamını Öğrenmek istediğiniz kelimeyi girin   :  ")
        kelimeCevir(kelime,kelimeler)
    elif secenekler==3:
        kelimeriListele()










# print(list(enumerate(kelimeler,1)))  # liste içinde bunları demetlere bölerek bir sayı bir deger olarak başlatırız.