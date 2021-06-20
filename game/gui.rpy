################################################################################
## 初始化内容（Initialization）
################################################################################

## init offset在其他文件之前运行初始化语句
init offset = -2
init -2:
    style say_thought:
        kerning 1.5
    style say_dialogue:
        kerning 1.5
    style nvl_dialogue:
        kerning 1.5
init -2 python:
    style.pref_slider.left_bar = "gui/left.png"
    style.pref_slider.right_bar = "gui/right.png"

    #style.pref_slider.xmaximum = 200
    #style.pref_slider.ymaximum =25

    #style.pref_slider.thumb = "GUI/Pref_Slider.png"
    #style.pref_slider.thumb_offset = 3.5
    style.pref_slider.thumb_shadow = None



## 调用gui.init将样式重置为合理的默认值，并设置
## 游戏的宽度和高度。
init python:
    gui.init(1280,720)



################################################################################
## GUI 配置变量
################################################################################


## 颜色(Color) ######################################################################
##
## 界面文本颜色

## 在整个界面使用的一种重点颜色，用于标记和突出文本。
define gui.accent_color = '#16a085'#'#006666'

## 当文本按钮既没被选中也没被悬停时使用的颜色。
define gui.idle_color = '#ffffff'##########################重要!

## small_color用于小型文本上(例如存档槽的日期名字，及快捷菜单按钮的文字)的颜色，
## 它需要更亮或更暗的颜色以便识别。
define gui.idle_small_color = gui.idle_color #'#333333'

## 用于GUI中获得焦点(鼠标悬停)的组件，包括按钮的文本、滑块和滚动条(可动区域)的滑块。
define gui.hover_color = '#1abc9c'#'#006666'

## 该颜色用于被选择的按钮文本。
## 这项优先级高于hover鼠标悬停和idle未获取焦点两种情况的颜色设置。
define gui.selected_color = '#1abc9c'

## 该颜色用于不接受用户输入的按钮的文本。
## 例如，一个rollback回滚按钮然而此时并不允许回滚。
define gui.insensitive_color = '#aaaaaa77'

## 沉默色，用于条(bar)、滚动条和滑块无法正确展示数值或者可视区域时，这些组件某些部分的颜色。
## 这只会出现在重新生成图片，而启动器中图片无法马上生效的情况下。
define gui.muted_color = '#66a3a3'
define gui.hover_muted_color = '#99c1c1'

## 用于对话和菜单选择界面颜色。
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#404040'

## 字体和字体大小 ########################################################

## 设置对话文本、菜单、输入和其他游戏内文字的字体。字体文件需要存在于game目录中。
define gui.text_font = "DroidSansFallback.ttf"

## 设置人物名字的字体。
define gui.name_text_font = "DroidSansFallback.ttf"

## 该字体用于用户接口元素的文本，例如主菜单与游戏菜单、按钮之类的。
define gui.interface_text_font = "DroidSansFallback.ttf"

## 对话字体大小。
define gui.text_size = 23

## 人物名字的大小。
define gui.name_text_size = 26

## 游戏用户接口静态文本的字号，也是游戏接口中按钮文本的默认字号。
define gui.interface_text_size = 22

## 用户接口标签部分的文本字号。
define gui.label_text_size = 24

## 通知文本字号。
define gui.notify_text_size = 16

## 标题文本字号。
define gui.title_text_size = 50

define gui.text_spacing = 300

## 主菜单和游戏菜单(Main Menu and Game Menu) #########################################################

## 图像用于主菜单和游戏菜单。
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## 对话（Dialogue） ####################################################################
##
## 这些变量控制对话如何在屏幕上一行一行的显示及其
## 方式。

## 包含对话的文本框的高度，这项应该跟gui.textbox.png文件的高度一致。
define gui.textbox_height = 145

## 文本框在屏幕上的垂直位置。0.0是顶部，0.5是中间，1.0是底部。
define gui.textbox_yalign = 1.0


## 名字(name)和名字框(namebox)的水平和垂直位置。通常我们会在文本框的左端和上端预留几个像素的空间。
## 把该配置项赋值为0.5，则可以让名字在文本框内居中(见下面的附图)。赋值可以是负数——例如，把
## gui.name_ypos赋值为“-22”就会使其在超过文本框顶端22个像素。
define gui.name_xpos = 265
define gui.name_ypos = -35

