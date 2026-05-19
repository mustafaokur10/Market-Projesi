
# Market Uygulamasi

Bu proje, SQLite veritabann kullanarak bir market ynetim sistemi gelitirmektedir. Proje, kullanclarn rn satn almasna, rn eklemesine, rn silmesine, kullanc eklemesine ve kullanc silmesine olanak tanr. Ayrca admin ve misafir kullanclar iin ayr menler bulunmaktadr.

# Dosya Yapisi

1. veritabani.py: Veritabanı baglantisi ve tablo olusturma islemlerini icerir.
2. urun.py: urunlerle ilgili islemleri icerir.
3. kullanici.py: Kullanicilarla ilgili islemleri icerir.
4. log.py : Log kayit islemleri buradan gerceklesir.
5. main.py: Programin giris noktasidir.
6. ACIKLAMA.md: Proje hakknda aciklamalar ve kullanim kilavuzunu icerir.

# Kullanim Kilavuzu

Program calistirmak icin yukarda gordugunuz sirada dosyalar sirayla calistirmaniz gerekmektedir.

# Veritabani Oluturma

Program altnda, `veritaban.py` dosyasndaki `Veritabani` snf kullanlarak veritaban ve tablolar oluturulur.
proje.db adna sahip olarak bir sqlite3 tablosu oluur 3 tane tablo oluur kullanclar loglar ve rnler isminde.

# Kullanici islemleri

- Yeni Kullanici Olusturma: `main.py` dosyasindaki menuden "Yeni Kullanici Olustur" secenegi ile kullanici olusturabilirsiniz.
- Giris Yapma: Kullanici ad ve sifre ile giris yapabilir ve kullanici rolune gore admin veya misafir menusune erisebilirsiniz.
- Asagidaki menulerde yazan her islemide yapabilirsiniz.
 
# Admin Menusu

Admin kullanicilar icin asagidaki islemler yaplabilir:
1. urun Satin Al
2. urun Ekle
3. urun Sil
4. urunleri Goster
5. Kullanicilari Gor
6. Kullanici Ekle
7. Kullanici Sil
8. Log Kayitlarini Gor
9. Hava Durumu
10. cikis Yap11. 

# Misafir Menusu

Misafir kullanicilar icin asagidaki islemler yapilabilir:
1. urun Satin Al
2. urun Ekle
3. urun Sil
4. urunleri Goster
5. Hava Durumu
6. cikis Yap

# Kod Aciklamalari

Her dosyada bulunan sinif ve fonksiyonlar detayli yorum satirlar ile aciklanmistir. Bu aciklamalar, kodun ne yaptigini ve nasil kullanildigini anlamaniza yardimci olacaktir.

# OKUL NUMARASI = 202307105016
# AD SOYAD = MUSTAFA OKUR
