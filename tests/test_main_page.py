import allure
import pytest

from data import answer_for_question, TestUrl
from pages.main_page import MainPage


class TestsMainPage:
    # Проверяем выпадающий список вопросы-ответы
    @allure.title('Проверяем выпадающий список вопросы-ответы')
    @pytest.mark.parametrize("question_id, expected_answer", answer_for_question.items())
    def test_check_answer_for_question(self, driver, question_id, expected_answer):
        main_page = MainPage(driver)
        main_page.open()  # Переход на главную страницу
        main_page.accept_cookie()
        assert main_page.get_answer_for_question(question_id) == expected_answer

    # Проверяем работу верхней кнопки Заказать
    @allure.title('Проверяем работу верхней кнопки Заказать')
    def test_click_order_button_up(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookie()
        main_page.click_order_button_up()
        assert main_page.is_order_page_opened()

    # Проверяем работу нижней кнопки Заказать
    @allure.title('Проверяем работу нижней кнопки Заказать')
    def test_click_order_button_down(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookie()
        main_page.scroll_to_order_button()
        main_page.click_order_button_down()
        assert main_page.is_order_page_opened()