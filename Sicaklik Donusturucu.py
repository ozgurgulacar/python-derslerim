def main():
    print("Sıcaklık Birimini Seçiniz \n1-Santigrad (°C)\n2- Fahrenheit (°F)\n3- Kelvin (°K)")
    x=girdi()
    print("Hangi Sıcaklık Birimine Çevireceğinizi Seçiniz \n1-Santigrad (°C)\n2- Fahrenheit (°F)\n3- Kelvin (°K)")
    y=girdi()
    print("Sıcaklığı Giriniz")
    while True:
        try:
            z=int(input())
            break
        except:
            print("Yanlış Bir Değer Girdiniz")
    if x==1:
        santigrad(y,z)
    elif x==2:
        fahrenheit(y,z)
    else:
        kelvin(y,z)




    

def santigrad(secim,derece):
    match secim:
        case 1:
            print(derece)
        case 2:
            x=derece*1.8
            print(x+32)
        case 3:
            print(derece+273)


def fahrenheit(secim,derece):
    match secim:
        case 1:
            x=(derece-32)/1.8
            print(x)
        case 2:
            print(derece)
        case 3:
            x=(derece+459.67)*(5/9)
            print(x)

def kelvin(secim,derece):
    match secim:
        case 1:
            print(x-273)
        case 2:
            x=(derece * (9/5))-459.67
            print(x)
        case 3:
            print(derece)



    

def girdi():
    a=3
    while a<5:
        try:
            x=int(input())
            if 0<x<4:
                return x
            else:
                print("Yanlış Bir Tercih Yaptınız Tekrar Deneyiniz")
        except:
            print("Geçerli Bir Değer Giriniz")











a= True
while a:
    main()
    x=input("Devam etmek istiyorsanız 'y' yazıp Enter'a basınız\n")
    if x!='y':
        a=False
    print("\n\n\n\n")
