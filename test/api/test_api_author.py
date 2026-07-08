import allure
import pytest
from pages.book_api_client import BookApiClient

@pytest.fixture(scope="module")
def api_client():
    return BookApiClient()
@allure.epic("Каталог книг")
@allure.feature("Поиск")
@allure.story("Поиск книг по автору")
def test_search_books_by_author_success():
    with allure.step("Подготовка тестовых данных"):
        target_author = "Шарлотта Бронте"

    # Шаг: Отправляем запрос через  метод клиента
    response = api_client.get_books_by_author(target_author)
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200, f"Неверный статус-код: {response.status_code}"
    with allure.step("Прверка сруктуры JSON и соответствия найденных книг"):
        response_data = response.json()
        
        assert "books" in response_data, "В ответе отсутствует ключ 'books'"
        assert len(response_data["books"]) > 0, f"Книги автора {target_author} не найдены"
    for book in response_data["books"]:
        assert book["author"] == target_author, f"Ожидали автора {target_author}, но получили {book['author']}"


