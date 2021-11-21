'''test the ability of sqlite to hold recipe objects'''


from app.meals import WM
import sqlite3
import pickle
import logging
import locale


class SaveBlob():
    """docstring for SaveBlob"""
    def __init__(self):
        super(SaveBlob, self).__init__()
        self.dlog = logging.getLogger('debug')
        self.recipe = WM(
        'https://cookieandkate.com/apple-steel-cut-oatmeal-recipe/')
        try:
            print(self.recipe.ingredients)
        except UnicodeEncodeError as uee:
            pass
        self.bin_recipe = pickle.dumps(self.recipe, protocol=5)
        self.construct_db()
        self.save_recipe()
        self.get_recipe()


    def construct_db(self):
        try:
            recipe_db = sqlite3.connect('.\meal-mixer.db')
            cur = recipe_db.cursor()
            cur.execute('''CREATE table recipes(id INTEGER PRIMARY KEY, name TEXT, recipe BLOB)''')
            recipe_db.commit()
            recipe_db.close()
        except Exception as exc:
            pass
        finally:
            recipe_db.close()

    def save_recipe(self):
        recipe_db = sqlite3.connect('meal-mixer.db')
        cur = recipe_db.cursor()
        cur.execute('''INSERT INTO recipes(name, recipe) VALUES(?, ?)''',(self.recipe.name, self.bin_recipe))
        recipe_db.commit()
        recipe_db.close()

    def get_recipe(self):
        recipe_db = sqlite3.connect('meal-mixer.db')
        cur = recipe_db.cursor()
        meal = cur.execute('''SELECT * from recipes''')
        bfetch = meal.fetchall()[0][2]
        meal = pickle.loads(bfetch)

        recipe_db.close()
        ingstr = str(meal.ingredients)

        print(ingstr.encode('utf-8'))
        print(meal.name)
        meal.name = 'new new'
        print(meal.name)





