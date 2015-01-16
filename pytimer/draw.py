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

