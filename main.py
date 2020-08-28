from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock


Window.size = (300, 500)

class WelcomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.change_screen,5)
    def change_screen(self, dt):
        self.manager.transition = FadeTransition(duration=1.2)
        self.manager.current = "main"
class MainScreen(Screen):
    pass
class MusicApp(MDApp):    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_palette = "Green"        
class Manager(ScreenManager):
    pass

if __name__ == '__main__':
    MusicApp().run()        