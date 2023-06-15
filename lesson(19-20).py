import string
for i in range(97, 123):
    lowercase = chr(i)
    print(''.join(lowercase), end='')

import random
import string
username = ''.join(random.sample(string.ascii_letters, 8))
password = ''.join(random.sample(string.ascii_uppercase + string.digits, 10))

print(username)
print(password)
