# File: main.py
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import time



Window.clearcolor = get_color_from_hex('#000000')

class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def update_clock(self, nap):
        if self.sw_started:
            self.sw_seconds +=nap
    
    def update_time(self,nap):
        self.root.ids.time.text = time.strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time,1)
        Clock.schedule_interval(self.update,0)

    #def on_start(self):

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        else:
            self.sw_seconds = self.sw_seconds
            
        minutes, seconds = divmod(self.sw_seconds,60)
        self.root.ids.stopwatch.text = (
            '%02d:%02d.[size=40]%02d[/size]' %
            (int(minutes), int(seconds), int(seconds * 100 % 100)))
        pass

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start'
            if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0
    
    pass


if __name__ == '__main__':
    ClockApp().run()
