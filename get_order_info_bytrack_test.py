
# Ольга Попова, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

def positive_assert_get_order_info(track):
    response = sender_stand_request.get_order_info(track)
    assert response.status_code == 200

def test_order_info_by_track():
    response_order, saved_track = sender_stand_request.post_new_order(data.order_body)
    positive_assert_get_order_info(saved_track)

