my_dict = \
    {
        'tuple': ('RU', 'KZ', 'UZ', 'TH', 'last_element'),
        'list': [1, '2_for_delite_element', 3, 4, 5],
        'dict': {'RU': 'Msk', 'KZ': 'Atyrau', 'KZ2': 'Almaty', 'TH': 'Sammui', 'for_delite': 'this_is_for_delite'},
        'set': {'taxi', 'air', 'boat', 'motobike', 'bikecircle'}
    }
print(my_dict['tuple'][-1])
my_dict['list'].append('new_item')
my_dict['list'].pop(1)
print(my_dict['list'])
my_dict['dict']['i am a tuple'] = 'New values'
my_dict['dict'].pop('for_delite')
print(my_dict['dict'])
print('i am a tuple' in my_dict['dict'].keys())
print('i am a tuple' in my_dict['dict'].values())
print('New values' in my_dict['dict'].values())
print(('i am a tuple','New values') in my_dict['dict'].items())
for key, value in my_dict['dict'].items():
	print(key, value)
my_dict['set'].add('car')
my_dict['set'].remove('bikecircle')
print(my_dict['set'])
print(my_dict)
