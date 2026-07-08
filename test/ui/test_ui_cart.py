import pytest
import allure
from selenium import webdriver
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.epic("Корзина")
@allure.feature("Управление количество товара")
@allure.story("Изменение количества товара кнопками плюс и минус")
def test_full_cart_quantity_flow(driver):
    cart = CartPage(driver)

    cart.open()
    cart.add_product_to_cart()
    cart.go_to_cart()
    
    cart.increase_quantity()
    cart.wait_for_quantity_to_be(2)
    
    cart.decrease_quantity()
    cart.wait_for_quantity_to_be(1)
    
    final_quantity = cart.get_current_quantity()
    with allure.step("Проверить, что итоговое количество товарав корзине равно 1"):
        assert final_quantity == 1, f"Количество товара не совпадает! На экране: {final_quantity} "