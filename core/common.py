from time import time
from random import randint
from os import path, getcwd, mkdir
from datetime import datetime
from selenium.webdriver.common.by import By


class Common:
    @staticmethod
    def switch_to(func):
        """A decorator to ensure switching to iframe and back to main window."""
        def wrapper(*args, **kwargs):
            args[0].driver.switch_to.frame(args[0].driver.find_element(by=By.TAG_NAME, value="iframe"))
            func(*args, **kwargs)
            args[0].driver.switch_to.default_content()
        return wrapper


    @staticmethod
    def create_dir(name: str):
        """Create a directory
        Arguments:
            - name: name of the directory
        """
        cwd_path = path.abspath(getcwd())
        
        if not path.exists(f"{cwd_path}/{name}"):
            mkdir(f"{cwd_path}/{name}")


    @staticmethod
    def get_btn_id(btn_id: int, rnd: bool = False) -> int:
        """Returns button id.
        
        Arguments:
            - btn_id: button id
            - rnd: if True, returns a random button id from 1 to btn_id

        Example:
            >>> get_btn_id(btn_id=3, rnd=True) -> 1 or 2 or 3
            >>> get_btn_id(btn_id=3, rnd=False) -> 3
        """
        return randint(1, btn_id) if btn_id and rnd else btn_id


    @staticmethod
    def show_stats(bot_name: str, stats: dict):
        """Prints bot's stats."""
        tasks_time = [i[1] for i in stats['tasks']]
        # print(f"\n[{bot_name}] - Завершил работу\n")
        print(f'[{bot_name}] - Выполнено заданий: {len(stats["tasks"])}')
        print(f'[{bot_name}] - Время выполнения: {round(sum(tasks_time))} сек')
        print(f'[{bot_name}] - Максимальное время выполнения: {max(tasks_time)} сек')
        print(f'[{bot_name}] - Минимальное время выполнения: {min(tasks_time)} сек')
        print(f'[{bot_name}] - Среднее время выполнения: {round(sum(tasks_time) / len(tasks_time), 3)} сек')


    @staticmethod
    def write_log(task_name: str, bot_name: str, item: int, start: float = None):
        """Writes bot's stats to a file.
        
        Arguments:
            - task_name: str - name of the task [rb - log radio button, tt - log task time]
            - bot_name: str - name of the bot
            - item: int - task's item number
            - start: float - task's start time
        
        Example:
            >>> write_log(task_name='rb', bot_name="Bot", item=i)
            >>> [Bot][26.05.2022 15:46:58:335] - Radio Buttons для 1 задания загружены
            >>> write_log(task_name='tt', bot_name="Bot", item=item, start=start)
            >>> [Bot][26.05.2022 15:47:04:857] - Задание 1 выполнено
            >>> [Bot][26.05.2022 15:47:04:857] - Время выполнения: 6.545 сек
        """
        now = datetime.now()
        dt_string = now.strftime("%d.%m.%Y %H:%M:%S:%f")[:-3]
        date_string = now.strftime("%d.%m.%Y")

        with open(f"./logs/logs_{date_string}.log", 'a', encoding='utf-8') as f:
            if task_name == 'rb':
                f.write(f"[{bot_name}][{dt_string}] - Radio Buttons для {item} задания загружены\n")
            elif task_name == 'tt':
                f.write(f"[{bot_name}][{dt_string}] - Задание {item} выполнено\n")
                f.write(f"[{bot_name}][{dt_string}] - Время выполнения: {round(time() - start, 3)} сек\n")
    
    @staticmethod
    def color_log(msg: str, color: str) -> None:
        """Prints colored text.
        
        Arguments:
            - msg: str - text to print
            - color: str - color of the text [red or green]
        
        Example:
            >>> color_log("I'm red", "red")
        """
        CRED = '\33[31m'
        CGREEN = '\33[32m'
        CEND = '\033[0m'
        if color.lower() == 'red':
            print(CRED + msg + CEND)
        elif color.lower() == 'green':
            print(CGREEN + msg + CEND)
        else:
            print('The value must be "red" or "green"')