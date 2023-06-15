text = input('Metn daxil edin: ')
reqemler = 0
herfler = 0
bosluqlar = 0
for element in text:
    if element.isalpha():
        herfler += 1
    elif element.isdigit():
        reqemler += 1
    else:
        bosluqlar += 1

print(reqemler)
print(herfler)
print(bosluqlar)
print(len(text))

sifre = input('Sifre daxil edin: ')
boyuk_herf = 0
kicik_herf = 0
reqem = 0
isare = 0

for element in sifre:
    if element.isupper():
        boyuk_herf += 1
    elif element.islower():
        kicik_herf += 1
    elif element.isdigit():
        reqem += 1
    else:
        isare += 1

if boyuk_herf >= 1 and kicik_herf >= 1 and reqem >=1 and isare >= 1 and len(sifre) >= 8:
    print('Sifre gucludur')
else:
    print('Sifre guclu deyil')

# String formatting
text = 'Hello'
print(text.center(10, '#'))    # umumi setrin uzunlugunu 10-a tamamlayir, setrimizin mezmununu merkezlesdirir.
                                # tamamlayici simvol 2-ci arqumentdeki simvol olur

print(text.ljust(10, '#'))      # umumi setrin uzunlugu 10-a tamamlanir, setrimiz soldan yazilir
print(text.rjust(10, '#'))      # umumi setrin uzunlugu 10-a tamamlanir, setrimiz sagdan yazilir


metn = '          Hello        '
print(metn.strip())     # bosluqlari silecek
print(metn.lstrip())    # soldaki bosluqlari silecek
print(metn.rstrip())    # sagdaki bosluqlari silecek

# raw stringler
text1 = r' salam hey \n sag ol'
print(text1)

# .format() metodu
user_login = input('Enter your nickname: ')
str_msg = 'Hello, {} user.'.format(user_login)
print(str_msg)

salary_msg = 'Hello, your salary is {0:3.2f}'.format(200.7873)
print(salary_msg)

# .find(), .rfind() metodu
text = 'Salam menem'
print(text.find('menem', 7, len(text)-1))   #soldan saga axtaris aparir
print(text.rfind('me'))        # sagdan sola axtaris aparir

# .index() ve .rindex() metodlari
print(text.index('men')) # soldan saga axtaris aparir
print(text.rindex('me')) # sagdan sola axtaris aparir
# index ile findin fergi altsetir tapilmadiqda find -1 index ise error qaytarir

# in ve not in acar sozleri

if 'Salam' in text:
    print(True)
if 'Sag ol' not in text:
    print(False)
text = 'This is a sample text. sample text'
# .split() metodu
text = 'This is a sample text. sample text'
print(text.split())     # setri hisselere parcalayir ve hemin hisseleri bir siyahiya yigir
# susmaya gore setirler bosluga gore parcalanir
# arqument ile deyismek olur
print(text.split('a'))

# Setrlerin birlesdirilmesi
# .join() metodu -> istenilen sayda element birlesdirir
text = 'This is a sample text. sample text'
print('+'.join(text.split()))

text = 'this is a sample text. sample text. sample text.'
sentences = text.split('. ')
capitalized_sentences = ''

for sentence in sentences:
    sentence = sentence.capitalize()
    capitalized_sentences += sentence + '. '

print(f'{capitalized_sentences}\b\b')

# string modulu
import string

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.printable)

import string
import random

# random kitabxanasinin .sample() metodu
print(random.sample(string.ascii_lowercase, 6))
print(''.join(random.sample(string.ascii_lowercase, 6)))
