import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassaPaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_saldot_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateinen_riittava_saldo(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(10000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 9600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_maukkaasti_kateinen_ei_tarpeeksi_rahaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateinen_riittava_saldo(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_edullisesti_kateinen_ei_tarpeeksi_rahaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_riittava_saldo(self):
        bool = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(bool)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_edullisesti_kortilla_riittava_saldo(self):
        bool = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(bool)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_maukkaasti_kortilla_riittamaton_saldo(self):
        kortti = Maksukortti(50)
        bool = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(bool)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 50)


    def test_syo_edullisesti_kortilla_riittamaton_saldo(self):
        kortti = Maksukortti(50)
        bool = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(bool)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 50)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_lataa_rahaa_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)