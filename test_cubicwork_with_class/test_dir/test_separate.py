import requests
import pytest
import allure
import sys
import os

from homework.yuryi_lopatin.Homework_21_locust.homework_21 import response
# Добавляем путь к корню проекта
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_cubicwork_with_class.endpoints.create_campaign import (CreateCamp)
from test_cubicwork_with_class.endpoints.get_list_campaign import GetListCamp
from test_cubicwork_with_class.endpoints.upload_advert import (UploadAdvert)
from test_cubicwork_with_class.endpoints.update_campaign import (UpdateCamp)
#from test_api_fin_project.endpoints.get_meme import (GetMeme)
#from test_api_fin_project.endpoints.delete_meme import (DeleteMeme)


# Глобальные переменные
uploaded_audio_file_id = None
created_campaigns = []  # Глобальная переменная для хранения ID созданных кампаний
calc_ids = []  # Глобальная переменная для хранения calcId из test_calc_players
file_info_ids = []  # Для хранения ID загруженных файлов
file_ids = []  # Для хранения ID файлов


@pytest.fixture(scope='session')
def start_testing():
    print('Start testing')
    yield
    print('Testing completed')


"""Тест загрузки файла на сервер"""
@allure.feature('Files')
@allure.story('Upload file')
@allure.title('Загрузка аудио файла на сервер')
@pytest.mark.smoke
def test_upload_audio_file(new_token):
    print(f'\n=== Тест загрузки аудио файла на сервер ===')

    # Получаем путь к корневой папке проекта
    current_file = os.path.abspath(__file__)  # Путь к текущему файлу с тестами
    test_dir = os.path.dirname(current_file)  # Папка с файлом тестов (test_dir)
    project_root = os.path.dirname(test_dir)  # Корневая папка проекта (на уровень выше)

    # Имя файла
    file_name = 'CR_(распродажа)_авг(1).mp3'

    # Универсальный путь (работает на Windows и Linux)
    file_path = os.path.join(project_root, file_name)

    print(f'Корень проекта: {project_root}')
    print(f'Путь к файлу: {file_path}')
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        # Показываем доступные файлы для отладки
        try:
            available_files = [f for f in os.listdir(project_root)
                               if os.path.isfile(os.path.join(project_root, f)) and
                               (f.endswith('.mp3') or f.endswith('.m4a') or f.endswith('.wav'))]

            pytest.fail(f"Файл не найден: {file_path}\nДоступные медиа файлы в проекте: {available_files}")
        except Exception as e:
            pytest.fail(f"Файл не найден: {file_path}\nОшибка при получении списка файлов: {e}")
    headers = {'Authorization': f'Bearer {new_token}'}
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_name, file, 'audio')}
            response = requests.post(
                'https://aooh-test.cubicservice.ru/v1/files/upload',
                files=files,
                headers=headers,
                timeout=30
            )

        print(f'Статус ответа: {response.status_code}')
        print(f'Ответ сервера: {response.text}')
        # Проверки с Allure
        with allure.step(f'Check status code for file upload is: {response.status_code}'):
            assert response.status_code == 200, f"Ошибка загрузки файла: {response.status_code} - {response.text}"

        # Сохраняем fileInfoID загруженного файла
        file_data = response.json()
        file_info_id = file_data.get('id') if isinstance(file_data, dict) else file_data

        with allure.step(f'Check that file ID is received'):
            assert file_info_id is not None, f"ID файла не найден в ответе: {file_data}"

        # Сохраняем в глобальный список
        file_info_ids.append(file_info_id)
        print(f'✅ Аудио файл {file_name} загружен с ID: {file_info_id}')

    except FileNotFoundError:
        pytest.fail(f"Файл не найден: {file_path}")
    except Exception as e:
        pytest.fail(f"Ошибка при загрузке файла: {str(e)}")


