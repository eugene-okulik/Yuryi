temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]
temperatures = set (temperatures)
temperatures = list(temperatures)
hot_temperaturs = filter(lambda x: x > 28, temperatures)
hot_list = list(hot_temperaturs)

print(max(hot_list))
print(min(hot_list))
all_elements_hot_list = (len(hot_list))
midle_temperature = sum(hot_list) / all_elements_hot_list
print(midle_temperature)
