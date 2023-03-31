# MASALAR, MENÜ => BAŞLANGIÇ ARA SICAK ANA YEMEK İÇCECEK SALATA MAKARNA ..VS

masalar: dict = {
    "Masa-1": "F",
    "Masa-2": "F",
    "Masa-3": "F",
    "Masa-4": "F",
    "Masa-5": "F",
}

corbalar: dict = {
    "1-Mercimek": "7.00",
    "2-Ezogelin": "7.00",
    "3-Yayla": "6.00",
}

baliklar: dict = {
    "1-Mezgit": "27.00",
    "2-Palamut": "32.00",
    "3-Çupra": "40.00",
}

etler: dict = {
    "1-Pirzola": "56.00",
    "2-Biftek": "65.00",
    "3-Lokum": "45.00",

}

makarnalar: dict = {
    "1-Bonolezli": "35.00",
    "2-Körili": "35.00",
    "3-Spagetti": "35.00",
}

ara_sicaklar: dict = {
    "1-İçli Köfte": "20.00",
    "2-Sigara Böreği": "40.00",
    "3-Patso": "10.00",
}

salatalar: dict = {
    "1-Çoban": "20.00",
    "2-Sezar": "50.00",
    "3-Mevsim": "35.00",
}

icecekler: dict = {
    "1-Kola": "10.00",
    "2-Ayran": "5.00",
    "3-Şalgam": "15.00",
    "4-Su": "10.00",
}

