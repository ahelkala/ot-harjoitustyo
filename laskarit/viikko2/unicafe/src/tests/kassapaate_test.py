import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti_rahaa = Maksukortti(1000)
        self.maksukortti_ei_rahaa = Maksukortti(100)

    def test_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyjen_edullisten_lounaiden_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_loudaiden_maara(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_lounas_kassaraha_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateisosto_edullinen_lounas_lounasmaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edullinen_lounas_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), 760)

    def test_kateisosto_edullinen_lounas_rahaa_ei_riittavasti_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_kateisosto_edullinen_lounas_rahaa_ei_riittavasti_lounasmaara(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0) 

    def test_kateisosto_edullinen_lounas_rahaa_ei_riittavasti_kassanrahat(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)      

    def test_kateisosto_maukas_lounas_kassaraha_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kateisosto_maukas_lounas_lounasmaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukas_lounas_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)

    def test_kateisosto_maukas_lounas_rahaa_ei_riittavasti_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_kateisosto_maukas_lounas_rahaa_ei_riittavasti_lounasmaara(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0) 

    def test_kateisosto_maukas_lounas_rahaa_ei_riittavasti_kassanrahat(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)    

    def test_maksukortti_edullinen_tarpeeksi_rahaa_veloitus_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rahaa))

    def test_maksukortti_edullinen_ei_tarpeeksi_rahaa_veloitus_false(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_ei_rahaa))

    def test_maksukortti_maukas_tarpeeksi_rahaa_veloitus_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rahaa))

    def test_maksukortti_maukas_ei_tarpeeksi_rahaa_veloitus_false(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_ei_rahaa))

    def test_maksukortti_edullinen_ei_tarpeeksi_rahaa_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_ei_rahaa)
        self.assertEqual(str(self.maksukortti_ei_rahaa), "saldo: 1.0")

    def test_maksukortti_maukas_ei_tarpeeksi_rahaa_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_ei_rahaa)
        self.assertEqual(str(self.maksukortti_ei_rahaa), "saldo: 1.0")
    
    def test_maksukortti_edullinen_ei_tarpeeksi_rahaa_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_ei_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)    

    def test_maksukortti_maukas_ei_tarpeeksi_rahaa_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_ei_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 0)    

    def test_maksukortti_maukas_lounaiden_maara_muuttuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksukortti_edullinen_lounaiden_maara_muuttuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_summa_veloitetaan_kortilta_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rahaa)
        self.assertEqual(str(self.maksukortti_rahaa), "saldo: 7.6")

    def test_summa_veloitetaan_kortilta_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rahaa)
        self.assertEqual(str(self.maksukortti_rahaa), "saldo: 6.0")

    def test_kortilla_maksaessa_kassan_saldo_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_maksaessa_kassan_saldo_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_maksaessa_kassan_saldo_ei_muutu_edullinen_ei_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_ei_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_maksaessa_kassan_saldo_ei_muutu_maukas_ei_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_ei_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rahaa, 1000)
        self.assertEqual(str(self.maksukortti_rahaa), "saldo: 20.0")

    def test_kortille_rahaa_ladattaessa_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rahaa, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_negatiivista_rahaa_ladattaessa_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rahaa, -1000)
        self.assertEqual(str(self.maksukortti_rahaa), "saldo: 10.0")

    def test_kortille_negatiivista_rahaa_ladattaessa_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rahaa, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

