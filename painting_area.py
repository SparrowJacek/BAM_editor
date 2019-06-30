from kivy.graphics import Line
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter


class PaintingAreaLabel(Label):
    pass


class ImageScatter(Scatter):
    def on_touch_down(self, touch):
        global current_tool
        if self.collide_point(*touch.pos):
            if touch.button == 'scrollup':
                if self.scale > self.scale_min:
                    self.scale *= 0.5
            if touch.button == 'scrolldown':
                if self.scale < self.scale_max:
                    self.scale *= 2
            x, y = touch.x, touch.y

            if not self.do_collide_after_children:
                if not self.collide_point(x, y):
                    return False

            touch.push()
            touch.apply_transform_2d(self.to_local)
            if super(Scatter, self).on_touch_down(touch):
                if 'multitouch_sim' in touch.profile:
                    touch.multitouch_sim = True
                touch.pop()
                self._bring_to_front(touch)
                return True
            touch.pop()

            if 'multitouch_sim' in touch.profile and current_tool == '':
                touch.multitouch_sim = True
            self._bring_to_front(touch)
            touch.grab(self)
            self._touches.append(touch)
            self._last_touch_pos[touch] = touch.pos

            return True


class ImageLabel(Label):
    pass
    # def on_touch_down(self, touch):
    #     with self.canvas:
    #         Color(1,0,1,1)
    #         touch.ud['line'] = Line(points=(touch.x, touch.y), width=10)
    #
    # def on_touch_move(self, touch):
    #     touch.ud['line'].points += (touch.x, touch.y)
