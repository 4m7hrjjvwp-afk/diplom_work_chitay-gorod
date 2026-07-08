import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.city_button = (By.CSS_SELECTOR, ".header-location")
        self.confirm_change_button = (By.CSS_SELECTOR, ".chg-app-button__content")
        self.city_list_modal = (By.CSS_SELECTOR, ".popular-cities__item")
        self.city_options_xpath = "//button[(@class, 'popular-cities__btn') and text()='{}']"
    
    @allure.step("Открыть главную страницу интернет-магазина")
    def open(self, url):
        self.driver.get(url)
     
    @allure.step("Нажать на кнопку города в шапке")
    def click_city_header_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.city_button))
        element.click()

    @allure.step("Нажать на кнопку 'Изменить город'")
    def click_change_city_confirmation(self):
        element = self.wait.until(EC.element_to_be_clickable(self.confirm_change_button))
        element.click()

    @allure.step("В появившемся списке нажать на кнопку с нужным городом")
    def select_city_from_list(self, city_name):
        city_locator = (By.XPATH, self.city_options_xpath.format(city_name))
        city_element = self.wait.until(EC.element_to_be_clickable(city_locator))
        city_element.click()

    @allure.step("Дождаться закрытия формы и убедиться в изменении")
    def wait_until_city_list_closes(self):
        self.wait.until(EC.invisibility_of_element_located(self.city_list_modal))    

