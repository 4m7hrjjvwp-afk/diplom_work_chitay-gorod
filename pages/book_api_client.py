import requests
import allure

class BookApiClient:
    def __init__(self):
        self.base_url = "https://www.chitai-gorod.ru"
        self.books_endpoint = f"{self.base_url}/web/api/v2/search/facet-search?new_buttons_reserve=variant_0&customerCityId=47&phrase=шарлотта бронте"
   
    @allure.step("GET-запрос для поиска книг по автору")
    def get_books_by_author(self, author_name: str):
        payload = {"author": author_name}
        response = requests.get(self.books_endpoint, params=payload)
        return response