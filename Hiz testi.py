import random
import datetime
import time


kelimeler=["Yazmak","Şirket","Çerçeve","Sıra","Boy","Meslek","Çok","Kalp","Sürekli","Zarar","Mektup","Yerine","Oturmak","Hastane","Koşul","Bakış","Bacak",
           "Katılmak","Oyun","Birlikte","Çıkar","Kurum","Sigorta","Değişiklik","Tüketici","Görüş","Mekan","Artık","Sanmak","Kanun","Hakkında","Sigara","Günlük",
           "Yaratmak","Beyin","Teknoloji","Doğal","Ortak","Trafik","Sunulmak","Edilmek","Yukarıda","Kesin","Çocuk","Anlatmak","Doğru","Evlenmek","Rağmen","Öldürmek"]




time.sleep(1)
print("\nEkrana gelen kelimeleri en Kısa sürede doğru şekilde yazmanız gerekiyor.")
time.sleep(1)
print("\nBir kelimeyi yazdıktan sonra Enter'a basınız")
time.sleep(1)
print("\nDoğru ise sıradaki kelimeyi bekleyiniz yanlış ise tekrar yazınız")


time.sleep(1)
while True:
    print("\nHazır olunca evet yazıp Enter'a basınız")
    x=input().lower()
    if x=="evet":
        break
baslangic=datetime.datetime.now()
for i in range(15):
    kelimemiz=random.choice(kelimeler).lower()
    print("    ",kelimemiz)
    x=True
    while x:
        girilen=input().lower()
        if girilen==kelimemiz:
            break
son=datetime.datetime.now()
print("\nGeçen Süre:  ",son-baslangic)
input()
