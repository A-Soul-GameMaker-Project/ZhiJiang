# 第一章下半部分
label cp2_start:
    #########
    # 内容：
    window hide
    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/2.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True
    jump .cp2_body


label .cp2_body:
    $ save.cp_name = "第二章"

    scene NightStreet with slow_fade#【场景：夜晚街道】

    play music "audio/bgm/钢琴1 缓和.mp3" fadeout 4.0 fadein 5.0#【bgm感觉：暴风雨前的宁静】
    # play music "audio/bgm/有点逆天的可控的日常.mp3" fadein 5.0#【BGM：忧愁抒情】
    show xw unconcerned frown with dissolve#【向晚：疲惫】
    window show

    "向晚走在静谧的街上，空荡的街道只有鞋跟与地面碰撞的声音在回响。"
    "月光洒落下来照亮了她的脸颊，点缀在脸上的不是笑颜，而是愁绪和疲惫。"
    "她真的已经累了…… "
    "向晚没有着急回去，反而坐在了一旁的长椅上，看着天上的月亮。"
    "明亮的月光照亮了夜晚，反而带来了更多的阴影。"
    show xw sad with dissolve
    xw "太晚了，我该回去了。"
    show xw expect with dissolve
    xw "打起精神来向晚！"
    "向晚站起身拍了两下自己的脸，抬起头看向悠远夜幕中破开黑暗指引方向的月亮。"

    scene LivingRoom_light 
    show xw unconcerned frown at r1
    with slow_fade#【场景：客厅】
    play sound "audio/se/room_door_C.mp3"#【音效：推门】

    xw "我回来了。"
    "向晚推开了房门，走进了自己熟悉的家中，房间里的摆设没有任何的变化，但是她却觉得这里有点陌生。"
    show bl anxiety at l1 
    show nl care at r3
    show jl worried at l3
    with dissolve
    bl "晚晚你回来啦。"
    "客厅里其他队友坐在沙发上。"
    bl "然然的事情怎么样了，应该没什么大碍吧？"
    "听到贝拉的问题，其他人的目光也一起聚焦到了向晚身上。"


    show xw gloomy 
    with dissolve#【立绘：向晚低落】
    xw "刚刚阿草找我谈了一次话……它的想法是让然然毕业安心养病，我们继续运营A-SOUL……"
    #【BGM：平静的音乐骤停】

    stop music fadeout 6.0

    "话语刚落，寂静瞬间蔓延在了整个客厅。"
    "贝拉原本还想说什么，可此刻也只得脸色茫然的微张着嘴，不知该如何回应。"
    "乃琳坐在一旁担忧的看着向晚。"
    "珈乐的眉头已经皱成了一团，纠结的看着向晚，"


    play music "audio/bgm/维瓦尔第 夏第一乐章.mp3"fadeout 4.0 fadein 4.0#【BGM：急促】
    show xw angery with dissolve
    xw "哼，但我们怎么可能丢下然然，让她一个人养病嘛。"
    "引起沉默的人率先打破了沉默，都是想要想法得到其他人的赞同。"
    "但向晚的演技确实很差，强撑起的笑容掩盖不了脸上的疲惫，故作欢快的话语打不破尴尬的氛围。"
    "大家的沉默，让向晚脸上的笑容逐渐消失……"
    "沉默在逐渐蔓延，向晚眼中的悲伤也在慢慢凝聚起来……"
    show nl care at r3 with dissolve#【立绘：乃琳关心】
    nl "晚晚你已经很累了，别傻站在那里来休息一下吧。"
    "向晚只是站在门口悲伤地看着她们。"

    show xw anxiety with dissolve#【立绘：向晚着急】
    xw "拉姐，我们不可能不等然然的吧…"
    xw "难道然然对我们来说就只是一个……同事吗？"
    show bl hesitate at l1 with dissolve#【立绘：贝拉犹豫】
    bl "晚晚我……"
    show jl helpless at l3 with dissolve#【立绘：珈乐无奈】
    jl "然然她……已经很累了。"
    jl "无论是刚出道时独自收到的无数恶意，还是直播中途大大小小的矛盾，然然已经经历了太多太多了……"
    "她们没有自己选择的权利，事实已经摆在眼前了。"
    "她们也只是被推在台面上的偶像罢了，对此根本无能为力……"
    "嘉然在最为艰难的时刻她挺身而出为大家抗住了所有压力。"
    "每一次舞蹈练习也都是她训练到最后……"
    "可是…………"
    show xw shock with dissolve#【立绘：向晚惊讶】
    xw "可是……"
    show jl sad with dissolve
    jl "然然她在直播承受了那么多的压力，现在应该好好休息了……"
    show xw angery with dissolve#【立绘：向晚愤怒】
    xw "这根本不是休不休息的问题，如果就这样不管了的话……那然然…就会被踢出A-SOUL了啊！"
    #【BGM：急促】
    "随着向晚的语气逐渐激烈，气氛变得紧张了起来。"
    show nl worried with dissolve#【立绘：乃琳担忧】
    nl "晚晚，我们先冷静下来休息一下，然后再谈这些事情。"
    show xw angery with dissolve#【立绘：向晚愤怒】
    play sound "audio/se/砰的一声关门.mp3"#【声音：拍击木桌或门】

    scene 争吵 with sshake

    xw "我很冷静！"


    xw "今天必须把这件事情说清楚！"
    "压抑的情绪在沉默中爆发了，没有谁会想到最亲密的队友竟然会成为火药的引线。"
    # show jl angery with dissolve#【立绘：珈乐不满】
    jl "向晚！你够了。"
    jl "然然现在已经失去了关于A-SOUL的记忆，已经无法跟我们一起活动和演出了！"
    # show xw angery with dissolve#【立绘：向晚生气】
    xw "难道因为这些我们就可以丢下嘉然，让她一个人了吗？在这样的时刻我们选择不等她？！"
    # show xw sad with dissolve
    xw "难道在你眼里，嘉然真的就只是一个同事罢了？"
    nl "…………"
    bl "…………"
    # show jl sad with dissolve
    jl "然然她是我最好的朋友，是我们大家最好的朋友！"
    # show jl sad with dissolve#【立绘：珈乐伤心】
    jl "但是然然失去了从出道到现在的所有记忆，别说是歌曲舞蹈，她甚至就连跟我们一起的经历也记不清楚了！"
    jl "你想让这个样子的然然再一次承受和习惯古怪的弹幕，和带有恶意的话语吗？"

    scene LivingRoom_light
    show xw cry at r1
    show bl hesitate at l1
    show jl angery  at l3
    show nl care at r3
    with Dissolve(3)
    xw "拉姐，你难道要抛下然然吗？"
    xw "拉姐…"
    xw "拉姐…求你了…"


    jl "够了向晚，你这是无理取闹，你就只坚持着自己的想法，你考虑过嘉然吗？你没有......你只在考虑你自己。"
    show jl normal with dissolve
    jl "在这种危难关头，A-SOUL不能就此止步不前。"
    jl "现在我们是枝江市最知名的偶像，我们是粉丝们心灵的依靠。"
    jl "我们完全可以继续将A-SOUL做的更好，等然然痊愈再让她归来，而不是现在这样做没用的争吵和等待。"
    show xw sad with dissolve #【立绘：向晚疲惫】
    xw "这样做是没用的。抛弃就是抛弃，就算有再多的华丽借口修饰也一样。"
    show jl angery with dissolve#【立绘：珈乐愤怒】
    jl "那你有解决的办法吗？！"
    #【向晚沉默，】
    xw "………"
    show jl normal with dissolve
    jl "说到底还是你在一厢情愿而已，冷静一下好好想想吧。"
    show bl angery with dissolve
    bl "够了！"
    show bl sad with dissolve
    bl "你们别吵了。"
    show bl normal with dissolve
    bl "晚晚，我们不会抛弃然然的。"
    #【立绘：贝拉日常】
    show jl shock with dissolve
    jl "拉姐…"
    show bl sad with dissolve
    bl "天下没有什么不散的宴席，也到了说再见的时候了。"
    bl "我也有些累了。"
    jl "拉姐？！你在说什么？！"
    "听到贝拉的回答，珈乐的情绪明显也到了爆发的边缘，这是队长做出来的决断，大家都清楚这意味着什么。"
    show bl sad with dissolve#【立绘：贝拉伤心】
    bl "珈乐，我已经决定了。"
    show bl serious with dissolve#【立绘：贝拉坚毅】


    "贝拉说的很慢，可是每一个字都很坚决。"
    show jl angery with dissolve
    jl "可是你的舞台梦怎么办，你放弃了，我们大家以后怎么办，难道遇到一些困难的时候就选择当缩头乌龟吗。"
    show jl normal
    jl "我印象里的贝拉可不会这么做。"
    jl "A-SOUL解散了，然然会开心吗？"
    show nl normal with dissolve
    nl "拉姐，你冷静一下…我知道你难受，但冲动是解决不了问题的。"
    # show jl #【立绘：珈乐愤怒】
    show jl sad with dissolve
    jl "拉姐……"
    show bl care with dissolve#【立绘：贝拉关心】
    bl "我已经决定了。"
    show jl angery with dissolve
    jl "（小声）你这个骗子，你这个大骗子！"
    jl "贝拉，你跟我出来一下…"
    show bl sad with dissolve
    bl "……"
    show jl sad with dissolve
    jl "跟我出来一下！！！"


    "珈乐的声音已经带上了哭腔。"
    hide jl
    hide bl
    with moveoutleft
    
    $ renpy.pause(1)
    show xw doubt at l2 #【立绘：向晚茫然】
    show nl care at r2 #【立绘：乃琳担忧】
    with moveoutleft
    play music "audio/bgm/emo.mp3" fadeout 8.0 fadein 5#【BGM：忧伤】

    "向晚无力地靠在门上。"
    show nl sad with dissolve

    nl "晚晚你没事吧，放心吧我们大家都会帮助然然的，我也会去劝劝贝拉和珈乐。"

    show xw unconcerned frown with dissolve

    xw "我…还有事要做，我先走了。"

    "向晚扭开了把手"
    

    hide xw with dissolve

    nl "....."
    
    hide nl with dissolve

    $ renpy.pause(0.75)


    scene 练舞室
    show screen memory_filter

    show jl child expect at r2 
    show bl child 练习 at l2
    with fade
    #【小珈乐】
    "小小的女孩从舞台上看到了黑色长发女孩的芭蕾。"
    show bl child  at l2

    "压腿，踢腿，耗叉，旁腿，耗腰，甩腰......重复而枯燥的基本功训练。"
    "白粥，清水，白菜，酸奶，水果......寡淡而严格控制饮食体重。"
    "酸胀，火辣，发麻，刺痛......训练和受伤造成的疼痛。"
    "忍耐着枯燥和痛苦，因为她想要和耀眼的她一同起舞。"
    "从头部到脖子，从脖子到肩膀，身体逐渐变得灵活起来，女孩终于在舞台上用脚尖旋转起来。"

    "【舞蹈老师】" "贝拉的进步实在是太快了，不出意外的话，连那个芭蕾舞团也能够格参加吧。"

    scene 练舞室 

    show jl child sad  
    with fade
    "【路人】" "呐，你听说了吗，因为腰伤，贝拉要从芭蕾舞台退役了。"
    "【路人】" "太可惜了吧…"
    #【小珈乐】悲伤，皱眉之类的立绘

    jl "...."

    scene 街道0 
    show jl helpless   
    with fade

    "珈乐走在路上，漫无目的地闲逛，或者说她想要寻找到一个目的"
    "一个女孩子拦住了珈乐，给她递了一张传单。"
    "【女孩】" "你的条件这么好，来了解一下我们的新企划吧？"

    "珈乐接过传单，随意扫了两眼。"
    "女子偶像团体成员招聘：想要实现在众人面前闪耀的梦想吗？快来加入我们吧！——详情请前往枝江大厦了解"
    #【小珈乐】

    jl "...."

    scene 练舞室 #【办公室】
    show jl smile   
    with fade
    #【办公室】
    jl "老师，我找到新的目标了，我要申请退出舞团。"
    "【舞蹈老师】" "你怎么也....?"
    "【舞蹈老师】" "唉，真是可惜。"
    #【转场，天台】

    scene tiantai
    show bl normal at l2
    show jl normal at r2 
    hide screen memory_filter
    with fade
    
    jl "第一次和你相遇的时候，我还是个小女孩。"
    jl "舞台上生涩的你，做好了芭蕾的起手式"
    show jl happy with dissolve
    jl "当音乐一响起的瞬间"
    jl "舞台因为你的舞蹈，像是被调色盘上了色一样五彩缤纷。"
    show jl happy with dissolve
    jl "和你在一起的每一个舞台，都让我觉得绚丽多彩。"
    jl "我每天都在想着拉近和你的距离，与你一起舞蹈，唱歌。"
    show jl normal  with dissolve
    jl "我还想再和你一起跳一曲《Trouble Maker》"
    show bl sad with dissolve
    bl "可能我注定不适合站上舞台吧。"
    "贝拉低下头，看着地面。"
    jl "拉姐，你抬抬头，看着我说。 "
    jl "你就这么把我们的梦想，一同放弃了吗？"
    bl "我还能怎么办。A-SOUL是五个人的A-SOUL，放弃然然，别说一个魂看不起我们，我自己都看不起我自己。"
    show jl sad with dissolve
    jl "你怎么可以看不起你自己……贝拉！"
    jl "你有更大的舞台啊，你的、还有我的舞台梦还等着我们去实现……"
    bl "可是我不能就这么抛下队友……"
    bl "我累了，珈乐，让我去做自己想做的事吧。"
    bl "我…或许会去当一个舞蹈老师或者武术教练……"
    "珈乐愤怒地将手掌扬起，看向那张熟悉的脸，还是没能下手。"
    bl "打下来我们两个人都会好受些"
    "珈乐放下了手，哭着跑了出去。"
    hide jl with moveoutright
    hide bl with dissolve

    show jl sad with fade
    jl "早知如此，当初不要相遇就好了..."

    jl "贝拉，你真是个过分的家伙..."
    show jl sad with dissolve
    jl "可恶，可恶…"
    "她要去找毁灭队伍的罪魁祸首算账。"
    #【贝拉随便一首歌的铃声】

    "这时，珈乐的手机突然响起来了。"
    #【短信图】
    "【阿草】" "珈乐，我有个事情想和你单独谈一谈，关于A-SOUL以后的事。"
    "那是阿草的短信。"
    jump .cp2_end


label .cp2_end:
    #########
    # 内容：
    stop music fadeout 4.0
    scene black with Dissolve(3)

    jump cp3_start




