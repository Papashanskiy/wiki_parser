from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from os import getenv
import csv


def get_random_article(unm: str, pwd: str) -> str:
    """
    This function login in Wikipedia https://ru.wikipedia.org/ than find and return url of random article.
    :param unm: username from environ
    :param pwd: password from environ
    :return: url of random article
    """
    service = Service('C:\\Users\\apashanskii.dr\\chrome\\chromedriver.exe')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('https://ru.wikipedia.org/')
    driver.find_element_by_link_text('Войти' or 'Log in').click()
    elem_unm = driver.find_element_by_id('wpName1')
    elem_pwd = driver.find_element_by_id('wpPassword1')
    elem_unm.send_keys(unm)
    elem_pwd.send_keys(pwd)
    elem_unm.send_keys(Keys.RETURN)
    driver.find_element_by_link_text('Случайная статья' or 'Random article').click()
    url = str(driver.current_url)
    driver.quit()
    return url


if __name__ == '__main__':
    unm, pwd = (getenv('UNM'), getenv('PWD'))
    print(get_random_article(unm, pwd))
