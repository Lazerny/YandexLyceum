import requests
import sys


def show_map(ll=None, delta='0.005,0.005', map='map'):
    map_params = {
        "ll": ll,
        "spn": delta,
        "l": map
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(ll)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    return response.content