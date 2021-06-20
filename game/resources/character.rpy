###################
# 角色声明
###################

#CTC 对话切换图标变化
image ctc_animation:     #CTC
    xalign 0.5 yalign 0.2
    "gui/ctc.png" with Dissolve(2,alpha=True)
    2
    "gui/ctc_1.png" with Dissolve(2,alpha=True)
    2
    repeat


define adv = Character(ctc="ctc_animation",ctc_position= "nestled", 
                    ctc_pause="ctc_animation", 
                    ctc_timedpause="ctc_animation",
                    )#模板

define name_only = Character(ctc="ctc_animation",ctc_position= "nestled", 
                    ctc_pause="ctc_animation", 
                    ctc_timedpause="ctc_animation",
                    )#路人模板

#主要角色
define bl = Character("【贝拉】", color="#ff6666",
                    callback=partial(char_fade, "bl")
                    )#贝拉

define jl = Character("【珈乐】", color="#6b72b3",
                    callback=partial(char_fade, "jl")
                    )#珈乐

define jr = Character("【嘉然】", color="#ffb2d9",
                    callback=partial(char_fade, "jr")
                    )#嘉然

define sjr = Character("【嘉然】", color="#ffd700",
                    callback=partial(char_fade, "jr")
                    )#圣嘉然

define xw = Character("【向晚】", color="#c78ae5",
                    callback=partial(char_fade, "xw")
                    )#向晚

define nl = Character("【乃琳】", color="#fffacc",
                    callback=partial(char_fade, "nl")
                    )#乃琳

#配角
define ac = Character("【阿草】",
                    callback=partial(char_fade, "ac")
                    )#阿草

define dm = Character("【弹幕】")

####
#辅助
define p = Character("")

define narrator = p # 默认旁白
define nvl_p = nvl_narrator#NVL模式需要的叙述人


define fellers_h = Character("【????】",color="#ff0000",
                    callback=partial(char_fade, "jr")
                    )      


define jr_h = Character("【??】",color="#ffb2d9",
                    callback=partial(char_fade, "jr")
                    )

define fellers = Character("【墨菲斯托】",color="#ff0000",
                    callback=partial(char_fade, "jr")
                    )      

define fellers_jr = Character("【墨菲斯托?】",color="#ff0000",
                    callback=partial(char_fade, "jr")
                    )      


####
# 用来在说话时暗淡其他角色的立绘的组件：
# 示例：增加callback
# define e = Character("嘉然", callback=partial(char_fade, "eileen"))



define speak_character = set(['jr', 'bl', 'jl', 'xw', 'nl', 'ac'])

define persistent.speakingHighlight = True


init -1 python:
    from functools import partial
    def show(name, isDark=False):
        at_ls = []
        if isDark:
            at_ls.insert(0, dark)
        else:
            at_ls.insert(0, dark_in)

        renpy.show(name, at_list=at_ls)

    def char_fade(character_name, event_name, *args, **kwargs):
        if not persistent.speakingHighlight:
            return

        if event_name == "begin":
            showing_character = speak_character & renpy.get_showing_tags()
            if character_name in showing_character:
                show(character_name)
            showing_character.discard(character_name)
            for chara in showing_character:
                show(chara, True)


transform dark_in:
        matrixcolor Matrix([ 1, 0, 0, 0,
                              0, 1, 0, 0,
                              0, 0, 1, 0,
                              0, 0, 0, 1.0, ])
        linear 0.2 zoom 100.5/100


transform dark:
        matrixcolor Matrix([ 0.70, 0, 0, 0,
                              0, 0.70, 0, 0,
                              0, 0, 0.70, 0,
                              0, 0, 0, 1.0, ])
        linear 0.3 zoom 100/100.5
