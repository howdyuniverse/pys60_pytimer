import os
import e32
import appuifw
import graphics
import key_codes

import timeutils
from window import Application
from draw import Draw


class PyTimerApp(Application):

    APP_TITLE = u"PyTimer"

    def __init__(self):
        appuifw.app.screen = "full"

        self.start_opt = (u"Start", self.start)
        self.pause_opt = (u"Pause", self.pause)

        self.menu = [
            self.start_opt,
            (u"Set timer", self.set_timer),
            (u"Exit", self.close_app)
        ]
        self.draw = Draw()
        self.start_time = u"00:00:00"
        self.curr_time = self.start_time
        self.pause_flag = False

        Application.__init__(self, PyTimerApp.APP_TITLE,
                            self.draw.canvas,
                            self.menu)
        self.draw_scene()

    def update_ui(self):
        self.set_ui(PyTimerApp.APP_TITLE, self.draw.canvas, self.menu)

    def start_controls(self):
        self.menu[0] = self.pause_opt
        self.update_ui()
        self.draw.canvas.bind(key_codes.EScancode5, self.pause)

    def start(self):
        self.start_controls()
        cd_sec = timeutils.to_sec(self.curr_time)

        for curr_sec in reversed(range(cd_sec)):
            if self.pause_flag:
                self.pause_flag = False
                break

            self.curr_time = timeutils.to_str(curr_sec)
            self.draw_scene()
            e32.ao_sleep(1)

    def pause_controls(self):
        self.menu[0] = self.start_opt
        self.update_ui()
        self.draw.canvas.bind(key_codes.EScancode5, self.start)

    def pause(self):
        self.pause_flag = True
        self.pause_controls()

    def set_timer(self):
        new_time = appuifw.query(u"Set time (hh:mm:ss):", "text", self.start_time)

        if timeutils.check_strtime(new_time):
            self.start_time = new_time 
            self.curr_time = self.start_time
            self.draw_scene()

    def draw_scene(self):
        self.draw.clear()
        self.draw.timer(self.curr_time)
        self.draw.redraw()

    def close_app(self):
        Application.close_app(self)
