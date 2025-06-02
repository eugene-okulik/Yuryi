import requests
import json


def get_all_obj():
    response = requests.get('http://167.172.172.115:52353/object').json()
    print(response)
get_all_obj()


def new_object():
    body = {"name": "lox", "data": {"color": "white", "size": "big"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json = body, headers = headers).json()
    print(response)
    return response['id']
new_object()


def get_new_object():
    post_id = new_object()
    response = requests.get(f'http://167.172.172.115:52353/object/{post_id}').json()
    print(response)
get_new_object()


def put_object():
    post_id = new_object()
    body = {
        "name": "saks",
        "data": {"color": "red", "size": "small"}
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{post_id}', json = body).json()
    assert response['name'] == 'saks'
    assert response['data'] == {"color": "red", "size": "small"}
    print(response)
put_object()


def patch_post():
    post_id = new_object()  # 409 #new_post() #1
    body = {
        "name": "ass",
        "data": {"color": "pink", "size": "very big"}
    }
    headers = {'Content-Type': 'application/json'}
    response = (requests.patch(f'http://167.172.172.115:52353/object/{post_id}', json = body, headers = headers)
                .json())
    assert response['name'] == 'ass'
    assert response['data'] == {"color": "pink", "size": "very big"}
    print(response)
patch_post()


def delete_a_post():
    post_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, 'status code'
    print(response)
    print(response.status_code)
delete_a_post()
