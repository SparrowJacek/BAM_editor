from kivy.config import Config

Config.set('kivy', 'window_icon', r'.\static\program_icon\BamEditor-icon.png')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.label import Label
from os.path import expanduser
from kivy.lang import Builder

Builder.load_file('main_toolbar.kv')
Builder.load_file('toolbox_toolbar.kv')
Builder.load_file('painting_area.kv')
Builder.load_file('palette_label.kv')
Builder.load_file('sequence_frame_label.kv')

current_tool = None

class MainLabel(Label):
    def __init__(self, path=expanduser('~')):
        super(MainLabel, self).__init__()
        self.path = path


class BamEditor(App):

    def build(self):
        main_label = MainLabel()
        return main_label


if __name__ == '__main__':
    BamEditor().run()
