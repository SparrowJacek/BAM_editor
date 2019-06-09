from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


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

    def touch_down_actions(self, touch, root):
        if self.collide_point(*touch.pos):
            if self.current_touch is not None:
                Clock.unschedule(self.on_single_press)
                self.on_double_press()
                self.current_touch = None
            else:
                self.current_touch = touch
                Clock.schedule_once(lambda dt: self.on_single_press(touch, root), 0.1)

    def on_double_press(self):
        color_picker_popup = ColorPickerPopup(self)
        color_picker_popup.open()

    def on_single_press(self, touch, root):
        if touch.button == "right":
            root.ids['right_mouse_color'].color = self.color
        if touch.button == "left":
            root.ids['left_mouse_color'].color = self.color

    def pick_color(self, *args):
        print(self.pos)


class ColorPickerPopup(Popup):
    def __init__(self, my_widget, **kwargs):  # my_widget is now the object where popup was called from.
        super().__init__(**kwargs)
        self.my_widget = my_widget
        self.color = my_widget.color

    def dismiss_popup(self, root):
        self.my_widget.color = self.color
        root.ids['left_mouse_color'].color = self.color


class MyColorPicker(ColorPicker):
    color = ListProperty((0.5, 0.5, 1, 1))