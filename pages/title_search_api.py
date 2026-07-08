import requests
import allure

class TitleSearchApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.search_endpoint = f"{self.base_url}/web/api/v2/search/facet-search?new_buttons_reserve=variant_0&customerCityId=47&phrase={'title'}"

    def search_books_by_title(self, title:str) -> requests.Response:
        with allure.step("Отправка запроса GET-запрос для поиска книг по названию"):
            params = {"title": title}
            response = requests.get(self.search_endpoint, params=params)
            return response
    