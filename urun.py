
from veritabani import Veritabani
from log import Log

class Urun:
    def ekle(self, kullanici_id, ad, fiyat):  # ÃœrÃ¼n eklemek iÃ§in fonksiyon tanÄ±mÄ±
        conn = Veritabani().baglan()  # VeritabanÄ±na baÄŸlanÄ±r
        cursor = conn.cursor()  # VeritabanÄ± Ã¼zerinde iÅŸlem yapabilmek iÃ§in imleÃ§ oluÅŸturur

        cursor.execute(
            "INSERT INTO urunler (ad, fiyat) VALUES (?, ?)",
            (ad, fiyat)
        )  # VeritabanÄ±na yeni Ã¼rÃ¼n eklemek iÃ§in SQL sorgusu Ã§alÄ±ÅŸtÄ±rÄ±r

        conn.commit()  # YapÄ±lan deÄŸiÅŸiklikleri veritabanÄ±na kaydeder
        conn.close()  # VeritabanÄ± baÄŸlantÄ±sÄ±nÄ± kapatÄ±r

        Log.kaydet(kullanici_id, f"ÃœrÃ¼n eklendi: {ad}, Fiyat: {fiyat} TL")  # Log kaydÄ± oluÅŸturur
        print("ÃœrÃ¼n baÅŸarÄ±yla eklendi.")    
    def sil(self, kullanici_id, urun_id):
        conn = Veritabani().baglan()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM urunler WHERE id=?", (urun_id,))
        conn.commit()
        conn.close()

        Log.kaydet(kullanici_id, f"Urun silindi: {urun_id}")
        
    def satin_al(kullanici_id, urun_id):  # ÃœrÃ¼n satÄ±n almak iÃ§in fonksiyon tanÄ±mÄ±
        conn = Veritabani().baglan()  # VeritabanÄ±na baÄŸlanÄ±r
        cursor = conn.cursor()  # VeritabanÄ± Ã¼zerinde iÅŸlem yapabilmek iÃ§in imleÃ§ oluÅŸturur
        cursor.execute("SELECT * FROM urunler WHERE id=?", (urun_id,))  # Belirtilen id'ye sahip Ã¼rÃ¼nÃ¼ veritabanÄ±ndan seÃ§mek iÃ§in SQL sorgusu Ã§alÄ±ÅŸtÄ±rÄ±r
        urun = cursor.fetchone()  # SQL sorgusunun dÃ¶ndÃ¼rdÃ¼ÄŸÃ¼ ilk satÄ±rÄ± alÄ±r (tek bir Ã¼rÃ¼n)
        if urun:  # EÄŸer Ã¼rÃ¼n bulunduysa
            Log.kaydet(kullanici_id, f"ÃœrÃ¼n satÄ±n alÄ±ndÄ±: {urun[1]}, Fiyat: {urun[2]} TL")  # SatÄ±n alma iÅŸlemini log kaydeder
            print(f"SatÄ±n alÄ±ndÄ±: {urun[1]}, Fiyat: {urun[2]} TL")  # ÃœrÃ¼n satÄ±n alÄ±ndÄ±ÄŸÄ±nÄ± ekrana yazdÄ±rÄ±r
        else:  # EÄŸer Ã¼rÃ¼n bulunamadÄ±ysa
            print("ÃœrÃ¼n bulunamadÄ±!")  # ÃœrÃ¼n bulunamadÄ±ÄŸÄ±nÄ± ekrana yazdÄ±rÄ±r
        conn.close()  # VeritabanÄ± baÄŸlantÄ±sÄ±nÄ± kapatÄ±r

    def listele():  # ÃœrÃ¼nleri listelemek iÃ§in fonksiyon tanÄ±mÄ±
        conn = Veritabani().baglan()  # VeritabanÄ±na baÄŸlanÄ±r
        cursor = conn.cursor()  # VeritabanÄ± Ã¼zerinde iÅŸlem yapabilmek iÃ§in imleÃ§ oluÅŸturur
        cursor.execute("SELECT * FROM urunler")  # VeritabanÄ±ndaki tÃ¼m Ã¼rÃ¼nleri seÃ§mek iÃ§in SQL sorgusu Ã§alÄ±ÅŸtÄ±rÄ±r
        urunler = cursor.fetchall()  # SQL sorgusunun dÃ¶ndÃ¼rdÃ¼ÄŸÃ¼ tÃ¼m satÄ±rlarÄ± alÄ±r
        for urun in urunler:  # Her bir Ã¼rÃ¼nÃ¼ dÃ¶ngÃ¼yle teker teker iÅŸler
            print(urun)  # ÃœrÃ¼nÃ¼ ekrana yazdÄ±rÄ±r
        conn.close()  # VeritabanÄ± baÄŸlantÄ±sÄ±nÄ± kapatÄ±r


