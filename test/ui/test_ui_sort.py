import pytest
import allure
from selenium import webdriver
from pages.sort_page import SortPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.epic("Каталог товаров")
@allure.feature("Сортировка")
@allure.story("Сортировка товаров по возрастанию цены")
def test_products_sorting_by_price(driver):
    sort = SortPage(driver)

    sort.open()
    sort.open_category()
    sort.sort_by_price_low_to_high()
    actual_prices = sort.get_all_prices()
    with allure.step("Проверить, что цены отсортированны корректно(от меньшей к большей)"):
        expected_prices = sorted(actual_prices)
        assert actual_prices == expected_prices, f"Сортировка неверная! Ожидалось {expected_prices}, но получили {actual_prices}"