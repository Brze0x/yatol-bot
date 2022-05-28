import pickle
from time import sleep
from core.tasks import TwoPic
from modules.elements import Elements
from modules.config import URL, DRIVER_PATH
from core.common import Common
from core.exception import ValueOutOfRangeException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Bot:
    def __init__(self, cookies_path: str, bot_name: str, tasks_number: int):
        self.url = URL
        self.stats = {}
        self.bot_name = bot_name
        self.tasks_number = tasks_number
        self.cookies_path = cookies_path
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.run(self.url)


    def make_random_click(self):
        """Makes a random click on the page."""
        ac = ActionChains(self.driver)
        ac.click().perform()


    def set_cookies(self):
        """Sets a cookie from the file to your current session."""
        with open(self.cookies_path, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    
    def get_tasks(self) -> tuple[dict, list[WebElement]]:
        """Returns a list of tasks and their names."""
        task_names = {}
        
        snipets = self.driver.find_element(by=By.CLASS_NAME, value=Elements.snipets)
        tasks = snipets.find_elements(by=By.CLASS_NAME, value=Elements.snippet)

        for idx, task in enumerate(tasks):
            task_names[idx + 1] = task.find_element(by=By.CLASS_NAME, value=Elements.snippet_title).text
        
        return task_names, tasks


    def show_tasks_list(self, task_names: dict):
        """Print tasks names.
        
        Arguments:
        task_names: dict with tasks names
        """
        print(*[f"{task}: {task_names[task]}" for task in task_names], sep='\n')


    def choose_task(self, tasks: list[WebElement]):
        """Chooses a task from the list.
        
        Arguments:
        tasks: list of tasks[WebElement]
        """
        try:
            task_id = int(input('Type the task number you want to run: '))
            if task_id > len(tasks) or task_id < 1:
                raise ValueOutOfRangeException
        except ValueError:
            Common.color_log("Invalid value.", "red")
            self.choose_task(tasks)
        except ValueOutOfRangeException:
            Common.color_log("This task number isn't on the list. Try again.", "red")
            self.choose_task(tasks)
        else:
            tasks[task_id - 1].find_element(by=By.CLASS_NAME, value=Elements.start_btn).click()


    def run(self, url: str):
        self.stats['tasks'] = []
        two_pic = TwoPic(driver=self.driver, stats=self.stats)

        self.driver.get(url)
        sleep(1)
        self.set_cookies()
        sleep(1)
        self.driver.refresh()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Elements.warning_btn))).click()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, Elements.new_first)))

        task_names, tasks = self.get_tasks()
        self.show_tasks_list(task_names)
        self.choose_task(tasks)

        Common.color_log(f'\n[{self.bot_name}] - Got to work\n', 'green')
        
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Elements.submit_btn)))

        sleep(3)
        
        two_pic.run(tasks_number=self.tasks_number, bot_name=self.bot_name)

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Elements.out_btn))).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Elements.out_btn_confirm))).click()

        sleep(5)

        Common.color_log(f'\n[{self.bot_name}] - Finished the work\n', 'green')
        Common.show_stats(bot_name=self.bot_name, stats=self.stats)

        self.make_random_click()
        self.driver.quit()
