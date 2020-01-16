# clock app
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import strftime
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = get_color_from_hex('#101216')


class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
        Clock.schedule_interval(self.update_clock, 0.016)

    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def update(self, nap):
        self.sw_seconds += nap

    def update_clock(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            minutes, seconds = divmod(self.sw_seconds, 60)

            self.root.ids.stopwatch.text = (
                    '%02d:%02d.[size=40]%02d[/size]' % (int(minutes), int(seconds), int(seconds * 100 % 100)))
            self.sw_seconds += nap

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0
        self.root.ids.stopwatch.text = '00:00:[size=40]00[/size]'


if __name__ == '__main__':
    from kivy.core.text import LabelBase
    LabelBase.register(name='Lobster', fn_regular='Lobster.ttf')

    ClockApp().run()
