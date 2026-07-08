import requests
import allure

class ProductApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.product_url = f"{self.base_url}web/api/v1/products/slug"

    @allure.step("Просмотр карточки товара по ID")
    def get_product_by_id(self, title: str, product_id: int) -> requests.Response:
        url = f"{self.product_url}/{title}/{product_id}"
        response = requests.get(url)
        return response
