from locust import task, HttpUser


class UserObj(HttpUser):
    def on_start(self):
        self.obj_id = None


    """Тест получения id всех объекта"""
    @task(1)
    def get_all_obj(self):
        self.client.get('/object', headers={'Content-Type': 'application/json'})


    """Тест создания объекта"""
    @task(1)
    def create_obj(self):
        response = self.client.post(
            '/object',
            json={"name": "lox", "data": {"color": "white", "size": "big"}},
            headers={'Content-Type': 'application/json'}
        )
        print(response)
        self.obj_id = response.json()['id']  # тут в self.post_id будет хранится ответ в виде id из json
        print(f'Created object with id: {self.obj_id}')


    """Тест получения id 1 объекта"""
    @task(1)
    def get_one_obj(self):
        if self.obj_id:
            self.client.get(f'/object/{self.obj_id}', headers={'Content-Type': 'application/json'})
        else:
            print("No obj_id available, skipping get_one_obj")


    """Тест обновления объекта (PUT)"""
    @task(1)
    def put_obj(self):
        if self.obj_id:
            response = self.client.put(
                f'/object/{self.obj_id}',
                json={"name": "saks","data": {"color": "red", "siz": "small"}},
                headers={'Content-Type': 'application/json'}
            )
            print(f'Update object: {self.obj_id}, response: {response.status_code}')
        else:
            print("No obj_id available, skipping get_one_obj")


    """Тест частичного обновления объекта (PATCH)"""
    @task(1)
    def patch_obj(self):
        if self.obj_id:
            response = self.client.patch(
                f'/object/{self.obj_id}',
                json={"name": "saks", "data": {"color": "red", "siz": "small"}},
                headers={'Content-Type': 'application/json'}
            )
            print(f'Update object: {self.obj_id}, response: {response.status_code}')
        else:
            print("No obj_id available, skipping get_one_obj")


    """Тест удаления объекта"""
    @task(1)
    def delete_obj(self):
        if self.obj_id:
            self.client.delete(f'/object/{self.obj_id}', headers={'Content-Type': 'application/json'})
        else:
            print("No obj_id available, skipping get_one_obj")
