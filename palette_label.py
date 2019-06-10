from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from shared_logics import get_widget_with_id


class ColorButtonsGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 256):
            palette_color_button = PaletteColorButton()
            palette_color_button.color = (i / 255, i / 255, i / 255, 1)
            self.add_widget(palette_color_button)


class PaletteColorButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_touch = None
        self.scheduled_action = None

    def reset_action_params(self):
        self.current_touch = None
        self.scheduled_action = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.current_touch is not None:
                Clock.unschedule(self.scheduled_action)
                self.on_double_press()
            else:
                self.current_touch = touch
                self.scheduled_action = Clock.schedule_once(lambda dt: self.on_single_press(touch),
                                                            0.25)

    def on_double_press(self):
        color_picker_popup = ColorPickerPopup()
        color_picker = MyColorPicker(color_picker_popup, self)
        color_picker_popup.add_widget(color_picker)
        color_picker_popup.open()

    def on_single_press(self, touch):
        try:
            self.set_mouse_color(touch)
        except AttributeError:
            pass
        finally:
            self.reset_action_params()

    def set_mouse_color(self, touch):
        right_mouse_color = get_widget_with_id('right_mouse_color')
        left_mouse_color = get_widget_with_id('left_mouse_color')
        if touch.button == "right":
            right_mouse_color.color = self.color
        if touch.button == "left":
            left_mouse_color.color = self.color

    def pick_color(self, *args):
        print(self.pos)


class ColorPickerPopup(Popup):
    pass


class MyColorPicker(ColorPicker):
    def __init__(self, linked_popup, linked_button, **kwargs):
        self.color = linked_button.color
        super().__init__(**kwargs)
        self.linked_popup = linked_popup
        self.linked_button = linked_button


class MyColorPickerButton(Button):
    def get_popup(self):
        parent = self.parent
        while True:
            if issubclass(type(parent), Popup):
                return parent
            parent = parent.parent

    def on_press(self):
        right_mouse_color = get_widget_with_id('right_mouse_color')
        left_mouse_color = get_widget_with_id('left_mouse_color')
        for col_widget in (right_mouse_color, left_mouse_color):
            if col_widget.color == self.parent.linked_button.color:
                col_widget.color = self.parent.color
        self.parent.linked_button.color = self.parent.color
        parent_popup = self.get_popup()
        parent_popup.dismiss()
