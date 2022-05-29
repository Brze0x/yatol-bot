from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
env_path = path.join(path.dirname(path.dirname(__file__)))
load_dotenv(path.join(env_path, ".env"))


# Get the environment variables
LOGIN = environ.get('LOGIN')
PASSWORD = environ.get('PASSWORD')
DRIVER_PATH = environ.get('DRIVER_PATH')

URL = "https://sandbox.toloka.yandex.ru/"


# Radio button id
radio_btn_id = 3

# If random_btn is False, then will be selected radio button with id = radio_btn_id
# If random_btn is True, then will be selected random radio button in range from 1 to radio_btn_id
random_btn = True

# Max number of tasks per page
tasks_number = 2