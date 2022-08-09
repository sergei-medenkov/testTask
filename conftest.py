from html_object_list import tests_dir
import pytest
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import os
import allure
from time import sleep

screenshot_dir = f"{tests_dir}/failures/"
step_name = allure.step


def pytest_addoption(parser):
    """PyTest method for adding custom console parameters"""
    parser.addoption("--driver_conf", action="store", default='chrome edge local', type=str,
                     help="Set additional value for driver version setup")


@pytest.fixture(scope="session")
def driver_conf(request):
    """Handler for --driver_conf parameter"""
    # return "chrome local show"
    return request.config.getoption("--driver_conf")


# add browser to 'params' list, it's run tests in each browser
@pytest.fixture(scope="class")
def driver(request, driver_conf):
    try:
        driver_conf = os.environ["pycharm_driver_conf"]
    except:
        pass

    if 'edge' in driver_conf:
        options = webdriver.EdgeOptions()
        if 'show' not in driver_conf:
            options.add_argument('--headless')

        web_driver = webdriver.Edge(options=options,
                                    service=EdgeService(EdgeChromiumDriverManager().install()))

    if 'chrome' in driver_conf:
        options = webdriver.ChromeOptions()
        if 'show' not in driver_conf:
            options.add_argument('--headless')

        web_driver = webdriver.Chrome(
            options=options,
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    web_driver.maximize_window()
    request.addfinalizer(web_driver.quit)  # Finish after all test
    return web_driver


@pytest.fixture()
def waiter(driver):
    def __waiter(page_object, wait=8):
        start_time = datetime.now()
        while (datetime.now() - start_time).seconds < wait:
            try:
                web_element = \
                    WebDriverWait(driver, wait).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, page_object)))
                return web_element
            except:
                sleep(0.05)
        pytest.fail('No such element')
    return __waiter


@pytest.fixture()
def clicker(driver, waiter):
    def page_object_click(page_object):
        element = waiter(page_object)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            ActionChains(driver).click(element).perform()
        except:
            sleep(1)
            ActionChains(driver).click(element).perform()
    return page_object_click


@pytest.fixture()
def inputer(driver):
    def __input(input_data):
        ActionChains(driver).send_keys(Keys.DOWN).send_keys(input_data).perform()
    return __input
