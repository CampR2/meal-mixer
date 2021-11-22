''' test the ability of sqlite to hold recipe objects

    ***CONFIRMED***

    author: Robert Camp (CampR2)
    last modified: 11/21/2021

'''


from ...meals import WM
import sqlite3
import pickle
import logging


class SaveBlob():
    """ save a meal-mixer scraper object in a db and retrieve it"""
    def __init__(self):
        super(SaveBlob, self).__init__()
        # path for universal locatin of the DB
        self.db_string = 'C:\\Users\\rbcmp\\apps\\meal-mixer\\app\\db\\_db\\meal-mixer.db'
        # get universal logger
        self.dlog = logging.getLogger('debug')
        #webmeal object imported from meals for testing only (this should not be done in production)
        self.recipe = WM('https://cookieandkate.com/apple-steel-cut-oatmeal-recipe/')
        try:
            self.dlog.debug('the recipe name before pickling %s' % (self.recipe.name))
        except UnicodeEncodeError as uee:
            pass
        # searilize a recipe object after it has been sanitized
        self.bin_recipe = pickle.dumps(self.recipe, protocol=5)
        self.construct_db()
        self.recipe_db_tools()
        self.get_recipe()


    def construct_db(self):
        ''' create a db and load the appropriate tables if they don't exist'''
        try:
            recipe_db = sqlite3.connect(self.db_string)
            cur = recipe_db.cursor()
            cur.execute('''CREATE table recipes(id INTEGER PRIMARY KEY, name TEXT, recipe BLOB)''')
            recipe_db.commit()
            recipe_db.close()
        except Exception as exc:
            self.dlog.debug('the DB is alreay in place')
            pass
        finally:
            recipe_db.close()

    def recipe_db_tools(self):
        ''' make a recipe presistant accross sessions'''
        recipe_db = sqlite3.connect(self.db_string)
        cur = recipe_db.cursor()
        cur.execute('''INSERT INTO recipes(name, recipe) VALUES(?, ?)''',(self.recipe.name, self.bin_recipe))
        recipe_db.commit()
        recipe_db.close()
        self.dlog.debug('recipe saved in meal-mixer.db')

    def get_recipe(self):
        ''' retrieve a recipe after it has been saved'''
        recipe_db = sqlite3.connect(self.db_string)
        cur = recipe_db.cursor()
        meal = cur.execute('''SELECT * from recipes''')
        bfetch = meal.fetchall()[0][2]
        meal = pickle.loads(bfetch)

        recipe_db.close()
        ingstr = str(meal.ingredients)

        self.dlog.debug(ingstr.encode('utf-8'))
        self.dlog.debug('the meal name after unpickling from the meal-mixer.db file %s' % (meal.name))





