
# Market Uygulamas

Bu proje, SQLite veritabann kullanarak bir market ynetim sistemi gelitirmektedir. Proje, kullanclarn rn satn almasna, rn eklemesine, rn silmesine, kullanc eklemesine ve kullanc silmesine olanak tanr. Ayrca admin ve misafir kullanclar iin ayr menler bulunmaktadr.

# Dosya Yaps

1. veritaban.py: Veritaban balants ve tablo oluturma ilemlerini ierir.
2. urun.py: rnlerle ilgili ilemleri ierir.
3. kullanici.py: Kullanclarla ilgili ilemleri ierir.
4. log.py : Log kayt ilemleri buradan gerekleir.
5. main.py: Programn giri noktasdr.
6. AIKLAMA.md: Proje hakknda aklamalar ve kullanm klavuzunu ierir.

# Kullanm Klavuzu

Program altrmak iin yukarda grdnz srada dosyalar srayla altrmanz gerekmektedir.

# Veritaban Oluturma

Program altnda, `veritaban.py` dosyasndaki `Veritabani` snf kullanlarak veritaban ve tablolar oluturulur.
proje.db adna sahip olarak bir sqlite3 tablosu oluur 3 tane tablo oluur kullanclar loglar ve rnler isminde.

# Kullanc lemleri

- Yeni Kullanc Oluturma: `main.py` dosyasndaki menden "Yeni Kullanc Olutur" seenei ile kullanc oluturabilirsiniz.
- Giri Yapma: Kullanc ad ve ifre ile giri yapabilir ve kullanc rolne gre admin veya misafir mensne eriebilirsiniz.
- Aadaki menlerde yazan her ilemide yapabilirsiniz.
 
# Admin Mens

Admin kullanclar iin aadaki ilemler yaplabilir:
1. rn Satn Al
2. rn Ekle
3. rn Sil
4. rnleri Gster
5. Kullanclar Gr
6. Kullanc Ekle
7. Kullanc Sil
8. Log Kaytlarn Gr
9. Hava Durumu
10. k Yap

# Misafir Mens

Misafir kullanclar iin aadaki ilemler yaplabilir:
1. rn Satn Al
2. rn Ekle
3. rn Sil
4. rnleri Gster
5. Hava Durumu
6. k Yap

# Kod Aklamalar

Her dosyada bulunan snf ve fonksiyonlar detayl yorum satrlar ile aklanmtr. Bu aklamalar, kodun ne yaptn ve nasl kullanldn anlamanza yardmc olacaktr.

# OKUL NUMARASI = 202307105016
# AD SOYAD = MUSTAFA OKUR
