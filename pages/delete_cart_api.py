import requests
import allure

class CartApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.cart_url = f"{self.base_url}web/api/v1/cart"

    @allure.epic("Каталог книг")
    @allure.feature("Корзина")
    @allure.story("Удаление товара из корзины")
    def delete_to_cart(self, product_id: int):
        with allure.step("Удаление конкретного товара из корзины"):
            url = f"{self.cart_url}/items/{product_id}"
            
            response = requests.delete(url)
            return response