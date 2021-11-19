
'''house custom decorator functions

    references:
        - https://docs.python.org/3/howto/regex.html#regex-howto
        - https://docs.python.org/3/library/re.html?highlight=regular%20expressions
        - https://docs.python.org/3/library/shelve.html#module-shelve

'''

import shelve
import re
from tools import _util


def make_persistent(recipe):
    ''' add custom attributes to a new MealMixer recipe_object'''
    def wrap_func(*args, **kwargs):
        new_func = wrap_func
        new_recipe = recipe(*args, **kwargs)
        recipe_scrapers_regex_pattern = re.compile(r'<class \'recipe_scrapers\.')
        print(f'{new_recipe.title()}: was created in {new_func.__name__} ')

        if recipe_scrapers_regex_pattern.match(str(type(new_recipe))):

            add_attributes_new_recipe_scrapers(new_recipe)
        else:
            add_attributes_new_recipes(new_recipe)
        return(new_recipe)

    return (wrap_func)

def add_attributes_new_recipe_scrapers(new_recipe):
    ''''''
    new_recipe = _add_attributes_common(new_recipe)

    
    new_recipe = is_vegetarian(new_recipe)
    return(new_recipe)

def add_attributes_new_recipes(new_recipe):
    ''''''
    print('add_attributes_new_recipes')
    return(new_recipe)

def _add_attributes_common(new_recipe):
    ''''''
    new_recipe = tools__util._timestamp_recipe_new(new_recipe)
    new_recipe = tools__util._timestamp_recipe_used(new_recipe)



def is_vegetarian(new_recipe):
    ''''''
    meat_flags = [
                  'steak',
                  'beef',
                  ''
                 ]

def is_vegan(new_recipe):
    ''''''
    pass

def make_recipe_object_persistent(new_recipe):
    ''''''
    pass
