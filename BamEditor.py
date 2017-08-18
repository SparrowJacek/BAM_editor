from kivy.config import Config
from kivy.app import App
from random import random as r
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.colorpicker import ColorPicker



class MainLabel(Label):
    pass

class ToolBarLabel(Label):
    pass

class NewFileButton(Button):
    pass

class OpenFileButton(Button):
    pass

class SaveFileButton(Button):
    pass

class UndoButton(Button):
    pass

class RedoButton(Button):
    pass

class PencilButton(ToggleButton):
    pass

class BrushButton(ToggleButton):
    pass

class EraserButton(ToggleButton):
    pass

class ColorPickerButton(ToggleButton):
    pass

class FloodFillButton(ToggleButton):
    pass

class ZoomInButton(Button):
    pass

class ZoomOutButton(Button):
    pass

class PaintingAreaLabel(Label):
    pass

class PaletteInfoLabel(ToolBarLabel):
    pass

class PaletteLabel(ToolBarLabel):
    def make_palette(self, layout):
        for i in range(0, 256):
            palette_color_button = PaletteColorButton()
            with palette_color_button.canvas:
                Color(i/255, i/255, i/255, 1)
            layout.add_widget(palette_color_button)


class PaletteColorButton(Button):
    pass

class BamEditor(App):
    Config.set('kivy', 'window_icon', r'E:\kivy_projects\static\program_icon\BamEditor-icon.png')
    def build(self):
        main_label = MainLabel()
        main_label.ids['palettelabel'].make_palette(main_label.ids['palettelayout'])
        return main_label

if __name__ == '__main__':
    BamEditor().run()