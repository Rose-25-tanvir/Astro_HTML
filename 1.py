from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kv = """
<classa>:
    FloatLayout:
        MDLabel:
            text: "HELLO WORLD"
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""


class classa(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        Builder.load_string(kv)
        sm = ScreenManager()
        sm.add_widget(classa(name="screen1"))
        return sm


if __name__ == "__main__":
    MyApp().run()
