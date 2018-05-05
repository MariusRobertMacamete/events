import kivy
kivy.require ('1.10.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import sqlite3

Builder.load_file('add_project.kv')
Builder.load_file('event_page.kv')

class AddProject(Screen):
    def check_event_name(self):
        if self.ids.txt_event_name.text!='':
            self.ids.error_event.text='correct'

    def restat_gui(self):
        self.ids.lbl_event_name.color=0,0,0,0
        self.ids.txt_event_name.text=''
        self.ids.lbl_description.color=0,0,0,0
        self.ids.txt_description.text=''
        self.ids.btn_create_event.color=0,0,0,0.5


class EventPage(Screen):
    pass

class Manager(ScreenManager):
    add_project=ObjectProperty(None)
    event_page=ObjectProperty(None)

class MainApp(App):
    def build (self):
        return Manager()

if __name__=='__main__':
    MainApp().run()
