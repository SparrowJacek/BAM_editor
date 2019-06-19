import os

from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.popup import Popup


class NewFileButton(Button):
    pass


class OpenFileButton(Button):
    def open_file_browser(self):
        OpenFilePopup().open()

    def on_press(self):
        self.open_file_browser()


class OpenFilePopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OpenFileListChooser(FileChooserListView):
    def print_path(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left':
            print(self.path)


class OpenFileIconChooser(FileChooserIconView):
    pass


class SaveFileButton(Button):
    pass


class UndoButton(Button):
    pass


class RedoButton(Button):
    pass
