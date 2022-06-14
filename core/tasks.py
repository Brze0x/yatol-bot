from time import time, sleep
from core.common import Common
from modules.elements import Elements
from modules.config import tasks_number, radio_btn_id, random_btn
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException


class TwoPic:
    def __init__(self, driver: WebDriver, stats: dict):
        self.driver = driver
        self.stats = stats


    @Common.switch_to
    def click_radio_btn(self, page: int, bot_name: str):
        """Get the radio button from the page and click it

        Arguments:
            - page: select 3 for the first or 2 for others pages
        """
        for i in range(1, tasks_number + 1): 
            try:
                Common.write_log(task_name='rb', bot_name=bot_name, item=i)
                x_path = Elements.get_radio_btn(task_id=i, page=page, btn_id=Common.get_btn_id(btn_id=radio_btn_id, rnd=random_btn))
                WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, x_path))).click()
            except (NoSuchElementException):
                print('Ошибка: NoSuchElementException')
                continue
            except (ElementClickInterceptedException):
                print('Ошибка: ElementClickInterceptedException')
                continue
            except (TimeoutException):
                print('Ошибка: TimeoutException')
                continue


    def run(self, tasks_number: int, bot_name: str):
        """Runs the task"""
        for item in range(1, tasks_number + 1):
            start = time()
            if item == 1:
                self.click_radio_btn(page=3, bot_name=bot_name)
            else:
                self.click_radio_btn(page=2, bot_name=bot_name)
            self.driver.find_element(by=By.XPATH, value=Elements.submit_btn).click()
            sleep(1)
            WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located((By.CLASS_NAME, Elements.spinner_overlay)))
            self.stats['tasks'].append((item, round(time() - start, 3)))
            Common.write_log(task_name='tt', bot_name=bot_name, item=item, start=start)


class EmptyField:
    def __init__(self, driver: WebDriver, stats: dict):
        self.driver = driver
        self.stats = stats


    @Common.switch_to
    def click_radio_btn(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, Elements.yes_btn))).click()


    @Common.switch_to
    def click_quality_bar(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, Elements.page_quality_bar))).click()


    def run(self, tasks_number: int, bot_name: str):
        """Runs the task"""
        for item in range(1, tasks_number + 1):
            start = time()
            self.click_radio_btn()
            self.click_quality_bar()
            self.driver.find_element(by=By.XPATH, value=Elements.submit_btn).click()
            sleep(1)
            WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located((By.CLASS_NAME, Elements.spinner_overlay)))
            self.stats['tasks'].append((item, round(time() - start, 3)))
            Common.write_log(task_name='tt', bot_name=bot_name, item=item, start=start)