## 角色名字水平对齐方式。0.0表左对齐，0.5表示居中，1.0表示右对齐。(常用0.0或者0.5)这个配置项会同时应用
## 在两处：gui.name_xpos相关的名字框(namebox)位置，选择何种对齐方式及对应边框的xpos值。
define gui.name_xalign = 0.5

## 角色名字框(namebox)的宽度、高度、和边框，或者用
## None 来自动确定大小。
define gui.namebox_width = None
define gui.namebox_height = None

## 角色名字框(namebox)的border，按左，上，右，下的顺序排列。
define gui.namebox_borders = Borders(5, 5, 5, 5)

## 如果是True，角色名字框(namebox)的背景将被平铺，
## 如果是False，namebox的背景将被缩放。
define gui.namebox_tile = True


## 实际对话内容的水平和垂直位置。这通常从文本框(textbox)的左端或者顶端开始计算，偏离的像素数。
## 如果设置为0.5则会让对话内容在文本框(textbox)内居中。
define gui.dialogue_xpos = 200
define gui.dialogue_ypos = 10

## 该配置项给定了每行对话内容的最大宽度，单位为像素。当达到最大宽度时，Ren'Py会换行。
define gui.dialogue_width = 850

## 对话内容的水平对齐方式。
## 0.0为左对齐，0.5为居中，1.0为右对齐。
define gui.dialogue_text_xalign = 0.0


## 按钮 #####################################################################
##
## 这些变量，以及Gui/button中的图像文件，控制了下面的按钮的显示方式。


## 按钮的宽度和高度，使用像素作为单位。如果值配置为“None”，系统会基于两项内容自定义
## 一个合适的大小，这两项内容之一是按钮上的文本尺寸，另一项则是borders。
define gui.button_width = None
define gui.button_height = None

## borders(边界)以左、上、右、下的顺序围绕一个按钮。
define gui.button_borders = Borders(4, 4, 4, 4)

## 如果配置为True，按钮背景的中心区域和四条边将增缩自身尺寸，并以tile形式码放。
## 如果配置为False，则中心区域和四边将使用缩放功能。
define gui.button_tile = False

## 按钮文本的字体。
define gui.button_text_font = gui.interface_text_font

## 按钮文本的字号。
define gui.button_text_size = gui.interface_text_size

## 各种情景下按钮的颜色。
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## 按钮文本的垂直方向对齐方式。0.0为左对齐，0.5为中央对齐，1.0为右对齐。
define gui.button_text_xalign = 0.0


## 这些变量覆盖了不同种类按钮的设置。
## 参阅Gui文档可以看到可用的按钮种类，以及每个按钮的用途。
##
## 这些自定义的设置被默认界面所使用。

define gui.radio_button_borders = Borders(36, 4, 4, 4)

