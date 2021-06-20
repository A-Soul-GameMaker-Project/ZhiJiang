###################
# 序章
###################

label cp0_start:
    $ save.cp_name = "序章"
    stop music  fadeout 1.0

    # jump .content

    #引入
    if not config.developer:
        jump .content
    label .last:
        menu:
            p "测试：要从哪一章开始？"
            "序章":
                jump .content
            "第一章":
                jump cp1_start
            "第二章":
                jump cp2_start    
            "第三章":
                jump cp3_start
            "第四章":
                jump cp4_start
            "第五章":
                jump cp5_start
            "第六章":
                jump cp6_start
            "下一页" if config.developer:
                jump .next

    label .next:
        menu:
            p "测试：要从哪一章开始？"

            "第7_n章":
                jump cp7_n_start
            "第8_n":
                jump cp8_n_start
            "ne":
                jump ne

            "第7_g章":
                jump cp7_g_start
            "第8_g章":
                jump cp8_g_start
            "第9_g章":
                jump cp9_g_start
            "ge":
                jump ge
            "te":
                jump te
            "上一页":
                jump .last


    label .content:
        window hide

        if not config.developer:
            show screen unskip
            $ _skipping = False
        $ renpy.movie_cutscene("audio/video/start/0.webm")
        if not config.developer:
            hide screen unskip
            $ _skipping = True

        scene black
        show screen saying("爱完全征服了恨，所以爱恨总相随。\n也正如此，有爱恨伴随的爱才比无恨的爱更伟大.",0.5,0.4,30,addImg=True) with Dissolve(3)
        $ renpy.pause(4.0)

        show screen saying("——本尼迪克特·斯宾诺莎，《伦理学》",0.8,0.9,30,addImg=True) with Dissolve(1)
        $ renpy.pause(4.0)
        hide screen saying with Dissolve(1)

        scene 病房房间 
        with fade
        play music "audio/zhijiang.wav" fadeout 3.0 fadein 1.0
        window show 

        show screen saying_black("2031年1月10日",0.5,0.4,30) with Dissolve(3)
        $ renpy.pause(2.0)
        hide screen saying_black with Dissolve(1)

        p "医院的病房被苍白的色调填满，唯一点缀着颜色的是床头摆放着的各式各样的零食，还有穿着蓝色病服躺在病床上的嘉然。"

        show xw sad at center with dissolve

        xw "然然，为什么会选择成为偶像呢。"

        p "房间里面只有两个人，坐在病床一侧的向晚问出了这个问题。"

        p "嘉然的目光看向左上角，那里正对着的是病房的一侧天花板，交错的条纹构成了棋盘的模样，她的眼神没有聚焦在具体的一点，或许眺望的是更远的远方。"

        p "一阵沉默回荡在二人之间。"

        jr "晚晚，我记不得了。"

        p "像是在安慰着露出明显失望神情的向晚，嘉然着急地寻找一个可以让向晚满意的答案，指着旁边放着的草莓蛋糕补充道"

        jr "或许是因为，成为偶像可以吃到从来没有吃过的草莓蛋糕。"

        xw "然然你..."

        p "向晚的眼角突然泛起了潮，慌慌张张地扭过头去。 "

        xw "...你先好好休息，我先出去一趟。"

        # 脚步声
        play sound "audio/se/runaway.mp3"
        hide xw with moveoutright

        p "向晚扭过了头，慌慌张张地逃出了病房。"
        stop sound
        jump .cp0_end


transform move_right:

