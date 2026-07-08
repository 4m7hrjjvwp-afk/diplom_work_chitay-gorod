import pytest
import allure
import requests

base_url = "https://web-agr.chitai-gorod.ru"
my_headers = {"Authorization": "Bearer сюда пиши свой токен"}


@allure.epic("Каталог книг")
@allure.feature("Корзина")
@allure.story("Добавление книги в корзину, позитивный тест")
def test_add_product_to_cart():
    with allure.step("Подготовка тестовых данных"):
        target_product_id = 2661990
        payload = {"id": target_product_id}

    with allure.step("Выполнение POST-запроса"):
        response = requests.post(
            f"{base_url}/web/api/v1/cart/product",
            json=payload,
            headers=my_headers,
        )
    with allure.step("Проверка статус-кода"):
        assert (
            response.status_code == 200
        ), f"Код ответа {response.status_code} вместо 200"


@allure.epic("Каталог книг")
@allure.feature("Корзина")
@allure.story("Добавление книги в корзину, негативный тест")
def test_no_add_product_to_cart():
    with allure.step("Подготовка тестовых данных"):
        target_product_id = "fgrydhcb"
        payload = {"id": target_product_id}

    with allure.step("Выполнение POST-запроса"):
        response = requests.post(
            f"{base_url}/web/api/v1/cart/product",
            json=payload,
            headers=my_headers,
        )
    with allure.step("Проверка статус-кода"):
        assert (
            response.status_code == 400
        ), f"Код ответа {response.status_code} вместо 400 "


@allure.epic("Каталог книг")
@allure.feature("Корзина")
@allure.story("Удаление книги из корзины, позитивный тест")
def test_delete_product_to_cart():
    with allure.step("Подготовка тестовых данных"):
        target_product_id = 2661990
        cart_id = 279248809
        payload = {"id": target_product_id}

    with allure.step("Выполнение POST-запроса"):
        response = requests.post(
            f"{base_url}/web/api/v1/cart/product",
            json=payload,
            headers=my_headers,
        )
    with allure.step("Проверка статус-кода"):
        assert (
            response.status_code == 200
        ), f"Код ответа {response.status_code} вместо 200"
    with allure.step("Удаление товара из корзины"):
        response = requests.delete(
            f"{base_url}/web/api/v1/cart/product/{cart_id}", headers=my_headers
        )
        assert (
            response.status_code == 204
        ), f"Код ответа {response.status_code} вместо 204"


@allure.epic("Каталог книг")
@allure.feature("Поиск")
@allure.story("Поиск книг по автору")
def test_search_product_author():
    with allure.step("Подготовка тестовых данных"):
        author = "Кинг"

    with allure.step("Выполнение GET-запроса"):
        response = requests.get(
            f"{base_url}/web/api/v2/search/facet-search?customerCityId=213&phrase={author}",
            headers=my_headers,
        )
    with allure.step("Проверка статус-кода"):
        assert (
            response.status_code == 200
        ), f"Код ответа {response.status_code} вместо 200"
    with allure.step("Проверка наличия автора в результатах"):
        assert author in response.text
