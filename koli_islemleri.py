# Kullanıcıdan alınan girdileri listeye ekleyen fonksiyon
def add_task(boş_koli):
    task = input("Eklenen eşyayı girin: ")
    boş_koli.append(task)
    print("Eşya eklendi.")

# Listede bulunan eşyaları gösteren fonksiyon
def show_tasks(boş_koli):
    print("Kolideki eşyalar: ")
    for task in boş_koli:
        print("- " + task)

# Listeden eşyayı silen fonksiyon
def delete_task(boş_koli):
    task = input("Silmek istediğiniz eşyayı giriniz: ")
    if task in boş_koli:
        boş_koli.remove(task)
        print("Eşya başarıyla silindi.")
    else:
        print("Eşya bulunamadı.")

def koli_sayfasi(koli):
    # Ana sayfa döngüsü
    while True:
        print("\nTo-Do List Uygulaması")
        print("1. Eşya Ekle")
        print("2. Eşyaları Göster")
        print("3. Eşya Sil")
        print("4. Çıkış")
        choice = input("Seçiminiz (1/2/3/4): ")
        
        if choice == "1":
            add_task(koli)
        elif choice == "2":
            show_tasks(koli)
        elif choice == "3":
            delete_task(koli)
        elif choice == "4":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")