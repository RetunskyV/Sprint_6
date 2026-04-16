import pytest
import allure
from pages.main_page import MainPage


class TestQuestions:

    @allure.title("Проверка выпадающего текста для вопроса №{index}")
    @allure.description("При клике на стрелку вопроса открывается соответствующий текст ответа")
    @pytest.mark.parametrize("index", range(8))
    def test_question_dropdown(self, driver, index):
        main_page = MainPage(driver)

        with allure.step(f"Кликнуть на вопрос №{index + 1}"):
            main_page.click_question(index)

        with allure.step(f"Проверить, что ответ на вопрос №{index + 1} виден"):
            assert main_page.is_answer_visible(index), f"Ответ на вопрос №{index + 1} не отображается"

        with allure.step(f"Получить текст ответа на вопрос №{index + 1}"):
            answer_text = main_page.get_answer_text(index)

        with allure.step(f"Проверить, что текст ответа на вопрос №{index + 1} не пустой"):
            assert answer_text != "", f"Текст ответа на вопрос №{index + 1} пустой"