import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class CategoryPage:
    URL = "https://www.chitai-gorod.ru"
    category_link = (By.CSS_SELECTOR, "a[href='/novelty']")
    product_cards = (By.CSS_SELECTOR, ".product_card")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу интернет-магазина")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Перейти в категорию 'Новинки'")
    def click_category(self):
        self.wait.until(EC.element_to_be_clickable(self.category_link)).click()

    @allure.step("Посмотреть все товары в категории 'Новинки'")
    def get_products_count(self):
        products = self.wait.until(EC.presence_of_all_elements_located(self.product_cards))
        return len(products)