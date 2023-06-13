# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome()

try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    driver.maximize_window()
    driver.get('https://fix-online.sbis.ru/')
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    assert login.is_displayed(), 'Не отображается поле Логин'
    login.send_keys('lisa_alisa')
    login.send_keys(Keys.ENTER)
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name = "Password"]')
    password.send_keys('qazwsx123')
    go = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__signInButton"]')
    go.click()

    # Перейти в реестр Контакты
    sleep(1)
    driver.get('https://fix-online.sbis.ru/page/dialogs')

    # Отправить сообщение самому себе
    sleep(1)
    plus = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus.click()
    sleep(2)
    search_contact = driver.find_element(By.CSS_SELECTOR,
                                         '[templatename = "Addressee/popup:Stack"] .controls-Field')
    search_contact.send_keys('Лисичкина Алиса')
    sleep(1)
    search_contact = driver.find_elements(By.CSS_SELECTOR,
                                          '[templatename = "Addressee/popup:Stack"] .controls-ListView__itemContent')
    search_contact[0].click()
    sleep(1)
    message_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message_txt = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(20))
    message_field.send_keys(message_txt)
    sleep(1)
    send_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_message.click()

    # Убедиться, что сообщение появилось в реестре
    sleep(1)
    check_message = driver.find_elements(By.CSS_SELECTOR,
                                         '.msg-dialogs-detail__layout-content '
                                         '.controls-ListView__item_default .msg-entity-text')
    assert check_message[0].text == message_txt, 'Текст первого в списке сообщения не соответствует отправленному'

    # Удалить это сообщение и убедиться, что удалили
    message = driver.find_elements(By.CSS_SELECTOR,
                                   '.msg-dialogs-detail__layout-content .controls-ListView__item_default')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message[0])
    action_chains.perform()
    sleep(1)
    delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete.click()
    sleep(1)
    check_message = driver.find_elements(By.CSS_SELECTOR,
                                         '.msg-dialogs-detail__layout-content '
                                         '.controls-ListView__item_default .msg-entity-text')
    assert check_message[0].text != message_txt, 'Первое в списке сообщение не пропало после удаления'

finally:
    driver.close()
