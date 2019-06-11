from kivy.uix.button import Button

from shared_logics import get_widget_with_id
from shared_widgets import RadioButton


class ToolButton(RadioButton):
    def __init__(self, tool_name, **kwargs):
        super().__init__(**kwargs)
        self.tool_name = tool_name
        self.bind(state=change_tool)

    def set_tool(self):
        im_scatter = get_widget_with_id('imagescatter')
        im_scatter.tool_used = self.tool_name


class MoveImageButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('move_image', **kwargs)


class PencilButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('pencil', **kwargs)


class BrushButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('brush', **kwargs)


class EraserButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('eraser', **kwargs)


class ColorPickerButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('color_picker', **kwargs)


class FloodFillButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('flood_fill', **kwargs)


class ImageCenterButton(ToolButton):
    def __init__(self, **kwargs):
        super().__init__('image_center', **kwargs)


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


def change_tool(tool_button, button_state):
    if button_state == 'down':
        tool_button.set_tool()
