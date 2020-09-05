from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty, ObjectProperty
from tkinter import filedialog
import tkinter as tk


root2 = tk.Tk()
root2.withdraw()

FolderName = ""

Window.size = (300, 500)

class WelcomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.change_screen,5)
    def change_screen(self, dt):
        self.manager.transition = FadeTransition(duration=1.2)
        self.manager.current = "Downloader"

class DownloaderScreen(Screen):
    text = StringProperty("")
    text2 = StringProperty("")
    text3 = StringProperty("")
    text4 = StringProperty("")
    text5 = StringProperty("Choose your video/song's format type")
    hint_text = "File Path"
    error = False
    downloadChoices = ""
    menu = ""

    def create_drop_down(self):
        self.downloadChoices = [{"text": "Video (Mp4 : 720p)"},
                                {"text": "Video (Mp4: 144p)"},
                                {"text": "Audio (Mp3: 720p)"}]
        self.menu = MDDropdownMenu(
            caller=self.ids.FormatButton,
            items=self.downloadChoices,
            width_mult=5,
            callback=self.menu_callback,
        )

    def open_drop_down(self):
        self.create_drop_down()
        self.menu.open()

    def menu_callback(self, instance):
        self.text5 = instance.text
    
    
    def OpenDirectory(self):
        global FolderName
        FolderName = filedialog.askdirectory()
        FolderName = str(FolderName)
        self.text = f"{FolderName}"
    
    
    def get_name(self):
        while True:
            self.text3 = self.ids.SongName.text
            return self.text3

class MusicApp(MDApp):    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_palette = "Green"        

class Manager(ScreenManager):
    pass

if __name__ == '__main__':
    MusicApp().run()        
