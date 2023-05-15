import allure
from selene.support import by
from selene.support.conditions import be
from selene import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


#1. Чистый Selene (без шагов)
def test_default():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').type('eroshenkoam/allure-example')
    s('.header-search-input').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text("#81")).should(be.visible)


#2. Лямбда шаги через with allure.step
def test_lambda():
    with allure.step("Открываем главную страницу"):
        browser.config.window_width = 1600
        browser.config.window_height = 900
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий"):
        s('.header-search-input').click()
        s('.header-search-input').type('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем таб Issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issues с номером 81"):
        s(by.partial_text("#81")).should(be.visible)


#3. Шаги с декоратором @allure.step
def test_decorator():
    open_main_page()
    search_for_repoditory('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('81')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.open('https://github.com')


@allure.step("Ищем репозиторий {repo}")
def search_for_repoditory(repo):
    s('.header-search-input').click()
    s('.header-search-input').type(repo)
    s('.header-search-input').submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s('#issues-tab').click()


@allure.step("Проверяем наличие Issues с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text("#" + number)).should(be.visible)


#4. Аннотации
def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Vitalll')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass