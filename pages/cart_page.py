import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class CartPage:
    url = "https://www.chitai-gorod.ru"
    add_to_cart_button = (By.CSS_SELECTOR, "[data-testid-button-mini-product-card='canBuy']")
    cart_badge = (By.CSS_SELECTOR, "[data-testid-indicator-header='cartCounter']")
    cart_header_button = (By.CSS_SELECTOR, "button.header-controls__btn")
    plus_button = (By.CSS_SELECTOR, "[data-testid-button-cart='increment']")
    minus_button = (By.CSS_SELECTOR, "[data-testid-button-cart='decrement']")
    quantity_input = (By.CSS_SELECTOR, "input.cart-quantity-input")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть главную страницу интернет-магазина")    
    def open(self):
        self.driver.get(self.url)
    
    @allure.step("Добавить товар в корзину")
    def add_product_to_cart(self):
        with allure.step("Нажать кнопку 'Купить'"):
            self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button)).click()
        with allure.step("Дождаться появления цифры '1' на индикаторе корзины"):
            self.wait.until(EC.text_to_be_present_in_element(self.cart_badge, "1"))

    @allure.step("Перейти в корзину кликом по индикатору в шапке страницы")
    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_header_button)).click

    @allure.step("Увеличить количество товаров(нажать на '+')")
    def increase_quantity(self):
        self.wait.until(EC.element_to_be_clickable(self.plus_button)).click

    @allure.step("Уменьшить количество товаров(нажать на '-')")
    def decrease_quantity(self):
        self.wait.until(EC.element_to_be_clickable(self.minus_button)).click
    
    @allure.step("Дождаться, пока количество товаров в корзине станет равным {expected_count}")
    def wait_for_quantity_to_be(self, expected_count):
        self.wait.until(EC.text_to_be_present_in_element_value(self.quantity_input, str(expected_count)))

    @allure.step("Получить текущее количество товаров с экрана")
    def get_current_quantity(self):
        element = self.wait.until(EC.presence_of_element_located(self.quantity_input))
        quantity = int(element.get_attribute("value"))
        allure.attach(str(quantity), name="Текущее количество", attachment_type=allure.attachment_type.TEXT)
        return quantity
    

