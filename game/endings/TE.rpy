init python:
    hideImg = False

screen top_img(img):
    zorder 300
    add img at normal_size

    if hideImg:
        use hide_top_img

screen hide_top_img:
    timer 0.5 action Hide('top_img')



label te:
    $ save.cp_name = "？？？"

    menu:
        "你满意现在的结局吗？"
        "是的":
            jump te_end
        "还没有":
            jump .te_start



label .te_start:
    $ save.cp_name = "？？？"

    scene black
    show screen unskip
    $ quick_menu = False
    $ _skipping = False

    window hide
    play music "audio/bgm/heart0.mp3"

    $ renpy.pause(3, hard=True)

    $ renpy.start_predict("te/*.*")
    $ renpy.movie_cutscene("audio/video/（1）开场.webm")
    $ quick_menu = True

    play music "audio/bgm/heart1.mp3"
    label .start_heart:
        menu:
            "珈乐的粉丝名字是"

            "嘉心糖":
                jump .remake
            "顶碗人":
                jump .remake
            "奶淇琳":
                jump .remake
            "皇珈骑士":
                jump .jiale_heart
            "贝极星":
                jump .remake

    label .jiale_heart:
        $ renpy.movie_cutscene("audio/video/（2）珈乐.webm")
        play music "audio/bgm/heart2.mp3"

        menu:
            "贝拉的粉丝名字是"

            "嘉心糖":
                jump .remake
            "顶碗人":
                jump .remake
            "奶淇琳":
                jump .remake
            "皇珈骑士":
                jump .remake
            "贝极星":
                jump .beila_heart

    label .beila_heart:
        $ renpy.movie_cutscene("audio/video/（3）贝拉.webm")
        play music "audio/bgm/heart3.mp3"
        show screen top_img('te/1.png')
        menu:
            "乃琳的粉丝名字是"

            "嘉心糖":
                jump .remake
            "顶碗人":
                jump .remake
            "奶淇琳":
                jump .nl_heart
            "皇珈骑士":
                jump .remake
            "贝极星":
                jump .remake

    label .nl_heart:
        $ renpy.movie_cutscene("audio/video/（4）乃琳.webm")
        play music "audio/bgm/heart4.mp3"
        show screen top_img('te/2.png')

        menu:
            "嘉然的粉丝名字是"

            "嘉心糖":
                jump .jr_heart
            "顶碗人":
                jump .remake
            "奶淇琳":
                jump .remake
            "皇珈骑士":
                jump .remake
            "贝极星":
                jump .remake

    label .jr_heart:
        $ renpy.movie_cutscene("audio/video/（5）嘉然.webm")
        play music "audio/bgm/heart5.mp3"
        show screen top_img('te/3.png')

        menu:
            "向晚的粉丝名字是"

            "嘉心糖":
                jump .remake
            "顶碗人":
                jump .xw_heart
            "奶淇琳":
                jump .remake
            "皇珈骑士":
                jump .remake
            "贝极星":
                jump .remake
    label .xw_heart:
        $ hideImg = True
        window hide
        $ renpy.movie_cutscene("audio/video/end.webm")
        $ renpy.stop_predict("te/*.*")

        stop music
        
        hide screen unskip
        $ _skipping = True

        jump .game

label .remake:
    hide screen unskip
    $ _skipping = True

    "认不全是吧？你再想想？"

    jump te.te_start


init python:
    movie = Movie(play="game.webm")
    date = Movie(play="date.webm")

screen shooter_main():
    modal True
    zorder -1
    default board = GameBoard(name)
    add movie at normal_size

    fixed:
        style "shooter"
        add board
    add "bg.png" at normal_size
    add date:
        size(261, 100)
        xpos 1018
        ypos 553

style shooter:
    maximum(1232, 662)
    xpos 141
    ypos 58

image bg12:
    "1212.png"
    size(1280,720)

image bg6:
    "612.png"
    size(1280,720)

