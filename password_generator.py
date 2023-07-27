import random
import string


total = string.ascii_letters + string.digits
length = int(input('Введите количество символов: '))
tmp = [random.choice(total) for i in range(length)]
password = "".join(tmp)
print(f'Ваш проль: {password}')
