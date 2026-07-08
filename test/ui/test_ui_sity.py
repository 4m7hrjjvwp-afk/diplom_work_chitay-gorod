import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.epic("Главная страница интернет-магазина")
@allure.feature("Геолокация пользователя")
@allure.story("Изменение города")
def test_change_city_in_bookstore(driver): 
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_city_header_button()
    main_page.click_change_city_confirmation()
    target_city = "Нижний Новгород"
    main_page.select_city_from_list(target_city)
    main_page.wait.until_city_lict_closes()

    with allure.step("Проверить, что в шапка отображается выбранный город"):
        actual_city = main_page.get_current_city_text()
        assert actual_city == target_city