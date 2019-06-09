from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from shared_widgets import RadioButton


class MoveImageButton(RadioButton):
    pass


class PencilButton(RadioButton):
    pass


class BrushButton(RadioButton):
    pass


class EraserButton(RadioButton):
    pass


class ColorPickerButton(RadioButton):
    pass


class FloodFillButton(RadioButton):
    pass


class ImageCenterButton(ToggleButton):
    pass


class ZoomInButton(Button):
    def zoom_in(self, root):
        if root.ids['imagescatter'].scale < root.ids['imagescatter'].scale_max:
            root.ids['imagescatter'].scale *= 2


class ZoomOutButton(Button):
    def zoom_out(self, root):
        if root.ids['imagescatter'].scale > root.ids['imagescatter'].scale_min:
            root.ids['imagescatter'].scale *= 0.5


class ScatterCenterButton(Button):
    def center_scatter(self, root):
        root.ids['imagescatter'].scale = 1
        root.ids['imagescatter'].pos = root.ids['imagescatter'].parent.pos