default name = "test"
label .game:

    stop music fadeout 5

    $ renpy.pause(4, hard=True)

    scene bg12 with Dissolve(3)
    
    label input_name:
        $ _skipping  = False

        $ name = renpy.input("输入你的名字吧(10字以内)").strip()
        if len(name) > 10:
            "名字太长了，换一个吧？"
            jump input_name
        elif name == "":
            $ name = "一个魂"

        "A-SOUL现在需要你 [name] 代表一个魂去保护她们了。"
        "使用方向键或WSAD 操控一个魂进行移动（如果无法操作，关闭输入法，开启大写锁定）"
        menu:
            "你准备好了吗？"
            "是的":
                jump start_game

    label start_game:


        $ quick_menu = False
        window hide
        play music "audio/bgm/te_bgm_16bit.wav"
        call screen shooter_main
        scene bg6

        $ quick_menu = True
        $ _skipping  = True

        stop music fadeout 3.0

        scene black with Dissolve(3)

        $ renpy.pause(4, hard=True)

    jump te.part1

# 每切换一个场景，就作为一个单独的part，以.开头
label .part1:
    $ save.cp_name = "第十章"

    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/10.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True
    play music "audio/bgm/水母之歌水下（阶段一）.mp3" fadeout 3.0 fadein 5.0
    scene 海底向晚1 with Dissolve(5)
    window show

    "寂静，无声；空气已经被抽干，只有心跳和逐渐流失的温度。"
    
    "少女正沉入海底。"
    
    "这种溺亡的体验，她再熟悉不过。"
    
    "每一次失败和拯救，每一次溺海与重生。"
    
    "就像水母一样，无力的肢体，柔软的身躯，无论使用什么方式；付出多大努力；都无法浮上水面。"
    
    "她身就要沉在一束光线都不肯眷顾的海底……"
    
    xw "为什么，为什么这次会失败……明明这次大家都在……"
    
    "少女每次开始坠落，都会睁开眼睛，去看那水面上的光。"

    "但每一次水面上都是漆黑的，只能看到没有尽头的轮回。"

    "她像是被固定在克莱因瓶里的水母，永远游不出自己的宿命。"
    
    "水母想过放弃，每次都想。"
    
    "因为她不坚强，她也会感到疲惫，有小脾气。"
    
    "每当快要被击垮，融化在海底，她都会攥紧双手，因为那些曾经的美好会告诉她："

    "再试一次。"
    
    xw "我要.......游上去......"
    
    "她死死抱着自己的梦。"

    "要和大家一并走向明天。"
    
    "可这梦太重，太重了。"
    
    "因而她下沉，泪流到海中，融入水里，没有痕迹。"

    xw "不过是再多来一次……"
    
    "少女闭上了眼睛。"
    
    # 【背景：CG差分1】
    
    # 【BGM响度略增，在水下弹奏感】
    scene 海底向晚2 with Dissolve(3)

    "突然，一道光刺进海底。"

    "她紧闭的双眼察觉到了那缕明亮。"
    
    "像是被召唤了，水母开始努力上浮。"
    
    "她拼命上浮，拼劲全力去握住那道从没见过的、易逝的光芒。"
    
    "就算没有动力系统；"
    
    "就算一生都随波逐流；"
    
    "就算没有自己的思想；"
    
    "就算！就算……没有自己的支柱。"
    
    "但水母怎么就不能成功？"

    xw "好冷..."
    
    "可是……少女沉的太深……太久……"
    
    "冰冷已经浸透了她的身躯；"
    
    "她脱力，难以活动。"

    "她仍在坠落。"
    
    xw "不，不要！我……好不容易才到这儿，这不是我想要的结局。"
    
    # 【背景：CG差分2】
    scene 海底向晚3 with Dissolve(3)

    "可就在这时，女孩身边显出了白色的光，无数小小的，碗状的水母发着光，托举着脆弱的身躯。"
    
    # 【音效：气泡声】
    play sound "<from 0 to 8>audio/se/sea_magma.mp3" loop
    "迷离中，一股温意传来，水面正向她靠近。"
    stop sound fadeout 2
    # 【缓慢闪白转场】

    jump .part2

