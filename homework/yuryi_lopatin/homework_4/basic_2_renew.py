my_dict = \
    {
        'tuple': ('RU', 'KZ', 'UZ', 'TH', 'last_element'),
        'list': ['first item', '2_for_delite_element', 3, 4, 5],
        'dict': {'RU': 'Msk', 'KZ': 'Atyrau', 'KZ2': 'Almaty', 'TH': 'Sammui', 'for_delite': 'this_is_for_delite'},
        'set': {'taxi', 'air', 'boat', 'motobike', 'bikecircle'}
    }
print(my_dict['tuple'][-1])
my_dict['list'].append('new_item')
my_dict['list'].pop(1)
print(my_dict['list'])
print(my_dict['list'].count('new_item'))
print(my_dict['list'].index('new_item'))
print(my_dict['list'][0])
print(my_dict['list'][-5])
print(my_dict['list'][-1])
print(my_dict['list'][4])
print(my_dict['list'][len(my_dict['list']) - 1])
print(my_dict['list'][-2])
print(my_dict['list'][3])
my_dict['dict']['i am a tuple',] = 'New values'
my_dict['dict'].pop('for_delite')
print(my_dict['dict'])
print(('i am a tuple',) in my_dict['dict'].keys())
print(('i am a tuple',) in my_dict['dict'].values())
print('New values' in my_dict['dict'].values())
print((('i am a tuple',), 'New values') in my_dict['dict'].items())
my_str = ''.join(my_dict['dict'][('i am a tuple',)])
print(my_str)
my_dict['set'].add('car')
my_dict['set'].remove('bikecircle')
print(my_dict['set'])
my_dict['set2'] = my_dict['set'].copy()
print(my_dict['set2'])
print((my_dict['set2']) == (my_dict['set']))
print((my_dict['set2']) is (my_dict['set']))
print((my_dict['set']).isdisjoint(my_dict['set2']))
print((my_dict['set']).issubset(my_dict['set2']))
print((my_dict['set']).issuperset(my_dict['set2']))
my_dict['set2'].clear()
print(my_dict['set2'])
print((my_dict['set']).isdisjoint(my_dict['set2']))
print((my_dict['set']).issubset(my_dict['set2']))
print(my_dict)
