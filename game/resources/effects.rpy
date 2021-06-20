init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)


#
define sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

define flash = Fade(.75, 0.5, 0.1, color="#fff")

#define wait_10 = wait_for_click(10)

define irisout = CropMove(1.0, "irisout")

define irisin = CropMove(1.0, "irisin")

define flashbulb = Fade(0.2,0.0,0.8,color='#fff')

define quick_fade = Fade(0.4,0.3,0,color='#000')

define slow_fade = Fade(1,0.6,2, color='#000')

transform normal_size:
    size(1280,720)


transform blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.2 xoffset -3
        contains:
            child
            alpha 0.2 xoffset 3
        contains:
            child
            alpha 0.2 yoffset -3
        contains:
            child
            alpha 0.2 yoffset 3


screen memory_filter:
    zorder 50
    add "回忆滤镜.png" at normal_size:
        alpha 0.7

image dirty_filter:
    "底层火焰.png"
    size(1280,720)

image 火星:
    "火星.png"
    size(1280,720)


screen brightness_increase_1:
    zorder 50
    add Solid("#fff"):
        alpha 0.4

screen brightness_increase_2:
    zorder 50
    add Solid("#fff"):
        alpha 0.7


screen black_filter1:
    zorder 50
    add Solid("#000"):
        alpha 0.3

screen black_filter2:
    zorder 50
    add Solid("#000"):
        alpha 0.65


# 播放视频用：
screen unskip:
    key "dismiss" action [[]]




transform l4:
    xcenter 150
    yalign 1.0

transform l3:
    xcenter 260
    yalign 1.0

transform l2:
    xcenter 380
    yalign 1.0

transform l1:
    xcenter 500
    yalign 1.0

transform lc:
    xcenter 660
    yalign 1.0

transform rc:
    xcenter 750
    yalign 1.0

transform r1:
    xcenter 800
    yalign 1.0

transform r2:
    xcenter 920
    yalign 1.0

transform r3:
    xcenter 1060
    yalign 1.0

transform r4:
    xcenter 1180
    yalign 1.0


transform normal_size:
    size(1280, 720)


transform body_shake:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0



#场景
screen saying(s,xalign=0.5,yalign=0.5,size=30,color="#fff",font="SourceHanSerifCN-Bold.otf", addImg=False):
    zorder 200
    text s xalign xalign yalign yalign size size color color font font
    if addImg:
        add "bg/背景花.png" at normal_size

screen saying_black(s,xalign=0.5,yalign=0.5,size=30,color="#000000",font="SourceHanSerifCN-Bold.otf"):
    zorder 200
    text s xalign xalign yalign yalign size size color color font font

screen text_title(s,xalign=0.5,yalign=0.5,size=30,color="#fff",font="SourceHanSerifCN-Bold.otf"):
    zorder 200
    text "{cps=6}"+s+"{/cps}" slow 100 xalign xalign yalign yalign size size color color font font outlines [ (absolute(3), "#ff000033", absolute(0), absolute(0)) ]
