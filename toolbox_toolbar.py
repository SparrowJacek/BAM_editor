from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from shared_logics import get_widget_with_id
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
    def on_press(self):
        im_scatter = get_widget_with_id('imagescatter')
        if im_scatter.scale < im_scatter.scale_max:
            im_scatter.scale *= 2


class ZoomOutButton(Button):
    def on_press(self):
        im_scatter = get_widget_with_id('imagescatter')
        if im_scatter.scale > im_scatter.scale_min:
            im_scatter.scale *= 0.5


class ScatterCenterButton(Button):
    def on_press(self):
        im_scatter = get_widget_with_id('imagescatter')
        im_scatter.scale = 1
        im_scatter.pos = im_scatter.parent.pos
