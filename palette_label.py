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
        self.scheduled_action = None

    def reset_action_params(self):
        self.current_touch = None
        self.scheduled_action = None

    def touch_down_actions(self, touch, root):
        if self.collide_point(*touch.pos):
            if self.current_touch is not None:
                self.on_double_press()
                self.reset_action_params()
            else:
                self.current_touch = touch
                self.scheduled_action = Clock.schedule_once(lambda dt: self.on_single_press(touch, root),
                                                            0.2)

    def on_double_press(self):
        color_picker_popup = ColorPickerPopup()
        color_picker = MyColorPicker(self)
        color_picker_popup.add_widget(color_picker)
        color_picker_popup.open()

    def on_single_press(self, touch, root):
        if touch.button == "right":
            root.ids['right_mouse_color'].color = self.color
        if touch.button == "left":
            root.ids['left_mouse_color'].color = self.color
        self.reset_action_params()

    def pick_color(self, *args):
        print(self.pos)


class ColorPickerPopup(Popup):
    def dismiss_popup(self, root):
        self.my_widget.color = self.color
        root.ids['left_mouse_color'].color = self.color


class MyColorPicker(ColorPicker):
    def __init__(self, linked_button, **kwargs):
        super().__init__(**kwargs)
        self.linked_button = linked_button
        self.color = linked_button.color
