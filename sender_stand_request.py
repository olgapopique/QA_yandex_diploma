import requests
import configuration
import data

def get_docs():
    response = requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
    return response
#Функция создания нового заказа
def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=body,
                             headers=data.headers)
    saved_track = response.json()["track"]
    return response, saved_track
# Функция получения информации о заказе по треку
def get_order_info(track):
    url = configuration.URL_SERVICE + configuration.GETTING_ORDER_PATH
    params = {'t': track}  # как в документации к API
    response = requests.get(url, params=params)
    return response
