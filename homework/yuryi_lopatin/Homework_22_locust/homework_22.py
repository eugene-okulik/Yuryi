import requests
from datetime import datetime

print('.........')
print('Start testing')

response = requests.get('http://167.172.172.115:52353/object')
print(response)  # <Response [200]>
print('.........')

print('Тест времени получения всех объектов')
start = datetime.now()
response = requests.get('http://167.172.172.115:52353/object')
print(response)  # <Response [200]>
end = datetime.now()
print(end - start)
print('.........')


"""Создает новый объект"""
print('Тест времени создания нового объекта')
start = datetime.now()
response = requests.post(
    'http://167.172.172.115:52353/object',
    json={"name": "lox", "data": {"color": "white", "size": "big"}},
    headers={'Content-Type': 'application/json'}
)
print(response)
end = datetime.now()
print(end - start)
obj_id = response.json()['id']  # тут в self.post_id будет хранится ответ в виде id из json
print(f'Created object with id: {obj_id}')
print('.........')


"""Тест получения объекта по ID"""
print('Тест получения объекта по ID')
start = datetime.now()
response = requests.get(f'http://167.172.172.115:52353/object/{obj_id}')
print(response)
end = datetime.now()
print(end - start)
print(f'Get object with id: {obj_id}')
print('.........')


"""Тест обновления объекта (PUT)"""
# def test_put_object(new_obj_id):
#     obj_id = new_obj_id
print('Тест обновления объекта (PUT)')
body = {
    "name": "saks",
    "data": {"color": "red", "size": "small"}
}
start = datetime.now()
response = requests.put(f'http://167.172.172.115:52353/object/{obj_id}', json=body).json()
print(response)
end = datetime.now()
print(end - start)
print(f'Put object with id: {obj_id}')
print('.........')


"""Тест частичного обновления объекта (PATCH)"""
# def test_patch_object(new_obj_id):
#     obj_id = new_obj_id
print('Тест частичного обновления объекта (PATCH)')
body = {
    "name": "ass",
    "data": {"color": "pink", "size": "very big"}
}
headers = {'Content-Type': 'application/json'}
start = datetime.now()
response = (requests.patch(f'http://167.172.172.115:52353/object/{obj_id}', json=body, headers=headers)
            .json())
print(response)
end = datetime.now()
print(end - start)
print(f'Patch object with id: {obj_id}')
print('.........')


"""Тест удаления объекта"""
requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
start = datetime.now()
print(f'Удаление объекта с id: {obj_id}')
print(response)
end = datetime.now()
print(end - start)
print(f'Delete object with id: {obj_id}')
print('.........')

print('Testing completed')
print('.........')