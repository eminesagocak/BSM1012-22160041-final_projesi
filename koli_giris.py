# Kullanıcıdan alınan girdileri listeye ekleyen fonksiyon
import siniflarim
def yeni_koli(kullanici):
    koliadı= input("koli adını giriniz: ")
    koli = siniflarim.Koli()
    koli.ad = koliadı
    koli.sahibi = kullanici
    kullanici.koliler.append(koli)
    print("koli oluşturuldu.")
    
def kolilerimi_göster(kullanici):
    print("Kolileriniz: ")
    for koli in kullanici.koliler:
        print("- " + koli.ad)  

    

    # koli döngüsü
def kolilerim(kullanici):
    while True:
        print("1. Koliyi ekle.")
        print("2. Kolilerimi göster.")
        print("3. koliyi aç.")
        print("4. Çıkış yap.")
        seçim = input("Seçiminiz (1/2/3/4): ")
        if seçim == "1":
            yeni_koli(kullanici)
        elif seçim == "2":
            kolilerimi_göster(kullanici)
        elif seçim =="3":
            print("koli seç")
        elif seçim == "4":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")