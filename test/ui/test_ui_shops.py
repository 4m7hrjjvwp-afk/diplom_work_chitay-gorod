import pytest
import allure
from selenium import webdriver
from pages.shops_section_page import ShopsSectionPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.epic("Главная страница интернет-магазина")
@allure.feature("Раздел 'Магазины'")
@allure.story("Проверка наличия адреса магазина в разделе")
def test_find_shop_address(driver): # Проверка наличия адреса магазина в разделе “Магазины”
    shops_section_page = ShopsSectionPage(driver)
    shops_section_page.open()
    shops_section_page.click_shops_in_header()
    shops_section_page.click_show_as_list()
    target_address = "603123, г. Нижний Новгород, Южное ш, д. 2 Г, ТРЦ 'Крымъ', 3 этаж"
    shops_section_page.select_shop_by_address(target_address)
    shops_section_page.wait_for_shop_page_load()

    with allure.step("Проверка URL магазина"):
        current_url = driver.current_url
        assert "chitai-gorod.ru/shops/" in current_url, f"Неверный URL после клика: {current_url}"
        
        shop_id = current_url.split("/shops/")[-1]
        assert shop_id.isdigit(), f"в конце URL не найден ID магазина: {current_url}"