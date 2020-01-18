from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButtonBehavior, ToggleButton
from kivy.graphics import Line, Color
from kivy.base import EventLoop
from kivy.config import Config


class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)


class CanvasWidget(Widget):
    line_width = 2

    def clear_canvas(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    def set_color(self, new_color):
        print(new_color)
        self.canvas.add(Color(*new_color))

    def set_line_width(self, line_width='Normal'):
        self.line_width = {'Thin': 1, 'Normal': 2, 'Thick': 4}[line_width]


class PaintApp(App):
    def build(self):
        EventLoop.ensure_window()
        if EventLoop.window.__class__.__name__.endswith('Pygame'):
            try:
                from pygame import mouse, cursors
                a, b = cursors.compile()
                mouse.set_coursor((24, 24), (9, 9), a, b)
            except:
                pass

        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(get_color_from_hex('#2980B9'))
        return self.canvas_widget


if __name__ == '__main__':
    Config.set('graphics', 'width', 960)
    Config.set('graphics', 'height', 540)
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    Window.clearcolor = get_color_from_hex('#FFFFFF')

    PaintApp().run()

