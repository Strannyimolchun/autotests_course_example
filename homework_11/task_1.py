# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# site = 'https://sbis.ru/'
# sbis_head = '[class="sbisru-Header__menu-link sbisru-Header__menu-link--hover"]'
# sbis_contacts = '.sbisru-Header__container [href="/contacts"]'
# sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'


driver = webdriver.Chrome()

try:
    # Перейти на https://sbis.ru/
    driver.maximize_window()
    driver.get('https://sbis.ru/')
    assert driver.current_url == 'https://sbis.ru/', 'Неверный url'
    assert driver.title == 'СБИС — экосистема для бизнеса: учет, управление и коммуникации', 'Неверный заголовок сайта'
    tabs = driver.find_elements(By.CSS_SELECTOR, '[class="sbisru-Header__menu-link sbisru-Header__menu-link--hover"]')
    assert len(tabs) == 3, 'Неправильное количество кнопок'

    # Перейти в раздел "Контакты"
    tab = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__container [href="/contacts"]')
    assert tab.text == 'Контакты', 'Неправильный текст кнопки'
    assert tab.is_displayed(), 'Кнопка не отображается'
    tab.click()

    # Найти баннер Тензор, кликнуть по нему
    sleep(2)
    banner = driver.find_element(By.CSS_SELECTOR,
                                 '[src="/resources/NewDesign/pages/Contacts/images/logo.svg?x_module=23.3206-53"]')
    assert banner.is_displayed(), 'Баннер не отображается'
    banner.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/'

    # Проверить, что есть блок новости "Сила в людях"
    sleep(2)
    news = driver.find_element(By.CSS_SELECTOR,
                               '[class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"] '
                               '[class="tensor_ru-Index__card-title tensor_ru-pb-16"]')
    assert news.text == 'Сила в людях', 'Нет заголовка "Сила в людях"'

    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    btn_read_more = driver.find_element(By.CSS_SELECTOR,
                                        '[class="s-Grid-col s-Grid-col--6 s-Grid-col--sm12"] '
                                        '[class ="tensor_ru-link tensor_ru-Index__link"]')
    btn_read_more.location_once_scrolled_into_view
    assert btn_read_more.text == 'Подробнее', 'Название кнопки не "Подробнее"'
    btn_read_more.click()
    sleep(3)
    assert driver.current_url == 'https://tensor.ru/about', 'Неправильная ссылка'

finally:
    driver.close()
