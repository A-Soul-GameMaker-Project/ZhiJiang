label be3:
    #【场景：病房房间-夜】
    play music "audio/bgm/普通 悲伤类的抒情1 .mp3"
    scene 病房强月光 
    
    show xw sad at r2
    show nl normal at l2

    with dissolve
    #【立绘：向晚-悲伤】
    #【BGM：悲伤】
    xw "乃琳，我害怕……"
    show xw sad at center with move
    "几乎是下意识地，她抓住乃琳将离的手。"
    #【立绘：乃琳-日常】
    nl "傻丫头，你吓我一跳。"
    nl "我不走啊，我怎么会走呢……"
    nl "我和你一起等拉姐，我们等到早上，就一起出发去找她，好吗？"
    #【立绘：向晚-日常】
    show xw normal with dissolve
    xw "嘿嘿，乃琳，你是不是怕黑啊~"
    #【立绘：乃琳-喜悦】
    show nl blush with dissolve
    nl "我不是，我没有，你别瞎说啊——"
    "……"

    scene 病房1 with dissolve
    "第二天天一亮，睡得昏昏沉沉的乃琳就被吵醒了。"
    play music "audio/bgm/危机1.mp3" fadein 4.0 fadeout 4.0

    "【???】" "是这一间吗？"
    "【???】" "定位上这不是清清楚楚吗？"
    play sound "audio/se/开门声.mp3"
    "不耐烦的声音，这是……"
    #【立绘：阿草-愤怒】
    show ac angery at center with dissolve
    ac "我以为你的行动会很迅速，乃琳。"
    "他的语气里充满了失望。"
    #【立绘：阿草-得意】
    show ac proud with dissolve
    ac "把人带走吧。"
    ac "门口那群疯子也处理一下。没打死吧？嗯……没出人命就行。"
    hide ac with dissolve
    #【立绘：向晚-惊讶】
    show xw shock at r2
    show nl sad at l2
    with dissolve
    xw "乃琳……他们是……"
    #【立绘：乃琳-悲伤】
    nl "向晚，对不起……"
    "乃琳掏出了她的伯莱塔92F，对准了向晚。"
    play sound "audio/se/枪声三连.mp3"
    #【三发枪声】
    scene black with dissolve
    "（枪声）"
    "向晚闭上了眼睛。"
    "却迟迟没有熟悉的痛感和嗓子里的那一股甜腥味。"
    scene 病房1 with dissolve
    show xw shock at r2
    show nl normal at l2
    with dissolve
    "她缓缓的睁开眼，只发现门外的三名黑衣保全人员已经被击倒在地。"
    "乃琳对他们很熟，他们是和她同期的特工。"
    "乃琳把向晚拉在墙边。"
    #乃琳【常】
    show xw wronged at r4
    show nl normal at r2
    with move
    nl "快，晚晚你带大家逃。"
    #晚晚【苦涩】
    xw "逃，我们能往哪里逃？"
    "乃琳抛过一把钥匙"
    nl "这是我的车，你带着大家从后门走，一直往城市外面开。"
    #【枪声三连】
    play sound "audio/se/枪声三连.mp3"
    "乃琳屏息凝神，单眼瞄准，三发子弹又一次射出枪膛。"
    "子弹向着阿草身上飞去，他不闪不避，好像一股无形的力量正守护着他，弹头近在咫尺却失去了全部动力，随着地心引力一颗不剩的全砸在地板上。"
    with vpunch
    jr "呀啊——！"
    show nl angery
    show xw despair
    show jr angery zorder 10 at l2
    show baoan at l4
    with dissolve
    "一把手枪正对准着嘉然的太阳穴。"
    "【???】""放下手枪束手就擒，不然我就开枪了。"
    xw "然然！"
    show xw at r1 with move
    with sshake
    xw "唔——"
    hide jr
    hide baoan
    with dissolve
    "向晚想冲过去撞开对方，却被人从后颈勒住。"

    show ac normal at l3 with dissolve

    "阿草不慌不避地直直地走向乃琳，乃琳已经将伯莱塔92F扔在地上。"
    #阿草【常】
    ac "真的很遗憾。"
    #阿草【哀】
    show ac proud with dissolve
    ac "可能对你们很抱歉，为了本市的发展。"
    #阿草【哀】
    ac "除了嘉然，你们，要死在这里。"
    #阿草【常】
    show ac normal with dissolve
    ac "还有你，乃琳得为自己的背叛道歉才行。"
    "阿草举起了手枪，对准了向晚。"
    #阿草【常】
    ac "再见了向晚，Time to live forever Baby。"
    #【黑屏】砰 枪声
    nl "晚晚！"
    show nl angery at center with move

    play sound "audio/se/枪声.mp3"
    "（砰）"
    hide nl normal with moveoutbottom
    


    "乃琳倒在了血泊里"
    show xw cry at r1 with dissolve
    xw "乃琳，乃琳！"
    "乃琳看着向晚为她而哭泣，落泪，但她已经没有力气去擦了，或许这个任务只能交给别人了。"
    nl "真美啊，天空。"
    "血色的玫瑰在她的胸前的晚礼服上绽放，她看到的最后一眼是向晚胸前的紫色水晶散发出的微光。"
    "晚晚，你知道吗？有家店的项链和你真的很搭……"
    "有机会一定带你去看看……"
    #【黑屏】
    scene 海底向晚4 with Dissolve(3)
    show screen saying("水母又回到了海底" ,0.5,0.4,30) with Dissolve(3)
    $ achievement.grant('be3')
    stop music fadeout 20
    $ renpy.pause(15.0)
    hide screen saying with Dissolve(3)


    $ persistent.be3 = True
    $ check_playthrough()
