from mimesis import Person
from mimesis.locales import Locale

'''
Этот скрипт создан для его дальнейшей реализации со скриптом отсюда : https://github.com/WhiteHodok/script-for-passwords
Всё также, используем максимально простые и понятные либы со стандартным Py.
Для изменения домена почты, поменяйте 14 строку,на нужный вам домен почты.
'''

person = Person(Locale.EN)
number = int(input('Введите нужное вам количество почт:'))

for i in range(number):
    print(person.email(domains=['gmail.com']))