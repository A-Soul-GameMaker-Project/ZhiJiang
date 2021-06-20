label cp6_start:
    #########
    window hide
    $ save.cp_name = "第六章"
    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/6.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True


    # 【场景一】
    scene 病房房间晚上 with dissolve
    window show

    # 【bgm：和平、温馨】
    play music "audio/bgm/电颤琴 枝江.mp3" fadeout 3.0 fadein 3.0

    # 【病房_yoru】
    # 【心电图的滴滴声】

    # {Chapter7 （未定）}
    "【护士】" "好了，等这瓶吊完今天你就可以休息啦。"

    # 【立绘：嘉然_微笑】
    show jr laugh at l2 with dissolve

    jr "谢谢你护士小姐，辛苦你了。"

    # 【立绘：嘉然_微笑】【淡出】
    hide jr

    p "负责输液的护士冲病床上的嘉然莞尔一笑，推着自己那装满医疗用具的小车走出了病房，器械之间零星碰撞的清脆声响在医院夜晚的走廊上回荡。"
    # 【关门的音效、逐渐远去的脚步声、推车的音效】

    p "脚步声渐渐远去，整个世界重新笼罩在治疗仪器运行所发出的白噪音下。"

    "冷风从窗沿的缝隙悄悄地吹入，向晚被这突如其来的寒流冻得一哆嗦，手不自觉地扯了扯身上的外套，鼻腔中吸入的空气满是消毒液的味道。 "

    # 【立绘：向晚_失落】
    show xw gloomy at r2 with dissolve

    xw "…………"

    # 【立绘：向晚_微笑】
    show xw normal with dissolve

    xw "然然你肚子饿了吗？我去给你买蛋糕吧！"

    "十分唐突的搭话，可是向晚清楚，如果不和她一直保持交流的话，眼前这位安静地靠在病床上的少女就会离她越来越远。"

    # 【立绘：向晚_日常】
    show xw smile with dissolve

    xw "呃……这个点可能蛋糕店关门了，要不我给你点外卖去吧！你想吃什么口味的？"

    # 【立绘：嘉然_日常】
    show jr haggard at l2 with dissolve

    jr "你好体贴呀，嗯……，向……，向……"

    "一阵恶寒又突然涌入向晚的身体。"

    "冬天真是一个残酷得让人讨厌的季节。"

    # 【BGM：悲伤、沮丧】
    play music "audio/bgm/emo.mp3" fadeout 3.0 fadein 3.0

    # 【立绘：嘉然_失落】
    show jr lost  with dissolve
    jr "对不起……我好像……" 

    "嘉然用双手抵住额头，姣好的面容因痛苦而变得有些扭曲。"

    # 【立绘：向晚_微笑】
    show xw happy with dissolve

    xw "我叫向晚啦！你要是有一天忘了直接问就行啦，我不会生你气的。当然你如果能记得叫我晚晚我会更开心就是了！"

    # 【立绘：嘉然_微笑】
    show jr laugh with dissolve

    jr "谢谢你。"

    show xw blush with dissolve
    xw "不用这么客气，你忘了我们是队友了吗？"

    "但哪怕身处再刺骨的极寒，向晚也会同嘉然展现出春日般的自我。"

    # 【立绘：嘉然_惊讶】
    show jr shock with dissolve

    # 【立绘：嘉然_失落】
    show jr lost with dissolve

    jr "……"

    show xw sad with dissolve
    "看着嘉然愣住的表情，向晚突然意识到了自己的失言。"

    "因为对嘉然来说，她没法原谅这个忘记了昔日队友的自己。"

    "嘉然是个敏锐的女孩，眼前这个自从失忆后就一直陪伴在自己身旁的人，她知道值得自己去信任与托付。"

    "但是嘉然不管怎么努力，也没法在记忆的迷宫里，用仅剩的碎片，拼凑出自己与她的过去。"

    "这份敏锐强化了失忆给她带来的伤害，她潜意识里总是能察觉到，自己忘记了不该忘记的事，忘记了不该忘记的人。"

    "忘记就是一种背叛，而她不想背叛自己的过去，背叛自己最爱的那些人。"

    "向晚有时候会想，是不是自己什么也不做，悄悄地离开，让A-SOUL的记忆在嘉然的大脑里彻彻底底地消逝，对嘉然来说才是一种解脱呢？"

    # 【立绘：向晚_日常】
    show xw angery with dissolve

    xw "王嘉然！"

    "不是的。"

    "不应该是这样的。"

    # 【立绘：嘉然_惊讶】【立绘震动】
    show jr shock
    with sshake

    jr "……诶？"

    "原本沉溺在自责情绪中的嘉然被突然兴致高涨的向晚吓得一惊。"

    xw "你给我听好了！" 

    show xw proud  with dissolve
    xw "那位个子高高、身材超好，头上顶个红色蝴蝶结，排练的时候凶巴巴，平时却傻乎乎的女人，她叫贝拉，是我们队长！"

    "向晚不是一个偶像力很强的人，她入团之前除了吉他几乎什么也不会，唱跳能力被队友远远甩在身后。"

    show xw shy with dissolve
    xw "然后是那个风情万种，嘴上不饶人，胆子却比谁都小的波浪卷乃琳！没有她我们的小剧场就要乱成一团啦！"

    "向晚也不是一个坚强的人，她会因为排练跟不上队友的步伐而大哭，会因为直播间里不友善
    的评论破防，会跟队友吵架后偷偷地躲在宿舍里擦拭自己的眼泪。"

    jr "嗯……嗯！"

    "嘉然瞪大了自己的小眼睛，试图把向晚说的话一字一句地刻在大脑皮层的每一个细胞里。"

    show xw happy with dissolve
    xw "还有珈乐！身为唱歌特别好听的短发酷盖，在私底下却是个特别温柔亲切的软妹，看不出来吧？我们合唱的时候低音部全靠她撑着哦！" 

    "但向晚从来不是一个为了避免犯错而宁愿什么都不做的人。"

    # 【立绘：嘉然_微笑】
    show jr angery with dissolve

    jr "这次……我……我会记住的……一定会的！" 

    "也从来不是一个看着队友痛苦却袖手旁观的人。"

    # 【立绘：向晚_失落】
    show xw angery with dissolve

    xw "会过去的，嘉然，相信我，相信这个噩梦一定会消失的。"

    "向晚俯身向前，轻轻地握住嘉然那正紧紧攥住被单的小手，一股冰冷的触感从掌心袭来。"
    # 【这里希望能加入一些类似布料或者皮肤摩擦的音效】

    xw "我们一起去找回属于A-SOUL的记忆吧。"

    # 【BGM淡出】
    stop music fadeout 2.0

    # 【场景淡出】
    hide xw 
    hide jr
    # scene 病房房间
    with fade   

    # 【场景二】
    # scene 购物中心早
    # 【购物中心_早】
    scene 购物中心早

    # 【加入一些嘈杂的人群声效】
    play sound "audio/se/熙攘的人群渐弱.mp3" 

    "广场中央的大屏幕：“截至早上八点，新科顶流偶像团体诞生了！”"

    "广场中央的大屏幕：“B-SPIRIT首单《Noise》以令人窒息的速度成功血洗各大流媒体榜单！”"

    "【路人甲】" "开什么玩笑啊，A-SOUL呢？停止活动这么久连一个说明都没有！到底把粉丝当成什么了？"

    "【路人乙】" "把嘉然还给我啊啊啊啊啊啊啊。"

    "【路人丙】" "无所谓了……已经……看不到乃琳……我……我已经……"

    "…………"

    "……"

    stop sound

    # 【场景淡出】


    # 【场景三】
    # scene 购物中心晚
    scene 购物中心晚

    # 【购物中心_傍晚】

    # 【BGM：欢快、轻松】
    play music "audio/bgm/欢快_日常？ 三拍子.mp3" fadeout 3.0 fadein 3.0

    # 【嘈杂的人群声效】
    play sound "audio/se/熙攘的人群渐弱.mp3"
    
    "身处繁华的步行街，向晚拉着嘉然在熙熙攘攘的人流中穿梭。"

    "这里是枝江市最热闹的地段之一，这条街上车水马龙，路人的谈笑声不绝于耳，与昨晚在医院里的那种沉重肃杀的氛围完全不同。"

    # 【嘈杂的人群声效音量减小或淡出】
    stop sound

    # 【立绘：向晚_生气】
    show xw proud at r2  with dissolve
    show jr laugh at l2 with dissolve

    xw "太过分了！"

    "向晚用一股恨不得把脚下的路面踏碎的气势向前走着，以至于好几次撞到迎面走来的行人。"

    # 【立绘：嘉然_日常】

    jr "晚晚，没关系的，也不是什么大事。"

    jr "你老是撞到人，虽然我们特地变了装，但是不小心被人认出来那就糟糕啦……"

    "嘉然乖巧地跟在后面，试图用话语平息向晚的怒火。"

    show xw unconcerned frown with dissolve
    xw "这家KTV怎么回事啊？我昨天明明预约好了的！"

    show xw proud with dissolve
    xw "结果居然跟我说包厢已经满了？啊好累让我歇一会儿。"

    "向晚喘着粗气，不顾自己的淑女形象一屁股坐在了马路中央的花坛围栏旁边。"

    jr "都说叫你走慢点了，消消气吧。"

    "一条可爱的小裙子也紧接着轻盈地落在向晚的身旁。"

    # 【立绘：向晚_日常】
    show xw normal with dissolve

    xw "嘉然，你还记得我们第一次来这家KTV的时候吗？"

    show xw expect   with dissolve
    xw "是在我们第一张团曲首发的当天晚上，公司庆功宴结束之后来的，那天真是玩的太开心了！"

    "自从嘉然失去记忆以后，向晚说话的情绪开始逐渐失去了原有的开朗与激昂。"

    "就连笑容也变得稀有。"

    "可每当快乐的回忆在脑中慢慢收束时，向晚原本紧绷的脸部肌肉还是无法抑制地慢慢舒展开来。"

    "【???】" "那家KTV好像还是我推荐给你们的吧？"
    # 【这里先不要放珈乐立绘，名称先用？？？代替】
    # 【立绘：嘉然_惊讶】
    show jr shock with dissolve

    jr "呜哇！"

    "突如其来的搭话声把嘉然吓得从地上弹了起来。"

    "嘉然转过头，看见一位帅气的蓝紫色短发姐姐正背着手站在她们身后。"

    show jr shock at l3
    show xw expect at lc
    # 【立绘：珈乐_微笑】
    show jl normal at r3 with dissolve

    jl "哎呀，不好意思，吓到小朋友啦。"

    "此时的她满脸微笑，可就算在金色的夕阳光照耀下，还是依旧能感受到她的疲倦。"

    show xw proud  with dissolve
    xw "你迟到咯，珈乐。"

    "向晚也站起身，拍了拍自己衣服刚刚粘上的灰尘。"

    show jl doubt with dissolve
    jl "不是本来定好在我以前经常去的那家KTV嘛？明明是你突然通知我改地方了。"

    show jl smile with dissolve
    jl "而且临时的碰头地点居然是在购物中心的花坛……不知道该说你是心大还是……"

    show xw proud with dissolve
    xw "哼，最危险的地方就是最安全的地方。"

    show jl happy with dissolve
    jl "对自己的变装有自信是好事，但是这种老掉牙的台词还是别再说了比较好哦。"

    jr "诶？……诶……？"

    show jr panic with dissolve
    "看着自然对话的两人，嘉然把两个小眼睛瞪得老大，嘴巴像金鱼一般一张一合。"

    show jl firm with dissolve
    jl "哈喽？你还好吗？"

    "珈乐把身子向靠近嘉然的方向探了探，然后对着嘉然的眼睛挥了挥手。"

    "可困惑和害怕似乎并未从嘉然的眼中散去。"

    show jl normal eyeclosd with dissolve
    jl "啊……原来是不记得我了。"

    show jl normal  with dissolve
    jl "那就只好……咳咳……爱上了也没办法"

    # 【立绘：向晚_惊讶】【立绘震动】
    show xw shock
    with sshake
    # 【BGM：欢快、调皮】
    play music "audio/bgm/日常 滑稽？.mp3" fadeout 1.0 fadein 3.0


    xw "停停停！不要在这种地方一本正经地做自我介绍啊啊啊啊！"

    show jl smile  with dissolve
    jl "不是你叫我跟嘉然见面的时候记得自我介绍的吗！"

    show xw proud with dissolve
    xw "那是以我们在KTV的包厢碰头为前提条件的好吗！"

    xw "而且就算我对自己的变装再怎么自信，也不会在人这么多的地方说出自己的招牌台词的啊！"

    "由于向晚的分贝不断提高的缘故，时不时的有路人向花坛这边望过来。"

    # 【嘉然立绘震动】
    show jr laugh
    with sshake
    jr "嘘！晚晚！你声音这么大不更引人注意了吗！"

    "【路人甲】" "花坛那边好像出什么事了？"

    "【路人乙】" "不清楚，不过好熟悉的声音啊……"

    # 【向晚立绘震动】

    show xw shock
    with sshake
    xw "不好！"

    show xw angery with dissolve
    xw "珈乐！快！赶紧带嘉然转移！"

    "话音未落，珈乐和向晚立马拉起嘉然的手，往人少的小巷跑去。"

    show jr normal  with dissolve
    jr "诶等一下……你们走慢一点！我腿短跟不上你们！"

    # 【三人的立绘淡出】
    hide xw
    hide jr 
    hide jl


    "三个人转眼间消失在人群之中。"

    # 【嘈杂的人群声效】
    play sound "audio/se/熙攘的人群渐弱.mp3"

    "…………"

    "……"

    "【路人丙】" "喂，我刚才好像听见嘉然的声音了。"

    "【路人丁】" "你脑子也烧坏了？我说，你可别变成新闻里的那群人一样啊，太恐怖了。"

    "【路人丙】" "我也不想……但是太久没有A-SOUL的消息好像让我的情绪有点不对劲……"
    "【路人丙】" "嘉然……我好想你啊……嘉然……"

    "…………"

    "……"

    # 【场景淡出】
    stop sound
    # 【场景四】
    scene 贝叶庙
    # 【BGM：和平、温馨】
    play music "audio/bgm/放松 温暖 平静.mp3" fadeout 3.0 fadein 3.0

    # 【贝叶庙1】
    # 【立绘：贝拉_日常（闭眼）】

    show bl normal eyeclosd at r1 with dissolve

    show jl normal at r4 with dissolve
    bl "所以，这就是你们跑得快要断气了的原因？"
    show xw normal at l1 with dissolve
    show jr normal at l4 with dissolve

    "A-SOUL的队长兼舞蹈担当贝拉靠在寺庙正门的红墙上，两只手交叉搭在胸前，一脸无语地看着面前三个气喘吁吁的队友。"

    show bl  normal with dissolve
    bl "还有KTV是怎么回事？向晚你不是让我在庙里等你吗？"

    # 【立绘：嘉然_日常】
    show jr embarrassed with dissolve

    jr "呼……呼……晚晚她是想……先跟珈乐……碰个头……"

    "嘉然喘着粗气，拿出手帕擦拭了一下自己满是汗水的额头，右手伸到胸前扯了扯被汗液浸透而紧紧贴在自己身体上的衬衣。"

    show jr normal with dissolve
    jr "她带着我去我们之前团建的地方……是想帮我……呼……找回我的记忆……呼……"

    jr "呼……呼……"

    # 【立绘：珈乐_日常】
    show jl normal 

    jl "……然然你先喘口气再说话吧。"

    "由于珈乐的身体素质比嘉然好一点，所以经过一段时间的休息之后说话的气息已经基本平稳了下来。"

    "而另外一位紫色钻头的状态似乎就不是那么理想了。"

    # 【立绘：向晚_日常（闭眼）】
    show xw normal eyeclosd with dissolve

    xw "……………………"

    show xw normal  with dissolve
    xw "…………"
    
    show jl helpless with dissolve
    jl "这边这位看样子一时半会是说不了话了。"

    show bl doubt with dissolve
    bl "这才多远的路程啊，居然给你们喘成这样。"

    show bl serious with dissolve
    bl "看来平时我还是对你们太友善了，那就从向晚开始每天加训5公里吧。"

    # 【向晚立绘震动】

    show xw despair
    with sshake
    xw "别！！！！！！！！！！！！！！！"

    show bl normal   with dissolve
    bl "……这不是还能说话吗"

    show xw proud with dissolve
    xw "……毕竟每个人都有不可退让的底线。"

    show jl smile with dissolve
    jl "为什么会在这种奇怪的地方有底线……"

    xw "都怪你先做了惹人注意的事情好吗！"

    show jl firm with dissolve
    jl "一激动就音量拉到Max的人不是很有资格说我哦。"

    "在这两人互怼的间隙，贝拉从自己的背包里拿出一个运动水壶，走到嘉然的面前。"

    show bl soft with dissolve
    bl "然然快喝口水吧。"

    # 【立绘：嘉然_惊讶】
    show jr laugh with dissolve
    
    jr "谢……谢谢！"

    jr "谢谢拉姐！"

    "这是来贝叶庙的路上向晚特地教给嘉然的，嘉然听了之后就一直在心里默念着，默念着这个自己曾经熟悉的陌生称呼。"

    show bl normal  with dissolve
    bl "大家对这里还有印象吗？"

    "贝拉轻轻搂着嘉然的肩膀，四人一齐往庙的内部走去。"

    show jl normal with dissolve
    jl "小的时候我可没少来打扰啊。"

    show bl daze with dissolve
    bl "你就别提了，这里就数你来的次数最多。"

    "贝拉的脸色突然阴郁下来。"

    # 【立绘：贝拉_失落】
    show bl sad  with dissolve

    bl "而且你第一次来的时候，我家的庙还没被拆呢。"

    "从遗留下的废墟的风化程度，能看出这个庙废弃许久了，不过依然能够想象出这个庙香火正旺时的样子。"

    show bl daze with dissolve
    jl "第一次是我妈妈带我来庙里上香，然后就有了我和你的初次见面。"

    # 【立绘：贝拉_微笑】
    show bl normal eyeclosd  with dissolve

    bl "我还记得我们两个在庙里玩捉迷藏玩疯了，阿姨找不到你都急得快报警了！"

    "贝拉转过头一脸坏笑地看着珈乐，身体则像一只小鹿一样在庙堂的废墟中轻盈地来回蹦跳。"

    show bl soft with dissolve
    bl "时间好快啊，没想到我们居然能做这么久的朋友呢！"

    show jl helpless  with dissolve
    jl "…………"

    jl "这才刚到哪儿啊。"

    "不知道是因为刚走过一躺鬼门关，还是久别重新见到贝拉的缘故，珈乐感觉今天的自己情绪异常亢奋。"
    # 【立绘：珈乐_日常】
    show jl normal with dissolve

    jl "…接…接下来的路不管遇到什么困难，我都会陪你一直走下去的" 

    show jl sad with dissolve
    "夕阳染红了珈乐的侧脸，珈乐一边等待着贝拉的回复，一边不安地摆弄起自己纤长的手指。"

    show bl normal eyeclosd with dissolve

    bl "珈乐……"

    # 【立绘：贝拉_日常（闭眼）】
    show bl normal with dissolve

    bl "我也会一直陪你走下去的……"

    # 【立绘：贝拉_微笑】
    show bl soft with dissolve

    bl "和我们A-SOUL所有人一起！"

    # 【立绘：向晚_惊讶】
    show xw shock with dissolve
    # 【立绘：嘉然_惊讶】
    show jr shock with dissolve

    xw "…………"

    jr "…………"

    xw "拉姐，虽然听见你这么说我是很高兴啦……"

    jr "但总觉得不是很合适……"

    play music "audio/bgm/梦幻曲 德彪西.mp3" fadeout 3.0 fadein 3.0
    show bl doubt with dissolve

    bl "诶？怎么了？"

    "贝拉困惑般地张开了嘴，右手挠了挠自己的后脑勺。"

    # 【立绘：贝拉_日常】
    show bl normal  with dissolve

    bl "好像有点扯远了，我们继续刚才的话题吧。"

    show bl smile with dissolve
    bl "除了珈乐以外，其他人第一次来这里是因为之前乃琳组织的户外烧烤吧？"

    show jl smile with dissolve
    jl "当时大家本来定在公园了，结果你非说这个庙附近环境更好。"

    show bl normal eyeclosd with dissolve
    bl "我这不是想家了，有了一点私心嘛。"

    # 【立绘：向晚_日常】
    show xw smile  with dissolve

    xw "啊，我想起来了，因为这里没有自来水，我和乃琳还特地跑了好远，费了好大功夫才搞了几桶水过来呢！"

    # 【立绘：贝拉_日常（闭眼）】
    show bl normal with dissolve

    bl "我还有话要说呢！"

    # 【立绘：贝拉_日常】
    show bl frown with dissolve

    bl "我自己一个人在那研究了半天怎么生火，结果一转头发现带来的点心都被你们吃光了！"

    # 【立绘：向晚_惊讶】
    show xw proud with dissolve

    xw "都是嘉然吃的，不关我的事。"

    # 【立绘：嘉然_惊讶】
    show jr panic with dissolve

    jr "诶？都是我吃的吗？"

    # 【幽默的击打音效】



    show jl normal eyeclosd with dissolve
    jl "你仗着然然失忆搁这搞记忆修正是吧。"

    show jl normal with dissolve
    "珈乐不由分说地冲着向晚的脑袋上地来了一记蓄意轰拳。"

    # 【向晚立绘震动】

    show xw wronged
    with sshake
    xw "痛痛痛……别打了，再打我就要变得更笨啦！"

    "向晚斜了一眼珈乐，委屈地嘟起了自己的小嘴。"

    # 【立绘：贝拉_日常】
    show bl normal  with dissolve

    bl "不过然然那个时候确实是挺能吃的，练完舞就要点奶茶，下完播还经常跟我撒娇要我帮她煮面。"

    show jl normal with dissolve
    jl "明明就是不久前的事情，说起来却感觉已经距离我们很遥远了。"

    show bl soft     with dissolve
    bl "大概是经历了很多事情的缘故吧。"

    show bl normal eyeclosd with dissolve
    "说到这里贝拉露出了一丝不易察觉的苦笑。"

    show bl normal with dissolve
    "不过随即就又恢复成了平常的那个元气队长。"

    show bl care with dissolve
    bl "不知道生病这几天然然在医院有没好好吃饭呢？"

    "贝拉轻轻揉了揉嘉然的脸。"

    # 【立绘：向晚_日常（闭眼）】
    show xw normal eyeclosd with dissolve

    xw "哼，你们放心吧，你们不在的时候我把她照顾的可好了。"

    show xw normal with dissolve
    xw "一天三顿一顿没落下，晚上饿了还再加个草莓蛋糕！"

    # 【立绘：嘉然_惊讶】
    show jr shock with dissolve

    jr "我……我哪有那么能吃！"

    # 【立绘：嘉然_微笑】
    show jr laugh with dissolve

    jr "不过，晚晚确实把我照顾的很好……"

    xw "…………"

    # 【立绘：珈乐_惊讶】
    show jl firm with dissolve

    jl "诶？向晚你的脸怎么突然……"

    # 【立绘：向晚_生气】
    show xw angery with dissolve
    # 【向晚立绘震动】
    with sshake

    xw "吵死了！要你管！"

    # 【珈乐立绘震动】

    show jl smile
    with sshake
    jl "等一下！怎么一言不合就要打人啊！我关心你一下而已嘛！"

    show bl normal eyeclosd with dissolve
    bl "晚晚真可靠啊。"

    show bl normal   with dissolve
    bl "我这个做队长的感到很欣慰！"

    # 【立绘：向晚_害羞】
    show xw shy with dissolve

    xw "哎呀……我不过是做好自己分内的事情罢了。"

    xw "不管是对嘉然也好，还是对你们也好。"

    # 【立绘：珈乐_微笑】
    show jl smile with dissolve

    jl "好了贝拉，你再夸她，她的脸就红的要烧开啦。"

    show xw proud with dissolve
    xw "哪有你说的那么夸张啊……"

    # 【立绘：贝拉_微笑】
    show bl soft     with dissolve

    bl "行吧行吧，时间也不早了，我们先回宿舍去吧。"

    show jr shock with dissolve
    jr "宿舍？"

    # 【立绘：向晚_日常】
    show xw normal   with dissolve

    xw "…………"

    show xw calm with dissolve
    xw "嘉然好久没回去了吧，忘了也是情有可原。"

    show jl firm with dissolve
    jl "是我们以前一起生活的地方哦。"

    show bl smile with dissolve
    bl "忘记有什么大不了的？然然晚上来我房间睡吧，我给你讲鬼故事~~~"

    show xw gloomy with dissolve
    xw "不行啊拉姐，我不敢一个人睡的。"

    show jl happy with dissolve
    jl "要来跟我一起吗？"

    show xw unconcerned frown with dissolve
    xw "还是免了。"

    stop music

