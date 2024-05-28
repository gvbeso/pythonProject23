from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<Signup>:
    MDLabel:
        text:"B A U"
        font_name:'stylish_font.ttf'
""")

class Signup(MDScreen):
    pass