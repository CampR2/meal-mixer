''' a custom recipe object'''

from ..recipes.base import Base

class Custom(Base):
    """docstring for Custom"""
    def __init__(self):
        super(Custom, self).__init__()
        self._ingredients = []
        self._cook_time = int()
        self._prep_time = int()
        self._total_time = self._cook_time + self._prep_time
        self._nutrients = {}
        self._instructions = ''
        self._yields = ''



    @property
    def ingredients(self):
        return self._ingredients

    @property
    def cook_time(self):
        return self._cook_time

    @property
    def prep_time(self):
        return self._prep_time

    @property
    def total_time(self):
        return self._total_time

    @property
    def nutrients(self):
        return self._nutrients

    @property
    def instructions(self):
        return self._instructions

    @property
    def yields(self):
        return self._yields


