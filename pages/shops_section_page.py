import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class ShopsSectionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    shops_button = (By.CSS_SELECTOR, "a[href='/shops']")
    show_list_button = (By.CSS_SELECTOR, "div.yandex-map-list-points-header__list-header")

    @allure.step("Открыть главную страницу интернет-магазина")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Открыть раздел 'Магазины' в шапке главной страницы")
    def click_shops_in_header(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.shops_button))
        btn.click()

    @allure.step("Нажать кнопку 'Показать списком'")
    def click_show_as_list(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.show_list_button))
        btn.click()

    @allure.step("Найти интересующий адрес")
    def select_shop_by_address(self, address: str):
        self.wait.until(EC.presence_of_element_to_be_clickable(self._get_shop_row_xpath(address)))
        to_shop_button = self.wait.until(EC.element_to_be_clickable(self._get_to_shop_button_xpath(address)))
        to_shop_button.click()

    @allure.step("Нажать кнопку 'В магазин'")
    def wait_for_shop_page_load(self):
        return self.wait.until(EC.url_contains("/shops/"))