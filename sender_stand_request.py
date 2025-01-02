import configuration
import requests

# Функция для создания нового заказа клиентом
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Функция для получения заказа по его номеру
def get_new_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_PATH + str (track_order))