############
    # 【场景淡出】

    # 【场景五】
    scene 玄关熄灯
    with fade   

    play music "audio/bgm/悬疑诡异气氛通用BGM1.mp3" fadeout 3.0 fadein 6.0

    "咔哒。"
    play sound "audio/se/室内关门.mp3"

    "伴随着一记清脆的声响，宿舍的大门被静静地推开。"

    "一个轻巧的优雅身影无声地从大门摸进宿舍的玄关，开始在玄关附近慢慢摸索。"

    # 【立绘：贝拉_日常】
    show bl normal at r1 with dissolve

    bl "没问题了，大家可以进来了。"

    "一直躲在门外等待贝拉指示的三人这才敢放心走入宿舍。"
    # 【立绘：嘉然_日常】
    # 【立绘：珈乐_日常】
    show jl normal at r4 with dissolve   


    # 【立绘：向晚_日常】
    show xw normal at l1 with dissolve   
    show jr normal at l4 with dissolve

    bl "我检查了一下，似乎那些人没有在我们宿舍设置机关，今天晚上应该可以放心地在这里休息了。"

    show jr embarrassed with dissolve
    jr "好黑啊。"

    show xw happy with dissolve
    xw "我来开一下灯吧，我记得开关好像是在……"

    show jl angery with dissolve
    jl "等一下！"

    # 【立绘：向晚_惊讶】【向晚立绘震动】
    show xw shock with dissolve
    with sshake

    "向晚已经快要摸到开关的手被珈乐一把抓住。"

    xw "怎么了？"

    jl "你们仔细听，好像房子里有动静。"

    "四个人屏住呼吸，用耳朵努力着去捕捉任何一点风吹草动。"

    show bl doubt with dissolve
    bl "我怎么没听见？"

    # 【立绘：向晚_日常】
    show xw normal  with dissolve

    xw "我也没有……"

    show jr shock with dissolve
    jr "我听见了，好像在房子里是有一些奇怪的声音。"

    show jl doubt with dissolve
    jl "我们先别声张，去客厅看看。"

    # 【场景淡出】

    with fade 
    # 【场景六】

    # 【无BGM】
    # 【客厅_熄灯】
    scene 客厅熄灯

    # 【立绘：贝拉_惊讶】
    show jl normal at r4 with dissolve     

    show bl shock at r1 with dissolve
    show xw shock at l1 with dissolve
    show jr normal at l4 with dissolve

    bl "啊，我也听到了。"

    # 【立绘：向晚_惊讶】

    xw "有男的声音在说话！"

    bl "果然还是追到这里来了吗？"

    # 【立绘：嘉然_日常】

    jr "你们快看，浴室的灯是开着的。"

    "透过浴室半透明的磨砂玻璃门看去，浴室里依稀可见活动着的人影。"

    show jr shock with dissolve
    jr "里面还有水流的声音。"

    # 【微弱的水流音效】
    play sound "audio/se/微弱水流声.mp3"

    # 【立绘：珈乐_日常】

    jl "大家冷静一点，现在敌在明我在暗，优势在我们这里。"

    # 【立绘：向晚_日常】
    show xw normal  with dissolve

    xw "…………"

    show xw angery with dissolve
    xw "我已经受够了被动的防守了，拉姐，我觉得我们应该在这里进行一波反击。"

    # 【立绘：贝拉_日常】
    show bl serious with dissolve

    bl "我认同向晚意见，这次机会难得，我们应该主动出击。"

    show jl firm with dissolve
    jl "保险起见，让嘉然留下，我们三个人一起冲进去吧。" 

    # 【立绘：嘉然_失落】
    show jr distressed with dissolve

    jr "我……我也想跟你们一起去。"

    "队长轻轻地把嘉然拉到自己怀中，温柔地看着嘉然的眼睛。"

    # 【立绘：贝拉_微笑】
    show bl soft  with dissolve

    bl "没关系的，A-SOUL出道的时候你帮我们承担了许多，现在也该我们来保护你了。"

    jr "贝拉……"

    # 【立绘：向晚_日常】
    show xw normal  with dissolve

    xw "咳咳……不好意思打扰一下二位，我觉得还是先解决浴室里面的人要紧。"

    show jl angery with dissolve
    jl "咳咳……我觉得向晚说得对，里面的人随时可能出来，到时候形势就对我们不利了。"

    show bl normal eyeclosd with dissolve
    bl "啊，说的也是。"

    show bl normal  with dissolve
    bl "那，我们就上吧！"

    "三个人随即各自摆出自己擅长的进攻态势，一步一步地往浴室走去。"

    show bl serious with dissolve
    bl "你们听好了，倘若等下局势对我们不利，就由我来拖住他们，你们一定要带着嘉然跑。"

    show jl firm with dissolve
    jl "我是不可能弃你而去的。"

    show xw angery with dissolve
    xw "水母的词典里可没有收录关于逃跑的条目啊。"

    jr "大家，一定要平安回来啊！"
    # 【立绘：贝拉_惊讶】
    show bl shock with dissolve

    bl "哈！"
    # 【门被撞击的音效】

    "作为领头羊的队长贝拉一脚踹开了浴室的玻璃门。"

    # 【场景淡出】
    hide jr
    hide bl 
    hide jl 
    hide xw
    with fade   
    # 【场景七】

    # 【无BGM】
    # 【浴室_晚】
    scene 浴室晚

    # 【立绘：贝拉_日常（闭眼）】
    show jl normal eyeclosd at r4

    show bl normal eyeclosd at r2 
    # 【立绘：珈乐_日常（闭眼）】
    # 【立绘：向晚_日常（闭眼）】
    show xw normal eyeclosd at l2 

    show jr thinking at l4
    play music "audio/bgm/日常 滑稽？.mp3" fadeout 3.0 fadein 6.0

    "【众人】" "…………………………………………"

    # 【立绘：乃琳_失落】
    show nl blush  with dissolve

    nl "怎么会这样……"

    nl "仅仅只是分别了几天……"

    nl "我的队友居然……"

    show nl surly with dissolve
    nl "成了会在别人洗澡的时候闯进来的变态。"

    # 【BGM：欢快、调皮】

    show bl normal
    show jl normal
    show xw proud
    xw "果咩纳塞！"

    show jl firm with dissolve
    jl "是向晚威胁我的……"

    show bl soft with dissolve
    bl "对不起，脚滑。"

    "五分钟前还趾高气扬的三个人，现在正整齐地跪在乃琳的面前，膝盖底下垫着三块搓衣板。"

    # 【立绘：嘉然_日常】
    show jr normal with dissolve

    jr "报告乃琳，我没有看到你洗澡哦。"

    # 【立绘：乃琳_微笑】
    show nl sneer  with dissolve

    nl "然然乖哦~"

    show nl happy with dissolve
    nl "不过如果是你的话，姐姐陪你一起洗也不是不可以。"

    # 【立绘：向晚_惊讶】
    show xw shock with dissolve

    xw "什么犯罪宣言？"

    # 【立绘：珈乐_日常】
    show jl normal with dissolve

    jl "小朋友，不可以被这个坏女人骗了哦。"

    # 【立绘：贝拉_失落】
    show bl serious with dissolve

    bl "乃琳，我好像有点看错你了。"

    # 【立绘：乃琳_生气】
    show nl frown  with dissolve

    nl "我的身体被你们看光的事情还没算完账呢好吧。"

    # 【立绘：向晚_日常】
    show xw wronged with dissolve

    xw "这也不能完全怪我们啊乃琳，为什么你回宿舍了不开灯啊？"

    # 【立绘：乃琳_日常】
    show nl normal   with dissolve

    nl "我不是说了好几次我个人喜欢昏暗的环境吗……"

    show nl happy with dissolve
    nl "而且你们都没有回来，就我一个人为什么要开灯啊。"

    show jl doubt   with dissolve
    jl "那你浴室里怎么会有男人的声音？"

    nl "…………"

    show nl helpless with dissolve
    nl "我在看比赛……那是解说的声音……"

    # 【立绘：贝拉_日常】
    show bl normal   with dissolve

    bl "乃琳我们知道错了，可以让我们先站起来吗，反正也不是第一次看了。"

    show xw blush with dissolve
    xw "很喜欢嘉然的一句话，乃琳刚洗完澡最好看。"

    # 【立绘：嘉然_惊讶】
    show jr shock with dissolve

    jr "诶？我说过吗？"

    # 【立绘：珈乐_日常（闭眼）】
    show jl normal with dissolve

    jl "……这次你好像还真说过。"

    # 【立绘：乃琳_日常】
    show nl normal   with dissolve

    nl "算了，这次就先原谅你们了。"

    nl "我们去客厅聊吧。"

    # 【场景淡出】
    hide jr
    hide nl
    hide jl
    hide bl
    hide xw 
    with fade   
    # 【场景八】

    # 【BGM：无】
    # 【客厅_晚】
    scene 客厅夜
    play music "audio/bgm/放松 温暖 平静.mp3" fadeout 3.0 fadein 3.0

    # 【立绘：向晚_微笑】
    show xw smile at l2 with dissolve
    xw "宿舍的沙发！我好想你啊！"

    "刚走出浴室，向晚就飞扑到沙发上，开始在沙发上打滚。"

    # 【立绘：嘉然_日常】
    show jr normal at l4 with dissolve

    jr "这里就是我们以前生活的地方吗？"

    # 【立绘：贝拉_微笑】
    show bl soft at r2 with dissolve

    bl "对啊，这里对我们来说就是第二个家。"

    # 【立绘：珈乐_日常】
    show jl normal at r4  with dissolve

    jl "又想起放假的时候五个人聚在客厅一起看电影的时光了。"

    # 【立绘：乃琳_微笑】
    show nl smile with dissolve

    nl "是啊。"

    # 【立绘：乃琳_失落】
    show nl sad with dissolve

    nl "如果贝拉能少放点恐怖片那就是一段完美的记忆了。"

    bl "我是觉得人多看恐怖片才有意思嘛。"

    # 【立绘：向晚_日常】
    show xw normal with dissolve

    xw "抱歉啊嘉然。"

    # 【BGM：严肃、沉重】	


    "向晚从沙发坐起来，摆出了一副认真的态势。"

    show xw gloomy with dissolve
    xw "等一切结束了之后，我们就可以带你重新体验当时的生活了。"

    xw "可惜今天晚上我们还有更重要的事情要商量。"

    "一连串严肃的发言让客厅内的空气似乎在一瞬间冻结了。"

    # 【立绘：贝拉_日常】
    show bl normal eyeclosd  with dissolve

    bl "要到决战的时候了。"

    bl "自从这场闹剧发生以来，不论是我们A-SOUL成员，还是一个魂。"

    show bl normal   with dissolve
    bl "都承受了太多不该承受的痛苦了。"

    bl "而现在，只有我们有能力去终结一切痛苦的源头。"

    show bl serious with dissolve
    bl "阿草无论在打什么算盘，都必须由我们来阻止。"

    show jl firm with dissolve
    jl "只是……"

    jl "以目前的情报来看，阿草想要利用嘉然达成的目的，恐怕远比我们想象的更恐怖。"

    # 【立绘：嘉然_失落】
    show jr lost with dissolve

    jr "…………"

    jr "对不起……"

    jr "我虽然失忆了，但是最近总能隐隐约约感受到某些心声。"

    show jr sad with dissolve
    jr "这些心声都是痛苦的，扭曲的。"

    jr "而这一切负面情绪的来源就是我。"

    show jr angery with dissolve
    jr "所以想要摆平这一事件，似乎不依靠我是不行的。"

    "嘉然苦笑了一下，但眼神中依然透出一股坚毅。"

    # 【立绘：向晚_失落】
    show xw gloomy with dissolve

    "听完嘉然的一番话，向晚露出了十分复杂的表情，她内心有不好的预感，但是看着集结在这里的几个队友，五个人在一起给她的信心还是把恐惧给压了下去。"

    "我们A-SOUL五个人就是无所不能的。"

    "这是向晚在入团的第一天就秉持的信念。"

    # 【立绘：向晚_日常】
    show xw normal with dissolve

    xw "不管怎么样，我都支持你的决定。"

    show xw angery  with dissolve
    xw "我们四个人会帮助你完成你的任务的。"

    show jr normal with dissolve
    jr "谢谢你，晚晚。"

    # 【立绘：乃琳_日常】
    show nl normal   with dissolve

    nl "我个人觉得，当务之急应该是安抚粉丝。"

    nl "这几天我一直有在留意各种社会新闻，如果我们再不出面的话，一个魂们的情绪会被有心人利用的。"

    "心思细腻的向晚也留意到这几天走在马路上总能感觉到整个社会处于一种不对劲的氛围之中。"

    show jl helpless with dissolve
    jl "可是我们现在各种社交平台的账号已经被公司控制了。"

    jl "而且现在网络上任何关于A-SOUL的消息都必须接受审查才能对外公布，也就是说我们无论以什么方式在公网上发送信息都会大概率被检测到然后删除。"

    # 【立绘：珈乐_日常（闭眼）】
    show jl normal eyeclosd with dissolve

    jl "可以说在网络空间对外发声的渠道基本被堵死了。"

    show xw normal with dissolve
    xw "我有想过是不是能在现实中召开一个集会。"

    xw "但那样的话我们的安全没法受到保障。"

    # 【立绘：贝拉_失落】
    show bl sad with dissolve

    bl "突然好怀念能跟一个魂们自由交流的时光啊……"

    bl "没有想到也有我们的心声无法传递给他们的一天。"

    jr "…………"

    show jr thinking with dissolve
    jr "没用的，这些对扑灭粉丝的负面情绪也只不过是杯水车薪。"

    jr "如果我不去完成那个的话……啊……"

    show jr lost with dissolve
    "嘉然的表情突然变得扭曲，头慢慢地低了下去。"

    jr "头好痛……"

    play music "audio/bgm/鲸.mp3" fadeout 4.0 fadein 5.0

    show nl surly with dissolve

    nl "…………"

    nl "…………似乎是又有新一批意识通过那个装置想要接入嘉然的大脑了。"

    show nl care with dissolve
    nl "那你知道该怎么做比较好吗，嘉然？"

    show jr lost with dissolve
    jr "我必须得去……得去那个高台……"

    jr "去完成……那个仪式……"

    # 【立绘：向晚_惊讶】
    show xw shock with dissolve

    xw "高台……仪式……"

    # 【立绘：向晚_日常（闭眼）】
    show xw normal eyeclosd with dissolve

    xw "我知道了。"

    # 【立绘：向晚_日常】
    show xw unconcerned frown  with dissolve


    "向晚不置可否，久久沉默"


    # 【立绘：贝拉_日常】
    show bl normal eyeclosd  with dissolve

    bl "既然这样的话。"

    show bl normal with dissolve
    bl "我们不如来分配一下任务吧。"

    # 【立绘：珈乐_日常】
    show jl normal  with dissolve

    jl "你身手最好，这几天一定要形影不离地跟着嘉然。"

    jl "保证她不会出什么意外。"

    show jl angery with dissolve
    jl "至于我的话，我很熟悉枝江大厦的内部构造。"

    jl "我可以试试看潜入进去安装几个间谍设备监视他们，如果有什么风吹草动第一时间告诉你们。"

    # 【乃琳：立绘_日常】
    show nl normal  with dissolve

    nl "去往高台的沿途交通就交给我吧，尽量帮你们规划出一条合理的线路来。"

    nl "至于向晚。"

    nl "我要你跟贝拉一起呆在嘉然身边。"

    show nl care with dissolve
    nl "看嘉然的样子，她现在精神状态应该已经快到极限了。"

    nl "而她到现在还能保持自我，除了她自身是个坚强的孩子以外。"

    nl "一定也是因为还有你在一直照顾她，陪伴她。"

    nl "现在她失忆越来越严重，我们五个人中你已经是她的唯一精神寄托了。"

    nl "不要让她感到太痛苦。"

    show xw angery with dissolve
    xw "嗯……我会的……"

    xw "嘉然的使命也是我的使命。"

    # 【立绘：珈乐_日常（闭眼）】
    show jl normal eyeclosd with dissolve

    jl "呼，说了这么多，感觉有点闷了。"

    # 【立绘：珈乐_日常】
    show jl normal with dissolve

    jl "透透气吧。"

    # 【落地窗被拉开的音效】
    play sound "audio/se/开窗window1_C.mp3"

    "珈乐走向客厅的落地窗，把窗子打开了一半。"

    "窗外的天空中，月光把几片轻薄的云朵照得微微发亮。"

    "向晚被清朗的夜空所吸引，不自觉地朝窗外的阳台走去。"

    # 【场景淡出】
    scene 天台

    with fade 

    # 【场景九】


    play music "audio/bgm/钢琴1 缓和.mp3" fadeout 4.0 fadein 5.0
    # 【0.5月_云】

    "一走上阳台，向晚就感觉到一股清冷的风把自己包围。"

    "这让事件发生以来就一直糊成一团的大脑久违地体会到了清爽。"

    "而且比起之前在医院时所感受到的风，这一次向晚感到了些许温暖。"

    # 【立绘：向晚_日常】
    show xw normal at l2  with dissolve

    xw "春天，好像要到了。"

    "想起A-SOUL刚出道就面临着无数的诋毁与攻击，而风评开始逆转，整个企划走向正轨，似乎就是在春天。"

    "在这之后从来就没有遇到过能够阻碍A-SOUL发展的脚步的困难。"

    "A-SOUL就这样势如破竹地成为枝江市名副其实的TOP1偶像团体。"

    "没有理由相信A-SOUL会在这里倒下。"

    # 【立绘：乃琳_日常】
    show nl normal at r2 with dissolve
    
    nl "一个人在阳台想什么呢？"

    "不知什么时候乃琳已经轻轻地贴近了向晚身边，沐浴后身体所散发的清香扑鼻而来，再加上此时浪漫的月色，让向晚一时间感到有所恍惚。"

    "真是个可怕的女人。"

    "向晚不禁暗自感叹。"

    show xw worried with dissolve
    xw "我在想今天吃什么。"

    "如果跟乃琳说自己在感时伤怀什么的，实在有点太难为情了。"

    show nl helpless with dissolve
    nl "别骗人了。"

    "真是个可怕的女人啊。"

    "向晚不禁再次暗自感叹。"
 
    show nl normal with dissolve
    nl "对于决战的事情，你有信心吗？"

    show xw angery with dissolve
    xw "现在的我比以往的任何时候都更有信心。"

    nl "那就好。"

    nl "不过，有一些事情我觉得还是得应该让你知道。"

    show nl sad with dissolve
    nl "我这一次行动，了解到了一些……"

    nl "枝江市背后的，不可告人的秘密。"

    show xw shock at l2 with dissolve
    xw "跟嘉然有关的吗？"

    # 【立绘：乃琳_失落】
    show nl surly with dissolve 

    nl "岂止是有关。"
    # 【立绘：乃琳_日常】
    show nl normal   with dissolve

    nl "不知道向晚之前你有没有好奇过。"

    show nl frown with dissolve
    nl "为什么明明是以偶像产业为主的枝江市，所具有生产力却能够远远超过其他发达城市？"

    nl "那就是因为情绪的存在。"

    # 【立绘：向晚_惊讶】
    show xw shock with dissolve

    xw "情绪？生产力和情绪有什么关系？"

    nl "我了解到，枝江市的统治者手中，持有一种装置。"

    nl "这种装置能够把人的憧憬、希望、梦想等正面情绪，转化成有效的生产力。"

    xw "……闻所未闻。"

    show nl sad with dissolve
    nl "那么，作为这个世界上贩卖梦想与希望的职业…………"

    # 【立绘：向晚_失落】
    show xw gloomy with dissolve

    xw "也就是偶像。"

    # 【立绘：乃琳_生气】
    show nl angery with dissolve

    nl "没错。偶像。成为了枝江市统治者用来引导民众正面情绪的来源。"

    nl "民众通过消费偶像产生正面情绪，然后统治者再利用这种特殊的装置来将其转化为生产力。"

    # 【立绘：向晚_生气】
    show xw angery with dissolve

    xw "…………"

    "一想到自己一直以来的梦想，只不是某些人随意使用的工具，向晚就气的浑身发抖。"

    # 【立绘：乃琳_日常】
    show nl normal   with dissolve

    nl "如果故事只到这里，这还能算可以接受。"

    # 【立绘：乃琳_失落】
    show nl sad with dissolve

    nl "可惜世界上所有事情都是有代价的。"

    # 【立绘：乃琳_日常】
    show nl normal with dissolve

    nl "所引导出的正面能量超出一个阈值时，这条钟形曲线也到了下坡的时候。"

    nl "而统治者为了保证这一机制能够良好运转，选择的做法是……"

    # 【立绘：乃琳_失落】
    show nl sad with dissolve

    nl "献祭掉那个偶像。"

    "说到这里，乃琳回头看了一眼坐在客厅内的嘉然。"

    # 【立绘：向晚_惊讶】
    show xw shock with dissolve

    xw "献……献祭？"

    # 【立绘：乃琳_生气】
    show nl angery with dissolve

    nl "他们会煽动粉丝，把粉丝对偶像的爱扭曲成恨意。"

    nl "能够进入枝江学院的偶像都是统治者通过大数据精挑细选出来的，他们通过性格，经历去筛选需要的人才，选出那些独自一人承受粉丝汹涌恶意。"

    nl "还愿意牺牲自己去净化粉丝负面情绪的偶像，给她们倾斜资源。"

    nl "而嘉然，是他们这次计划的重中之重，他们把能够联通粉丝情感的药物给嘉然服用，这种药物的副作用就是失去记忆，直至彻底与粉丝心中的理想的形态同调，就能举行仪式。"
    
    # 【立绘：乃琳_失落】
    show nl sad with dissolve

    nl "这种仪式也是净化粉丝恶意的唯一手段。"

    # 【立绘：向晚_失落】
    show xw sad with dissolve

    xw "所以嘉然才说，不靠她去完成仪式是不行的。"

    nl "他们只是把这件事告诉了嘉然，嘉然就主动答应献祭的事情了，她什么条件都没提。"

    nl "她只是想让大家的生活过得更好一些。"

    xw "....天生的偶像"

    show xw sad
    xw "就算嘉然是自愿的，可是这样一来我们就要失去嘉然了。"

    nl "可是，如果她不去完成那个仪式的话。"

    nl "那么所有的粉丝都将会走向疯狂。"

    "向晚沉默了半晌，一时有些迷茫。"

    # 【立绘：乃琳_日常】
    show nl normal eyeclosd

    nl "先不用这么悲观。"

    nl "会选择自毁的偶像往往都是完全失去了精神依托。"

    show nl normal
    nl "可嘉然不一样，只要她还记得你，把你当做精神依靠。"

    # 【立绘：乃琳_微笑】
    show nl smile with dissolve

    nl "事情就说不定会有转机。"

    xw "…………"

    "一股无形的压力又重重地落在了向晚身上。"

    "不过不能在这里泄气，好不容易走到这一步了，绝对不能在这里停下来。"

    # 【立绘：向晚_日常】
    show xw normal   with dissolve

    xw "你说的对，我也相信我们A-SOUL是特别的。"

    xw "只要我们五人一起努力的话，问题总会有方法解决的。"

    nl "看到你能这么想我就放心多了。"

    nl "我们回去吧，这里开始变得越来越冷了。"

    show xw gloomy with dissolve
    xw "走吧，现在这个节骨眼上要是生病了可就麻烦了。" 

    nl "哦还有，这件事情，暂时先跟他们保密吧。"

    nl "等到合适的时机再跟她们坦白。"

    "向晚轻轻地点了点头。"

    if persistent.playthrough > 1:
        xw "乃琳你听说过，我们的粉丝举措越来越激进了这件事吗？"

        "乃琳看了向晚一眼。"

        nl "谁知道呢。"

    # 【场景淡出】
    hide xw 
    hide nl
    with fade   

    # 【场景十】

    # 【BGM：和平、温馨】
    # 【客厅_晚】
    scene 客厅夜

    # 【立绘：珈乐_日常】
    show jl normal at r4  with dissolve
    show bl smile at r2 with dissolve

    show nl normal with dissolve
    show xw smile at l2 with dissolve

    show jr laugh at l4 with dissolve

    jl "你们回来啦。聊了些什么？"

    # 【立绘：乃琳_微笑】

    nl "没什么，看了看月亮。你们在干什么呢？"

    jl "贝拉从冰箱里找到了一块草莓蛋糕，她和嘉然应该在厨房切蛋糕呢。"

    # 【立绘：嘉然_微笑】

    jr "大家一起吃吧。"

    "贝拉和嘉然两个人端着五人份的蛋糕从厨房走来。"

    # 【立绘：向晚_微笑】
    show xw smile with dissolve

    xw "刚好我肚子饿了。"

    # 【立绘：珈乐_微笑】
    show jl smile with dissolve

    jl "这份小的给我吧，嘉然你吃这块。"

    # 【立绘：乃琳_生气】
    show nl angery with dissolve

    nl "今天的卡路里摄入又要超标了。"

    # 【立绘：贝拉_微笑】
    show bl smile with dissolve

    bl "多消耗消耗就好。"

    "嘉然默默地看着正大快朵颐的四个人，眼角开始有些微微湿润。"

    jr "大家，我想说。"

    show jr laugh with dissolve
    jr "我今天真的好开心。"

    jr "自从住院以来已经很久没有这么开心过了。"

    show jr lost with dissolve
    jr "真的很谢谢大家……"

    show jl normal with dissolve
    jl "不用不用，我们都是A-SOUL的一员。"

    # 【立绘：珈乐_日常】
    show jl normal   with dissolve

    jl "而且我们的故事还远远没有结束呀。"

    # 【立绘：贝拉_日常（闭眼）】
    show bl normal eyeclosd with dissolve
    bl "现在说结尾祝词还太早了哦。"

    # 【立绘：贝拉_日常】
    show bl normal with dissolve

    bl "我们还有很多舞要和你一起练呢。"

    # 【立绘：乃琳_日常】
    show nl normal with dissolve

    nl "事情结束之后我们把之前没打完的游戏一起打通关吧！"

    xw "还要一起去吃更好吃的蛋糕！"

    # 【结尾CG】

    "仅此一刻，大家可以把对抗与阴谋抛在脑后，把情绪从窒息的泥潭中解放出来。"

    "五人那往日熟悉的笑颜又再次出现，温暖的日常也重新填满了宿舍。"

    "属于A-SOUL的黎明一定会到来。"

    "这是此时向晚唯一的感受。"

    stop music fadeout 3
    scene black with Dissolve(3)
    if persistent.playthrough == 4:
        menu:
            "无知之人扑了个空，娇小的少女踏上归途。":
                jump cp7_g_start
            "然而在黎明到来之前，娇小的少女已经被无知的人掳走。":
                jump cp7_n_start

    jump .cp6_end



label .cp6_end:
    #########
    # 内容：

    if persistent.playthrough == 1:
        jump cp7_n_start
    elif persistent.playthrough <= 3:
        jump cp7_g_start