label .cp0_end:
    scene 直播用房间 
    show screen memory_filter
    with slow_fade
    # 慌乱 压抑的bgm
    play music "audio/bgm/危机1.mp3" fadeout 3.0 fadein 2.0
    show jr normal at center with dissolve

    $ tmp_dmk_list = ["别混了别混了别混了", "混混混混混混混混混"]

    show screen dmk_screen(haveColor=True)

    jr "大家...我不是...不是就差一点就通关了嘛..."

    jr "我没混啊，你们又说要看这个，然后你们又...又..."
    
    jr "然然跳舞和运动是两个体力槽....那然然来给你们跳舞吧？"

    $ tmp_dmk_list = ["别混了别混了别混了", "混混混混混混混混混", "矮子快下去吧。", "能整点高难度的舞吗"]

    jr "你们想看什么呀？"

    show jr sad with dissolve

    $ tmp_dmk_list = ["别混了别混了别混了","换珈乐换珈乐换珈乐", "矮子快下去吧。", "能整点高难度的舞吗", "芒种"]

    jr "什么叫高难度的舞呀，跳what is love大家觉得可以吗？"
    
    jr "芒种？芒种可以啊，等我下次练好扇子，就给你们跳。"

    jr "(读弹幕)换珈乐？"

    jr "你们想看珈乐，不想看我啊......"

    $ tmp_dmk_list.append('然然已经不是小主播了，不用尽全力了。')
    $ tmp_dmk_list.append('主播失忆了是吧。')
    $ tmp_dmk_list.append('你又混')

    jr "很难不混？我真的没有混，我都跳了好几支舞了..."

    show jr distressed with dissolve
    jr "(读弹幕)“你又混！”。"
    
    show jr smile with dissolve

    jr "我才没有混，我来给大家跳舞好不好？"

    show jr angery with dissolve
    jr "我才没失忆！"
    show jr normal with dissolve

    "嘉然轻轻放下了健身环"

    jr "再见，健身环宝贝，今天你实在...太拉胯了，下次注意一点。"

    $ tmp_dmk_list = ["再见再见", "下次也不见", "别下次了", "嘉然你给我下来！"]

    show jr sad with dissolve


    $ tmp_dmk_list.append('快点下播吧')
    $ tmp_dmk_list.append('别折磨了')
    $ tmp_dmk_list.append('快下班吧')
    $ tmp_dmk_list.append('不想播就赶紧下播')
    $ tmp_dmk_list.append('怎么还有人不想见到然然的嘛，现在就催然然下播嘛')
    $ tmp_dmk_list.append('混混混混混混混混混混混混混混')
    $ tmp_dmk_list.append('不爱看别看')
    $ tmp_dmk_list.append('切割切割切割')
    $ tmp_dmk_list.append('内战内战内战')
    $ tmp_dmk_list.append('才八点')

    jr "才八点对吧...我知道你们肯定会这么说的..."


    "内战开始了"

    with vpunch
    jr "大家不要吵...."

    show jr angery with dissolve
    jr "不要吵架！然然跟你们说过多少次了...不许吵架，吵架的不是好孩子..."
    jr "都让你们不要吵架了你们还要吵架...不听然然的话是吧，不听然然话的人不乖！"

    $ tmp_dmk_list.append('然然看起来好像有点累，说话有点没力气.')

    show jr sad with dissolve

    jr"不许吵架，要相亲相爱和睦相处好吗..."

    jr "(读弹幕)然然看起来好像有点累，说话有点没力气"
    jr "然然不是一直被大家嘲笑说话虚嘛，大家习惯一下就好..."

    p "直播间的一侧，A-SOUL四人担心地看着嘉然的状态，几次要求切断直播，但都被嘉然摆摆手暗示拒绝了。"

    show jr smile with dissolve

    jr "那最后再给大家跳支舞好吗？"
    
    jr "你们想看跳舞吗，都说了你们想看几支就跳几支嘛，你们太宠我了，你们今天都没有要求我跳舞..."

    show jr haggard 
    with slow_fade

    "一支舞过后，嘉然轻轻地喘息着。"

    $ tmp_dmk_list.append('晚安.')

    jr "....这是今天最后一支舞啦，晚安大家，晚安晚安"

    hide jr with moveoutbottom
    hide screen dmk_screen

    play sound "audio/se/down.mp3"
    with sshake

    p "随着直播结束时嘉然倒下的那声响声，众人才发现然然已经昏了过去。"

    "【乃琳/贝拉/向晚/珈乐】" "然然！"

    window hide
    scene black 
    hide screen memory_filter
    with Dissolve(3)
    show screen saying("倘若在梦中把昨天当成前生，今晚也可当成来世。",0.5,0.4,30) with Dissolve(3)
    stop music fadeout 3.0
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(4)

    $ renpy.pause(2.0, hard=True)
    $ renpy.movie_cutscene("audio/video/start/op.webm")
    $ renpy.pause(2.0, hard=True)

    jump cp1_start

    