"""Тест проверки загрузки аудио файла на сервер"""
@allure.feature('Files')
@allure.story('Upload file')
@allure.title('Проверка загрузки аудио файла на сервер')
@pytest.mark.smoke
def test_status_upload_advert_files(new_token):
    print(f'\n=== Тест проверки загрузки аудио файла для рекламной кампаний ===')
    # Проверяем, что есть fileInfoId
    if not file_info_ids:
        pytest.skip("Нет fileInfoId для тестирования")
    # Используем ID первой созданной fileInfoId
    file_info_id = file_info_ids[0]
    print(f'Используем fileId: {file_info_id}')
    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    # Используем динамический fileId отправляем массив ID
    body = [file_info_id]  # Массив вместо объекта file_id!
    response = requests.post(f'https://aooh-test.cubicservice.ru/v1/files/get-upload-statuses',
                             json=body, headers=headers)
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200


"""Тест создания собственного файла на основе загруженного аудио файла"""
@allure.feature('Files')
@allure.story('Upload file')
@allure.title('Проверка создания собственного файла на основе загруженного аудио файла')
@pytest.mark.smoke
def test_renew_advert_file(new_token):
    print(f'\n=== Тест проверки создания собственного файла на основе аудио файла для рекламной кампаний ===')
    # Используем fileInfoId
    file_info_id = file_info_ids[0]
    print(f'Используем fileInfoId: {file_info_id}')

    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    # Используем динамический fileId отправляем массив ID
    body = {"type": 2, "name": "собственный рекламный ролик", "fileInfoId": file_info_id}  # Массив вместо объекта file_id!
    response = requests.post(
        f'https://aooh-test.cubicservice.ru/v1/files/new?CounterpartyId=7',
        json=body, headers=headers
    )
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200

    # Сохраняем fileID загруженного файла
    file_data = response.json()
    file_id = file_data.get('id') if isinstance(file_data, dict) else file_data

    with allure.step(f'Check that file ID is received'):
        assert file_id is not None, f"ID файла не найден в ответе: {file_data}"

    # Сохраняем в глобальный список
    file_ids.append(file_id)
    print(f'✅ Аудио файл загружен с ID: {file_id}')

"""Создаем кампанию с fileID и сразу её обновляем"""
@allure.feature('Campaigns')
@allure.story('Manipulate adverts campaigns')
@allure.title('Создание и обновление рекламной кампании')
def test_create_and_update_advert_camp(new_token):
    print(f'\n=== Создание и немедленное обновление ===')
    # Проверяем что есть загруженные файлы
    if not file_info_ids:
        pytest.skip("Нет загруженных файлов для создания кампании")
    # Используем fileId
    file_id = file_ids[0]
    print(f'Используем fileId: {file_id}')

    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}

    # 1. Создаем кампанию
    create_body = {
        "name": "campaign_to_update",
        "categoryId": 2,
        "schedules": [
            {"dateFrom": "2025-08-20", "dateTo": "2025-09-03", "timeFrom": "10:10:30", "timeTo": "13:10:34",
             "weekDays": [1]}],
        "limit": {"type": 1, "value": 10},
        "files": [{"position": 1, "fileId": file_id}]
    }

    create_camp = CreateCamp()
    create_camp.create_new_camp(create_body=create_body, headers=headers)
    #assert create_camp.status_code == 200, f"Ошибка: {create_camp.status_code} - {create_camp.text}"

    campaign_data = create_camp.response.json()
    # print(f'📝 Создана кампания ID: {campaign_id}')
    # Сохраняем ID созданной кампании
    campaign_id = campaign_data
    print(f'🆔 API вернул ID как число: {campaign_id}')
    if campaign_id:
        created_campaigns.append(campaign_id)
        print(f'✅ Кампания создана с ID: {campaign_id}')

    # 2. Сразу обновляем компанию (пока она в статусе draft)
    update_body = {
        "name": "updated_campaign_name",
        "categoryId": 2,
        "schedules": [
            {"dateFrom": "2025-08-21", "dateTo": "2025-09-22", "timeFrom": "11:11:31", "timeTo": "14:11:31",
             "weekDays": [1, 5]}],
        "limit": {"type": 1, "value": 20},
        "files": [{"position": 1, "fileId": file_id}]
    }

    update_camp = CreateCamp()
    update_camp.create_new_camp(create_body=create_body, headers=headers)
    #assert create_camp.status_code == 200, f"Ошибка: {update_camp.status_code} - {update_body.text}"
    print(f'✅ Кампания успешно создана и обновлена!')


