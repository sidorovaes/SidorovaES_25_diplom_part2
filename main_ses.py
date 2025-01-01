# Екатерина Сидорова, 25-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

URL_SERVICE = "https://bf3cdfb6-1471-4c96-a97f-a95b290c8f30.serverhub.praktikum-services.ru"
CREATE_ORDER_PATH = "/api/v1/orders"
GET_TRACK_PATH = "/api/v1/orders/track?t="

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 96,
    "phone": "+78003553535",
    "rentTime": 5,
    "deliveryDate": "2025-01-10"
}

def test_return_create_order_code_200 ():
    response_new_order = requests.post(URL_SERVICE + CREATE_ORDER_PATH,
                         json=order_body)
    track_order = response_new_order.json()["track"]
    response_get_new_track = requests.get(URL_SERVICE + GET_TRACK_PATH + str (track_order))
    assert response_get_new_track.status_code == 200, 'Тест провален'