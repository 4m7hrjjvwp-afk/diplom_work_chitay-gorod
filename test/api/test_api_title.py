import allure
import pytest
from pages.title_search_api import TitleSearchApi

base_url = "https://www.chitai-gorod.ru"

@pytest.fixture
def api():
    return TitleSearchApi(base_url)

@allure.epic("Каталог книг")
@allure.feature("Корзина")
@allure.story("Поиск книг по названию")
def test_search_books_by_title(api):
    with allure.step("Подготовка и ввод тестовых данных"):
        response = api.search_books_by_title("мозг. ваша личная история")
    with allure.step("Проверка статус-кода"):
        assert response.status_code ==200, "Ожидался статус-код 200"
    with allure.step("Проверка cтруктуры JSON и соответствия найденной книги"):
        data = response.json()
        assert len(data) > 0, "Список найденных книг пуст"
    
        first_book_title = data[0].get("title")
        assert "Мозг. Ваша личная история" in first_book_title
    