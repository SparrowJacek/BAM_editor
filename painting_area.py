from kivy.uix.label import Label
from kivy.uix.scatter import Scatter


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
            self._bring_to_front(touch)
            touch.grab(self)
            self._touches.append(touch)
            self._last_touch_pos[touch] = touch.pos

            return True


class ImageLabel(Label):
    pass
