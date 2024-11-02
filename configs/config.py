from dataclasses import dataclass
from environs import Env

@dataclass
class Config:
    token: str
    logger_format: str
    parse_mode: str
    user_database_path: str
    words_database_path: str

def load():
    env = Env()
    env.read_env()

    return Config(token = env("TOKEN"),
                  logger_format="%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
                  parse_mode="HTML",
                  user_database_path=env("USER_DATABASE_PATH"),
                  words_database_path=env("WORDS_DATABASE_PATH"))
