kontrol2=0
def musteri_ekleme():
    musteri_sayisi=int(input("Lutfen kac musteri eklemek istediginizi giriniz:"))
    for i in range(musteri_sayisi):
        print(f"Eklenecek {i + 1}. musteri bilgileri")
        tc = input(f"Lutfen eklenecek {i + 1}. musterinin tc kimlik numarasini giriniz:")
        ad = input(f"Lutfen eklenecek {i + 1}. musterinin adini giriniz(Birden fazla adiniz varsa arada bosluk birakmadan giriniz):")
        soyad = input(f"Lutfen eklenecek {i + 1}. musterinin soyadini giriniz:")
        yas = input(f"Lutfen eklenecek {i + 1}. musterinin yasini giriniz:")
        tel_no = input(f"Lutfen eklenecek {i + 1}. musterinin telefon numarasini giriniz:")
        beden = input(f"Lutfen eklenecek {i + 1}. musterinin beden bilgisini giriniz:")
        print("Yeni musteri basariyla eklendi:)")
        dosya = open("musteri.txt", "a")
        dosya.write(tc + " " + ad + " " + soyad + " " + yas + " " + tel_no + " " + beden + "\n")
        dosya.close()
def musteri_listeleme():
    print("Butun musteriler:")
    dosya=open("musteri.txt","r")
    veri=dosya.read()
    print(veri)
    dosya.close()
def musteri_silme():
    silinecek_tc = input("Lutfen silinecek musterinin tc kimlik numarasini giriniz:")
    dosya_silme=open("musteri.txt","r")
    veri=dosya_silme.readlines()
    dosya_silme.close()
    print(veri)
    tc_nolar=[] # liste kullanimi
    kontrol=0
    for i in veri:
        bilgi=i.split(" ")
        tc_nolar.append(bilgi[0])
        for j in range(len(tc_nolar)):
            if silinecek_tc == tc_nolar[j]:
                tc_nolar.remove(tc_nolar[j])
                veri.remove(i)
                kontrol += 1
    yeni_dosya=open("musteri.txt","w")
    for i in range(len(veri)):
        silme=yeni_dosya.write(veri[i])
    yeni_dosya.close()
    if kontrol==0:
        print("Lutfen dogru tc kimlik numarasi giriniz!!!")
    else:
        print("Silme islemi basariyla gerceklesti:)")
def musteri_arama():
    aranan_tc=input("Lutfen aranan musterinin tc kimlik numarasini giriniz:")
    dosya_arama=open("musteri.txt","r")
    veri=dosya_arama.readlines()
    dosya_arama.close()
    tc_nolar=[]
    kontrol=0
    for i in veri:
        bilgi=i.split(" ")
        tc_nolar.append(bilgi[0])
    for j in range(len(tc_nolar)):
        if aranan_tc==tc_nolar[j]:
            print("Aranan musterinin bilgileri:",veri[j])
            kontrol+=1
    if kontrol==0:
        print("Lutfen dogru tc kimlik numarasi giriniz!!!")
    else:
        print("Aranan musterinin bilgilerine basariyla erisildi:)")
def musteri_guncelleme():
    guncellenecek_musteri = input("Lutfen bilgisi guncellenecek musterinin tc kimlik numarasini giriniz:")
    print("Secim1:Tc kimlik numarasi guncelleme")
    print("Secim2:Ad guncelleme")
    print("Secim3:Soyad guncelleme")
    print("Secim4:Yas guncelleme")
    print("Secim5:Telefon numarasi guncelleme")
    print("Secim6:Beden guncelleme")
    secim2 = int(input("Lutfen guncellemek istediginiz bilginin numarasini giriniz:"))
    dosya_guncelleme = open("musteri.txt", "r")
    veri = dosya_guncelleme.readlines()
    dosya_guncelleme.close()
    sozluk = {}  # sozluk kullanimi
    kontrol = 0
    for i in veri:
        bilgi = i.split(" ")
        tc_no = bilgi[0]
        ad = bilgi[1]
        soyad = bilgi[2]
        yas = bilgi[3]
        tel_no = bilgi[4]
        beden = bilgi[5]
        sozluk[tc_no] = [tc_no, ad, soyad, yas, tel_no, beden]
    for key in sozluk:
        if key == guncellenecek_musteri:
            kontrol += 1
            if secim2 == 1:
                yeni_tc = input("Lutfen yeni tc giriniz:")
                sozluk[key][0] = yeni_tc
            if secim2 == 2:
                yeni_ad = input("Lutfen yeni adi giriniz:")
                sozluk[key][1] = yeni_ad
            elif secim2 == 3:
                yeni_soyad = input("Lutfen yeni soyadi giriniz:")
                sozluk[key][2] = yeni_soyad
            elif secim2 == 4:
                yeni_yas = input("Lutfen yeni yasi giriniz:")
                sozluk[key][3] = yeni_yas
            elif secim2 == 5:
                yeni_tel_no = input("Lutfen yeni telefon numarasi giriniz:")
                sozluk[key][4] = yeni_tel_no
            elif secim2 == 6:
                yeni_beden = input("Lutfen yeni beden giriniz:")
                sozluk[key][5] = yeni_beden
            else:
                print("Lutfen gecerli deger giriniz!!!")
            dosya=open("musteri.txt","w")
            for i in sozluk.values():
                musteri=i[0]+" "+i[1]+" "+i[2]+" "+i[3]+" "+i[4]+" "+i[5]+"\n"
                dosya.write(musteri)
            dosya.close()
    dosya_bosluk = open("musteri.txt", "r")
    veri = dosya_bosluk.readlines()
    for i in veri:
        if i=="\n":
            veri.remove(i)
    dosya_bosluk.close()
    yeni_dosya = open("musteri.txt", "w")
    for i in range(len(veri)):
        silme = yeni_dosya.write(veri[i])
    yeni_dosya.close()
    if kontrol == 0:
        print("Lutfen dogru tc kimlik numarasi giriniz!!!")
    else:
        print("Musteri guncelleme islemi basariyle gerceklesti:)")
