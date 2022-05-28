from os import environ, path
from dotenv import load_dotenv
from random import randint


basedir = path.abspath(path.dirname(__file__))
env_path = path.join(path.dirname(path.dirname(__file__)))
load_dotenv(path.join(env_path, ".env"))


# Get the environment variables
LOGIN = environ.get('LOGIN')
PASSWORD = environ.get('PASSWORD')
DRIVER_PATH = environ.get('DRIVER_PATH')

URL = "https://sandbox.toloka.yandex.ru/"

# Radio button id
radio_btn_id = randint(1, 3)

# Max number of tasks per page
tasks_number = 2