my_dict = {
    'tuple': ('RU', 'KZ', 'UZ', 'TH', 'last_element'),
    'list': [1, '2_for_delite_element', 3, 4, 5],
    'inside_dict': {'RU': 'Msk', 'KZ': 'Atyrau', 'KZ2': 'Almaty', 'TH': 'Sammui', 'for_delite': 'this_is_for_delite'},
    'set': {'taxi', 'air', 'boat', 'motobike', 'bikecircle'}
          }
print(my_dict['tuple'][-1])
my_dict['list'].append('new_item')
my_dict['list'].pop(1)
print(my_dict['list'])
my_dict['inside_dict']['new_key'] = 'new_value'
my_dict['inside_dict'].pop('for_delite')
print(my_dict['inside_dict'])
my_dict['set'].add('car')
my_dict['set'].remove('bikecircle')
print(my_dict['set'])
print(my_dict)