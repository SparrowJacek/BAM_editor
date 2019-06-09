from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior


class RadioButton(ToggleButton):

    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)
