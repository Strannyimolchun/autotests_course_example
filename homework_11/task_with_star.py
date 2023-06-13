# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path

# переопределяем настройки, чтобы скачать файл в нашу директорию и чтобы браузер не ругался на возможный вред файла
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"C:\autotests_course\homework_11", "safebrowsing.enabled": True}
chromeOptions.add_experimental_option("prefs", prefs)
chromedriver = r"C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=chromeOptions)

file_name = "sbisplugin-setup-web.exe"

try:
    # Перейти на  https://sbis.ru/
    driver.maximize_window()
    driver.get('https://sbis.ru/')
    sleep(1)

    # В Footer'e найти "Скачать СБИС" и перейти по ней
    download = driver.find_element(By.CSS_SELECTOR, '[href = "/download?tab=ereport&innerTab=ereport25"]')
    download.location_once_scrolled_into_view
    download.click()
    sleep(2)

    # выбрать вкладку 'СБИС Плагин'
    select_tab = driver.find_elements(By.CSS_SELECTOR, '[name="TabButtons"] [class="controls-tabButton__overlay"]')
    select_tab[1].click()
    sleep(1)

    # Скачать СБИС Плагин для вашей ОС в папку с данным тестом
    select_tab = driver.find_element(By.CSS_SELECTOR,
                                      '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    select_tab.click()
    sleep(10)

    # Убедиться, что плагин загрузился
    assert Path(file_name).is_file(), 'Файл не загружен'

    # Вывести на печать размер скачанного файла в мегабайтах
    print(f'Размер файла: {round(Path(file_name).stat().st_size / 1_048_576, 2)} Мбайт')
    sleep(5)

finally:
    Path.unlink(Path(file_name))
    driver.close()
