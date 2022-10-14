import random
import time
from colorama import Fore,init

deste=["KARO A","KARO JİLET","KARO PAPAZ","KARO KIZ","KARO 10","KARO 9","KARO 8","KARO 7","KARO 6","KARO 5","KARO 4","KARO 3","KARO 2",
       "SİNEK A","SİNEK JİLET","SİNEK PAPAZ","SİNEK KIZ","SİNEK 10","SİNEK 9","SİNEK 8","SİNEK 7","SİNEK 6","SİNEK 5","SİNEK 4","SİNEK 3","SİNEK 2",
       "KUPA A","KUPA JİLET","KUPA PAPAZ","KUPA KIZ","KUPA 10","KUPA 9","KUPA 8","KUPA 7","KUPA 6","KUPA 5","KUPA 4","KUPA 3","KUPA 2",
       "MAÇA A","MAÇA JİLET","MAÇA PAPAZ","MAÇA KIZ","MAÇA 10","MAÇA 9","MAÇA 8","MAÇA 7","MAÇA 6","MAÇA 5","MAÇA 4","MAÇA 3","MAÇA 2",
       "KARO A","KARO JİLET","KARO PAPAZ","KARO KIZ","KARO 10","KARO 9","KARO 8","KARO 7","KARO 6","KARO 5","KARO 4","KARO 3","KARO 2",
       "SİNEK A","SİNEK JİLET","SİNEK PAPAZ","SİNEK KIZ","SİNEK 10","SİNEK 9","SİNEK 8","SİNEK 7","SİNEK 6","SİNEK 5","SİNEK 4","SİNEK 3","SİNEK 2",
       "KUPA A","KUPA JİLET","KUPA PAPAZ","KUPA KIZ","KUPA 10","KUPA 9","KUPA 8","KUPA 7","KUPA 6","KUPA 5","KUPA 4","KUPA 3","KUPA 2",
       "MAÇA A","MAÇA JİLET","MAÇA PAPAZ","MAÇA KIZ","MAÇA 10","MAÇA 9","MAÇA 8","MAÇA 7","MAÇA 6","MAÇA 5","MAÇA 4","MAÇA 3","MAÇA 2"]


def main():
    random.shuffle(deste)
    bilgisayar=deste[0:52]
    oyuncu=deste[52:]
    sıra=yazıtura()
    yer=[]
    while True:
        if len(oyuncu)>0 and len(bilgisayar)>0:
            oyuncununkartı=oyuncu[0]
            bilgisayarınkartı=bilgisayar[0]
            oyuncu.pop(0)
            bilgisayar.pop(0)
            b1=""
            o1=""
            y1=""
            init(autoreset=True)
            
            if bilgisayarınkartı[0]=="S":
                b1=bilgisayarınkartı[6:]
            else:
                b1=bilgisayarınkartı[5:]
                
            if oyuncununkartı[0]=="S":
                o1=oyuncununkartı[6:]
            else:
                o1=oyuncununkartı[5:]
  
            
            if sıra=="oyuncu":
                
                print(Fore.RED+"SENİN KARTIN: "+oyuncununkartı)
                time.sleep(1)
                print(Fore.BLUE)
                print(Fore.GREEN+"BENİM KARTIM: "+bilgisayarınkartı)
                time.sleep(1)
                repeat=True
                dene=True
                while repeat:
                    time.sleep(2)
                    if len(yer)>0:
                        
                        
                        if yer[0][0]=="S":
                            y1=yer[0][6:]
                        else:
                            y1=yer[0][5:]
                            
                        
                        if y1==o1 and dene==True:
                            print("SEN ALDIN")
                            yer.insert(0,oyuncununkartı)
                            oyuncu=oyuncu+yer
                            yer.clear()
                            yer.insert(0,bilgisayarınkartı)
                        if y1!=o1 or dene==False:
                            if dene==True:
                                yer.insert(0,oyuncununkartı)
                            if y1==b1:
                                print("BEN ALDIM")
                                sıra="bilgisayar"
                                print("\n\nİLK ATACAK OLAN  ARTIK BENİM")
                                yer.insert(0,bilgisayarınkartı)
                                bilgisayar=bilgisayar+yer
                                yer.clear()
                            else:
                                yer.insert(0,oyuncununkartı)
                        repeat=False
                                
                    else:
                        yer.insert(0,oyuncununkartı)
                       
                        dene=False
                oyuncu.pop(0)
                bilgisayar.pop(0)
                

            if sıra=="bilgisayar":
                print(Fore.GREEN+"BENİM KARTIM: "+bilgisayarınkartı)
                time.sleep(1)
                print(Fore.RED+"SENİN KARTIN: "+oyuncununkartı)
                time.sleep(1)
                repeat=True
                dene=True
                while repeat:
                    time.sleep(2)
                    if len(yer)>0:
                        
                        if yer[0][0]=="S":
                            y1=yer[0][6:]
                        else:
                            y1=yer[0][5:]
                            
                            
                        if y1==b1 and dene==True:
                            print("BEN ALDIM")
                            yer.insert(0,bilgisayarınkartı)
                            bilgisayar=bilgisayar+yer
                            yer.clear()
                            yer.insert(0,oyuncununkartı)
                        if y1!=o1 or dene==False:
                            if dene==True:
                                yer.insert(0,oyuncununkartı)
                            if y1==o1:
                                print("SEN ALDIN")
                                print("\n\nİLK ATACAK OLAN ARTIK SENSİN")
                                sıra="oyuncu"
                                
                                yer.insert(0,oyuncununkartı)
                                oyuncu=oyuncu+yer
                                yer.clear()
                            else:
                                yer.insert(0,bilgisayarınkartı)
                        repeat=False      
                    else:
                        yer.insert(0,bilgisayarınkartı)
                        
                        dene=False 
                oyuncu.pop(0)
                bilgisayar.pop(0)
                
    
    time.sleep(5)
    print(bilgisayar)
    print("\n\n\n")
    ###print(y[6:])
    print(oyuncu)
    liste=["yeni kart","yeni kart2"]
    oyuncu.append(liste)
    print(len(liste))
    print("\n\n\n",oyuncu)
    yenisi=["1"]
    print("\nListemizin adedi=",len(yenisi))
    yenisi.pop(0)
    print("\nListemizin adedi=",len(yenisi))






def yazıtura():
    print("İlk oynayacak kişiyi seçmek için Yazı-Tura oynayacaz")
    secenek=["yazı","tura"]
    para=random.choice(secenek)
    sıra=""
    while True:
        x=input("Yazı mı Tura mı seç.").lower()

        
        if x=="yazı" and para=="yazı":
            sıra="oyuncu"
            break
        
        elif x=="yazı" and para=="tura":
            sıra="bilgisayar"
            break
        
        elif x=="tura" and para=="tura":
            sıra="oyuncu"
            break
        
        elif x=="tura" and para=="yazı":
            sıra="bilgisayar"
            break
        
        else:
            print("lütfen yazı veya tura yazınız")
    print(para)
    print("Önce başlayacak olan oyuncumuz",sıra)
    return sıra









main()
