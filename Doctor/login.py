from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
class CustomTextField(MDRelativeLayout):
    _hint=StringProperty()

Builder.load_string("""
<Login>:
    MDBoxLayout:
        orientation:"vertical"
        spacing: dp(75)
        padding: dp(50)
        MDBoxLayout:
            size_hint_y:0.35
            MDLabel:
                text:"Registration"
                halign:"center"
                font_size:'64sp'
                font_name:"DejaVuSans.ttf"
                theme_text_color:'Custom'
                text_color:app.theme_cls.primary_color
                font_name:'stylish_font.ttf'
                
                
                
                
        MDAnchorLayout:
            anchor_x:"center"
            anchor_y:"top"
            MDBoxLayout:
                orientation:"vertical"
                adaptive_size:True
                MDTextField:
                    size_hint_x:None
                    width:dp(300)
                    hint_text:"E-mail"
                    validator:"email"
                    error_color:app.theme_cls.primary_light
                CustomTextField:
                    size_hint_x:None
                    width:dp(300)
                    _hint:"password"
                MDBoxLayout:
                    adaptive_size:True
                    pos_hint:{"right":1}
                    padding:[0,dp(20),0,0]
                    spacing:dp(20)
                    MDFlatButton:
                        text:"Signup"
                    MDRaisedButton:
                        text:"Login"                    


<CustomTextField>:
    size_hint_y:None
    height: textfield.height
    MDTextField:
        id: textfield
        hint_text:root._hint
        password: True
    MDIconButton:
        pos_hint: {"right":1, "center_y":0.5}
        icon: "eye-off"
        theme_icon_color:"Custom"
        icon_color: app.theme_cls.primary_color
        on_press:
            self.icon = "eye" if self.icon=="eye-off" else "eye-off"
            textfield.password=False if self.icon=="eye" else True



""")

class Login(MDScreen):
    pass
