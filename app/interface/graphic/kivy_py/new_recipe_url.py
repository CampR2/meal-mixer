from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
import logging
from app import meals

Builder.load_string('''
<NewRecipeURL>:
    name: 'new_recipe_url'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation:'horizontal'
            BoxLayout:
                id: pic_box
                canvas:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source:root.manager.get_screen('home').meals_screen_background
            BoxLayout:
                orientation:'vertical'
                Button:
                    text: 'New Meal'
                    font_size: 30
                    opacity: 1
                    on_release: app.root.current = 'new_recipe'
                Button:
                    text: 'Edit Meal'
                    font_size: 30
                    opacity: 1
                    on_release: app.root.new_color_screen()

        TextInput:
            id: url_input
            # canvas.before:
            #     Color:
            #         rgba: [1,0,0,.0]
            #     Rectangle:
            #         pos: self.pos
            #         size: self.size
            focus: True
            write_tab: False
            multiline: False
            on_text_validate: root.get_url_meal()
            text_size: self.width, None
            font_size: 30
            size_hint: 1, None
            text: root.start_text

    ''')

class NewRecipeURL(Screen):
    """docstring for NewRecipeURL"""
    meal = ObjectProperty(None)
    start_text = StringProperty('Type the Web Address Here')

    def __init__(self, **kwargs):
        super(NewRecipeURL, self).__init__(**kwargs)
        self.log = logging.getLogger('root')

    def get_url_meal(self):
        ''''''

        url = self.ids['url_input'].text
        ''' later functionality: this could be made to handle more than one
          url pull at a time url can become urls below and it can be a list
            of urls instead of a single one. I can then loop through the list
            there will need to be a more flexible way to account for bad URLs
            end
        '''
        self.log.info(f'this is the url: {url}')
        self.meal = meals.WM(url)
        if self.meal.name == 'base':
            self.ids['url_input'].text = 'There was something wrong with the \
address you entered.\nPlease try again.'
        else:
            self.ids['url_input'].text = f'{self.meal.name} imported successfully from\n \
URL: {url}'
            Clock.schedule_once(self.reset_text, 4)

    def reset_text(self, dt):
        self.ids['url_input'].text ='Type the Web Address Here'
