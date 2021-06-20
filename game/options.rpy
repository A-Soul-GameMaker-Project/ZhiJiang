## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。
#init python early:
#    define config.savedir = "game\saves"
## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。


## 自定义快捷键 ########################################################################
##
##

init -160 python:

    custom_keymap = dict(
        dismiss             = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'mousedown_5' ],
        voice_replay        = [],
        skip                = ['K_LCTRL', 'K_RCTRL' ],
        fast_forward        = ['keydown_K_LCTRL'],
        stop_skipping       = ['keyup_K_LCTRL'],
        toggle_skip         = ['K_F5'],
        toggle_afm          = ['K_F6', 'a'],
        game_menu           = ['K_ESCAPE', 'K_MENU'],
        save_menu           = ['K_F2', 's'],
        load_menu           = ['K_F3', 'l'],
        call_history        = ['mousedown_4', 'h'],


        hide_windows        = ['K_SPACE', 'mousedown_3'],
        toggle_fullscreen   = [ 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11'],
        rollback            = ['K_PAGEUP', 'repeat_K_PAGEUP'],
        rollforward         = [ 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
        screenshot          = [ 'alt_K_s' ],
        help                = [ ],
        save_delete         = [ 'K_DELETE' ],

        quit                = [ ],
        hard_quit           = [ ],

        # launch_editor     = [ 'E' ],
        # developer         = [ 'D', 'alt_shift_K_d' ],
        # dump_styles       = [ ],
        # reload_game       = [ 'R', 'alt_shift_K_r', ],
        # inspector         = [ 'I' ],
        # full_inspector    = [ 'alt_I' ],
        # choose_renderer     = [ 'alt_shift_K_g' ],
        # progress_screen   = [ 'alt_shift_K_p', 'meta_shift_K_p' ],
        # console           = [ 'shift_O', 'alt_shift_K_o' ],
        # console_older     = [ 'K_UP', 'repeat_K_UP' ],
        # console_newer     = [ 'K_DOWN', 'repeat_K_DOWN'],
        # director            = [ 'alt_K_d' ],
        # performance         = [ 'K_F9' ],
        image_load_log      = [ ],

        # I'm not sure if these actually do anything, but I moved them just in case.
        memory_profile      = [ ] ,
        profile_once        = [ ],
        performance         = [ ],

        accessibility       = [ ],
        self_voicing        = [ ],
        # clipboard_voicing   = [ 'alt_shift_K_c' ],
        # debug_voicing       = [ 'alt_shift_K_v', 'meta_shift_K_v' ],
    )


    ## Applies custom keybindings. Only affects modified keybindings
    config.keymap = (custom_keymap)


define config.developer = False#####################################################

define config.rollback_enabled = False #全场禁止任意回滚
define config.name = _("枝江往事")


## 决定上面给出的标题是否显示在主界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = False
define gui.show_version = False
define gui.accent_color = '#ffffff'
## 游戏版本号。

define config.version = ""


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p(
"""
制作组: A-SOUL GameMaking Project  一个魂游戏制作

copyright A-SOUL GameMaking Project 2021 Presents. \n
                All Rights Reserved\n

此游戏为同人作品，遵守A-SOUL二创规则说明3.0，并受中华人民共和国法律约束和保护\n

同人出处：A-SOUL_Official\n

感兴趣请B站或抖音关注A-SOUL成员：\n
向晚大魔王，\n
嘉然今天吃什么，\n
乃琳Queen，\n
珈乐Carol，\n
贝拉kira\n


效果音来源: \n
子弹击中泥土/岩石 许可:CC-BY 作者:卡鲁拉诺 来源:耳聆网 \n
新锁新 \n
艾米迪利姆 \n
艾米迪利姆 \n
迪沃瑞德 \n
nicola_ariutti \n
complex_waveform \n
震撼金属碰撞 许可:CC-BY 作者:jobro 来源:耳聆网 \n
鼠的摇动 许可:CC-BY 作者:Peacewaves 来源:耳聆网 \n
水底 许可:CC-BY 作者:carmsie 来源:耳聆网 \n
纸张摩擦 许可:CC-BY-NC 作者:LloydEvans09 来源:耳聆网 \n
碰撞音效 许可:CC-BY 作者:Tritus 来源:耳聆网 \n
碰撞音效 许可:CC-BY 作者:RSilveira_88 来源:耳聆网 \n
刹车 许可:CC-BY 作者:CNCNM 来源:耳聆网 \n
击打桌子  作者：Gutturalgutfuck\n
放映机机械滑动 许可:CC-BY 作者:hpebley3 来源:耳聆网 \n
""")


## 在生成的发布版中，可执行文件和目录所使用的短名称。此处必须是仅 ASCII 字符，并
## 且不得包含空格、冒号和分号。

define build.name = "AStoryInZhiJiang"


## id
define config.steam_appid  = 1641270

## 音效和音乐 #######################################################################

## 这三个变量控制默认显示给用户的混音器。任一设置为 False 将隐藏对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## 允许用户在音效或语音轨道上播放测试音频文件，将以下语句取消注释并设置样音就可
## 以使用。

##define config.sample_sound = "sample-sound.wav"

## 将以下语句取消注释就可以设置主界面播放的背景音乐文件。此文件将在整个游戏中持
## 续播放，直至音乐停止或其他文件开始播放。

define config.main_menu_music = "audio/zhijiang.wav"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = Dissolve(0.3)
define config.exit_transition = Dissolve(0.3)


## 各个游戏菜单之间的转场。

define config.intra_transition = Dissolve(0.5)


## 载入游戏后使用的转场。

define config.after_load_transition = Dissolve(0.5)


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = Dissolve(3.0)


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 声明。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。如果是“show”，对话框将永远显示。如果是“hide”，
## 仅在存在对话时显示。如果是“auto”，对话框会在 scene 声明前隐藏，并在有新对话时
## 重新显示。
##
## 在游戏开始后，此变量可通过“window show”、“window hide”和“window auto”声明来改
## 变。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 是瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 25


## 默认的自动前进延迟。越大的数字会产生越长的等待，有效范围为 0 - 30。

default preferences.afm_time = 25

define config.default_sfx_volume = 0.5

## 存档目录 ########################################################################
##
## 控制 Ren'Py 为此游戏放置存档的，基于平台的特定目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该命令一般不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "ZhiJiang-Save"
define config.autosave_slots = 6
define config.autosave_on_quit = False

## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/logo.png"


## 启用 matrixcolor 功能
define config.gl2 = True


define config.history_length  = 50

## 生成配置 ########################################################################
##
## 这部分控制 Ren'Py 如何将您的工程转变为发行版文件。

init python:

    ## 以下功能为指定文件模式。文件模式大小写不敏感，且匹配基础目录相关的路径，
    ## 包括或不包括 /。如果多个文件模式匹配，将执行第一个。
    ##
    ## 在一个文件模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中所有的 txt 文件，“game/**.ogg”匹配所有的游戏目
    ## 录或子目录中的 ogg 文件，“**.psd”匹配工程中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从已生成的分发版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('**.psd', None)

    ## 若要打包文件，需将其列为“archive”。########################################################
    # Declare two archives.
    build.archive("sys", "all")
    build.archive("images", "all")
    build.archive("audio", "all")

    # Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.bmp", "images")


    build.classify('game/**.ttf', 'sys')
    build.classify('game/**.otf', 'sys')
    build.classify('game/**.rpy', 'sys')
    build.classify('game/**.rpyc', 'sys')
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.wav', 'audio')
    build.classify('game/**.mp3', 'audio')
    build.classify("game/**.webm", "audio")


    ## 匹配为文档模式的文件，将在 Mac 应用的生成中复制，因此它们同时存在于 app
    ## 和 zip 文件中。
    build.documentation('*.html')
    build.documentation('*.txt')

## 在 Mac 上将此设置为包含有您 Apple Developer ID Application 的字符串来启用代码
## 签名。确保将其更改为您自己的，由苹果签发的 ID。

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## 需要一个 Google Play 授权密钥来下载扩展文件并执行应用内购。授权密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 工程关联的用户名和工程名，以斜杠分隔。

# define build.itch_project = "renpytom/test-project"
