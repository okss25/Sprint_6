import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # поиск элемента
    @allure.title('Ищем элемент на странице')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # кликает по элементу
    @allure.title('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    # добавляет текст в элемент
    @allure.title('Добавляем текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # получает текст элемента
    @allure.title('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # прокручивает страницу до элемента
    @allure.title('Пролистываем страницу до элемента')
    def scroll_for_element(self, name_element):
        self.driver.execute_script("arguments[0].scrollIntoView();", name_element)

    # переход между вкладками
    @allure.title('Переходим на последнюю открывшуюся вкладку')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # форматируем локаторы
    def format_locators(self, locator_1, question_id):
        method, locator = locator_1
        locator = locator.format(question_id)

        return (method, locator)