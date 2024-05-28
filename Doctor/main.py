from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class Interface(MDScreenManager):
    pass

class DoctorAPP(MDApp):
    def Build(self):
        self.theme_cls.primary_palette='Pink'
        self.theme_cls.primary_hue='300'
        self.theme_cls.accent_palette="Gray"
        self.theme_cls.accent_hue='700'
        self.theme_cls.primary_light_hue="50"
        self.theme_cls.material_style="M2"


DoctorAPP().run()