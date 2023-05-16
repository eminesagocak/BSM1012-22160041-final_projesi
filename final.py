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

ADMIN = 0
KULLANICI = 1
kullanicilar = {
    "emine": ("1234", ADMIN),
    "utku": ("4567", KULLANICI),
}

#Yeni üyenin kayıt bilgilerini alan fonksiyon.
def uye_kayit(kullanicilar):
    isim = input("Kullanıcı Adı giriniz: ")
    if isim in kullanicilar:
        print("Aynı adlı kullanıcı mevcut. \n Lütfen başka bir kullanıcı adı seçiniz.")
        return
    
    sifre = input("Şifre: ")
    kullanicilar[isim] = (sifre, KULLANICI)
    
    print("Kullanıcı Eklendi.")

#Kullanıcının giriş yapmasını sağlayan fonksiyon.
def giris_ekrani(kullanicilar):
    isim = input("Kullanıcı adı: ") 
    sifre = input("Kullanıcının şifresi: ")
    if isim in kullanicilar and kullanicilar[isim][0] == sifre:
        print("Giriş yapıldı.")
    else:
        print("Kullanıcı adı veya şifre yanlış.")

#Kullanıcı silmeyi sağlayan fonksiyon.
def silinecek_kayit(kullanicilar):
    isim = input("Silinecek Kullanıcı adı: ") 
    sifre = input("Silinecek Kullanıcının şifresi: ")
    if isim in kullanicilar and kullanicilar[isim][0] == sifre:
        del kullanicilar[isim]
     
    else:
        print("Kullanıcı adı veya şifre yanlış.")

#Kullanıcının şifre yenilemesini sağlayan fonksiyon.
def şifre_yenileme(kullanicilar):
    isim = input("Şifresi değiştirilecek kullanıcının adı:")
    if isim in kullanicilar:
        sifre1 = input("Kullanıcının yeni şifresi")
        kullanicilar[isim] = (sifre1,  kullanicilar[isim][1])
        

#Kullanıcının ana sayfa ekranı.
while True:
    print("1. Üye Ol")
    print("2. Sisteme Giriş Yap.")
    print("3. Üye Sil.")
    print("4. Şifremi Unuttum.")
    print("5. Çıkış Yap")
    secim = input("Seçiminizi Giriniz(1/2/3/4/5):")

    if secim =="1":
        uye_kayit(kullanicilar)
    elif secim =="2":
        giris_ekrani(kullanicilar)
    elif secim =="3":   
        silinecek_kayit(kullanicilar)
    elif secim == "4":
        şifre_yenileme(kullanicilar)
    elif secim =="5":  
        print("Uygulamadan Çıkış Yapıldı")
        break
    else:
        print("Geçersiz tuşlama yaptınız.")  








