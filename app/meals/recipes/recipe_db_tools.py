''' make a newly created recipe persistant accross sessions of MealMixer

    Author: Robert Camp (CampR2)
    Last Modified: 11/21/2021

'''

from ...meals import WM
import sqlite3
import pickle
import logging

class RecipeDBTools():
    """ save and retrieve a recipe """
    def __init__(self):
        super(RecipeDBTools, self).__init__()
        # path for universal locatin of the DB
        self.db_string = 'C:\\Users\\rbcmp\\apps\\meal-mixer\\app\\db\\_db\\meal-mixer.db'
        # get universal logger
        self.log = logging.getLogger('')
        self.construct_db()

    def construct_db(self):
        ''' create a db and load the appropriate tables if they don't exist'''
        try:
            recipe_db = sqlite3.connect(self.db_string)
            cur = recipe_db.cursor()
            cur.execute('''CREATE table recipes(id INTEGER PRIMARY KEY, name TEXT, recipe BLOB)''')
            recipe_db.commit()
            recipe_db.close()
        except Exception as exc:
            # self.log.debug('the DB is alreay in place')
            pass
        finally:
            recipe_db.close()

    def save_recipe(self, recipe):
        ''' make a recipe presistant accross sessions'''
        recipe_db = sqlite3.connect(self.db_string)
        bin_recipe = pickle.dumps(recipe, protocol=5)
        cur = recipe_db.cursor()
        cur.execute('''INSERT INTO recipes(name, recipe) VALUES(?, ?)''' , (recipe.name, bin_recipe))
        recipe_db.commit()
        recipe_db.close()
        # self.log.debug('recipe saved in meal-mixer.db')

    def get_recipe(self, recipe_name):
        ''' retrieve a recipe by name'''
        # I will need to come up with a better search method than just name
        # but for now that will do to get the ball rolling
        # possibly a mixture of name and ID. I could store a JSON file with the
        # names and matching IDs of the recipes that will make things more tidy
        # future
        recipe_db = sqlite3.connect(self.db_string)
        cur = recipe_db.cursor()
        meal = cur.execute('''SELECT * FROM recipes WHERE name = ?''', (recipe_name,))
        bfetch = meal.fetchall()[0][2]
        meal = pickle.loads(bfetch)
        recipe_db.close()

        # self.log.debug(ingstr.encode('utf-8'))
        # self.log.debug('the meal name after unpickling from the meal-mixer.db file %s' % (meal.name))

        return(meal)





