import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open(self):
        from data import TestUrl
        self.driver.get(TestUrl.MAIN_URL)  # использовать TestUrl.MAIN_URL

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.click_to_element(MainPageLocators.button_cookie)

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_order_button_up(self):
        self.click_to_element(MainPageLocators.order_button_up)

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_order_button_down(self):
        self.click_to_element(MainPageLocators.order_button_down)

    @allure.step('Проверка, что страница заказа открыта')
    def is_order_page_opened(self):
        # Предполагается, что у вас есть локатор для заголовка страницы заказа
        return self.is_element_visible(OrderPageLocators.title_order_page)

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainPageLocators.answer_locator, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(locator_answer)

    @allure.step('Проверяем ответ на вопрос')
    def check_answer_for_question(self, question_id):
        self.click_for_question(question_id)
        return self.get_answer_text(question_id)

    @allure.step('Прокручиваем страницу до последнего вопроса')
    def scroll_for_question_block(self):
        last_question = self.find_element_with_wait(MainPageLocators.question_locator_for_scroll)
        self.scroll_for_element(last_question)

    @allure.step('Клик на вопрос')
    def click_for_question(self, question_id):
        locator_question = self.format_locators(MainPageLocators.question_locator, question_id)
        self.scroll_for_question_block()
        self.click_to_element(locator_question)