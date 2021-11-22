''' Intake a recipe-scrapers 13.3.5 object and modify it for use in TestMixer.
    Save newly created object instance to a shelve (for now).

    references:
        - https://pypi.org/project/recipe-scrapers/
        - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        - https://date_util.readthedocs.io/en/stable/index.html

'''


from . import _decorators as dec
from ..recipes import custom, scraper
import sys

PATH_RECIPES = 'C:\\Users\\rbcmp\\git\\MealMixer\\TestMixer\\recipes\\'


@dec.make_persistent
def get_scrapers_object(url='', wild_mode=False):
    ''' get a recipe-scrapers object given a url and return it'''

    scr = scraper.Scraper()
    return()

# @dec._add_recipe_attributes
# def _get_recipe_custom_object():

# @dec._add_recipe_attributes
# def _get_recipe_restaurant_object():
#     pass
#
def recipe_db_tools():
    # print(f'current recursion limit: {sys.getrecursionlimit()}')
    # sys.setrecursionlimit(3000)
    # print(f'current recursion limit: {sys.getrecursionlimit()}')
    # url = 'https://www.allrecipes.com/recipe/222183/wasabi-trout/'
    # scr = scrape_me(url, wild_mode=False)
    # del scr.soup
    # # print(f'\nremoved {scr.soup}')
    # with shelve.open('saved_recipes_d') as test_shelve:
    #     print('\nsaving the recipe')
    #     title = scr.title()
    #     test_shelve[title] = scr
    # print('\nthe recipe has been saved')

    # with shelve.open('saved_recipes_d') as test_shelve:
    #     print(f'\n{test_shelve}')
    #     obj = test_shelve[title]
    #     print(obj.title())

    print('\nthe recipe has been retrieved')


def main():

    # scr = _get_recipe_scrapers_object('https://www.allrecipes.com/recipe/12720/grilled-salmon-i/', True)
    # print(scr._timestamp_created_when)
    # print(scr._timestamp_log_usage)
    recipe_db_tools()


if __name__ == '__main__':
    main()

