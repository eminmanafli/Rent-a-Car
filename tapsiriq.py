# task 1
class Mehsul:
    def __init__(self, ad, qiymet):
        self.ad = ad
        self.qiymet = qiymet

    def melumatlari_goster(self):
        print(self.ad)
        print(self.qiymet)

    def endirim_teyin_et(self, endirim):
        self.qiymet = self.qiymet * (100-endirim) / 100
        print(f'Yeni qiymet: {self.qiymet}')


class Elektronika(Mehsul):
    def __init__(self, ad, qiymet, brend, garanti_muddeti):
        super().__init__(ad, qiymet)
        self.brend = brend
        self.garanti = garanti_muddeti

    def model_goster(self):
        print(self.brend)


class Telefon(Elektronika):
    def __init__(self, ad, qiymet, brend, garanti_muddeti, isleme_sistemi, kamera):
        super().__init__(ad, qiymet, brend, garanti_muddeti)
        self.isleme_sistemi = isleme_sistemi
        self.kamera = kamera

    def zeng_et(self):
        print('Zeng edilir...')


class AkilliSaat(Elektronika):
    def __init__(self, ad, qiymet, brend, garanti_muddeti, ekran_olcusu, batareya_omru):
        super().__init__(ad, qiymet, brend, garanti_muddeti)
        self.ekran_olcusu = ekran_olcusu
        self.batareya_omru = batareya_omru

    def bildiri_goster(self):
        print('Bildirim')


avtomobil = Mehsul(ad='Chevrolet Camaro', qiymet=149000)
avtomobil.melumatlari_goster()
avtomobil.endirim_teyin_et(50)

komputer = Elektronika(ad='Dell G7', qiymet=4000, brend='Dell', garanti_muddeti=2)
komputer.model_goster()

telefon = Telefon(ad='Iphone 14', qiymet=2000, brend='Iphone', garanti_muddeti=2, isleme_sistemi='IOS 17', kamera=48)
telefon.zeng_et()

saat = AkilliSaat(ad='HW 8 Ultra', qiymet=130, brend='HW', garanti_muddeti=2, ekran_olcusu='520x580', batareya_omru='4-5 gun')
saat.bildiri_goster()

# task 2
class Person:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def melumatlari_goster(self):
        print(self.ad)
        print(self.soyad)
        print(self.yas)

    def qarsilama_et(self):
        print('Salam, xos gelmisiniz!')


class Isci(Person):
    def __init__(self, ad, soyad, yas, vezife, maas):
        super().__init__(ad, soyad, yas)
        self.vezife = vezife
        self.maas = maas

    def ishe_basla(self):
        print('Ishe basladi!')

    def maas_artir(self, qiymet):
        self.maas += qiymet


class Menecer(Isci):
    def __init__(self, ad, soyad, yas, vezife, maas, departament, bonus):
        super().__init__(ad,soyad,yas,vezife,maas)
        self.departament = departament
        self.bonus = bonus

    def ishcileri_yonet(self):
        print('Ishciler yonetilir!')

    def bonus_teyin_et(self, bonus):
        self.maas += self.bonus


adam1 = Person(ad='Magnus', soyad='Carlsen', yas=32)
adam1.melumatlari_goster()
adam1.qarsilama_et()

adam2 = Isci(ad='Emin', soyad='Manafli', yas= 16, vezife='Mudir', maas = 3000)
adam2.ishe_basla()
adam2.maas_artir(qiymet=200)
