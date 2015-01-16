import appuifw
import graphics


class DrawBase(object):

    CLEAR_COLOR = (255, 255, 255)

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

    TIMER_COLOR = (0, 0, 0)
    TIMER_FONT = (u"Nokia Sans S60", 54)
    PROGRESS_BGCOLOR = (200, 200, 200)
    PROGRESS_COLOR = (0, 0, 0)

    def __init__(self):
        DrawBase.__init__(self)

    def timer(self, tvalue):
        """
            Drawing timer value
            Args:
                tvalue (unicode): timer value
        """
        self.buf.text((20, self.sheight*0.4),
                      tvalue,
                      Draw.TIMER_COLOR,
                      Draw.TIMER_FONT)

    def progress(self, curr_time, start_time):
        # full line width
        fline_w = self.swidth - 40

        bg_coord = (20, self.sheight*0.5, 20+fline_w, self.sheight*0.5+20)
        self.buf.rectangle(bg_coord, fill=Draw.PROGRESS_BGCOLOR)

        # calc current width of the progress line
        if start_time != 0:
            cline_w = fline_w * ((curr_time / float(start_time) * 100.) / 100.)
        else:
            cline_w = 0
        
        li_coord = (20, self.sheight*0.5, 20+cline_w, self.sheight*0.5+20)
        self.buf.rectangle(li_coord, fill=Draw.PROGRESS_COLOR)
