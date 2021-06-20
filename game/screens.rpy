################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    zorder 100
    window:
        id "window"
        style "say_window"
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        # text what id "what"
        if renpy.is_seen(ever = True) and persistent.lightRead:  # ever 为false时对本次运行起效，此处需要对过去所有阅读起效
            text what id "what" color "#f9d198" # 标记颜色
        else:
            text what id "what" color "#FFFFFF" # 未读颜色

    key "mousedown_4" action ShowMenu('history')

    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background im.MatrixColor(
            Image("gui/textbox.png"), im.matrix.opacity(float(persistent.say_window_op)/100), xalign=0.5, yalign=1.0
            )

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)

    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_bar():
    key "K_F4" action MainMenu()
    if quick_menu:
        key "K_F7" action QuickSave()
        key "K_F8" action QuickLoad()

    mousearea:
        area (275, config.screen_height - 150, 900, 150)
        hovered Show("quick_menu", transition = Dissolve(0.2))
        unhovered Hide("quick_menu", transition = Dissolve(0.2))

screen quick_menu():
    zorder 150
    if quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            if config.developer:
                textbutton _("回退") action Rollback()

            textbutton _("隐藏") action HideInterface()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("快进") action Skip() alternate Skip(fast=True)
            textbutton _("保存") action ShowMenu('save')
            textbutton _("读取") action ShowMenu('load')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')
            if persistent.showCP:
                text save.cp_name:
                    xoffset 200
## 此代码确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”屏幕。
init python:
    config.overlay_screens.append("quick_bar")


default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    hover_color "#00cc99"


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing
        if persistent.playthrough == 3 and main_menu:
            textbutton _("再次开始?"):
                text_style "sp_button_text"
                action Start('te_cp9_start')

            textbutton _("设置") action ShowMenu("preferences")

        else:
            if main_menu:

                textbutton _("开始游戏") action Start()
                if persistent.playthrough == 4:
                    textbutton _("再次开始?"):
                        text_style "sp_button_text"
                        action Start('geGoTe')

            else:

                textbutton _("历史") action ShowMenu("history")

                textbutton _("保存") action ShowMenu("save")

            textbutton _("读取游戏") action ShowMenu("load")

            textbutton _("设置") action ShowMenu("preferences")

            if main_menu:

                textbutton _("鉴赏") action ShowMenu("gallery")
                textbutton _("关于") action ShowMenu("about")
                if persistent.playthrough == 4:
                    textbutton _("制作人员") action Start('TE_ED')

            if _in_replay:

                textbutton _("结束回放") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("标题界面") action MainMenu()


            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## “帮助”对移动设备来说并非必需或相关。
                textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            textbutton _("退出") action Quit(confirm=True)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    activate_sound "audio/se/ui click.mp3"
    hover_sound "audio/se/ui hover.mp3"

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style sp_button_text:
    properties gui.button_text_properties("navigation_button")
    color "#f0d2b1"
    hover_color gui.selected_color

## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

screen main_menu():

    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu

    add gui.main_menu_background

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    ## “use”语句将其他的界面包含进此界面。标题界面的实际内容在导航界面中。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"
        keysym "mousedown_3"

        # if main_menu:
        #     action Return(),Play('sound', 'audio/bgm/zhijiang.wav')
        # else:
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color "#1abc9c"
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。

screen about():

    tag menu

    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "[config.name!t]"
            # text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            # text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_text:
    color gui.text_color


style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################
##
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## “range(1, 10)”给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################
##
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
##
## https://www.renpy.cn/doc/screen_special.html#preferences
define persistent.config_skip_delay = 75
define persistent.say_window_op = 60
define config.skip_delay = persistent.config_skip_delay

init python in save:
    tmp_op = 0
    cp_name = "test"

init python:
    save.tmp_op = persistent.say_window_op
    def setNum(v):
        config.skip_delay = v
        persistent.config_skip_delay = v

    def set_op(v):
        persistent.say_window_op = v

    def chech_op():
        if save.tmp_op == persistent.say_window_op:
            return
        save.tmp_op = persistent.say_window_op
        gui.rebuild()

