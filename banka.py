class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim = ISIM
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,ID:str,PAROLA:str,ISIM:str):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("Bankamıza kayıt yaptırdığınız için teşekkürler...")

def main():
    banka = Banka()
    while True:
        print("""
        [1] Banka Müiterisiyim
        [2] Banka Müşteri olmak istiyorum
        """)

        secim = input("Merhana Internet Bankacılığına Hosgeldiniz Lütfen Yapmak Istediginiz Islemi Seciniz: ")
        
        if secim == "1":
            ids = [i.id for i in banka.musteriler]
            ID = input("ID: ")
            if ID  in ids:
                for musteri  in banka.musteriler:
                    if ID == musteri.id:
                        print("Hoşgeldiniz {}".format(musteri.isim))
                        while True:
                        
                            print("""
                            1- Bakiye Sorgulama
                            2-Bu Hesaba Para Yatırma
                            3-Başka Hesaba Para Yatırma
                            4-Para Cekme
                            Q-Çıkış """)
                            
                            secim2 = input (" Lütfen işleminizi seçiniz: ")
                            if secim2 == "1":
                                print("Bakiyeniz : {}".format(musteri.bakiye))
                                input("Ana Menüye Donmek Icın Lütfen 'Enter'a Basınız...")
                            elif secim2== "2" :
                                miktar = int(input("Miktar: "))
                                onay = input("Kendi Hesabınıza {} TL para yatırma işlemini onaylıyormusunuz ? : E/H ".format(miktar))
                                if onay == "E" or onay == "e":
                                    musteri.bakiye += miktar
                                    print("Paranız Yatırıldı")
                                    input("Ana Menüye Dönmek 'Enter'a Basınız")
                                elif onay== "H" or onay=="h":
                                    print("İşleminiz Iptal Edildi")
                                    input("Ana Menüye Dönmek 'Enter'a Basınız")
                                else:
                                    print("Hatalı Giriş Yapıldı")
                            elif secim2=="3":
                                arananID = input("Müşteri ID: ")
                                if arananID in ids:
                                    for digerMusteri in banka.musteriler:
                                        if arananID == digerMusteri.id:
                                            miktar = int(input("Miktar: "))
                                            if miktar <= musteri.bakiye:
                                                onay = input("{} adlı müsterimize {} TL para yatırma islemini onaylıyor musunuz?: E/H".format(digerMusteri.isim,miktar))
                                                if onay == "e" or onay=="E":
                                                    digerMusteri.bakiye += miktar
                                                    musteri.bakiye -= miktar

                                                elif onay == "h" or onay== "H":
                                                    print("İşleminiz Iptal Edildi")
                                                    input("Ana Menüye Dönmek 'Enter'a Basınız")
                                                else:
                                                    print("Hatalı Giriş Yapıldı")
                                                    input("Ana Menüye Dönmek 'Enter'a Basınız")
                                            else:
                                                print("Bakiyeniz bu islem icin yetersiz")
                                                input("Ana Menüye Dönmek 'Enter'a Basınız")
                                else:
                                    print("Müsteri bulunamadı")
                                    input("Ana Menüye Dönmek 'Enter'a Basınız")
                            elif secim2=="4":
                                miktar = int(input("Miktar: "))
                                if miktar <= musteri.bakiye:
                                    musteri.bakiye -= miktar
                                    print("Islem tamamlandı paranızı alınız: ")
                                else:
                                    print("Bakiyeniz Yetersiz islem yapılamadı: ")
                            elif secim2 == "q" or secim2=="Q":
                                break
        elif secim == "2":
            ISIM= input("Adınız ve Soyadınız:  ")
            ID = input("ID numarınız: ")
            PARALO = input("Lütfen Parolo Olusturunuz: ")
            banka.musteri_ol(ID,PARALO,ISIM)

if __name__ == "__main__":
    main()


                                            


                        