define gui.check_button_borders = Borders(36, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 20
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## 你也可以添加自己的自定义设置，通过添加正确的变量的命名。
## 例如，你可以取消对下面一行的编辑，以设置一个
## 导航按钮的宽度

define gui.navigation_button_width = 110


## 选择按钮(choice button) ##############################################################
##
## 选择按钮在游戏菜单中使用。

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#0e0e0e"####默认颜色淡得能看见？？
define gui.choice_button_text_hover_color = "#ffffff"


## 存档槽按钮(slot button) ###########################################################
##
## 存档槽按钮是一种特殊的按钮，它包含一个缩略图，
## 以及描述存档槽内容的文字。
## 一个存档槽就像其他按钮一样使用图像文件在Gui/button中。

## 存档槽的一些设置。
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 5, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color =gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## 存档缩略图的宽度和高度。注意这两个配置项的生存期存在命名空间config中，而不在命名空间gui中。
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## 保存槽列表中的列数和行数。
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 定位和间距（Positioning and Spacing） #####################################################
##
## 这些变量控制着各种用户界面元素的定位和间距。
## 

## 导航按钮左边的位置，相对于屏幕左边的位置。
define gui.navigation_xpos = 40

## 跳过指示器的垂直位置。
define gui.skip_ypos = 10

## 通知画面的垂直位置。
define gui.notify_ypos = 45

## 菜单选项之间的间距。
define gui.choice_spacing = 22

## 主菜单和游戏菜单的导航部分的按钮间距。
define gui.navigation_spacing = 20

## 控制偏好(preferences)之间的间隔量。
define gui.pref_spacing = 10

## 控制偏好(preferences)按钮之间的间隔量。
define gui.pref_button_spacing = 0

## 存档按钮之间的间隔量。
define gui.page_spacing = 0

## 存档槽之间的间距。
define gui.slot_spacing = 10

## 主菜单文本的位置。
define gui.main_menu_text_xalign = 0.5


## 框架(Frame) ######################################################################
##
## 这些变量控制框架的外观，当overlay图层或是窗口不存在时，这些框架可以包含用户界面的外观。


## 通用框架
define gui.frame_borders = Borders(4, 4, 4, 4)

## 作为可确定界面(Confirm)的一部分的框架。
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## 作为跳过界面(Skip)一部分的框架。
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## 作为通知画面(Notify)一部分的框架。
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## 框架背景应该平铺吗？
define gui.frame_tile = False


## 条，滚动条，和滑块(Bars, Scrollbars, and Sliders)###############################################
##
## 这些变量控制了条，滚动条，和滑块的外观。
##
## 默认的图形用户界面（Gui）只使用滑块和垂直滚动条。
## 所有其他的条(bar)都是在创建者的屏幕中编写的。

## 水平条，滚动条，滑块的高度以及垂直条，滚动条，滑块的宽度。
define gui.bar_size = 20 #水平条(bar)的高度，也是垂直条(bar)的宽度
define gui.scrollbar_size = 5
define gui.slider_size = 20

## 如果条形图象应该是平铺(tile)的，则为真。如果它们应该是线性缩放(linear scaling)的，则为假。
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = True

## 水平边框（borders）
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## 垂直边框（borders）
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## 如何处理Gui中的不可滚动的滚动条。"hide "可以隐藏它们，而None可以显示它们。
define gui.unscrollable = "hide"


## 历史（History） #####################################################################
##
## 历史界面显示玩家以及经历过的对话。

## 多少数量的语块（block）对话Ren'py会保留在历史上。
define config.history_length = 250

## 历史(history)层(entry)的高度，单位为像素。该项可以为空，这样可以允许历史(history)层(entry)
## 高度根据实际情况而定——当define gui.history_height为None时,config.history_length可能需要被明显调低。
define gui.history_height = None######################################################

## 历史中说话角色名字的标签的位置，宽度和对齐方式。可以用左端偏移像素量或是用小数表示对齐方式。下同
define gui.history_name_xpos = 130
define gui.history_name_ypos = 0
define gui.history_name_width = 350
define gui.history_name_xalign = 1.0

## 历史中对话文本标签的位置，宽度和对齐方式。
define gui.history_text_xpos = 150
define gui.history_text_ypos = 2
define gui.history_text_width = 700
define gui.history_text_xalign = 0.0


## NVL模式（NVL-Mode） ####################################################################
##
## NVL-模式屏幕显示NVL-模式人物的对话。 

## NVL模式围绕背景图的border(边界)。
define gui.nvl_borders = Borders(0, 30, 0, 20)

## Ren'Py将显示NVL模式条目的最大数量。当有更多的条目时，最老的条目将被移除。
define gui.nvl_list_length = 30

## 一个NVL模式条目的高度。将此设置为None,以使条目动态调节高度。
define gui.nvl_height = None

## 当gui.nvl_height的值为None时，各个层(entry)之间的spacing(间隔)大小，也是NVL模式菜单按钮的间隔大小。
define gui.nvl_spacing = 25

## NVL模式中说话角色名字的标签的位置，宽度和对齐方式。
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 300
define gui.nvl_name_xalign = 1.0

## NVL模式中对话文本的位置，宽度和对齐方式。
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## NVL模式中内心活动/叙述（thought/narration）的位置，宽度和对齐方式。
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## NVL菜单按钮的位置
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## 本地化（Localization） ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## 移动设备(Mobile devices)
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(40, 14, 40, 14)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Adjust the location of the textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100

        ## Change the size and spacing of various things.
        gui.slider_size = 36

        gui.choice_button_width = 1240

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 800

        gui.quick_button_text_size = 25

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20


##########################end credits###
init python:
    staffimage = LiveComposite(
        (1000,600),
        (100,300),Text("张三"),
        (200,300),Text("李四"),
        (300,300),Text("李四")
    )
