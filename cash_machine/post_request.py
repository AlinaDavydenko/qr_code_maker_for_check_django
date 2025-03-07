import requests
import json


def post_request(data):
    """ отправка post запроса на сервер """

    url = 'http://127.0.0.1:8000/cash_machine/'

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return f"Запрос выполнен успешно!"
    else:
        return f"Произошла ошибка. Статус код: {response.status_code} \nОтвет от сервера:, {response.text}"
