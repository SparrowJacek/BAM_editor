from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from shared_logics import get_widget_with_id


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
    def on_submit(self, selected, touch):
        pass


class FilePathTextInput(TextInput):
    pass


class FileSubmitButton(Button):
    pass


class OpenFileIconChooser(FileChooserIconView):
    pass


class SaveFileButton(Button):
    pass


class UndoButton(Button):
    pass


class RedoButton(Button):
    pass
