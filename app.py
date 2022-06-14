from os import walk
from modules.login import Login
from core.core import Bot
from core.exception import ValueOutOfRangeException
from core.common import Common
from threading import Thread


def get_files(dir_path: str):
    """Get a list of files from directory [dir_path].

    Arguments:
        - dir_path: directory path

    Returns: list with files names
    """
    files = []
    for data in walk(dir_path):
        files.extend(data)
    return files


def get_files_names(files_list: list) -> dict:
    """Get files names.
    
    Arguments: 
        - files_list: list with files names

    Returns: dict with files names or empty dict
    """
    if files_list:
        files = {idx + 1: name for idx, name in enumerate(files_list)}
    else:
        return {}
    return files


def show_cookies_names(cookies_names: dict) -> None:
    """Print cookies names.
    
    Arguments:
        - cookies_names: dict with cookies names
    """
    print(*[f"{idx}: {name}" for idx, name in cookies_names.items()], sep='\n')


def get_cookies_num(cookies_dict: dict) -> int:
    """Select the cookie number.
    
    Arguments:
        - cookies_dict: dict with cookies names
    """
    while True:
        try:
            num = int(input('Type the number of the cookie:\n'))
            if num > len(cookies_dict) or num < 1:
                raise ValueOutOfRangeException
            break
        except ValueError:
            Common.color_log("Invalid value.", "red")
            continue
        except ValueOutOfRangeException:
            Common.color_log("This value isn't in the list. Try again.", "red")
            continue
    return num


def set_tasks_number() -> int:
    """Set the number of tasks."""
    while True:
        try:
            tasks_number = int(input('Type the number of tasks:\n'))
            if tasks_number > 100 or tasks_number < 1:
                raise ValueOutOfRangeException
            break
        except ValueError:
            Common.color_log('Invalid value.', 'red')
            continue
        except ValueOutOfRangeException:
            Common.color_log("Out of range. Enter a number between 1 and 100.", "red")
            continue
    return tasks_number


def start_thread(cookies_path: str, bot_name: str, tasks_number: int) -> None:
    """Start thread with bot.

    Arguments:
        - cookies_path: path to the cookie
        - bot_name: name of the bot
        - tasks_number: number of tasks
    """
    bot_thread = Thread(target=Bot, args=(cookies_path, bot_name, tasks_number))
    bot_thread.start()
    bot_thread.join(timeout=30)
    return None


def run_bot() -> None:
    """Run the bot."""
    if cookies_names := get_files_names(files_list=get_files('./cookies')[2]):
        show_cookies_names(cookies_names=cookies_names)
        num = get_cookies_num(cookies_dict=cookies_names)
        cookies_path = f'./cookies/{cookies_names[num]}' #  get the path to the cookie
        bot_name = input('Type the name of the bot:\n').title() #  set the name of the bot
        tasks_number = set_tasks_number() #  set the number of tasks
        Common.color_log(f'All ok. Starting {bot_name} bot...', 'green')
        start_thread(cookies_path=cookies_path, bot_name=bot_name, tasks_number=tasks_number)
    else:
        Common.color_log('No cookies found.\n', 'red')


def main():
    Common.create_dir(name='logs') #  Create directory for logs
    Common.create_dir(name='cookies') #  Create directory for cookies
    run = input('Type "login" to get cookies.\nType "run" to run the bot.\nType "exit" to exit.\n')
    while run != 'exit':
        if run == 'login':
            Login().login()
        elif run == 'run':
            run_bot()
        else:
            Common.color_log('Sorry, I didn\'t understand that.\n', 'red')

        run = input('Type "login" to get cookies.\nType "run" to run the bot.\nType "exit" to exit.\n')


if __name__ == '__main__':
    main()
