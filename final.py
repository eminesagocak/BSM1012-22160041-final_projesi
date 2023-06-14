#Emine Sağocak - 221601041
#github hesabımın linki - https://github.com/eminesagocak/BSM1012-22160041-final_projesi.git

# Giriş Sayfası
# 1 - Sisteme Üye Ol (+)
# 2 - Sisteme Giriş Yap (+)
# 3 - Üye sil
# 4 - Şifremi Unuttum olmalıdır (+)
# 5 - Uygulamadan Çık (+)
#
# Kullanıcı Sayfası
# 1 - Koli Ekle
# 2 - Kolilerini Göster
# 3 - Koliyi Sil
# 4 - Koliyi Aç ...
# 5 - Çıkış
#
# Kullanıcı Koli Sayfası 
# 1 - Eşya Ekle (+)
# 2 - Eşyaları Göster (+)
# 3 - Eşya Sil (+)
# 4 - Koliden Çık (+)

import sqlite3
import koli_islemleri
import koli_giris
import siniflarim

# SQL GIRIŞ
vt=sqlite3.connect("final.db")
imlec=vt.cursor()

sorgu="CREATE TABLE if not exists 'Kullanicilar' ('Ad', 'Sifre', 'Yetki')"
imlec=vt.cursor()
imlec.execute(sorgu)

# GLOBAL DEĞİŞKENLER
ADMIN = 0
KULLANICI = 1

#Yeni üyenin kayıt bilgilerini alan fonksiyon.
def uye_kayit():
    isim = input("Kullanıcı Adı giriniz: ")
    
    # TODO: veritabanından isime sahip kullanıcıyı çek
    imlec.execute("select * from Kullanicilar where Ad = '{}';".format(isim))
    kullanici = imlec.fetchall() # [(ad, şifre, yetki), ...]

    print("Debug: ", kullanici)

    # TODO: eğer aynı isme sahip kullanıcı varsa hata ver ve çık.
    if len(kullanici) > 0:
        print("Aynı adlı kullanıcı mevcut.\nLütfen başka bir kullanıcı adı seçiniz.")
    else:
        # TODO: Şifreyi boş mu diye kontrol et, boşsa yeniden sor,
        sifre = ''
        while sifre == '':
            sifre = input("Şifre: ")
        
        # TODO: (isim, şifre, yetki) ile veritabanına yaz. 
        imlec.execute("Insert Into Kullanicilar Values (?,?,?)", (isim, sifre , KULLANICI))
        vt.commit()
        print("Kullanıcı Eklendi.")

#Kullanıcının giriş yapmasını sağlayan fonksiyon.
def giris_ekrani():
    isim = input("Kullanıcı adı: ")

    # TODO: veritabanından isime sahip kullanıcıyı çek
    imlec.execute("select * from Kullanicilar where Ad = '{}';".format(isim))
    kullanici = imlec.fetchall() 

    # TODO: eğer hiç bir kullanıcı yoksa bu isme sahip hata ver ve kapat.
    if len(kullanici) == 0:
        print("Kullanıcı yok.")
    else:
        sifre = input("Kullanıcının şifresi: ")

        # TODO: kullanıcı varsa şifre aynı mı diye kontrol et, aynı değilse hata, aynıysa giriş yap.
        if  kullanici[0][1] == sifre:
            üye = siniflarim.Kullanici()
            üye.ad = kullanici[0][0]
            üye.yetki = kullanici[0][2]

            print("Giriş yapıldı.")
            koli_giris.kolilerim(üye)
        else:
            print("Şifre yanlış.")

#Kullanıcı silmeyi sağlayan fonksiyon.
def silinecek_kayit():
    isim = input("Silinecek Kullanıcı adı: ") 
    # TODO: veritabanın ismi çek
    imlec.execute("select * from Kullanicilar where Ad = '{}';".format(isim))
    kullanici = imlec.fetchall() 
    if len(kullanici) == 0:
        print("Kullanıcı yok.")
    else:
        sifre = input("Silinecek Kullanıcının şifresi: ")
        # şifreyi kontrol et
        if  kullanici[0][1] == sifre:
            imlec.execute("delete from Kullanicilar where Ad = '{}';".format(isim))
            vt.commit()
             
            print("Kullanıcı başarıyla silindi.")
        else:
            print("Şifre yanlış.")

    

#Kullanıcının şifre yenilemesini sağlayan fonksiyon.
def şifre_yenileme():
    isim = input("Şifresi değiştirilecek kullanıcının adı:")
    # TODO: veritabanından ismi çek, eğer isim doğruysa yeni şifreyi al, ve veritabanını güncelle.
    imlec.execute("select * from Kullanicilar where Ad = '{}';".format(isim))
    kullanici = imlec.fetchall() 
    if len(kullanici) == 0:
        print("Kullanıcı yok.")
    else:
        sifre = input("Kullanıcının yeni şifresi: ")
        imlec.execute("update Kullanicilar set sifre = '{}' where Ad ='{}';".format(sifre,isim))
        vt.commit()
        print("Kullanıcı şifresi başarıyla değiştirildi.")

        

#Kullanıcının ana sayfa ekranı.
while True:
    print("1. Üye Ol")
    print("2. Sisteme Giriş Yap.")
    print("3. Üye Sil.")
    print("4. Şifremi Unuttum.")
    print("5. Çıkış Yap")
    secim = input("Seçiminizi Giriniz(1/2/3/4/5):")

    if secim =="1":
        uye_kayit()
    elif secim =="2":
        giris_ekrani()
    elif secim =="3":   
        silinecek_kayit()
    elif secim == "4":
        şifre_yenileme()
    elif secim =="5":  
        print("Uygulamadan Çıkış Yapıldı")
        break
    else:
        print("Geçersiz tuşlama yaptınız.")  

vt.commit()
vt.close()







