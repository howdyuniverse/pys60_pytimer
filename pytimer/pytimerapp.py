import os
import e32
import appuifw
import graphics
import key_codes
import miso

import timeutils

from window import Application
from draw import Draw


class PyTimerApp(Application):

    TITLE = u"PyTimer"

    def __init__(self):
        appuifw.app.screen = "full"
        appuifw.app.exit_key_handler

        self.start_opt = (u"Start", self.start)
        self.pause_opt = (u"Pause", self.pause)

        self.menu = [
            self.start_opt,
            (u"Reset", self.reset),
            (u"Set timer", self.set_timer),
            (u"Exit", self.close_app)
        ]

        # key codes and their offsets that change timer
        self.inc_keys = {
            key_codes.EScancode3: 10,
            key_codes.EScancode2: 60,
            key_codes.EScancode1: 3600,
            key_codes.EScancode9: -10,
            key_codes.EScancode8: -60,
            key_codes.EScancode7: -3600
        }
        
        self.draw = Draw()
        self.controls = self.draw.canvas
        self.start_time = u"00:01:00"
        self.curr_time = self.start_time
        self.pause_flag = False

        Application.__init__(self,
                            title=PyTimerApp.TITLE,
                            body=self.draw.canvas,
                            menu=self.menu,
                            exit_handler=self.close_app)
        self.init_controls()
        self.draw_scene()

    def update_ui(self):
        self.set_ui(PyTimerApp.TITLE,
                    self.draw.canvas,
                    self.menu,
                    self.close_app)

    def init_controls(self):
        self.controls.bind(key_codes.EScancode4, self.reset)
        self.pause_controls()

    def start_controls(self):
        self.menu[0] = self.pause_opt
        self.update_ui()
        self.controls.bind(key_codes.EScancode5, self.pause)
        self.controls.bind(key_codes.EScancode6, lambda: None)
        self.disbale_inc_controls()

    def pause_controls(self):
        self.menu[0] = self.start_opt
        self.update_ui()
        self.controls.bind(key_codes.EScancode5, self.start)
        self.controls.bind(key_codes.EScancode6, self.set_timer)
        self.enable_inc_controls()

    def enable_inc_controls(self):
        for key in self.inc_keys:
            offset = self.inc_keys[key]
            callback = lambda offset=offset: self.change_time(offset)
            self.controls.bind(key, callback)

    def disbale_inc_controls(self):
        for key in self.inc_keys:
            self.controls.bind(key, lambda: None)

    def change_time(self, offset):
        sec = timeutils.to_sec(self.curr_time)
        sec += offset
        self.start_time = timeutils.to_str(sec)
        self.curr_time = self.start_time
        self.draw_scene()

    def pause(self):
        self.pause_flag = True

    def reset(self):
        self.pause()
        self.curr_time = self.start_time
        self.draw_scene()

    def set_timer(self):
        new_time = appuifw.query(u"Set time (hh:mm:ss):", "text", self.start_time)

        if new_time is None:
            return

        if timeutils.check_strtime(new_time):
            self.start_time = new_time 
            self.curr_time = self.start_time
            self.draw_scene()
        else:
            appuifw.note(u"Wrong time format", "error")

    def draw_scene(self):
        self.draw.clear()
        self.draw.timer(self.curr_time)
        self.draw.progress(timeutils.to_sec(self.curr_time),
                            timeutils.to_sec(self.start_time))
        self.draw.controls()
        self.draw.redraw()

    def start(self):
        if self.curr_time == "00:00:00":
            return

        self.pause_flag = False
        self.start_controls()
        cd_sec = timeutils.to_sec(self.curr_time)

        for curr_sec in reversed(range(cd_sec)):
            if self.pause_flag:
                break

            self.curr_time = timeutils.to_str(curr_sec)
            self.draw_scene()
            e32.ao_sleep(1)

        if self.curr_time == "00:00:00":
            miso.vibrate(1000, 50)

        self.pause_controls()

    def close_app(self):
        Application.close_app(self)
