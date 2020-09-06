from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from tkinter import filedialog
import tkinter as tk
import os
from spotdl.command_line.core import Spotdl
from kivy.core.window import Window


from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast


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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        
        )

    

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.ids.FilePathTextField.text = path

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    
    
    
    
    def download(self):
        self.song_name = self.ids.SongName.text

        args = {
            "no_encode": False,
        }
        spotdl_handler = Spotdl(args)
        spotdl_handler.download_track(self.song_name)
    def change_file_path(self):
        self.file_path = self.ids.FilePathTextField.text
        os.chdir(self.file_path)

   
class MusicApp(MDApp):    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_palette = "Green"        
    def help_dialog_box_for_downloader(self):
            dialog_box_string = "1. Click on the Choose Your Location Button. A file system screen should pop-up\n\n" \
                                "2. Choose the directory your video/song should be downloaded into\n\n" \
                                "3. Enter the name your song or a youtube or spotify link\n\n" \
                                "4. Click on the download button and Voila your video/song has been downloaded !\n\n" \
                                "WARNINGS:\n\n" \
                                "1. Please do not enter an invalid youtube link or url....\n\n" \
                                "2. Please choose a name for your video or song that does not already exist in your " \
                                "folder.\n\n" \

            close_button = MDFlatButton(text="Close", text_color=self.theme_cls.primary_color, on_release=self.close_dialog)
            self.dialog = MDDialog(title="INSTRUCTIONS:", text=dialog_box_string,
                                size_hint=(0.7, 1), buttons=[close_button])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
class Manager(ScreenManager):
    pass

if __name__ == '__main__':
    MusicApp().run()        
