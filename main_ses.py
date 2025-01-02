# Екатерина Сидорова, 25-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

def test_return_create_order_code_200 ():
    response_new_order = sender_stand_request.post_new_order(data.order_body)
    track_order = response_new_order.json()["track"]
    response_get_new_track = sender_stand_request.get_new_track(track_order)
    assert response_get_new_track.status_code == 200, 'Тест провален'