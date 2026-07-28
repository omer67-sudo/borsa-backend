import pandas as pd
import yfinance as yf

# BIST Katılım Endeksi (Helal Sertifikalı) Hisse Listesi (240+ Hisse)
katilim_hisseleri = [
    "ACSEL.IS", "ADEL.IS", "ADESE.IS", "AEFES.IS", "AFYON.IS", "AGESA.IS", "AGHOL.IS", "AGROT.IS", "AHGAZ.IS", "AKCNS.IS",
    "AKFGY.IS", "AKFYE.IS", "AKMGY.IS", "AKSA.IS", "AKSEN.IS", "AKSUE.IS", "ALARK.IS", "ALBRK.IS", "ALCAR.IS", "ALCTL.IS",
    "ALKA.IS", "ALKIM.IS", "ALMAD.IS", "ALTNY.IS", "ALVES.IS", "ANELE.IS", "ANGEN.IS", "ANHYT.IS", "ANSGR.IS", "ARASE.IS",
    "ARCLK.IS", "ARDYZ.IS", "ARENA.IS", "ARSAN.IS", "ARTMS.IS", "ARZUM.IS", "ASELS.IS", "ASGYO.IS", "ASTOR.IS", "ATAGY.IS",
    "ATAKP.IS", "ATATP.IS", "ATEKS.IS", "ATSYH.IS", "AVOD.IS", "AVPGY.IS", "AYCES.IS", "AYDEM.IS", "AYGAZ.IS", "AZTEK.IS",
    "BAGFS.IS", "BAKAB.IS", "BALAT.IS", "BANVT.IS", "BARMA.IS", "BATIS.IS", "BAYRK.IS", "BEGYO.IS", "BERA.IS", "BEYAZ.IS",
    "BFREN.IS", "BIENY.IS", "BIGCH.IS", "BIMAS.IS", "BINHO.IS", "BIOEN.IS", "BIZIM.IS", "BJKAS.IS", "BLCYU.IS", "BMTKS.IS",
    "BNTAS.IS", "BOBET.IS", "BORAB.IS", "BORSK.IS", "BOSSA.IS", "BRKSN.IS", "BRKVY.IS", "BRSAN.IS", "BRSAT.IS", "BRYAT.IS",
    "BSOKE.IS", "BTCIM.IS", "BUCIM.IS", "BURCE.IS", "BURVA.IS", "BVSAN.IS", "BYDNR.IS", "CANTE.IS", "CASA.IS", "CATES.IS",
    "CCOLA.IS", "CELHA.IS", "CEMAS.IS", "CEMTS.IS", "CEOEM.IS", "CIMSA.IS", "CLEBI.IS", "CMBTN.IS", "CMENT.IS", "CONSE.IS",
    "COSMO.IS", "CRFSA.IS", "CUSAN.IS", "CVKMD.IS", "CWENE.IS", "DAGHL.IS", "DAGI.IS", "DAPGM.IS", "DARDL.IS", "DGATE.IS",
    "DGGYO.IS", "DITAS.IS", "DMRGD.IS", "DMSAS.IS", "DNISI.IS", "DOAS.IS", "DOBUR.IS", "DOCO.IS", "DOGTE.IS", "DOHOL.IS",
    "DOKTA.IS", "DURDO.IS", "DYOBY.IS", "EDATA.IS", "EDIP.IS", "EGEEN.IS", "EGGUB.IS", "EGPRO.IS", "EGSER.IS", "EKIZ.IS",
    "EKSUN.IS", "ELITE.IS", "EMKEL.IS", "ENERY.IS", "ENJSA.IS", "ENKAI.IS", "EPLAS.IS", "ERBOS.IS", "EREGL.IS", "ESEN.IS",
    "ETILR.IS", "EUPWR.IS", "EUREK.IS", "EYGYO.IS", "FADE.IS", "FLAP.IS", "FMIZP.IS", "FONET.IS", "FORMT.IS", "FORTE.IS",
    "FRIGO.IS", "FROTO.IS", "FZLGY.IS", "GARAN.IS", "GENIL.IS", "GEREL.IS", "GESAN.IS", "GIPTA.IS", "GLBMD.IS", "GLRYH.IS",
    "GLYHO.IS", "GMTAS.IS", "GOKNR.IS", "GOLTS.IS", "GOODY.IS", "GOZDE.IS", "GRSEL.IS", "GRTHO.IS", "GSDHO.IS", "GSDEVR.IS",
    "GUBRF.IS", "GWIND.IS", "GZAGH.IS", "HALKB.IS", "HATEK.IS", "HEATR.IS", "HEKTS.IS", "HKTM.IS", "HUBVC.IS", "HUNER.IS",
    "HURGZ.IS", "ICUGS.IS", "IDGYO.IS", "IEYHO.IS", "IHAAS.IS", "IHEVA.IS", "IHGZT.IS", "IHLGM.IS", "IHLAS.IS", "INDES.IS",
    "INFO.IS", "INGRM.IS", "INTEM.IS", "INVEO.IS", "INVES.IS", "IPEKE.IS", "ISCTR.IS", "ISDMR.IS", "ISFIN.IS", "ISGSY.IS",
    "ISGYO.IS", "ISKPL.IS", "ISMEN.IS", "ISSEN.IS", "IZINV.IS", "IZMDC.IS", "JANTS.IS", "KAPLM.IS", "KAREL.IS", "KARSN.IS",
    "KARTN.IS", "KATMR.IS", "KAYSE.IS", "KBORU.IS", "KCAER.IS", "KCHOL.IS", "KENT.IS", "KERVT.IS", "KFEIN.IS", "KGYO.IS",
    "KLGYO.IS", "KLMSN.IS", "KLNMA.IS", "KLRHO.IS", "KLYSN.IS", "KMPUR.IS", "KNFRT.IS", "KONTR.IS", "KONYA.IS", "KORDS.IS",
    "KOZAL.IS", "KOZAA.IS", "KRDMD.IS", "KRONT.IS", "KRPLS.IS", "KRTEK.IS", "KRVGD.IS", "KSTUR.IS", "KTLEV.IS", "KTCUR.IS",
    "KUTPO.IS", "KUYAS.IS", "KZBGY.IS", "KZGYO.IS", "LIDER.IS", "LILAK.IS", "LINK.IS", "LKMNH.IS", "LOGOS.IS", "LUKSK.IS",
    "MAALT.IS", "MACKO.IS", "MAKIM.IS", "MAKTK.IS", "MANAS.IS", "MARKA.IS", "MARTI.IS", "MAKTN.IS", "MEDTR.IS", "MEGAP.IS",
    "MEGMT.IS", "MEPET.IS", "MERCN.IS", "MERIT.IS", "MERKO.IS", "METRO.IS", "METUR.IS", "MGROS.IS", "MHRGY.IS", "MIATK.IS",
    "MNDTR.IS", "MOBTL.IS", "MOGAN.IS", "MPARK.IS", "MRGYO.IS", "MSGYO.IS", "MTRKS.IS", "MTRKS.IS", "NATEN.IS", "NETAS.IS",
    "NIBAS.IS", "NTGAZ.IS", "NTHOL.IS", "NUGYO.IS", "OBAMS.IS", "ODAS.IS", "OFSYM.IS", "ONCSM.IS", "ORGE.IS", "ORMA.IS",
    "ORTBO.IS", "OTKAR.IS", "OYAKC.IS", "OYYAT.IS", "OZATD.IS", "OZKGY.IS", "OZSUB.IS", "PAGYO.IS", "PAMEL.IS", "PAPIL.IS",
    "PARSN.IS", "PASEU.IS", "PENGD.IS", "PETKM.IS", "PETUN.IS", "PGSUS.IS", "PINSU.IS", "PNSUT.IS", "POLHO.IS", "PRKME.IS",
    "PRDGS.IS", "PRZMA.IS", "PSDTC.IS", "PSGYO.IS", "QNBFB.IS", "QNBFL.IS", "RALYH.IS", "RAYSG.IS", "REEDR.IS", "RNPOL.IS",
    "RODRG.IS", "ROYAL.IS", "RTALB.IS", "RUBNS.IS", "RYGYO.IS", "RYSAS.IS", "SAHOL.IS", "SAMAT.IS", "SANEL.IS", "SANFM.IS",
    "SANKO.IS", "SARKY.IS", "SASA.IS", "SAYAS.IS", "SDTTR.IS", "SEGMN.IS", "SEKFK.IS", "SEKUR.IS", "SELEC.IS", "SELVA.IS",
    "SEYKM.IS", "SILVR.IS", "SISE.IS", "SKBNK.IS", "SKTAS.IS", "SMART.IS", "SMRTG.IS", "SNAAM.IS", "SNNAM.IS", "SOKE.IS",
    "SOKM.IS", "SONME.IS", "SRVGY.IS", "SUMAS.IS", "SUNTK.IS", "SURGY.IS", "SUWEN.IS", "TATEN.IS", "TATGD.IS", "TAVHL.IS",
    "TCBANK.IS", "TCELL.IS", "TCKRC.IS", "TDGYO.IS", "TEKTU.IS", "TERA.IS", "TGPBA.IS", "THYAO.IS", "TKFEN.IS", "TKNSA.IS",
    "TLMAN.IS", "TMPOL.IS", "TMSN.IS", "TNZTP.IS", "TOASO.IS", "TRCAS.IS", "TRGYO.IS", "TRILC.IS", "TSKB.IS", "TSPOR.IS",
    "TTKOM.IS", "TTRAK.IS", "TUCLK.IS", "TUKAS.IS", "TURGG.IS", "TURSG.IS", "TUPRS.IS", "UFUK.IS", "ULAS.IS", "ULKER.IS",
    "UNLU.IS", "USAK.IS", "VAKBN.IS", "VAKKO.IS", "VAKFN.IS", "VBTYZ.IS", "VERTU.IS", "VERUS.IS", "VESBE.IS", "VESTL.IS",
    "VKFYO.IS", "VKGYO.IS", "YAPRK.IS", "YATAS.IS", "YAYLA.IS", "YEOTK.IS", "YGGYO.IS", "YGYO.IS", "YKBNK.IS", "YONGA.IS",
    "YUNSA.IS", "YYLGD.IS", "ZOREN.IS", "ZRGYO.IS"
]

def borsa_verilerini_getir(hisse_listesi):
    sonuclar = []

    print(f"Toplam {len(hisse_listesi)} katılım hissesi taranıyor, lütfen bekleyin...\n")

    for hisse in hisse_listesi:
        try:
            ticker = yf.Ticker(hisse)
            info = ticker.fast_info

            # Anlık online fiyat ve açılış fiyatı
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
            continue

    df = pd.DataFrame(sonuclar)
    return df

if __name__ == "__main__":
    veri_tablosu = borsa_verilerini_getir(katilim_hisseleri)
    print(veri_tablosu.to_string(index=False))
