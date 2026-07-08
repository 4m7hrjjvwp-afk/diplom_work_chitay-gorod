import pytest
import allure
from pages.add_cart_api import CartApi

@pytest.fixture
def cart_api():
    base_url = "https://www.chitai-gorod.ru"
    return CartApi(base_url)

@allure.epic("Каталог книг")
@allure.feature("Корзина")
@allure.story("Добавление книги в корзину")
def test_add_product_to_cart(cart_api):
    with allure.step("Подготовка тестовых данных"):
        target_product_id = 2661990
    with allure.step("Выполнение POST-запроса"):
        response = cart_api.add_to_cart(product_id=target_product_id)
    with allure.step("Проверка статус-кода"):
        assert response.status_code, f"Код ответа {response.status_code} вместо 200/201"
    with allure.step("Проверка cтруктуры JSON и соответствия найденной книги"):
        cart_data = response.json()
        
        assert "items" in cart_data, "В ответе корзины отсутствует список 'items'"
        assert "total_price" in cart_data, "В ответе отсутствует общая стоимость 'total_price'"

    with allure.step("Проверка, что добавленная книга есть в списке"):
        added_item = None
        for item in cart_data["items"]:
            if item ["product_id"] == target_product_id:
                added_item = item
                break
        assert added_item is not None, f"Товар с ID {target_product_id} не найден в корзине"
