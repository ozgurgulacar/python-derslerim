import random
import time

def main():
    secenekler=["TAŞ","KAĞIT","MAKAS"]
    sevinc=["BASİTTİ","EZ GAME","SENİ YENMEK ÇOCUK OYUNCAĞIYDI","BİR DAHAKİNE DAHA İYİ BİR RAKİP GETİR LÜTFEN"]

    while True:
        try:
            bitis=int(input("Kaçta Biter?\n"))
            if bitis < 0:
                print("Lütfen Geçerli Bir Sayı Giriniz")
            else:
                break
        except:
            print("Lütfen Geçerli Bir Sayı Giriniz")
    oyuncu=0
    bilgisayar=0
    i=0
    while i<bitis+bitis:
        if oyuncu==bitis:
            print("TEBRİKLER KAZANDIN")
            break
        elif bilgisayar==bitis:
            print(random.choice(sevinc))
            break
        else:
            print("\n\n\nBen seçimimi yaptım sıra sende\nTaş mı Kağıt mı Makas mı")
            while True:
                oyuncusecim=input().upper()
                if  oyuncusecim=="TAŞ":
                    break
                elif oyuncusecim=="MAKAS":
                    break
                elif oyuncusecim=="KAĞIT":
                    break
                else:
                    print("Yanlış yazmış olabilirsin tekrar dene")
            x= random.choice(secenekler)
            print("Benim seçimim= ",x)
            donus=tur(x,oyuncusecim)
            if donus == 1:
                bilgisayar+=1
                print("\nBen kazandım")
                i+=1
            elif donus == -1:
                oyuncu+=1
                i+=1
                print("\nSen kazandın")
            else:
                print("\nBerabere")
            print("Ben-Sen\n ",bilgisayar," - ",oyuncu,sep="",end="\n\n")




def tur(bilgisayar,oyuncu):
    if bilgisayar=="TAŞ":
        if oyuncu=="MAKAS":
            return 1
        elif oyuncu == "KAĞIT":
            return -1
        else:
            return 0
    elif bilgisayar =="MAKAS":
        if oyuncu=="MAKAS":
            return 0
        elif oyuncu == "KAĞIT":
            return 1
        else:
            return -1
    elif bilgisayar=="KAĞIT":
        if oyuncu=="MAKAS":
            return -1
        elif oyuncu == "KAĞIT":
            return 0
        else:
            return 1






main()
