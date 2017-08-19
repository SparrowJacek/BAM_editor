from kivy.config import Config
Config.set('kivy', 'window_icon', r'.\static\program_icon\BamEditor-icon.png')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from random import random as r
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
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

class ImageCenterButton(ToggleButton):
    pass

class ZoomInButton(Button):
    def on_press(self):
        if root.ids['imagescatter'].scale < root.ids['imagescatter'].scale_max:
            root.ids['imagescatter'].scale *= 2

class ZoomOutButton(Button):
    def on_press(self):
        if root.ids['imagescatter'].scale > root.ids['imagescatter'].scale_min:
            root.ids['imagescatter'].scale *= 0.5

class ScatterCenterButton(Button):
    def on_press(self):
        root.ids['imagescatter'].scale = 1
        root.ids['imagescatter'].pos = root.ids['imagescatter'].parent.pos

class PaintingAreaLabel(Label):
    pass

class ImageScatter(Scatter):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'scrollup':
                if self.scale > self.scale_min:
                    self.scale *= 0.5
            if touch.button == 'scrolldown':
                if self.scale < self.scale_max:
                    self.scale *= 2
            x, y = touch.x, touch.y

                    # if the touch isnt on the widget we do nothing
            if not self.do_collide_after_children:
                if not self.collide_point(x, y):
                    return False

            # let the child widgets handle the event if they want
            touch.push()
            touch.apply_transform_2d(self.to_local)
            if super(Scatter, self).on_touch_down(touch):
                # ensure children don't have to do it themselves
                if 'multitouch_sim' in touch.profile:
                    touch.multitouch_sim = True
                touch.pop()
                self._bring_to_front(touch)
                return True
            touch.pop()

            # if our child didn't do anything, and if we don't have any active
            # interaction control, then don't accept the touch.
            if not self.do_translation_x and \
                    not self.do_translation_y and \
                    not self.do_rotation and \
                    not self.do_scale:
                return False

            if self.do_collide_after_children:
                if not self.collide_point(x, y):
                    return False

            if 'multitouch_sim' in touch.profile:
                touch.multitouch_sim = True
            # grab the touch so we get all it later move events for sure
            self._bring_to_front(touch)
            touch.grab(self)
            self._touches.append(touch)
            self._last_touch_pos[touch] = touch.pos

            return True
class ImageLabel(Label):
    pass

class PaletteInfoLabel(ToolBarLabel):
    pass

class PaletteLabel(ToolBarLabel):
    def make_palette(self, layout):
        for i in range(0, 256):
            palette_color_button = PaletteColorButton()
            palette_color_button.color = (i/255, i/255, i/255, 1)
            layout.add_widget(palette_color_button)


class PaletteColorButton(Button):
    def pick_color(self, *args):
        print(self.pos)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
             if touch.is_double_tap:
                color_picker_popup = ColorPickerPopup(self)
                color_picker_popup.open()

             if touch.button == "right":
                 root.ids['right_mouse_color'].color = self.color
             if touch.button == "left":
                 root.ids['left_mouse_color'].color = self.color

class CurrentColorLabel(ToolBarLabel):
    pass

class ColorPickerPopup(Popup):
    def __init__(self,my_widget,**kwargs):  # my_widget is now the object where popup was called from.
        super(ColorPickerPopup, self).__init__(**kwargs)
        self.my_widget = my_widget
    def on_dismiss(self):
        self.my_widget.color = self.color
        root.ids['left_mouse_color'].color = self.color

class SequenceFrameInfoLabel(ToolBarLabel):
    pass

class SequenceFrameTabbedPanel(TabbedPanel):
    pass

class SequenceLabel(Label):
    pass

class SequenceFrameButtonsLabel(ToolBarLabel):
    pass

class SequenceAnimationPlayButton(Button):
    pass

class SequenceAnimationStopButton(Button):
    pass

class PreviewAnimationButton(Button):
    pass

class FrameLabel(Label):
    pass

class BamEditor(App):

    def build(self):
        main_label = MainLabel()
        global root
        root = main_label

        main_label.ids['palettelabel'].make_palette(main_label.ids['palettelayout'])
        return main_label


if __name__ == '__main__':
    BamEditor().run()