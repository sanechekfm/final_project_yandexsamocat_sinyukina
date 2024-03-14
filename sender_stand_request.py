# Александра Синюкина, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
                         #headers=data.headers)

response = post_new_order(data.order_body)
track = response.json()["track"]
print(response.status_code)
print(track)
def get_order(track):
   return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                      params={"t": track})