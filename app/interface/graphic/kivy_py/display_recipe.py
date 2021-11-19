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
import meals

Builder.load_string('''
<DisplayRecipe>:
    name: 'display_recipe'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation:'horizontal'
            BoxLayout:
                id: info_box
                size_hint: 1, 1
                canvas:
                    Color:
                        rgba: [1,0,0,.6]
                    Rectangle:
                        pos: self.pos
                        size: self.size
            BoxLayout:
                orientation:'vertical'
                padding: [5,5,5,5]
                size_hint: .3, 1
                Button:
                    size_hint_y: None
                    text_size: self.width, None
                    height: self.texture_size[1]
                    text: 'Edit Ingredients'
                    font_size: 30
                    opacity: 1
                    on_release: app.root.current = 'new_meal'
                    # size_hint: 1, 1

                Button:
                    background_color: (0, 0, 0, 0)
                    background_normal: ''
                    canvas.before:
                        Color:
                            rgba: (48/255, 84/255, 150/255, 1)
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [58]
                    size_hint_y: None
                    text_size: self.width, None
                    halign: 'center'
                    valign: 'middle'
                    height: self.texture_size[1]
                    text: 'Edit Directions'
                    font_size: 30
                    # opacity: .5
                    on_release: app.root.new_color_screen()
                    size_x: 1

        TextInput:
            id: recipe_input
            focus: True
            write_tab: False
            multiline: False
            on_text_validate: root.get_url_meal()
            text_size: self.width, self.height
            font_size: 30
            size_hint: 1, .09
            text: root.start_text

    ''')

class DisplayMeal(Screen):
    """docstring for DisplayMeal"""
    meal = ObjectProperty(None)
    start_text = StringProperty('Type the recipe name here.')

    def __init__(self, **kwargs):
        super(DisplayMeal, self).__init__(**kwargs)

    def get_url_meal(self):
        ''''''

        recipe = self.ids['recipe_input'].text
        ''' later functionality: this could be made to handle more than one
          url pull at a time url can become urls below and it can be a list
            of urls instead of a single one. I can then loop through the list
            there will need to be a more flexible way to account for bad URLs
            end
        '''
        print(f'this is the recipe: {recipe}')
