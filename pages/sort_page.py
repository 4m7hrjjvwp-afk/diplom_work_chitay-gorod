import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class SortPage:
    url = "https://www.chitai-gorod.ru"
    category_link = (By.CSS_SELECTOR, "a[href='/novelty']")
    sort_menu_button = (By.CSS_SELECTOR, "svg.app-catalog-sorting__icon")
    low_to_high_option = (By.CSS_SELECTOR, "[data-testing-item-sort-catalog='priceAsc']")
    product_prices = (By.CSS_SELECTOR, "span.product-mini-card-price product-card__price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу интернет-магазина")    
    def open(self):
        self.driver.get(self.url)

    @allure.step("Открыть страницу категории 'Новинки'")
    def open_category(self):
        self.wait.until(EC.element_to_be_clickable(self.category_link)).click()

    @allure.step("Выбрать сортировку 'Сначала дешевые'")
    def sort_by_price_low_to_high(self):
        with allure.step("Нажать на кнопку открытия меню сортировки"):
            self.wait.until(EC.element_to_be_clickable(self.sort_menu_button)).click()
        with allure.step("Выбрать вариант 'Сначала дешевые'"):
            self.wait.until(EC.element_to_be_clickable(self.low_to_high_option)).click()
   
    @allure.step("Собрать цены всех товаров со страницы") 
    def get_all_prices(self):
        price_elements = self.wait.until(EC.presence_of_all_elements_located(self.product_prices))

        prices = []
        for element in price_elements:
            text = (element.text
                    .replace("₽", "")
                    .replace("$", "")
                    .replace(" ", "")
                    .replace("\xa0", "")
                    .strip())
            if text:
                prices.append(float(text))
        return prices