screen preferences():

    tag menu
    on "hide" action Function(chech_op)
    on "replaced" action Function(chech_op)

    use game_menu(_("设置"), scroll="viewport"):
        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label "常规设置"
                    textbutton _("高亮已读") action ToggleVariable("persistent.lightRead")
                    textbutton _("说话人物高亮效果") action ToggleVariable("persistent.speakingHighlight")
                    textbutton _("忽略转场效果") action InvertSelected(Preference("transitions", "toggle"))
                    textbutton _("显示当前章节") action ToggleVariable("persistent.showCP")

                vbox:
                    style_prefix "check"
                    label _("快进设置")
                    textbutton _("快进未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续快进") action Preference("after choices", "toggle")

                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动时每段文本停止时间")

                    bar value Preference("auto-forward time")

                    label _("快进时每段文本停止时间")

                    bar:
                        style "slider"
                        xmaximum 350
                        adjustment  ui.adjustment(range=300, value=config.skip_delay, changed=setNum, step=10, adjustable=True)

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文本框不透明度")
                    bar:
                        style "slider"
                        xmaximum 350
                        adjustment  ui.adjustment(
                        range=100,
                        value=persistent.say_window_op,
                        changed=set_op,
                        step=2,
                        adjustable=True
                        )

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## 鉴赏界面 ########################################################################
##
##



screen CG:
    viewport:
        yoffset 70
        ymaximum 500
        scrollbars "vertical"
        mousewheel True

        vpgrid :
            cols 3
            spacing 25

            for img in cg_name_list:
                python:
                    if renpy.seen_image(img):
                        small_img = img + '_s'
                    else:
                        small_img = 'locked'
                add g.make_button(img, small_img, xalign=0.5, yalign=0.5)

init python:

    #  步骤1，创建一个MusicRoom实例。
    mr = MusicRoom(loop=False,single_track=True)

    # Step 2. 添加音乐文件。
    for i in music_list:
        mr.add("audio/bgm/" + i['file'], always_unlocked=i.get('isUnlock', False))

    def get_audio_duration():
        duration = renpy.music.get_duration()
        return convert_format(int(duration))

    def get_audio_position():
        music_pos = renpy.music.get_pos()
        # music_pos can be None
        if music_pos:
            return convert_format(int(music_pos))
        return "0.00"

    def convert_format(second):
        minute = second // 60
        second = second % 60
        result = ""
        result = str(minute) + ":"
        if second < 10:
            result += '0'
        result += str(second)
        return result


