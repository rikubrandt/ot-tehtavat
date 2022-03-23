import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(2)
        self.assertEqual(self.maksukortti.saldo, 12)

    def test_rahan_ottaminen_nakyy_saldossa(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(self.maksukortti.saldo, 8)

    def test_liian_paljon_rahan_ottamista_ei_vahenna(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_rahan_ottaminen_palauttaa_arvon(self):
        arvo = self.maksukortti.ota_rahaa(12)
        self.assertFalse(arvo)
        arvo = self.maksukortti.ota_rahaa(5)
        self.assertTrue(arvo)

    def test_maksukortin_saldo_tulostus(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")