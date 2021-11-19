''' MealMixer Screen Manager (User Interface Core)

    author: Robert Camp (campR2)
    last modified: 11/11/2021
'''

from . import config
import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from os import listdir
from os.path import abspath, dirname, join
import random

# import additional Kivy classes and functionality written in Python
from . import kivy_py
import time

# import additonal .kv files
gi_path = abspath(dirname(__file__))
kv_path = join(gi_path, "kivy_kv")
for kv_file in listdir(kv_path):
    Builder.load_file(kv_path+"\\"+kv_file)

# Screen Backgrounds:
izzy_smile = join(gi_path, "media", "home_screen_izzy_smile.jpg")
potito_burrito = join(gi_path, "media", "meals_screen_potito_burrito.jpg")


class HomeScreen(Screen):
    home_screen_background = StringProperty(izzy_smile)
    meals_screen_background = StringProperty(potito_burrito)
    pass

class ColorScreen(Screen):
    color = ListProperty([1., 0., 0., 1.])

class ScManager(ScreenManager):
    pass

class MealMixerApp(App):
    # config settings to be added at a later date
    # def build_config(self, config):
    #     config.setdefaults('section1', {
    #         'key1': 'value1',
    #         'key2': '42'
    #     })

    def build(self):
        return ScManager()


# if __name__ == '__main__' or 'kivyApp':
#     print('not intended to be run as a stand alone module')
    # MealMixerApp().run()