init -1 python:
    music_list = (
        {
            "name": "枝江钢琴",
            "file": "zhijiang.wav",
            "author": "信陵陵止",
            'isUnlock': True
        },
        {
            "name": "枝江（Vibraphone ver）",
            "file": "电颤琴 枝江.mp3",
            "author": "叫我镜大人-"
        },
        {
            "name": "AvvvvA",
            "file": "第一章医院.mp3",
            "author": "kirllanto"
        },
        {
            "name": "Take me with you Miss Diana",
            "file": "第一章黄昏街道.wav",
            "author": 'kirllanto'
        },
        {
            "name": "Une Zhijiang effrayante",
            "file": "阴间的枝江.mp3",
            "author": '米凯尔的坩锅'
        },
        {
            "name": "冰湖上的极光",
            "file": "emo.mp3",
            "author": 'Sansssss'
        },
        {
            "name": "六龙回日",
            "file": "浩荡磅礴宏伟气氛.mp3",
            "author": 'BreaKalltherules'
        },
        {
            "name": "水母与鲸",
            "file": "鲸.mp3",
            "author": 'Sansssss'
        },
        {
            "name": "トロンボーンの悲鳴",
            "file": "普通 悲伤类的抒情1 .mp3",
            "author": '叫我镜大人-'
        },
        {
            "name": "danse1",
            "file": "回忆 伤感.mp3",
            "author": 'tetsuyaaa'
        },
        {
            "name": "jumping fire",
            "file": "能说的不多了感觉弦乐完整.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "一夫当关",
            "file": "第三章重点曲1阶段战斗清场BGM.mp3",
            "author": 'BreaKalltherules'
        },
        {
            "name": "Kira～镇魂 Reburn A Soul",
            "file": "第三章重点曲中boos bgm.mp3",
            "author": 'loop_again'
        },
        {
            "name": "折断的旗帜",
            "file": "第三章重点曲3阶段悲壮战斗.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "逆天",
            "file": "有点逆天的可控的日常.mp3",
            "author": '涅不拉几的'
        },
        {
            "name": "啼夜月",
            "file": "悬疑诡异气氛通用BGM2.mp3",
            "author": 'BreaKalltherules'
        },
        {
            "name": "愁空山",
            "file": "悬疑诡异气氛通用BGM1.mp3",
            "author": 'BreaKalltherules'
        },
        {
            "name": "然然嘿嘿然然",
            "file": "放松 温暖 平静.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "长锥",
            "file": "诡异.mp3",
            "author": '叫我镜大人-'
        },
        {
            "name": "I don't Dao",
            "file": "争吵.mp3",
            "author": 'kirllanto'
        },
        {
            "name": "在温柔的夜里",
            "file": "钢琴1 缓和.mp3",
            "author": 'tetsuyaaa'
        },
        {
            "name": "Close whisper温暖的低语",
            "file": "缓和弦乐.mp3",
            "author": '宁远'
        },
        {
            "name": "了转反",
            "file": "第四章反转.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "枝江的日常",
            "file": "欢快_日常？ 三拍子.mp3",
            "author": 'tetsuyaaa'
        },
        {
            "name": "反转了！是顶晚人捏",
            "file": "日常 滑稽？.mp3",
            "author": 'tetsuyaaa'

        },
        {
            "name": "misty",
            "file": "悬疑.mp3",
            "author": 'tetsuyaaa'
        },
        {
            "name": "溺死在枝江的晚风",
            "file": "伤感双吉他.mp3",
            "author": '叫我镜大人-'
        },
        {
            "name": "梧桐树下的少女",
            "file": "抒情双吉他.mp3",
            "author": '叫我镜大人-'

        },
        {
            "name": "枝江（musicbox ver）",
            "file": "枝江音乐盒.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "P0s1tif",
            "file": "日常（可循环）.mp3",
            "author": '米凯尔的坩埚'
        },
        {
            "name": "How can I describe you ",
            "file": "第二章 悲伤回忆.mp3",
            "author": 'Kirllanto'
        },
        {
            "name": "Light",
            "file": "第二章-希望.mp3",
            "author": 'Kirllanto'
        },
        {
            "name": "珈乐是谁",
            "file": "纷乱 第三章.mp3",
            "author": '我也很绝望啊'
        },
        {
            "name": "battle filed",
            "file": "Battle field可循环.mp3",
            "author": '伏夏雪人'
        },
        {
            "name": "Slient elegy",
            "file": "Silent elegy 可循环(1).mp3",
            "author": '伏夏雪人'
        },
        {
            "name": "grow",
            "file": "kirl老师的旋律发散.mp3",
            "author": '啥都想学菜鸟ye'

        },
        {
            "name": "雾月",
            "file": "抒情1.mp3",
            "author": 'tetsuyaaa'
        },
        {
            "name": "枯萎",
            "file": "绝望ne改.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "butterflies",
            "file": "第八章 夜蝶 he hope.mp3",
            "author": 'tetsuyaaa'
        },
        {
            "name": "Back to the time bring her home",
            "file": "te_bgm_16bit.wav",
            "author": 'loop_again'

        },
        {
            "name": "深潜的告白",
            "file": "水母之歌水下（阶段一）.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "/remake",
            "file": "水母之歌水上（阶段二）.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "一束追光",
            "file": "水母之歌庄严（阶段三）.mp3",
            "author": '啥都想学菜鸟ye'
        },
        {
            "name": "我所挚爱的一个魂灵",
            "file": "第十章末 希望.mp3",
            "author": "tetsuyaaa"
        },

    )