"""Тест получения списка кампаний"""
@allure.feature('Campaigns')
@allure.story('Get adverts campaigns')
@allure.title('Получение списка рекламных кампаний')
@pytest.mark.smoke
def test_get_list_adverts_campaigns(new_token):
    print(f'\n=== Тест получения рк по ID ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Используем ID первой созданной кампании
    campaign_id = created_campaigns[0]
    print(f'Используем ID кампании: {campaign_id}')
    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    body = {"order": [{"field": "id", "direction": 2}],
            "page": 1,
            "pageItemCount": 10,
            "id": campaign_id,
            "status": 1}
    get_list_camp = GetListCamp()
    get_list_camp.get_list_adverts_campaigns(body=body, headers=headers)
    #print(f'Статус ответа: {response.status_code}')
    #print(f'Ответ: {response.text}')
    # with allure.step(f'Check status code for test_get_list_rk is: {response.status_code}'):
    #     assert response.status_code == 200

"""Тест получения кампании"""
@allure.feature('Campaigns')
@allure.story('Get adverts campaigns')
@allure.title('Получение рекламной кампаний')
@pytest.mark.smoke
def test_get_adverts_campaigns(new_token):
    print(f'\n=== Тест получения одной рк по ID ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Используем ID первой созданной кампании
    campaign_id = created_campaigns[0]
    print(f'Используем ID кампании: {campaign_id}')
    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    body = {"order": [{"field": "id", "direction": 2}],
            "page": 1,
            "pageItemCount": 10,
            "id": campaign_id,
            "status": 1}
    response = requests.post(f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/get?counterpartyId=7',
                             json=body, headers=headers)
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test get one rk is: {response.status_code}'):
        assert response.status_code == 200
    # # Дополнительная проверка, что возвращается нужная кампания
    if response.status_code == 200:
        campaign_data = response.json()
        with allure.step(f'Check that returned campaign has correct ID: {campaign_id}'):
            # Предполагаем, что в ответе есть поле id
            if isinstance(campaign_data, dict) and 'id' in campaign_data:
                assert campaign_data['id'] == campaign_id

"""Расчет подходящих плееров кампании"""
@allure.feature('Campaigns')
@allure.story('Get calc-players')
@allure.title('Получение подходящих плееров для рекламной кампаний')
@pytest.mark.smoke
def test_calc_players(new_token):
    print(f'\n=== Тест получения подходящих плееров для рекламной кампаний ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Используем ID первой созданной кампании
    campaign_id = created_campaigns[0]
    print(f'Используем ID кампании: {campaign_id}')
    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    response = requests.post(
        f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/calc-players?CounterpartyId=7',
        headers=headers
    )
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    # проверяем статус код ответа
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200, f"Ошибка: {response.status_code} - {response.text}"
    # Сохраняем calcId из ответа
    response_data = response.json()
    if isinstance(response_data, dict) and 'calcId' in response_data:
        calc_id = response_data['calcId']
        calc_ids.append(calc_id)
        print(f'Получен calcId{calc_id}')
    else:
        print(f'calcId не найде в ответе: {response_data}')
        # В случае, если структура ответа другая, попробуем найти calcId
        if isinstance(response_data, int):
            # Если весь ответ - это calcId
            calc_ids.append(response_data)
            print(f'✅ API вернул calcId как число: {response_data}')


"""Получение плеера из расчета"""
@allure.feature('Campaigns')
@allure.story('Get calc-players')
@allure.title('Получение плееров для рекламной кампаний')
@pytest.mark.smoke
def test_get_players(new_token):
    print(f'\n=== Тест получения плееров для рекламной кампаний ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Проверяем, что есть calcId
    if not calc_ids:
        pytest.skip("Нет calcId для тестирования")
    # Используем ID первой созданной кампании и первый calcId
    campaign_id = created_campaigns[0]
    calc_id = calc_ids[0]
    print(f'Используем ID кампании: {campaign_id}')
    print(f'Используем calcId: {calc_id}')

    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    body = {"order": [{"field": "name", "direction": 2}],
            "page": 2,
            "pageItemCount": 2,
            "calcId": calc_id,  # Используем динамический calcId
            "profileId": 0,
            "localityId": 0,
            "pricePerMinute": 0}
    response = requests.post(
        f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/get-players?CounterpartyId=7',
        json=body, headers=headers
    )
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200


"""Выбор плеера для рекламной компании"""
@allure.feature('Campaigns')
@allure.story('Get player for adverts')
@allure.title('Выбор плеера для рекламной кампаний')
@pytest.mark.smoke
def test_get_players_for_adverts(new_token):
    print(f'\n=== Тест выбора плеера для рекламной компании ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Проверяем, что есть calcId
    if not calc_ids:
        pytest.skip("Нет calcId для тестирования")
    # Используем ID первой созданной кампании и первый calcId
    campaign_id = created_campaigns[0]
    calc_id = calc_ids[0]
    print(f'Используем ID кампании: {campaign_id}')
    print(f'Используем calcId: {calc_id}')

    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    body = {"calcId": calc_id, "playerIds": [45806], "preview": False}
    response = requests.post(
        f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/get-players?CounterpartyId=7',
        json=body, headers=headers
    )
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200


"""Назначение на плеер рекламных компании"""
@allure.feature('Campaigns')
@allure.story('Assign adverts campaigns on player')
@allure.title('Назначение на плеер рекламной кампаний')
@pytest.mark.smoke
def test_assign_adverts_on_player(new_token):
    print(f'\n=== Тест назначение на плеер рекламных кампаний ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Проверяем, что есть calcId
    if not calc_ids:
        pytest.skip("Нет calcId для тестирования")
    # Используем ID первой созданной кампании и первый calcId
    campaign_id = created_campaigns[0]
    calc_id = calc_ids[0]
    print(f'Используем ID кампании: {campaign_id}')
    print(f'Используем calcId: {calc_id}')

    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    body = {"calcId": calc_id, "playerIds": [45806], "preview": False}
    response = requests.post(
        f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/assign?CounterpartyId=7',
        json=body, headers=headers
    )
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200

"""Назначение на плеер рекламной компании"""
@allure.feature('Campaigns')
@allure.story('Rewiev adverts')
@allure.title('Назначение на плеер рекламной кампании')
@pytest.mark.smoke
def test_rewiev_adverts(new_token):
    print(f'\n=== Тест назначение на плеер рекламной кампаний ===')
    # Проверяем, что есть созданные кампании
    if not created_campaigns:
        pytest.skip("Нет созданных кампаний для тестирования")
    # Проверяем, что есть calcId
    if not calc_ids:
        pytest.skip("Нет calcId для тестирования")
    # Используем ID первой созданной кампании и первый calcId
    campaign_id = created_campaigns[0]
    #calc_id = calc_ids[0]
    print(f'Используем ID кампании: {campaign_id}')
    #print(f'Используем calcId: {calc_id}')

    headers = {'Authorization': f'Bearer {new_token}', 'Content-Type': 'application/json'}
    #body = {"calcId": calc_id, "playerIds": [45806], "preview": False}
    response = requests.post(
        f'https://aooh-test.cubicservice.ru/v1/campaigns/{campaign_id}/review?CounterpartyId=7',
        headers=headers  # json=body
    )
    print(f'Статус ответа: {response.status_code}')
    print(f'Ответ: {response.text}')
    with allure.step(f'Check status code for test_get_players is: {response.status_code}'):
        assert response.status_code == 200