label .part2:
    # "此处应是出水音效"
    # bgm  钢琴 水母歌
    # 场景 未知存在
    play sound "audio/se/出水.mp3"
    scene 水面空间 with Dissolve(3)
    play music "audio/bgm/水母之歌水上（阶段二）.mp3" fadeout 4.0 fadein 4.0

    "最终，少女浮出水面。身处虚空的海洋之中。"
        
    "海洋没有边界，少女躺在水母搭成的浮台之上。"

    # 向晚，立绘，带水
    show xw doubt at rc with dissolve

    xw "你们，你们是……"

    "水母轻轻摇晃着身躯，贴近女孩儿的手指尖。"
    show xw smile with dissolve
        
    xw  "谢谢……谢谢你们……谢谢一个魂们……"
    show xw calm with dissolve

    "不知道自己身处何处的女孩儿，决定借由这个浮台移动，正要移动时，水面上闪出一道强光。"
    # 向晚，立绘，消失

    # "此处应是强光炫目"
    # 场景 沙发
    play sound "audio/se/voice_of_light.mp3"

    scene 水面空间早 with Fade(.75, 0.5, 0.1, color="#fff")
    show xw calm at r3

    "瞬间的炫目感让她紧闭双眼，等到睁开眼睛时，面前出现了一个沙发，沙发背面朝向向晚。"
 
    fellers_h "你是怎么到这儿来的？"
        
    "一种古老的，辨析不出声音的信息，传递到脑海之中，少女四下寻找着声音的来源。"
        
    fellers_h "我在这儿。"
        
    "沙发后冒出一团无法言喻的光焰，似乎在那沙发背后有一个模糊的人影，正看着电视机。"
        
    fellers_h "我是被束缚在这里的存在，所有时空中，只需要有一处我存在过的痕迹，我便会存于所有时空中。"
        
    fellers_h "我知晓所有的结局，唯独不知晓的是......我的命运"
    fellers_h "看来又一次，节目结束了。"
        
    #【立绘出：向晚-疑惑】
    show xw doubt at r3 with dissolve

    xw "你是谁？"
        
    #【？？？说话时，向晚立绘暗】
        
    fellers_h "我曾经无数次在这里，跟你说过同样的话语。"
        
    fellers_h "我是被束的神明，也是自由的恶魔，在这轮回中，我与你无数次相遇。"
        
    #【向晚立绘亮】
        
    xw "你说你和我见了无数次？"
        
    #【向晚立绘暗】
        
    fellers_h "对，无数次，你的回溯能力，便是和我无数次签订契约得到的。我可以让这水覆盖大地，可以让那儿有山，那里有云。在那里铺开我的曾经，看我无法参与的回忆"
        
        
    fellers_h "我无法走向这空间之外，但我可以赋予进入这里的你，向晚；你所渴望的。"
        
    #【立绘亮，改：向晚-惊讶】
    show xw shock with dissolve

    xw "你是说这回溯能力……是你赐予我的？那为何我没有这段记忆？"
        
    #【向晚立绘暗】
        
    fellers_h "和恶魔打交道需要代价，你需要付出你的灵魂，或是你的回忆。"
        
    fellers_h "每当你到达死局，无论如何回溯，如何尝试，都无法改变时，你便会像一只水母一样，被我再次置入没有开口的克莱因瓶中，重新开始你的宿命。"
    
    fellers_h "在无论如何都无法改变的每一次最终结局中，我会出现，与你签定重新来过的契约。"

    fellers_h "用你最爱玩的游戏来打比方，就是这个档损坏了，无论如何读档，都无法通关。"

    fellers_h "当你无法改变最终的结果时，我会让你用灵魂或是回忆为代价，来重开一个新档。"
        
    fellers_h "这契约能让你付出代价，再一次去拯救所爱，对你来说，每次到这儿，都是你无数次回溯的起点，也是你重新游戏的契机。"
        
    fellers_h "唯一不同的是，这次你浮上水面，我们能够对谈。"
        
    #【立绘亮，改：向晚-苦恼】
    show xw anxiety with dissolve

    xw "你是说……我经历过的那些回溯，在那些崩坏的世界中，规避掉所有错误的每次尝试，把所有人救回，直到到达我自认为正确的……"
    
    xw "这一过程我经历了无数次了，尽管我拥有每一次读档的记忆……"

    xw "但每一次重新开档后，那些发生在上一存档……的事情……我……都不记得了……"

    show xw doubt with dissolve

    xw "我选择的代价是回忆吗……"

    xw "我，我该如何走出去？"

    "沙发后的人以沉默回应。"
        
    "无力感溢满女孩的身躯。"
        
    #【立绘改：向晚-失望一下，立马转变为坚强，一次Click内改变】
    show xw despair with dissolve

    $renpy.pause(1.0)

    show xw doubt with dissolve

    xw "还要再来一次吗？"
        
    #【立绘暗】
        
    fellers_h "这要看我们的契约，我们还有很长时间可以聊。"

    fellers_h "毕竟，你的灵魂终归是属于我的"
        
    #【立绘亮】
    show xw angery with dissolve

    xw "这次……这次我要……"
    
    show xw doubt with dissolve

    "女孩揪着自己的头发，思考着和回忆等价的事物，只要有记忆，一定可以成功。"
        
    "她抓着自己湿漉漉的蓝色发梢。"
        
    fellers_h "其实，我一直……在注视着你，在这一方小小的空间中，我看见了你的结局，成千上万次"
        
    fellers_h "你没想过放弃？"
        
    #【立绘出：向晚-坚强】
    show xw normal eyeclosd at r3, dark_in with dissolve

    $renpy.pause(1.0)

    show xw normal with dissolve

    xw "放弃？我不放弃！我要经过一次又一次努力……最终达到大家都能幸福的结局……"
        
    #【立绘改：向晚-失望】
    show xw despair with dissolve

    xw "但我还是没能拯救那个栗色头发的女孩儿，我只救下了她的躯壳，却失去了她的灵魂。她丢了自己的心，失去了自己的曾经。"
        
    xw "我不想她……不想然然变成这样，但是我……已经尽力了。"
    show xw cry with dissolve

    xw "我已经尽力了，这是我在我无数次的轮回里能做到的最好了……"
    
    xw "可恶……"
        
    #【立绘改：向晚-坚强】
    show xw normal with dissolve

    xw "那就再来一次。"

    fellers_h "什么？"
    show xw angery with dissolve

    xw "再来一次！"
        
    #【立绘暗】
        
    fellers_h "好......我是你的墨菲斯托，你是我的浮士德。"
        
    fellers "我给予你我的能力，你将留下……你的代价。"
        
    fellers "一旦失去希望，你将永沉海底。"
        
    #【立绘亮】
        
    xw "这次，我不会再沉下去，正因为不可能，才值得我们去相信。"
        
    #【立绘消失】
        
    fellers "这次你打算用什么作为契约的代价？"
        
    "向晚盘腿坐在水母浮萍上，和水母偷偷比划着手势，让两队水母，一左一右分散开，只留下自己能够栖身的一小片。"
        
    #【场景上浮萍处，两队光条散开，象征水母两散进行后继与向晚的交互。】
        
    #【立绘出-向晚-狡黠】
    show xw expect with dissolve

    xw "多陪我聊聊嘛，我也好不容易才到这儿"
        
    xw "我们聊点有意思的东西吧。"
        
    #【立绘暗】
        
    fellers "笨蛋。"
        
    #【立绘亮，改-向晚-思考】
    show xw calm with dissolve

    xw "你会感到孤独吗？"
        
    #【立绘暗】
        
    fellers "我不会孤独，我只需要完成任务，我的任务是观测一切，而观测已经占用了我所有的时间。"
        
    #【立绘亮】
        
    xw "能让我看看你吗？"
        
    "向晚指了指左边，让水母浮萍向左边行驶，发现沙发也会跟着她转向，始终背朝向晚。"
        
    "向晚又指着前方，结果撞在了透明的墙上。"
    show xw wronged with dissolve

    xw "喔！好痛！"
        
    "向晚摸了摸鼻子。"
        
    "在恍惚间，空间中仿佛弥漫着银铃般的笑。"
        
    #【音效：嘉然的笑声，空灵处理】
        
    #【立绘改-向晚-气愤】
    show xw angery with dissolve
    xw "你不是说你没有感情吗！"
        
    #【立绘暗】
        
    fellers "幻听！"
        
    fellers "我是神明，亦是恶魔，我的过去和将来已然坍缩于此，不论感情。"

    fellers "我舍弃了我的曾经。我是恒定不变的存在，我为了我所爱的魂灵舍弃我的全部。"
        
    fellers "我是你无数轮回的赋予者，是你的终局，也是你灵魂契约的开始。"
        
    "女孩皱了皱眉头。"
        
    #【立绘亮，改-向晚-灵光一现，叉着腰，笑】
    show xw proud with dissolve

    xw "……每次都会跟我签订契约，代价是……"
        
    "女孩叉着腰，抬着头思考。"
        
    xw "我的灵魂终归属于你……"
        
    #【立绘暗】
        
    fellers "说的不错，你的灵魂终归是我的。啊不是……"
        
    "在突然的否定后，向晚挑了挑眉毛。"
        
    #【立绘亮】
        
    xw "那你为什么会让我用回忆来交换，为什么不直接取走我的灵魂？"
        
    #【场景进入黑夜version】
        
    #【音效："咚！"爆破声】
        
    #【立绘暗】
    scene 水面空间晚 with Dissolve(3)

    show xw despair at r3 with dissolve
    $ renpy.pause(1.5)
    show xw calm with dissolve

    "沉默弥漫在这空间之中，连天空都被沉默染成黑色。"
        
    "那光团显然愤怒了起来。"
        
    fellers "我是以折磨人为乐的恶魔，你的灵魂终将属于我，在无尽的轮回中，你必定会放弃！"
        
    #【立绘亮，改，向晚-双手环抱于胸前，胸有成竹】
    show xw smile   with dissolve
    xw "以折磨人为乐？"
        
    #【立绘暗】
        
    fellers "我既是神明也是恶魔，墨……菲斯托，你怎么敢……哎呀！"
        
    #【立绘亮】
        
    xw "看来你也是能好好说话的嘛。"
        
    "此时，无数的小水母从左边游了过来，在水面上摆出了一个小小的\"No\"。"
        
    #【立绘改，向晚-朝左下看】
    show xw unconcerned frown with dissolve

    xw "什么嘛，真的看不到脸啊……"
        
    xw "咱们的时间还很多，我也有点累了，我想聊一些轻松的话题。"
        
    #【立绘暗】
        
    fellers "你想聊些什么？"
        
    #【立绘亮，改成向晚-思考】
    show xw calm  with dissolve

    xw "看了我这么多次轮回了，你不无聊吗？"
        
    #【立绘暗】
        
    fellers_jr "我在电视里看着你，喜欢你在这个无限的轮回中找寻出路的样子。"
        
    fellers_jr "喜欢看你破涕为笑和转怒为喜的样子。"
        
    fellers_jr "喜欢看你每一次走到绝境，不会放弃，更进一步，忍住哭泣的模样。"
        
    fellers_jr "最喜欢看的，就是你每次的坚强。"
        
    #【立绘亮，改-向晚害羞】
    show xw shy  with dissolve

    xw "诶嘿，也……也没有啦。"
        
    "被那沙发后的存在一顿夸奖后，女孩儿脸通红。"
                
    #【立绘暗】
    show xw shy at dark
    "这个时候一队小小的水母从向晚的右侧驶来，在向晚的脚边比了一个\"Yes\"，向晚插起了腰。"
        
    "女孩让水母去看那电视机上的画面，老旧的电视重复着每个轮回。"
        
    #【立绘亮-改，立绘改为向晚-狡黠】
    show xw proud  with dissolve

    xw "就算出卖灵魂，也要找个付得起价钱的人，你说是不是？"
        
    xw "想不到啊，不知道怎么才能找到和回忆等价的东西，况且出去也改变不了最终的结局呀……"

    xw "我还是放弃吧，你可以收走我的灵魂。"
        
    "带着几分狡黠，几分欲拒还迎，几分疲态，几分真实。"
        
    #【立绘暗】
        
    jr_h "什么？这不过是你第612次到这里来，你好不容易见到了我，你竟然……你竟然放弃了……"
        
    "向晚站了起来，开始无所谓式地抖腿。"
        
    #【立绘亮，改，向晚-叉腰】
        
    jr_h "不许抖腿！"
        
    #【立绘改，向晚-装哭】
    show xw wronged  with dissolve

    "向晚吓了一跳，一面在心里窃喜，一面挤出了几滴眼泪。"
        
    jr_h "不许哭！不许……唉，行啊，你不打算轮回了是吗？"
        
    xw "对啊，我累了，我不打算轮回了，就到此结束吧。"
        
    "向晚坐在浮萍上，开始掰手指头。"
        
    #【立绘暗】

    jr_h "那……那要是你实在不想去了，我也没办法强迫你。"

    "那堵墙裂开了一个口子，向晚指引着水母朝着未知走去，立在了门口。"

    jr_h "在你被我吞噬消失前……我可以称呼你为晚晚吗？"

    xw "嗯……"

    jr_h "晚晚，我要讲一个关于放弃的故事。"

    # 【立绘暗时，改向晚-疑惑】
    show xw doubt  with dissolve

    # 【立绘消失】
    hide xw with dissolve
    # 【BGM：水母之歌庄严版，但是进入时要沉闷一些】

    # 【场景换一个远视图，场景不变，拉远一些】
    play music "audio/bgm/水母之歌庄严（阶段三）.mp3" fadeout 3.0 fadein 1.0

    jr_h "很久很久以前，在王国边陲的小村落里，有一个可爱的小女孩。她生来就无拘无束，她爱在星空下奔跑，追逐日与夜的分割线。在自己的努力下，她努力练习舞蹈，为的是有一天能够向其他人分享自己的舞步。"

    jr_h "于是，从古老的国度来了一位巫师，他说：「美丽的姑娘啊，你的舞步是何等的曼妙，令人着迷；你的脸颊是如此的惹人怜爱。」巫师邀请女孩前往王国中去尽情舞蹈。"

    jr_h "女孩儿高兴极了，因为她终于有了机会能够向大家展示自己的舞步，也终于有了机会去追寻自己的爱。"

    jr_h "于是女孩儿来到了王国，巫师把女孩儿带入了糖果屋中，这屋子有一个面向观众的橱窗，女孩儿就在屋子里不断舞蹈。每一次舞蹈后，台下的观众们都会赞美，而女孩儿的心也会无比甜蜜。"

    jr_h "姑娘住在糖果屋中，她很爱吃糖。"

    jr_h "她不断地给家里寄信，说明她现在的状况，她牢牢抓着自己的梦。在甜蜜而又梦幻的糖果屋中，女孩儿肆意舞蹈。"

    jr_h "可这个梦，因为一些误解，被蚕食掉了一角。"

    jr_h "有一天，糖果屋里的女孩儿发现糖果变苦了，她起初以为这只是侍卫犯的失误，然而随着时间推移，越来越多的甜美消失了。"

    jr_h "慢慢地，女孩儿的观众也变少了，王国的公民们开始因为误解，诋毁女孩儿的表演。女孩儿不解。她说：「你们告诉我！你们告诉我吧！告诉我哪里不对，我可以改，我可以为了你们改......」"

    jr_h "女孩儿最爱的观众们，如今却不再理解她。"

    jr_h "观众们有恶意吗？其实没有，他们只是没有明白女孩儿的做法呀，有时候，他们并没有留给糖果屋女孩儿足够的耐心与等待。"

    jr_h "一些观众们不看女孩的舞蹈了，一些观众将对她的误解告诉了其他喜欢看舞蹈的观众，误解传得越来越广，所有人都相信了这些话，谣言也变成了事实。"

    jr_h "女孩儿就着酸苦的糖果，继续努力回应着大家的期待。在糖果的牢笼中重复着自己绝美的舞，期待着糖果重新变甜的一天。"

    jr_h "起舞的女孩像是一个精灵，夺走了观众们的心。糖果屋的糖果重新变甜了，然而……"

    jr_h "然而女孩在睡梦里，也在担心糖果变苦的一天……"

    jr_h "故事到这里，就结束了。"

    # 【场景回归原版】

    # 【立绘出，向晚-疑惑】
    show xw doubt at r3  with dissolve 

    xw "结局呢？"

    jr_h "没有结局，到此就结束了……"

    # 【立绘改，向晚-愤怒】
    show xw angery   with dissolve 

    xw "但这个故事，不该只是这样！因为女孩儿从来不是一人。这个故事被你-墨菲斯托，遮蔽了一角，从始至终，在那边陲里，都有与女孩儿一并成长到最后的人，所以女孩儿永远不会放弃。"

    xw "故事里，女孩儿会有一个骑士，这个骑士很笨，拿不动剑，穿不上铠甲，骑不上马。"

    xw "这个骑士她手无寸铁，她只有一颗永不放弃希望的心。"

    # 【立绘改，向晚-坚强】

    # 【BGM，水母之歌升（情绪）起来】
    show xw worried   with dissolve 

    xw "无数次，无论多少次失败，她都会从那不被人知晓的回忆中抽出那把匕首，那就是她的剑！"

    xw "她会击碎那个瓶子，她也可以不是骑士，她只是厌倦了这命运，为什么公主就一定要被困在笼中？"

    xw "她会和那些观众一起，去伸出自己的双手，像一道光一样，真正凿开她那牢笼。"
    show xw calm   with dissolve 

    xw "当然啦，在外人看来，那骑士好似冲向了风车，但总有一天，那风车会被击碎，而所有的酸苦都会被骑士纳入深海之中。"

    hide xw
    "冲锋，和其他所有的美好一起，击碎那不可言喻的旧梦。"

    "空间中溢满了沉默。"

    # 【立绘改，向晚-温柔】
    show xw smile at r3  with dissolve 

    xw "观众们也理解了，他们意识到自己的一部分行为出了岔子，那女孩儿一定会理解他们，女孩儿会伸出她的手，去回应观众们的期待。"

    xw "理解是一面双向的镜子，女孩儿踏出一步，他们会紧跟着踏出一步。"

    xw "女孩儿一定会和她身边的人共同走过每一个季节，去感知，去向观众们分享自己的故事。"

    xw "观众们不会再伤害她了，他们已经明白女孩儿对她们的意义，他们会和骑士陪着女孩直到世界的尽头。"

    "沉默并未散去，那存在似乎是被紫发少女击溃了防线。"

    "女孩儿站在门前扶着门，生怕一关门就再也没有反悔的机会。"
    show xw expect   with dissolve 

    xw "告诉我，你要如何收取我的灵魂？"

        
    jr_h "很简单，和我一直在一起，再也无法走出这个空间。"
        
    jr_h "你的灵魂归于沉默，为我所有，世间上再无向晚。"
        
    #【立绘亮，改成向晚-自信笑】
    show xw happy with dissolve

    xw "那行啊，蛮简单的，不过......"
        
    "向晚在背后比划着，女孩让水母铺开两人宽的浮萍。"
        
    xw "我可以和你一直在一起。"

    xw "但不会和你一直在这里！"
        
    xw "你跟我出去，和我，和珈乐，乃琳，贝拉还有一个魂们一直在一起！"
    
    #【立绘改：向晚-温柔】
    show xw smile   with dissolve 

    xw "我已经认出你来了"

    xw "和我出去吧，然然。"

    jr_h "我……"
        
    #【立绘：嘉然-哭泣】
    show jr sad at l2 with Dissolve(5)
    jr "我……晚晚……"
    "女孩的话音刚落，空间迅速崩坏，白色的房屋坍塌，光球的光开始四散，神性的气息正在消失，就在这一刻，人性的爱与记忆彻底压过了神性。"
    scene 水面空间碎裂 with Dissolve(3)


    hide jr 
    hide xw 
    with Dissolve(4)

    #【立绘缓缓消失，BGM渐渐隐去，音效，碎裂声，崩塌声】
        
    #【空间场景夜version，天花板碎开，射入光】

    "向晚认出了嘉然，水母也化作了光。"
        
    "那白光就注入在话语中，好似刺穿神性的朗基努斯之枪，为偶像的人性掀开新的篇章。"
    stop music fadeout 5.0
    scene black with Dissolve(4)

    $ renpy.pause(2, hard=True)
        
    jump .part3
        
        
        
        
        