screen audio:
    vbox:
        yoffset -70
        hbox:
            spacing 20
            vbox:
                xminimum 100
                yalign .5
                xalign .5
                if renpy.music.get_pause():
                    label "{size=15}Pausing"  xalign .5
                else:
                    label "{size=15}Now Playing"  xalign .5

                label current_music['name'] xalign .5
            vbox:
                xminimum 100
                label "{size=15}作者"  xalign .5
                label current_music['author'] xalign .5

            textbutton "■":
                action [PauseAudio('music', value='toggle')]
                yoffset -2
                keysym "K_SPACE"

define current_music = {"name": "", "author": ""}

screen music:
    tag menu

    viewport:
        yoffset 100
        ymaximum 450
        mousewheel True
        scrollbars "vertical"


        vpgrid :
            cols 3

            xspacing 20
            yspacing 30
            for i_m in range(len(music_list)):
                $ music_name = "audio/bgm/"+music_list[i_m]["file"]
                textbutton music_list[i_m]["name"]:
                    xminimum 300

                    action [mr.Play(music_name),
                            SetVariable('current_music',music_list[i_m]),
                            ]

    use audio

screen gallery():
    tag menu
    default tab = "music"
    use game_menu(_("鉴赏")):
        hbox:
            xpos 250
            spacing 200
            textbutton _("音乐") action SetScreenVariable("tab", "music")
            textbutton _("CG") action SetScreenVariable("tab", "CG"),Hide('audio')
        fixed:
            if tab == "CG":
                use CG
            elif tab == "music":
                use music

    if current_music['name'] != '' or renpy.music.get_pause() or not renpy.music.get_playing():
        on "replaced" action  [Play("music",config.main_menu_music),
                            SetVariable('current_music',{"name": "", "author": ""}),
                            ]



style gallery_button is button:
    xysize(thumbnail_x ,thumbnail_y)
#    hover_xsize thumbnail_x+10
#    hover_ysize thumbnail_y+10
#    hover_color "#006666"
#    hover_xysize(thumbnail_x+10,thumbnail_y+10)
#    idle_background "#f7f7f7aa" #纯颜色可以作为按钮背景
#    hover_background "#00FFFFaa"

## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

screen history():

    tag menu

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("尚无对话历史记录。")


## 此语句决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text:
    color gui.text_color

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("向前至之后的对话。")
    hbox:
        label _("Esc")
        text _("存档界面。")
    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")
    hbox:
        label _("F1")
        text _("打开帮助。")
    hbox:
        label _("F4")
        text _("返回标题界面")
    hbox:
        label _("F5")
        text _("切换对话快进。")
    hbox:
        label _("F6")
        text _("切换自动。")
    hbox:
        label _("F7")
        text _("快速保存")
    hbox:
        label _("F8")
        text _("快速读取")
    hbox:
        label _("F11")
        text _("切换全屏显示。")
    hbox:
        label "空格键"
        text _("隐藏用户界面。")
    hbox:
        label "Alt+s"
        text _("截图。")



screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("右键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("鼠标滚轮上")
        text _("查看之前的对话记录。")

    # hbox:
    #     label _("鼠标滚轮下")
    #     text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

# style help_label_text:
#     outlines [ (1, "#999999", 0, 0 ) ]

style help_text:
    color gui.accent_color

#     outlines [ (0.5, "#999999", 0, 0 ) ]

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("确定"):
                    action yes_action
                    keysym ["K_KP_ENTER", "K_RETURN"]

                textbutton _("取消"):
                    keysym "mousedown_3"
                    action no_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color gui.text_color

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")




## 快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl

init python:
    style.nvl_dialogue.line_spacing = 30

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing -30

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