siparisler: dict = dict()
# https://patorjk.com/software/taag/#p=display&h=3&v=0&f=Big&t=KARDESLER%20%20%20KEBAP
print("""
  _  __         _____  _____  ______  _____ _      ______ _____      _  ________ ____          _____  
 | |/ /   /\   |  __ \|  __ \|  ____|/ ____| |    |  ____|  __ \    | |/ |  ____|  _ \   /\   |  __ \ 
 | ' /   /  \  | |__) | |  | | |__  | (___ | |    | |__  | |__) |   | ' /| |__  | |_) | /  \  | |__) |
 |  <   / /\ \ |  _  /| |  | |  __|  \___ \| |    |  __| |  _  /    |  < |  __| |  _ < / /\ \ |  ___/ 
 | . \ / ____ \| | \ \| |__| | |____ ____) | |____| |____| | \ \    | . \| |____| |_) / ____ \| |     
 |_|\_/_/    \_|_|  \_|_____/|______|_____/|______|______|_|  \_\   |_|\_|______|____/_/    \_|_|     


""")
while True:
    menu: int = int(input("""

                Sipariş Almak İçin      :1
                Hesap Almak İçin        :2
                Menü Güncellemek İçin   :3
                Çıkış İçin              :4
                Seçiminiz:"""))

    if menu == 4:
        break

    elif menu == 1:

        while True:

            kisi_sayisi = int(input("Kaç kişisiniz ?"))

            musteri_masasi = str()

            for masa in masalar:

                if masalar[masa] == "F":
                    musteri_masasi = masa

                    masalar[masa] = "T"

                    break

            siparis = dict()

            for kisi in range(kisi_sayisi):

                print(f"{kisi + 1} . müşteri siparişi")

                while True:

                    print("""
                                1- Çorba Çeşitleri
                                2- Balık Çeşitleri
                                3- Et Çeşitleri
                                4- Makarna Çeşitleri
                                5- Arasıcak Çeşitleri
                                6- Salata Çeşitleri
                                7- İçecek Çeşitleri
                        """)

                    secim = int(input("Seçiminiz: "))

                    if secim == 1:

                        for corba in corbalar:
                            print(f"{corba} :{corbalar[corba]}₺")

                        corba_secim = int(input("Çorba Seçiminiz:"))

                        if corba_secim == 1:

                            siparis["Mercimek Çorbası"] = "7.00"

                        elif corba_secim == 2:

                            siparis["Ezogelin Çorbası"] = "7.00"

                        elif secim == 3:

                            siparis["Yayla Çorbası"] = "7.00"

                        else:
                            print("Hatalı çorba seçimi")
                            continue

                    elif secim == 2:

                        for balik in baliklar:
                            print(f"{balik} {baliklar[balik]} ₺")

                        secim_balik = int(input("Balık Seçiminiz: "))

                        if secim_balik == 1:

                            siparis["Mezgit"] = "27.00"

                        elif secim_balik == 2:

                            siparis["Palamut"] = "35.00"

                        elif secim_balik == 3:

                            siparis["Çupra"] = "45.00"

                        else:

                            print("Hatalı balık seçimi")

                            continue

                    elif secim == 3:

                        for et in etler:
                            print(f"{et} {etler[et]} ₺")

                        secim_et = int(input("Et Seçiminiz: "))

                        if secim_et == 1:

                            siparis["Pirzola"] = "56.00"

                        elif secim_et == 2:

                            siparis["Biftek"] = "65.00"

                        elif secim_et == 3:

                            siparis["Lokum"] = "45.00"

                        else:

                            print("Hatalı et seçimi")

                            continue

                    elif secim == 4:

                        for makarna in makarnalar:
                            print(f"{makarna} {makarnalar[makarna]} ₺")

                        secim_makarna = int(input("Makarna Seçiminiz: "))

                        if secim_makarna == 1:

                            siparis["Bonolezli"] = "35.00"

                        elif secim_makarna == 2:

                            siparis["Körili"] = "35.00"


                        elif secim_makarna == 3:

                            siparis["Spagetti"] = "35.00"

                        else:

                            print("Hatalı Makarna Seçimi")

                            continue


                    elif secim == 5:

                        for arasicak, fiyat in ara_sicaklar.items():
                            print(f"{arasicak} {fiyat} ₺")

                        secim_arasicak = int(input("Arasıcak Seçiminiz: "))

                        if secim_arasicak == 1:

                            siparis.update({"İçli Köfte": "20.00"})

                        elif secim_arasicak == 2:

                            siparis.update({"Sigara Böreği": "40.00"})

                        elif secim_arasicak == 3:

                            siparis.update({"Patso": "10.00"})

                        else:

                            print("Hatalı Arasıcak Seçimi")

                            continue

                    elif secim == 6:

                        for salata, fiyat in salatalar.items():
                            print(f"{salata} {fiyat} ₺")

                        secim_salata = int(input("Salata Seçiminiz: "))

                        if secim_salata == 1:

                            siparis.update({"Çoban Salatası": "20.00"})

                        elif secim_salata == 2:

                            siparis.update({"Sezar Salata": "40.00"})

                        elif secim_salata == 3:

                            siparis.update({"Mevsim Salatası": "20.00"})

                        else:

                            print("Hatalı Salata Seçimi")

                            continue


                    elif secim == 7:

                        for icecek, fiyat in icecekler.items():
                            print(f"{icecek} {fiyat} ₺")

                        secim_icecek = int(input("İçecek Seçiminiz: "))

                        if secim_icecek == 1:
                            siparis.update({"Kola": "8.00"})

                        elif secim_icecek == 2:
                            siparis.update({"Ayran": "10.00"})

                        elif secim_icecek == 3:

                            siparis.update({"Şalgam": "15.00"})

                        elif secim_icecek == 4:

                            siparis.update({"Su": "10.00"})

                        else:

                            print("Hatalı İçecek Seçimi")

                            continue

                    else:
                        print("Hatalı Seçim")

                        continue

                    cevap = input("Başka bir arzunuz var mı ?(E/H)").upper()

                    if cevap == "E":

                        continue

                    elif cevap == "H":

                        siparisler.update({masa: siparis})

                        print(siparisler)

                        break

                    else:

                        print("Hatalı seçim")

                        continue

            break


    elif menu == 2:

        print("Hesap Bölümü")

        for siparis, deger in siparisler.items():
            print(f"{siparis}  =>  {deger}")

        hesap: float = 0.00

        masa_hesabi = input("Hangi masa hesabı alınacak ?")

        for i in siparisler["Masa-" + masa_hesabi].values():
            hesap += float(i)

        print(f"Toplam Fiyat: {hesap}")

        hesap_odendi_mi: str = input("Hesap ödendi mi ?(E/H)").upper()

        if hesap_odendi_mi == "E":
            masalar.update({"Masa-" + masa_hesabi: "F"})

        for masa, deger in masalar.items():
            print(f"{masa} => {deger}")

    elif menu == 3:
        while True:
            print("""
                                            1- Çorba Çeşitleri
                                            2- Balık Çeşitleri
                                            3- Et Çeşitleri
                                            4- Makarna Çeşitleri
                                            5- Arasıcak Çeşitleri
                                            6- Salata Çeşitleri
                                            7- İçecek Çeşitleri
                                    """)

            menu_secim: int =int(input("güncellemek istediğiniz menüyü girin:"))

            if menu_secim == 1:
                yeni_corba: str = input("eklemek istediğiniz corbayı ve fiyatını  giriniz:")
                yeni_corba_fiyat: float = float(input("yeni çorbanın fiyatıni giriniz:"))
                corbalar.update({yeni_corba: yeni_corba_fiyat})
                print(corbalar)

            elif menu_secim == 2:
                yeni_balik: str = input("eklemek istediğiniz balik ve fiyatını  giriniz:")
                yeni_balik_fiyat: float = float(input("yeni balığın fiyatıni giriniz:"))
                baliklar.update({yeni_balik: yeni_balik_fiyat})
                print(baliklar)

            elif menu_secim == 3:
                yeni_et: str = input("eklemek istediğiniz et ve fiyatını  giriniz:")
                yeni_et_fiyat: float = float(input("yeni etin fiyatıni giriniz:"))
                etler.update({yeni_et: yeni_et_fiyat})
                print(etler)

            elif menu_secim == 4:
                yeni_makarna: str = input("eklemek istediğiniz makarna ve fiyatını  giriniz:")
                yeni_makarna_fiyat: float = float(input("yeni makarnanın fiyatıni giriniz:"))
                makarnalar.update({yeni_makarna: yeni_makarna_fiyat})
                print(makarnalar)

            elif menu_secim == 5:
                yeni_arasicak: str = input("eklemek istediğiniz arasıcak ve fiyatını  giriniz:")
                yeni_arasicak_fiyat: float = float(input("yeni arasicak fiyatıni giriniz:"))
                ara_sicaklar.update({yeni_arasicak: yeni_arasicak_fiyat})
                print(ara_sicaklar)


            elif menu_secim == 6:
                yeni_salata: str = input("eklemek istediğiniz salata ve fiyatını  giriniz:")
                yeni_salata_fiyat: float = float(input("yeni salatanın fiyatıni giriniz:"))
                salatalar.update({yeni_salata: yeni_salata_fiyat})
                print(salatalar)


            elif menu_secim == 7:
                yeni_icecek: str = input("eklemek istediğiniz içecek ve fiyatını  giriniz:")
                yeni_icecek_fiyat: float = float(input("yeni içecek fiyatıni giriniz:"))
                icecekler.update({yeni_icecek: yeni_icecek_fiyat})
                print(icecekler)


            else:
                print("yanlış menü seçimi!")
                continue

            cevap_2: str = input("Başka bir arzunuz var mı ?(E/H)").upper()

            if cevap_2 == "E":
                continue

            elif cevap_2 == "H":
                break

            else:
                print("hatalı secim")
                continue

        break




