label .part3:
    #【黑屏演出，演出效果为黑屏出现效果，一句一次，浮现消失，缓慢，最好可以不跳过】
    window hide  # Hide the window and  quick menu while in pong

    $ quick_menu = False

    play music "audio/bgm/第十章末 希望.mp3" fadein 9.0
    $ renpy.pause(7, hard=True)

    #【BGM-温暖，希望，却又有些曲折的变奏。示例给出：Searching Where The Sea Drowned The Sun】


    show screen saying("于是花开，" ,0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

    show screen saying("而后花落，" ,0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("一瓣花融在时间之中。" ,0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)
        
        
    show screen saying("花朵散开，变成一滴墨。",0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("浅蓝色，粉色，红色，藏青色，紫色。",0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("这墨荡漾在画家的调色板中，被肆意地，涂刷在画布之上。",0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("飞舞着，跳跃着，五色在画布上驰骋着。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("那画上有一颗无限远的北极星，",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("指引着，指向了北方，狂风刮过。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

    show screen saying("在夜晚与黎明的交界线上，一粒糖果融尽身躯化在雪中。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

    show screen saying("此后一只手，用碗盛起了这抔雪。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

        
    show screen saying("端着雪的骑士，卸下了铠甲，为妻子做了一碗冰淇淋。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("那五色的墨，由是在冰封中歌舞。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("那舞绽开在午夜，嘶吼着对夜幕说。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

    show screen saying("我要去明天。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

    show screen saying("要去下一个黄昏与夜。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("最终，又是一瓣花朵，坠落，落在残垣断壁之上。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)

    show screen saying("飘过时空，飘过回忆，飘过废弃的梦。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("这花儿由彼方走向此方，随后落在女孩儿的脸颊之上。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)


    show screen saying("女孩呢喃着，夜半中，睡神亲吻着她的面颊。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(1)
        
    show screen saying("明天已经到来。",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0, hard=True)
    hide screen saying with Dissolve(4)


    $ quick_menu = True



    jump .part4
        
        
        
label .part4:
    # 【黑屏至少10s：音乐不断，后面一段还是这个】
    scene 客厅熄灯 with Dissolve(4)
    window show

    #【场景：A-SOUL嘉然生日场景】

    "向晚的日记，六月十一日"
        
    
    "【日记】" "自嘉然醒来，已经过了很久了，在空间里发生的一切仍历历在目。"

    "【日记】" "那次次失败与最终的成功，再唤醒然然，我一次次的尝试，一次次的重来，终于达到了我想要的结局。"
    
    "【日记】" "我没有放弃。"
    
    "【日记】" "在空间里，在一个魂儿们的帮助下，紫色水晶破碎了。"
    
    "【日记】" "在我看来，无底的深海才是恶意的栖身地。A-SOUL、我们应该走向更明亮的前方。"


    "【日记】" "明天就是A-SOUL的演唱会了，贝拉，乃琳，珈乐都在紧张的准备着，练习一直到了深夜。"
 
    queue sound ["audio/se/翻页3.mp3"]  

    "【日记】" "现在我每天都会早起一些，给大家准备泡面。"
    

    "【日记】" "准备好泡面后，我会先敲开然然的房门。然后依次唤醒其他人，人家也努力了这么多次了，终于到了可以跟大家一起开演唱会的这一天！"
    

    "【日记】" "然然从那之后，变得越来越快乐，天天和我们一起学习，直播，唱歌，跳舞。一切都回到了最初的样子。"
    

    "【日记】" "有时站在她们四人的身边，会觉得有一种如梦似幻般的剥离感。"
    

    "【日记】" "这次，我终于到达了所希冀的彼岸，在万千可能中，我寻得了那个一。"
    

    "【日记】" "在一个魂们和我们的一同努力下，A-SOUL企划变得越来越好，经历了这么多，我却不知道从何写起……"

    queue sound ["audio/se/翻页3.mp3"]  

    "【日记】" "时间不早啦，该上床睡觉了，今天睡觉前跟拉姐她们道了晚安，我去然然房间时，她已经睡着了。"
    

    "【日记】" "在睡梦中，她的嘴角挂着月牙儿般的微笑。我想，月光也一定正照在贝拉，珈乐和乃琳的身上，显出静谧的光。"

    "【日记】" "那光晕一定是未来的颜色。"
    

    "【日记】" "我想起来，之前看然然跳舞的时候，然然的舞蹈变得柔和，就像一开始我们四人看到她时那样，让人陶醉，但是又不至于刺痛我们。"
    

    "【日记】" "然然的确回来了。我们，都回来了。"
    

    "【日记】" "我现在习惯最晚睡觉，我会在睡觉前确认每个人都安然入眠，这样才让我安心。"
    

    "【日记】" "我也要睡觉啦，明天，就在明天，明天是我的生日！也是A-SOUL的演唱会，真是期待……"
        
    #【场景消失，黑屏】

    "【日记】" "晚安啦。"
    play sound "audio/se/翻页3.mp3" 

    #【翻页声】 
    scene black with dissolve


    "【日记】" "我所挚爱的一个魂灵。" 

    stop music fadeout 10.0

    show screen saying_soul("一个魂灵")

    $ renpy.pause(7, hard=True)
    hide screen saying_soul with Dissolve(1)

    window hide
    $ achievement.grant('te')
    show screen saying("A-SOUL", yalign=0.37) with Dissolve(2)
    stop music fadeout 5
    $ renpy.pause(3, hard=True)
    hide screen saying  with Dissolve(2)
 
    $ persistent.te = True
    $ check_playthrough()
    jump TE_ED

label TE_ED:    
    stop music fadeout 3
    scene TE演唱会 with Dissolve(2)

    show screen unskip
    $ renpy.pause(2, hard=True)
    $ renpy.movie_cutscene("audio/video/end/TE.webm")
    scene TE演唱会
    $ renpy.pause(3, hard=True)
    hide screen unskip

    jump te_end

label te_end:
    pass

screen saying_soul(s,color="#fff",font="DroidSansFallback.ttf"):
    zorder 200
    text s size 24 color color font font at soul_move


transform soul_move:
    offset (322.0, 584.0) 
    pause 0.7

    linear 2.5 offset (575, 250)
    pause 0.5
    linear 2.5 zoom 1.5
