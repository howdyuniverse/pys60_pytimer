import appuifw
import graphics


class DrawBase(object):

    CLEAR_COLOR = (0, 0, 0)

    def __init__(self):
        self.canvas = appuifw.Canvas(redraw_callback=self.redraw)
        self.buf = graphics.Image.new(self.canvas.size)
        self.swidth = self.canvas.size[0]
        self.sheight = self.canvas.size[1]

    def redraw(self, rect=(0, 0, 0, 0)):
        if not self.canvas:
            return
        if self.buf:
            self.canvas.blit(self.buf)

    def clear(self):
        self.buf.clear(DrawBase.CLEAR_COLOR)


class Draw(DrawBase):

    TIMER_COLOR = (255, 255, 255)
    TIMER_FONT = (u"Series 60 ZDigi", 54)
    CTRLS_FONT = ("dense", 16)
    PROGRS_BGCOLOR = (45, 45, 45)
    PROGRS_COLOR = (6, 135, 135)
    BORDER_WIDTH = 20

    def __init__(self):
        DrawBase.__init__(self)
        # draw area width
        self.darea_width = self.swidth - Draw.BORDER_WIDTH*2
        self.clock_h = self.sheight * 0.3
        self.progrs_h = self.sheight * 0.4
        self.ctrls_h1 = self.sheight * 0.7
        self.ctrls_h2 = self.sheight * 0.9

    def timer(self, tvalue):
        """ Drawing timer value
            Args:
                tvalue (unicode): timer value
        """
        self.buf.text((20, self.clock_h),
                      tvalue,
                      Draw.TIMER_COLOR,
                      Draw.TIMER_FONT)

    def progress(self, curr_time, start_time):
        """ Drawing progress line
        Args:
            curr_time (int): current time in seconds
            start_time (int): starting time in seconds (represents 100% of time)
        """
        bg_coord = (Draw.BORDER_WIDTH,
                    self.progrs_h,
                    Draw.BORDER_WIDTH + self.darea_width,
                    self.progrs_h + 20)
        self.buf.rectangle(bg_coord, fill=Draw.PROGRS_BGCOLOR)

        # calc current width of the progress line
        if start_time != 0:
            cline_w = self.darea_width * ((curr_time / float(start_time) * 100.) / 100.)
        else:
            cline_w = 0
        
        li_coord = (Draw.BORDER_WIDTH,
                    self.progrs_h,
                    Draw.BORDER_WIDTH + cline_w,
                    self.progrs_h + 20)
        self.buf.rectangle(li_coord, fill=Draw.PROGRS_COLOR)

    def controls(self):
        ctrl_width = self.darea_width / 3. - 5
        margin = Draw.BORDER_WIDTH

        stop_cords = (margin,
                    self.ctrls_h1,
                    margin + ctrl_width,
                    self.ctrls_h2)
        stop_mark = (margin + ctrl_width, self.ctrls_h1 - Draw.CTRLS_FONT[1])

        margin += ctrl_width + 7.5

        play_cords = (margin,
                    self.ctrls_h1,
                    margin + ctrl_width,
                    self.ctrls_h2)
        play_mark = (margin + ctrl_width, self.ctrls_h1 - Draw.CTRLS_FONT[1])
        
        margin += ctrl_width + 7.5


        set_cords = (margin,
                    self.ctrls_h1,
                    margin + ctrl_width,
                    self.ctrls_h2)
        set_mark = (margin + ctrl_width, self.ctrls_h1 - Draw.CTRLS_FONT[1])

        self.buf.rectangle(stop_cords,
                            outline=Draw.PROGRS_COLOR,
                            width=1)
        self.buf.text(stop_mark, u"4", Draw.TIMER_COLOR, Draw.CTRLS_FONT)
        self.buf.rectangle(play_cords,
                            outline=Draw.PROGRS_COLOR,
                            width=1)
        self.buf.text(play_mark, u"5", Draw.TIMER_COLOR, Draw.CTRLS_FONT)
        self.buf.rectangle(set_cords,
                            outline=Draw.PROGRS_COLOR,
                            width=1)
        self.buf.text(set_mark, u"6", Draw.TIMER_COLOR, Draw.CTRLS_FONT)
