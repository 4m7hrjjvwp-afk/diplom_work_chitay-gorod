import pytest
import requests
import allure
from pages.delete_cart_api import CartApi

@pytest.fixture
def cart_api():
    base_url = "https://www.chitai-gorod.ru"
    return CartApi(base_url)

@allure.epic("Каталог книг")
@allure.feature("Корзина")
@allure.story("Поиск книг по названию")
def test_delete_product_to_cart(cart_api):
    with allure.step("Подготовка и ввод тестовых данных"):
        target_product_id = 26619190
        
        add_payload = {"product_id": target_product_id,}
        requests.post(f"{cart_api.base_url}/web/api/v1/cart/product", json=add_payload)

    with allure.step("Выполнение DELETE-запрос"):
        response = cart_api.delete_to_cart(product_id=target_product_id)
    with allure.step("Проверка статус-кода"):
        assert response.status_code, f"Код ответа {response.status_code} вместо 200/204"
    with allure.step("Проверка cтруктуры JSON и что товара больше нет в корзинt"):
        if response.status_code ==200 and response.text:
            cart_data = response.json()
            assert "items" in cart_data, "В ответе корзины отсутствует список 'items'"
            item_ids = [item["product_i"] for item in cart_data["items"]]
            assert target_product_id not in item_ids, f"Товар {target_product_id} все еще остался в корзине"

