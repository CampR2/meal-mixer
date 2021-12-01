''' capture user URL input to scrape a recipe from the web

    Author: Robert Camp (CampR2)
    Last Modified: 11/19/2021

'''

from kivy.uix.screenmanager import Screen
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
import logging
from app import meals

Builder.load_string('''
<NewRecipeURL>:
    name: 'new_recipe_url'
    BoxLayout:
        id: box_1
        orientation: 'vertical'
        Label:
            id: title_label
            text: 'New URL Recipe'
            halign: 'center'
            valign: 'middle'
            font_size: 30
            text_size:self.width, None
            # height: self.texture_size[1]
            size: self.texture_size
            size_hint: 1, .2

            # canvas.before:
            #     Color:
            #         rgba: [0,0,0,1]
            #     Rectangle:
            #         size: self.size
            #         pos: self.pos
        BoxLayout:
            id: box_2
            orientation:'horizontal'
            Label:
                id: label_1
                text: 'INFO BOX'
                halign: 'center'
                valign: 'middle'
                text_size: self.width, None
                font_size: 30
                canvas.before:
                    Color:
                        rgba: [.4, .4, .5, 1]
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        # source:root.manager.get_screen('home').meals_screen_background
            BoxLayout:
                id: box_3
                orientation:'vertical'
                StandardButton:
                    id: button_1
                    text: 'Search Recipe'
                    font_size: 30
                    opacity: 1
                    on_release: app.root.current = 'search_recipe'
                StandardButton:
                    id: button_2
                    text: 'New User Recipe (Manual) <nonfunctional/in-process>'
                    font_size: 30
                    opacity: 1
                    # on_release:
                # # redundant: may be removed in the future
                # StandardButton:
                #     id: button_3
                #     text: 'Exit to Recipes'
                #     font_size: 30
                #     opacity: 1
                #     on_release: app.root.current = 'recipes'
                StandardButton:
                    id: button_4
                    text: 'Exit to Home'
                    font_size: 30
                    opacity: 1
                    on_release: app.root.current = 'home'

        TextInput:
            id: text_in_url
            focus: True
            write_tab: False
            multiline: False
            text: root.start_text
            text_size: self.width, None
            halign: 'left'
            valign: 'middle'
            height: self.minimum_height
            width: self.width
            font_size: 30
            size_hint: 1, None
            on_text_validate: root.get_url_recipe()


    ''')

class NewRecipeURL(Screen):
    """ provide functionality for NewRecipeURL window

        properties:
            - recipe: the recipe retrieved from the scraper.py module
            - start_text =  default display text in the search bar

    """
    recipe = ObjectProperty(None)
    start_text = StringProperty('Type the Web Address Here')

    def __init__(self, **kwargs):
        super(NewRecipeURL, self).__init__(**kwargs)
        # get core logger
        self.log = logging.getLogger('root')

    def get_url_recipe(self):
        ''' capture the user's url input'''

        url = self.ids['text_in_url'].text
        ''' later functionality: this could be made to handle more than one
          url pull at a time url can become urls below and it can be a list
            of urls instead of a single one. I can then loop through the list
            there will need to be a more flexible way to account for bad URLs
            end
        '''
        self.log.info(f'{__name__}.id[\'text_in_url\'] info entered by user: {url}')
        self.recipe = meals.WM(url) # the magic
        # the name of the recipe being base indicated that only the "base"
        # object was loaded and therefore an error has occured with the scrape
        if self.recipe.name == 'base':
            self.ids['text_in_url'].text = self.start_text
            label_1 = self.ids['label_1']
            # flash red screen
            self.cover_rect = Rectangle(size=label_1.size, pos=label_1.pos)
            self.cover_color = Color(1, 0, 0)
            label_1.canvas.after.add(self.cover_color)
            label_1.canvas.after.add(self.cover_rect)
            # provide user feedback
            self.ids['label_1'].text = 'There was something wrong with the \
address you entered.\nPlease try again.'
            # schedule widget reset
            Clock.schedule_once(self.reset_text, 2)
        else:
            meals.SR().save_recipe(self.recipe)
            meals.SR().get_recipe(self.recipe.name)
            self.ids['label_1'].text = f'{self.recipe.name} imported successfully from \
URL: {url}'
            self.ids['text_in_url'].text = ''
            Clock.schedule_once(self.reset_text, 1)

    def reset_text(self, dt):
        ''' reset the text_in_url widget and remove the red flash if present'''
        self.ids['text_in_url'].text = self.start_text
        label_1 = self.ids['label_1']
        # this is not the most tidy way to do this
        # I will come back and change to something more fluid in the future
        # check for he existence of cover_color and cover_rect without error
        try:
            label_1.canvas.after.remove(self.cover_color)
            label_1.canvas.after.remove(self.cover_rect)
        except AttributeError as AE:
            pass