def odenecek_tutar_hesaplama():
    odeme_yapacak_musteri=input("Lutfen odeme yapacak musterinin tc kimlik numarasini giriniz:")
    dosya_odeme=open("musteri.txt","r")
    veri=dosya_odeme.readlines()
    dosya_odeme.close()
    tc_nolar=[]
    kontrol=0
    for i in veri:
        bilgi=i.split(" ")
        tc_nolar.append(bilgi[0])
    for j in range(len(tc_nolar)):
        if odeme_yapacak_musteri == tc_nolar[j]:
            indirim() #foksiyon icinde fonksiyon cagirimi
            kontrol+=1
    if kontrol==0:
        print("Lutfen dogru tc kimlik numarasi giriniz!!!")
    elif kontrol2==0:
        print("Odenecek tutar hesaplama islemi basariyla gerceklesti:)")
def indirim():
    global kontrol2
    kontrol2=0
    try:
        tutar = int(input("Lutfen alısveris tutarini giriniz:"))
        sezon = input("Lutfen alinan elbisenin eski sezon mu yeni sezon mu oldugunu giriniz(eski:e,yeni:y):")
        yil = int(input("Lutfen kac yillik musterimiz oldugunuzu giriniz:"))
        if sezon == "e" or sezon == "E":
            indirim1 = tutar * 0.15
        elif sezon == "y" or sezon == "Y":
            indirim1 = tutar * 0.1
        if yil > 0 and yil <= 2:
            indirim2 = tutar * 0.01
        elif yil > 0 and yil <= 4:
            indirim2 = tutar * 0.03
        elif yil >= 5:
            indirim2 = tutar * 0.05
        print("Odemeniz gereken tutar:", tutar - indirim1 - indirim2)
    except ValueError:
        print("Lutfen gecerli deger giriniz!!!")
        kontrol2+=1
    except :
        print("Bilinmeyen bir hata olustu lutfen gecerli bir deger giriniz!!!")
        kontrol2+=1
def ana_menu():
    print(">>>>BUTİK OTOMASYONUNA HOSGELDINIZ<<<<")
    while True:
        print("Secim1:Musteri Ekleme")
        print("Secim2:Musteri Listeleme")
        print("Secim3:Musteri silme")
        print("Secim4:Musteri arama")
        print("Secim5:Musteri Guncelleme")
        print("Secim6:Odenecek tutar hesaplama")
        print("Secim7:Cikis")
        try:
            secim = int(input("Lutfen yapmak istediginiz islemi seciniz:"))
            if secim == 1:
                musteri_ekleme()
            elif secim == 2:
                musteri_listeleme()
            elif secim == 3:
                musteri_silme()
            elif secim == 4:
                musteri_arama()
            elif secim == 5:
                musteri_guncelleme()
            elif secim == 6:
                odenecek_tutar_hesaplama()
            elif secim == 7:
                print("Cikis yapiliyorrrr...")
                break
            else:
                print("Lutfen gecerli bir deger giriniz!!!")
        except ValueError:
            print("Hata!!! Lutfen gecerli bir rakam degeri giriniz!!!")
ana_menu()