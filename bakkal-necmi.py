#!/usr/bin/env python3
import requests
import os
import sys

def hava_durumu():
    sehir = input("Ula, hangi köyün havasını öğrenekisen? ").strip()
    if not sehir:
        print("Hee, şehir ismi boş kalmaz da hava nasıl tutar, uşak?")
        return

    url = f"http://wttr.in/{sehir}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{sehir} için hava hali: {response.text}")
        else:
            print("Vay be, hava bilgisini alamadum bak, ne çıka hırdavat!")
    except Exception as e:
        print(f"Bi’şeyler karıştı, hata geldi ha: {e}")

NOT_DOSYA = "notes.txt"

def notlari_listele():
    if not os.path.exists(NOT_DOSYA):
        print("Diyom ya, not yok henüz defterde, boş kaldı her yer.")
        return

    with open(NOT_DOSYA, "r", encoding="utf-8") as f:
        notlar = f.readlines()
    if not notlar:
        print("Defter bomboş, not falan yok ha!")
        return

    print("Defterdekiler bak hele:")
    for i, not_ in enumerate(notlar, 1):
        print(f"{i}. {not_.strip()}")

def not_ekle():
    not_metni = input("Yaz hele notunu, anan uşak: ").strip()
    if not not_metni:
        print("Boş not olmaz ha, yemezler onu!")
        return
    with open(NOT_DOSYA, "a", encoding="utf-8") as f:
        f.write(not_metni + "\n")
    print("Not yazıldı, kurusu senin olsun!")

def not_sil():
    notlari_listele()
    try:
        secim = int(input("Hangi notu sileyim ha? Numara ver! "))
        with open(NOT_DOSYA, "r", encoding="utf-8") as f:
            notlar = f.readlines()
        if 1 <= secim <= len(notlar):
            silinen = notlar.pop(secim - 1).strip()
            with open(NOT_DOSYA, "w", encoding="utf-8") as f:
                f.writelines(notlar)
            print(f"'{silinen}' notunu sildim, rahat et uşak.")
        else:
            print("Ula, öyle numara mı olur? Daldan dala atıyorsun!")
    except ValueError:
        print("Sayısal gir hele, latifeler değil!")

def hesap_makinesi():
    print("Hesap makinesi lazımsa, doğru yere geldin ha!")
    try:
        sayi1 = float(input("Birinci rakamı ver hele: "))
        islem = input("İşlem seç (+, -, *, /): ").strip()
        sayi2 = float(input("İkinci rakamı da ver hele: "))

        if islem == '+':
            sonuc = sayi1 + sayi2
        elif islem == '-':
            sonuc = sayi1 - sayi2
        elif islem == '*':
            sonuc = sayi1 * sayi2
        elif islem == '/':
            if sayi2 == 0:
                print("Ula sıfıra bölünür mü lan, onu yapma!")
                return
            sonuc = sayi1 / sayi2
        else:
            print("Oğlum, böyle işlem mi olur? Bi’ daha dene bakalım.")
            return

        print(f"Sonuç bu işte: {sonuc}")
    except ValueError:
        print("Ula, rakam koy ne olur, harf mi var burada?!")

def not_menu():
    while True:
        print("\nBakkalın Defteri - Notlar Menüsü")
        print("1) Notları Göster")
        print("2) Not Yaz")
        print("3) Not Sil")
        print("q) Kaç bak, çıkalım")

        secim = input("Ne yapacaksan söyle artık: ").strip().lower()
        if secim == '1':
            notlari_listele()
        elif secim == '2':
            not_ekle()
        elif secim == '3':
            not_sil()
        elif secim == 'q':
            print("Güle güle, yolun açık olsun uşak!")
            break
        else:
            print("Anlamadım ulan, düzgün konuş!")

def shorten_lishli(long_url):
    api_url = "https://lish.li/API/api_post.php"
    data = {"origlink": long_url}
    response = requests.post(api_url, data=data)
    response.raise_for_status()
    result = response.json()
    if result.get("error"):
        print(f"API hatası ha: {result['error']}", file=sys.stderr)
        sys.exit(1)
    return result.get("shortlink")


def main():
    while True:
        print("\n===== NECMİ BAKKAL'A HOŞ GELDİN UŞAĞIM! =====")
        print("1) Necmi Amca Hava Durumuna Bakalım mı? 🌦️")
        print("2) Hesap Makinesi Kullanalım mı? 🧮")
        print("3) Deftere Not Düşelim mi? 📒")
        print("q) Gidiyoruz, bakkalı kapatıyoruz!")

        secim = input("Ne yapalım, uşak? ").strip().lower()

        if secim == '1':
            hava_durumu()
        elif secim == '2':
            hesap_makinesi()
        elif secim == '3':
            not_menu()
        elif secim == 'q':
            print("Ula görüşürüz, hava güzel olsun, helal sana!")
            break
        else:
            print("Ne dedin sen, tekrar bir bak hele ne diyorsun!")
            
if __name__ == "__main__":
    main()
