import pytest
import allure
from selenium import webdriver
from pages.category_page import CategoryPage

@pytest.fixture
def  driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.epic("Каталог")
@allure.feature("Категории товаров")
@allure.story("Отображение товаров в категории")
def test_products_display_in_category(driver):
    category = CategoryPage(driver)
    category.open()
    category.click_category()
    with allure.step("Проверить, что товары отобразились"):
        assert category.get_products_count() > 0, "Товары в категории не найдены!"