import abc

from markup.markup import Keyboards
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):
    """Инициализируем бота, разметку кнопок, менеджер для работы с БД"""

    def __init__(self, bot):
        self.bot = bot
        self.keybords = Keyboards()
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
