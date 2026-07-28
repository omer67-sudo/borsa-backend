import pandas as pd
import yfinance as yf

# Katılım Endeksi (Helal Sertifikalı) örnek BIST hisse listesi (.IS uzantılı)
katilim_hisseleri = [
    "THYAO.IS", "ASELS.IS", "EREGL.IS", "BIMAS.IS", "KRDMD.IS",
    "KONTR.IS", "SASA.IS", "HEKTS.IS", "ASTOR.IS", "ALARK.IS"
    # İhtiyaca göre 240 hisselik listenin tamamı buraya eklenebilir
]

def borsa_verilerini_getir(hisse_listesi):
    sonuclar = []

    print("Veriler çekiliyor, lütfen bekleyin...\n")

    for hisse in hisse_listesi:
        try:
            ticker = yf.Ticker(hisse)
            info = ticker.fast_info

            # Anlık ve açılış fiyatları
            online_fiyat = info.last_price
            acilis_fiyat = info.open

            if online_fiyat and acilis_fiyat:
                degisim_yuzde = ((online_fiyat - acilis_fiyat) / acilis_fiyat) * 100
                
                sonuclar.append({
                    "Hisse": hisse.replace(".IS", ""),
                    "Açılış Fiyatı (TL)": round(acilis_fiyat, 2),
                    "Online Fiyat (TL)": round(online_fiyat, 2),
                    "Fark (%)": f"%{round(degisim_yuzde, 2)}",
                    "Helal Durum": "Katılım Endeksi"
                })
        except Exception as e:
            print(f"{hisse} verisi alınamadı.")

    # Tablo formatına dönüştürme
    df = pd.DataFrame(sonuclar)
    return df

# Çalıştırma
if __name__ == "__main__":
    veri_tablosu = borsa_verilerini_getir(katilim_hisseleri)
    print(veri_tablosu.to_string(index=False))
