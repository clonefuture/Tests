import unittest
import requests
from auth_data import token


url = 'https://cloud-api.yandex.net/v1/disk/resources'
url_err = 'https://cloud-api.yandex.net/disk/resources'
path_dir = '/Netology/test'
headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
params = {'path': path_dir}


class TestApiYandex(unittest.TestCase):

    def test_ya_api_disc1(self):
        # проверка отсутствия папки /Netology/test на Я.Диск

        get_response = requests.get(url, headers=headers, params=params)
        self.assertEqual(get_response.status_code, 404)

    def test_ya_api_disc2(self):
        # проверка выполнения PUT запроса на создание папки в Я.Диск

        response = requests.put(url, headers=headers, params=params)
        self.assertEqual(response.status_code, 201)

    def test_ya_api_disc3(self):
        # проверка выполнения GET запроса к созданной папке на Я.Диск

        get_response = requests.get(url, headers=headers, params=params)
        self.assertEqual(get_response.status_code, 200)

    def test_ya_api_disc4(self):
        # проверка выполнения PUT запроса на создание папки в Я.Диск, без указания версии API

        response = requests.put(url_err, headers=headers, params=params)
        self.assertEqual(response.status_code, 404)

    def test_ya_api_disc5(self):
        # проверка выполнения PUT запроса на создание уже существующей папки в Я.Диск

        response = requests.put(url, headers=headers, params=params)
        self.assertEqual(response.status_code, 409)






