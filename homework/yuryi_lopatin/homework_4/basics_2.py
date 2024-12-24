my_dict = {'tuple': 'my_tuple', 'list': 'my_list', 'dict': 'my_dict', 'set': 'my_set'}
my_tuple = ('RU', 'KZ', 'UZ', 'TH', 'last_element')
print(my_tuple[-1])
my_list = [1, '2_for_delite_element', 3, 4, 5]
my_list.append('new_item')
my_list.pop(1)
print(my_list)
my_inside_dict = {'RU': 'Msk', 'KZ': 'Atyrau', 'KZ2': 'Almaty', 'TH': 'Sammui', 'for_delite': 'this_is_for_delite'}
my_inside_dict['i_am_a_tuple'] = 'add_new_tuple'
my_inside_dict.pop('for_delite')
print(my_inside_dict)
my_set = {'taxi', 'air', 'boat', 'motobike', 'bikecircle'}
my_set.add('car')
my_set.remove('bikecircle')
print(my_set)
print(my_dict)
