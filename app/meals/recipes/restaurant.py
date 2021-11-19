'''base recipe object



'''

class Base_Recipe(object):
    """docstring for Base_Recipe"""
    def __init__(self, name: str,
                       ingredients: list[str],
                       instructions: list[str],
                       prep_time: int = -1,
                       cook_time: int = -1,
                       total_time: int = -1,
                       nutrients: dict = {str:str}):
        super(Base_Recipe, self).__init__()
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.nutrients = nutrients
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.total_time = total_time

