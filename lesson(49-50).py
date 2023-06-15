'''
# OOP - encapsulation, polymorphism, inheritance
# sahe 2 cur olur: public ve private
class Person:
    def __init__(self, age):
        self.__age = age

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Yas menfi ola bilmez!')

    def show(self):
        print(f'My age is {self.__age}')

person1 = Person(2)
person1.age = 10
person1.show()
print(person1.age)

class Transport:
    def __init__(self, ticket_price, start_point, end_point):
        self.ticket_price = ticket_price
        self.start_point = start_point
        self.end_point = end_point
        self.balans = 0

    def ticket_pass(self):
        self.balans += self.ticket_price

    def show_info(self):
        print(f'Ticket price: {self.ticket_price}')
        print(f'Start point: {self.start_point}')
        print(f'End point: {self.end_point}')
        print(f'Balans: {self.balans}')


class Bus(Transport):
    def __init__(self, ticket_price, start_point, end_point, bus_number):
        super().__init__(ticket_price, start_point, end_point)
        self.bus_number = bus_number

    def signal(self):
        print('Beeep!')

    def show_balance(self):
        print(self.balans)

    def show_info(self):
        super().show_info()
        print(f'Bus number: {self.bus_number}')


class Plane(Transport):
    def __init__(self, ticket_price, start_point, end_point, company):
        super().__init__(ticket_price, start_point, end_point)
        self.company = company

    def distribute_meals(self):
        print('All passengers got meals!')


class Taxi(Transport):
    def __init__(self, ticket_price, start_point, end_point, masin_nomresi):
        super().__init__(ticket_price, start_point, end_point)
        self.masin_nomresi = masin_nomresi

    def musteri_tap(self):
        print('Musteri axtariram...')

bus1 =  Bus(0.40, 'Genclik Mall', 'Qara Qarayev', '205')
bus1.ticket_pass()
bus1.ticket_pass()
bus1.ticket_pass()
bus1.ticket_pass()
bus1.ticket_pass()
bus1.show_balance()
bus1.signal()
bus1.show_info()

# task
class Heyvan:
    def __init__(self, ad, cins, yas):
        self.ad = ad
        self.cins = cins
        self.yas = yas

    def melumatlari_goster(self):
        print(f'Ad:{self.ad}')
        print(f'Cins:{self.cins}')
        print(f'Yas:{self.yas}')

    def salam_ver(self):
        print('Salam verildi!')

    def oyan(self):
        print('Heyvan oyandi!')

    def yemek_ye(self):
        print('Heyvan yemeyini yedi!')


class Qartal(Heyvan):
    def __init__(self, ad, cins, yas, kanat_uzunlugu, ucus_sureti):
        super().__init__(ad, cins, yas)
        self.kanat_uzunlugu = kanat_uzunlugu
        self.ucus_sureti = ucus_sureti

    def uc(self):
        print('Qartal ucur!')

    def ovlamaq(self):
        print(f"Qartal ovlayir!")

    def melumatlari_goster(self):
        super().melumatlari_goster()
        print(f'Qanat uzunlugu: {self.kanat_uzunlugu}')
        print(f'Ucus Sureti: {self.ucus_sureti}')


class Kopek(Heyvan):
    def __init__(self, ad, cins, yas, sexse_sadiq, boyun_uzunlugu):
        super().__init__(ad, cins, yas)
        self.sexse_sadiq = sexse_sadiq
        self.boyun_uzunlugu = boyun_uzunlugu

    def hav_havla(self):
        print('It hurur!')

    def eyles(self):
        print('It eylesir!')

    def melumatlari_goster(self):
        super().melumatlari_goster()
        print(f'Sexse sadiq: {self.sexse_sadiq}')
        print(f'Boyun uzunluqu: {self.boyun_uzunlugu}')


class At(Heyvan):
    def __init__(self, ad, cins, yas, yarismaq_sureti, hereket_novu):
        super().__init__(ad, cins, yas)
        self.yarismaq_sureti = yarismaq_sureti
        self.hereket_novu = hereket_novu

    def atla(self):
        print('At atlayir!')

    def hereket_et(self):
        print('At hereket edir!')

    def melumatlari_goster(self):
        super().melumatlari_goster()
        print(f'Yarismaq sureti: {self.yarismaq_sureti}')
        print(f'Hereket novu: {self.hereket_novu}')

qartal1 = Qartal('Sahin', 'Qirgi qartali', 2, 50, 80)
qartal1.melumatlari_goster()
qartal1.uc()
qartal1.ovlamaq()

it1 = Kopek('It', 'Bulldog', 5, 'Sadiqdir', 1)
it1.melumatlari_goster()
it1.hav_havla()
it1.eyles()

at1 = At('At', 'Qarabag ati', 4, 10, 'qacmaq')
at1.melumatlari_goster()
at1.atla()
at1.hereket_et()
'''
class Şəxs:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def melumatlari_goster(self):
        print(f'Ad:{self.ad}')
        print(f'Soyad:{self.soyad}')
        print(f'Yas:{self.yas}')

    def qarsilama_et(self):
        print(f'{self.ad}: Salam!')

