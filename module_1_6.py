my_dict = {'ex@mail.ru': 89995552266, 'ex@yandex.ru': 89777876677}
print(my_dict)
print(my_dict.get('ex@yandex.ru'))
print(my_dict.get('ex@gmail.com'))
my_dict.update({'python@mail.ru': 84956432589,
                'ban@gmail.com': 89745683274})
a = my_dict.pop('ex@mail.ru')
print(a)
print(my_dict)

my_set = {1,2,3,'mail',(1,2,3,4,5,6),1,2,3}
my_set = set(my_set)
print(my_set)
my_set.discard((1,2,3,4,5,6))
my_set.add(666)
my_set.add(777)
print(my_set)