import pytest
import allure
from pages.product_api import ProductApi

@pytest.fixture
def product_api():
    base_url = "https://www.chitai-gorod.ru"
    return ProductApi(base_url)

@allure.epic("Каталог книг")
@allure.feature("Карточка товара")
@allure.story("Проверка карточки товара")
def test_get_product_card(product_api):
    with allure.step("Подготовка тестовых данных"):
        target_product_id = 2661990
        expected_title = "Мозг. Ваша личная история"
    with allure.step("Вызов метода API"):
        response = product_api.get_product_by_id(target_product_id)
    with allure.step("Проверка статус-кода"):
        assert response.staus_code == 200, f"Код ответа {response.status_code} вместо 200"
    with allure.step("Проверка cтруктуры JSON и обязательных полей в карточке найденной книги"):
        product_data = response.json()
        assert "id" in product_data, "В карточке товара отсутствеут поле 'id'"
        assert product_data["id"] == target_product_id, "ID товара в ответет не совпадает с запошенным"
        assert "title" in product_data, "В карточке товара отсутствует поле 'title'"
        assert product_data["title"] == expected_title, f"Ожидалось название '{expected_title}', пришло '{product_data['title']}'"
        assert "price" in product_data, "В карточке товара отсутствует поле 'price'"
        assert product_data["price"] > 0, "Цена товара должна быть больше нуля"
        assert "in_stock" in product_data, "В карточке товара отсутствует статус наличия 'in_stock'"