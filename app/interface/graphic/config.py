from kivy.config import Config

# get rid of red dot when presisng ctrl+mouse button
Config.set('input', 'mouse', 'mouse,disable_multitouch')
# Config.set('kivy', 'window_icon','your_app_icon_64x64.png' )
Config.set('kivy', 'exit_on_escape', 0)
