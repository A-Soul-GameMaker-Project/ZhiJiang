label cp5_start:
    window hide
    $ save.cp_name = "第五章"
    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/5.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True

    scene black
    show screen saying("隐蔽自我，推卸责任，偶像的外表，一定要光鲜亮丽。" ,0.5,0.4,30,addImg=True) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)

    show screen saying("间谍也是如此。" ,0.5,0.4,30,addImg=True) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)

    jump .part1

label .part1: #两支箭

    #【场景 枝江市广景-傍晚】
    #【BGM 鸟叫虫鸣声】
    scene 枝江市广景傍晚 with dissolve
    play music "audio/se/虫鸣鸟叫声.mp3" fadein 2.0
    window show

    "夜晚是副面具。"
    "如今的枝江，正要把这面具戴在脸上。"
    "凉风，吹过无辜的城。"

    scene 病房晚 
    show nl normal at l2
    show xw sad at r2

    with dissolve
    #【BGM 悲伤/例 风居住的街道】
    play music "audio/bgm/第一章医院.mp3" fadeout 3 fadein 3.0
    nl "晚晚，睡一会儿吧。"
    #【立绘 向晚-悲伤】
    xw "睡不着。"

    "向晚依旧守候在嘉然的床榻旁，握着粉红少女柔弱纤细的小手，愁眉不展。"
    #【立绘 乃琳-悲伤】
    show nl sad at l2
    show xw sad at r2
    with dissolve
    "乃琳靠过去，女孩一抬头，露出的就是通红的眼眶。"
    "这孩子一定又在偷偷抹眼泪了。乃琳心想。"
     #【立绘 乃琳-日常】
    show nl normal with dissolve
    nl "要是你明早顶着个黑眼圈被贝拉发现了，我们两个可是都要挨棍的哦？"
     #【立绘 向晚-悲伤】
    xw "拉姐她……"
     #【立绘 乃琳-日常】
    nl "瞎想什么呢，傻姑娘。"
    "乃琳抓住女孩冰凉的手，坚定有力地握住。"
    nl "你要记住，我们的心意是相通的。要是贝拉知道你在担心她，她就发挥不出正常水平了。"
     #【立绘 向晚-悲伤】
    show xw normal with dissolve
    xw "乃琳，你是不是……知道什么啊？"
     #【立绘 向晚-日常】
    "女孩强挤出的笑颜，看得乃琳心里一阵绞痛。"
    #【立绘 乃琳-悲伤】
    show nl sad with dissolve
    "她知道一切的真相吗？"
    "她扪心自问，不知。"
    "可危难时刻，没尽到力，就是最大的不负责任。"
    nl "唉。"
    "她叹了口气，摊摊手，没有回答。"
     #【立绘 向晚-悲伤】
    show xw sad with dissolve
    "她多希望，晚晚能坚强起来，独当一面，不让她操心。"
    "她又多希望，晚晚能一直这样，软软的，保持着天真，被她保护。"
     #【立绘 乃琳-悲伤】
    "向晚比以前成熟了。"
    nl "晚晚，我给你讲个故事吧？"
     #【立绘 向晚-悲伤】
    xw "嗯。"
     #【立绘 乃琳-日常】

    show nl normal with dissolve
    nl "很久很久以前，希腊有个太阳神，叫阿波罗。"
     #【黑屏转出】
     #【场景 天空-满月】
    play music "audio/bgm/阿拉伯风1 德彪西.mp3" fadeout 4 fadein 4
    scene 夜空满月 with fade
     #【BGM 诗意/例 青空】
    "玉盘高挂，微风吹拂。"
    "月光照在乃琳的身上"
    nl "从前，太阳神阿波罗看到小爱神丘比特在摆弄自己的弓箭。"
     #【场景 乡村-仓库-午】
    scene 乡村仓库 with dissolve
     #【无立绘】
    nl "太阳神警告丘比特，箭是成年人才能玩的东西，嘲笑他只是个小孩子。"
    nl "丘比特不服气，正巧这个时候，走来了一位名叫达芙妮的美丽少女。"
    nl "小爱神张弓搭箭，让阿波罗爱上了那位少女，却又让达芙妮深深地厌恶爱情。"
     #【场景 病房房间-夜】
    scene 病房晚 with dissolve
     #【立绘 向晚-惊讶】

    show xw shock at r2
    show nl happy at l2
    with dissolve
    xw "丘比特的箭也会对太阳神生效嘛？"
     #【立绘 乃琳-喜悦】
    nl "因为人类的爱是无穷无尽的呀。"
     #【场景 河边-早】
    scene 河边 with dissolve
     #【无立绘】
    nl "阿波罗不舍昼夜地追求达芙妮，可少女拼了命要摆脱他。"
    nl "眼见心上人躲进深山不肯出来，太阳神心里着急，就拿出竖琴，演奏起美妙的乐曲。"
    nl "达芙妮被乐曲打动，双脚抑制不住地，带她走出山洞，和阿波罗见面。"
    nl "她被心中燃起的爱意吓坏了，憎恶自己的不洁。"
    scene 神界树 with dissolve
    nl "她再度奔逃，直至走投无路。河神怜惜她，将她变成了一棵月桂，深深扎入泥土中。"
    #【场景 神界-树】
    #【无立绘】
    nl "由于太阳神的垂爱，终年常青。"
    #【场景 病房房间-夜】
    scene 病房晚 with dissolve
    #【立绘 向晚-惊讶】
    show xw shock at r2
    show nl normal at l2
    with dissolve
    #【BGM 放松/例 夏夜】

    xw "那太阳神也太可怜了吧？丘比特那个熊孩子！"
    #【立绘 乃琳-日常】
    nl "可是，晚晚，你知道吗？"
    nl "就连这个故事里的\"受害者\"阿波罗，也曾因为嫉妒，诱导孪生妹妹杀害她的爱人哦。"
    #【立绘 向晚-愤怒】
    show xw angery with dissolve
    xw "啊？"
    xw "我就说嘛，希腊神话都是骗人的！"
    "还挂着红眼圈就忍不住嗔怪的向晚，着实让乃琳明白了什么叫\"可爱\"。"
    "乃琳扶着胸，开心地笑着。"
    "这是她今天第一次感到轻松，所有的不愉快，在向晚面前，完全没有抵抗力。"
    "我们的晚晚真是太可爱了。"
    #【立绘 乃琳-日常】
    nl "不能这么说哦，晚晚。"
    nl "人的情感，就是这样奇妙。之前深入骨髓的恨，或许哪一天就会转变为刻骨铭心的爱。"
    nl "而人，总是会变。"

    #【黑屏转出】
    #【场景 天空-阴】
    scene 天空阴 
    with Dissolve(3)
    "【??】" "转变为爱，哈？"
     #【立绘 乃琳-阴沉（打阴影）】
    "【??】" "你明明知道那么多，却还在这里打哑谜。"
    "【??】" "你真的有在为她们考虑吗？"
    "【??】" "抱着偶然生发出来的，怜悯的爱自我陶醉、举棋不定。"
    "【??】" "——真让人失望。"
    "这是梦。乃琳告诉自己。"
    "现实里，绝对不会有个和她一模一样的人站在她面前，打破她的幻想，逼她做出选择。"
    "【??】" "你要是真的为她们好，现在就说服向晚，把嘉然带过去。"
    "【??】" "忘了吗？你刚加入A-SOUL的那天，他们说——"
    "【??】" "嘉然身上最后的价值，能拯救成千上万人的命。"
    "【??】" "那是他们的承诺。他们的承诺，不会有错。"
    "【??】" "你那所谓刻骨铭心的爱，又能救多少人？"
    "【??】" "乃琳……你不能犹豫了。"
    "内心的不安，时刻提醒自己牢记多年的命令。"

    "——药效失控，就带走目标。"
    # 【立绘：乃琳-悲伤】
    nl "我该怎么……背叛你们？"
    # 【黑屏转出】
    # 【场景：病房房间-夜】

    scene 病房强月光 with fade
    play music "audio/bgm/月光 德彪西.mp3" fadeout 4 fadein 4
     #【立绘 向晚-担忧】

    show xw worried at r2
    show nl sad at l2
    with dissolve
     #【BGM 诗意/例 青空】
    xw "乃琳，你做噩梦了？"
    xw "你浑身都在冒冷汗……"
    "身上盖着外套，是晚晚平时出门最喜欢穿的那件，目测价值不低于四位数。"
    "——她居然睡着了，就在她间谍事业的节点。"
    nl "唔……"
     #【立绘 乃琳-悲伤】
    "乃琳的胳膊有些麻，她强撑着坐起来。"
    "病房的椅子很硬，让她本就僵硬的腰肢雪上加霜。"
    "一滴水沿着她的锁骨缓缓流下来，又湿又冷。"
    nl "气温好像下降了。"
    "眼角湿湿的，嗓子干得发紧。她转移话题，希望没有暴露自己的情绪。"
    nl "咳。"
    nl "嘉然没事吧？"
     #【立绘 向晚-喜悦】
    show xw smile with dissolve
    xw "没事的~体温正常、心跳正常——有我在身边呢！"

    "乃琳见到向晚的故作镇定，哑然而笑。"

     #【立绘 乃琳-日常】
    show nl normal with dissolve
    nl "嗯，我相信你。"
     #【场景：满月-远景】
    play music "audio/bgm/有点逆天的可控的日常.mp3" fadeout 4 fadein 4
    scene 夜空满月 with dissolve
    #【BGM 悲伤/例 风居住的街道】

    #【无立绘】
    "今晚的月光，真是清澈。"
    "若没有云层遮挡，一眼望去，恰像花季少女晶亮的眸子，远望在水一方的情人。"
    "这热切的目光如今正照进来，照在嘉然的床尾，为安静的少女披上一缕羽衣。"
    "紫色头发的女孩盘起双马尾，就趴在床边，注视着怎么也不肯醒来的挚友，忧伤地，嘴角带笑。"
     #【背景 病房房间-夜】
    show 病房强月光 with dissolve
     #【立绘 向晚-悲伤】

    show xw sad at r2
    show nl thinking at l2
    with dissolve
    xw "乃琳姐姐，我想明白你的故事了。"
     #【立绘 乃琳-疑惑】
    nl "哦？"
     #【立绘 向晚-日常】
    show xw normal with dissolve
    xw "其实我们都和阿波罗一样，有很多个自己。"
    #【背景 天空-满月】
    scene 夜空满月 with dissolve
    #【无立绘】
    xw "爱上了什么，就要拼命追逐的自己。"
    xw "讨厌了什么，就要极力避开的自己。"
    xw "相信了什么，就要尽心维护的自己。"
    xw "想带给大家快乐的自己、想扮出最好状态的自己……"
    xw "还有那个……只能留给自己看的，柔软的自己。"

    show 病房晚 
    show xw sad at r2 
    show nl sad at l2

    with dissolve
    xw "……"
    xw "乃琳，你说……大家之前是不是都在隐藏自己最软弱的一面，所以才吵得那么凶的啊……"
    "向晚的眼角有一滴泪。"
    "像颗小小的月亮。"
    xw "大家是不是……都在担心给彼此添麻烦啊……"
    xw "可是，我们不是队友嘛……！"
    show xw cry with dissolve
    
    xw "我就算再怎么拉胯，也希望能帮到你们啊！" with sshake
    #【立绘 乃琳-悲伤】
    show xw cry at r2
    with dissolve
    nl "......"
    "向晚哭了。"
    "虽然已经经历了无数次这样的场景，但这次，不一样。"
    "乃琳已经不知道用什么立场安慰她了。"
    "她在担心谁呢？嘉然？珈乐？贝拉？"
    "……还是自己？"
    "乃琳被自己的自私吓了一跳。可是她否认不了这件事——压力大的时候，她也希望……能够放声大哭。"
    "但她做不到，她放不开。"

    nl "晚晚……"
     #【立绘 向晚-悲伤】
    show nl sad at center with move
    "向晚就伏在床旁。乃琳看不清她的表情，只能听到隐隐的抽泣声。"
     #【立绘 乃琳-悲伤】
    "哭一会儿，挺好的。"
    "乃琳把手轻轻覆在向晚头上，向后温柔地捋着。 "
    "月光，照在她冷静得吓人的脸上。 "

    #【无背景】
    scene 夜空繁星 with dissolve
    nl "真实的自己……"
    "（吗？）"

    # 【无立绘】
    # 【无BGM】
    "【乃琳母亲】" "琳琳，这个假期别出去玩了哈，要是考不上枝江大学，我和你爸可就没脸见人了！"
    # 【立绘：乃琳-阴沉】
    # show nl gloomy at center with dissolve
    nl "……"
    # 【立绘：乃琳-阴沉】
    nl "嗯，好的，妈妈！"
    "……"
    # 【无立绘】

    "【老师】" "乃琳啊，我跟枝江大厦那边联系好了，回头我们的实习，就去做他们的特工，你很有资质。"
    # 【立绘：乃琳-愤怒】
    # show nl angery with dissolve
    nl "可是，老师……"
    "【老师】" "去吧，听话——"
    "【老师】" "为了枝江市奉献一生，不也挺好吗？"
    "【老师】" "你说呢？"
     #【立绘 乃琳-悲伤】
    # show nl sad with dissolve
    nl "是的，老师，我明白。"
    # hide nl with dissolve
    "那么，什么是\"自我\"呢？"
     #【立绘 乃琳-悲伤】
    # show nl sad with dissolve
    nl "（悄声）晚晚啊……如果我真的把嘉然带走了，你会恨我吗……？"
     #【场景 繁星】
     #【无立绘】
     #【BGM：诗意/例：青空】
    play music "audio/bgm/月光 德彪西.mp3" fadeout 4 fadein 4
    "月亮悄悄地，转到她们看不见的地方去了。"
    "晚晚似乎睡着了，趴在床上没了动静。"
    "乃琳想起与阿草签订的协议。"
    "要是拖到了明天早上，大厦就会亲自派人来找自己，她的身份就会被曾经无比信任自己的队友知晓。"
    "一定要走了。"
     #【场景 病房房间-夜】
    scene 病房强月光 with dissolve
     #【立绘 乃琳-日常】
    show nl normal at center with dissolve
    nl "珈乐....拉姐...."
    "她捋着晚晚的发丝，喃喃着，眼中满是悲哀的美好。"
    nl "明早我回来的时候，可以为我弹一遍那首《水母之歌》吗？……"
    nl "我很喜欢。"
     #【无立绘】
    hide nl with dissolve
    "乃琳转身那一刻，向晚是有所犹豫的。"
    "她装作休息，等待乃琳的动作。"
    "她听到了乃琳的呢喃。"
    "如果不留住她，她会把嘉然带走嘛？"
    "……"

menu:
    xw "（我....）"
    "挽留":
        jump be3
    "什么也不做":
        jump .part2

label .part2: #两条路
    #【无BGM】
    "向晚张了张嘴，到底还是没能说出挽留的话。"
    "而乃琳，也只是在床边犹豫了一会儿。"
    "离去时，没有带走一个人。"
    "……"
     #【黑屏转场】 #【无BGM】
    scene black with fade
    show screen saying("黑夜是个贪吃的孩子。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    show screen saying("吞食落难者的祈祷，痛饮失格者的希望。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    #屏幕背景语 黑夜是个贪吃的孩子。
    #吞食落难者的祈祷，痛饮失格者的希望。
     #【场景 枝江市广景-深夜】
    scene 枝江市广景深夜 with dissolve
    show screen saying("而梦想家们，在恐惧中，期待黎明。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    #屏幕背景语 而梦想家们，在恐惧中，期待黎明。
    "……"
     #【场景 医院角落菜地-夜】
    scene 医院角落菜地夜 
    show nl surly at center 

    with dissolve
     #【BGM 诡异】
    play music "audio/bgm/悬疑诡异气氛通用BGM2.mp3" fadein 1.0
    "把光明关在身后的乃琳小姐，根本没想象过门外的荒凉。"
    "如果城市也有生命的话，现在的它，一定已病入膏肓。"
     #【立绘 乃琳-恐惧】
    "她还记得早上的时候，对面家属楼的一家三口还在这附近遛弯，孩子吵着闹着要吃冰激凌。"
    "生病的老大爷会推着轮椅迎过来，跟那家的父亲聊天，问问最近的偶像节目行情。"
    "一旁总有个伤脑筋的护士，小碎步赶上来，扶住轮椅上拴着的吊瓶。"
    "花坛里有蝴蝶飞舞，水池边有孩童打闹。"
    "——而现在，什么都没有。"
    "一片寂静。"
    "寂静，就代表未知。"

    scene 枝江大厦幕墙 
    show ac angery at l2
    show nl sad at r2
    show screen memory_filter 
    with fade
    #【无立绘】
    #【无BGM】
    
    ac "你怎么还是那么怕黑啊！乃琳！你这样怎么执行任务？" with sshake
    #【立绘：乃琳-悲伤】
    show nl gloomy  with dissolve
    nl "我……胆子有点小。"
    #【无立绘】
    ac "唉，算了，麻烦。"
    #【立绘：乃琳-悲伤】
    nl "对不起……"
    #【无立绘】
    ac "别在情报科干了，我把你调到间谍组，以后你也去做偶像。"
    nl "是……"
    #【场景 道路-夜】
    scene 道路夜 
    show nl gloomy
    hide screen memory_filter
    with fade
    play sound "audio/se/高跟鞋脚步声中.mp3"
    "再拐三个路口就到了……"
    "乃琳默念着。她几乎不敢睁眼。"
    "但她还是睁着眼。微弱的视觉至少能带给她暂时的安全感。"
    "街道两侧的居民楼变多了，可没有一扇窗户是闪着亮光的。"
    "她走在一条……\"黑暗\"的路上。"
    "她抑制不住自己的好奇心，想靠居民楼近一些。"
    #【场景拉近】
    scene 道路夜放大 with dissolve
    "【？】" "倏——倏——" with sshake

    nl "啊——！！！" with sshake

    play sound "audio/se/鼠窜.mp3"
    "诡秘的声音从四面响起，吓得乃琳急忙退开。"

    "【？】" "倏——倏——" with sshake
    "声音愈发接近了，扒着乃琳的肩膀。"
    play sound "audio/se/高跟鞋脚步声快.mp3"
    "她不敢回头，只能佯装淡定地快步前行。"
    "快点……再快点……"
    "……"
    stop sound


    scene 道路夜 
     #【BGM 黑暗】
    play music "audio/bgm/阴间的枝江.mp3" fadein 4.0 fadeout 4
     #【立绘 乃琳-阴沉】
    show nl gloomy at center with dissolve
    "【???】" "回去吧。"
     #【立绘 乃琳-恐惧】
    #show nl

    nl "谁？！" with sshake
     #【立绘 乃琳-阴沉】
    show nl gloomy with dissolve
    "【???】" "回去吧，乃琳。我就是你，我了解你。"
    "【乃琳的内心】" "回去，带上嘉然，这样，向晚也会一起。"
     #【立绘 乃琳-愤怒】
    show nl angery with dissolve
    nl "嗯……"
    #【立绘 乃琳-阴沉】
    "【乃琳的内心】" "有她们在，你就不怕了。"
    "【乃琳的内心】" "她们会为你唱歌打气。"
    "【乃琳的内心】" "会给你讲土味情话。"
    "【乃琳的内心】" "会跟你分享零食。"
    "【乃琳的内心】" "区区黑夜，算得了什么呢？"
    "【乃琳的内心】" "回去吧，那是一条充满光明的路。"
     #【立绘 乃琳-愤怒】
    nl "……"
    "有那么一瞬间，乃琳犹豫了。"
    "她有很多种身份——队里的大姐姐，奶淇琳们的女王，枝江大厦的特工。"
    "但是现在……"
     #【立绘 乃琳-悲伤】
    show nl sad with dissolve
    "她只是她，一个人的时候，也会怕黑。"
    hide nl with dissolve
     #【屏幕闪动】
     #【立绘 向晚-悲伤】
    show xw sad at center  with dissolve
    with Pause(1)
    hide xw with dissolve
    show jr haggard at center with dissolve
    with Pause(1)
    hide jr with dissolve
    show nl angery at center with dissolve
    #【立绘 乃琳-愤怒】
    nl "我不！"
    "她想起嘉然憔悴的神情，向晚红肿的眼。"
    "回头，是最错误的选择。"
    play sound "audio/se/高跟鞋脚步声快.mp3"
    "她深吸一口气，加快脚步。"

     #【BGM 急迫/例Hello Zepp】
     #【无立绘】
    play music "audio/bgm/能说的不多了感觉弦乐完整.mp3" fadein 4.0 fadeout 4
    "应该快到了、应该快到了……"
    "她转过路口，迫不及待拿出手机照亮，确认自己的位置。"
    "乃琳这才发现，因为种种变数，她今天这是第一次打开手机。"
     #【立绘 乃琳-日常】
    show nl normal at center with dissolve
    "她检查手机里的动态提示。"
    "黑暗中，手机发出刺眼的光，照亮乃琳的一脸担忧。"
    "嘉然出事之后，她们的账号已经不能使用了。"
    "所以，列表里应该没有珈乐或是贝拉的留言。"
    nl "那这么多动态提示是……"
    #【无立绘】
    #【BGM 放松/例 夏夜】
    # play music "audio/bgm/放松 温暖 平静.mp3" fadeout 1.0 fadein 1.0
    "【奶淇琳A】" "乃老师，晚安捏，大腿别着凉啦~"
    "【奶淇琳B】" "乃琳，在看嘛？在看Mua你一下！"
    "【奶淇琳C】" "乃琳，回个复吧，我的乃琳——"
     #【立绘 乃琳-日常】
    show nl normal at center with dissolve
    "黑暗会给人带来恐惧。"
    "很多人低估了恐惧，认为单纯的勇敢面对，就能战胜它。"
    "事实上，啼笑皆非的戏剧感，才是摧毁恐惧的最佳手段。"
    show nl happy at center with dissolve
    nl "扑哧……"
    "又发怪话。"
    "乃琳一边快步向前，一边翻阅着还没来得及查看的信息。没想到，在她最迷茫的时候，居然是奶淇琳们的信息给了她动力。"
    show nl normal at center with dissolve
    nl "咦……？"
    "手机收到的最后的提示，让乃琳不禁停住了动作。"
    #【无背景】


    scene 枝江大厦幕墙 
    show ac angery at l2
    show nl sad at r2
    show screen memory_filter
    with fade
    ac "你能不能管管你那帮粉丝？"
    ac "怎么？让你做间谍你就只会做间谍了是吧？"
    ac "你和你那些假同事一样，要把粉丝牢牢抓住，抓住！明白吗？"
    ac "认真点！"
    #【立绘：乃琳-悲伤】
    show nl sad  with dissolve
    nl "是……"
    #【场景 枝江大厦-夜】
    scene 枝江大厦夜 
    show nl normal 
    hide screen memory_filter 
    with fade
    #【立绘：乃琳-日常】
    nl "我的奶淇琳们……"
    nl "我相信你们，你们是最棒的。"
    "天穹被人类创造的光源点亮，再抬头的时候，大厦已经出现在乃琳的面前。"
    "乃琳擦干眼角的热泪，不再犹豫，收起手机，从容地走了进去。"


    jump .part3

label .part3: #两杯酒
     #【黑屏转场】 #【无BGM】
    scene black with fade
    show screen saying("爱神的两支箭，一支指向幸福与爱，一支指向分离与恨。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    show screen saying("命运，本来就是不公平的。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    #屏幕背景语 爱神的两支箭，一支指向幸福与爱，一支指向分离与恨。
    #命运，本来就是不公平的。
    #【场景 枝江大厦-夜】
    #【BGM 脚步声】
    show screen saying("你会得到哪一支的眷顾？" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    #屏幕背景语 你会得到哪一支的眷顾？
    #【场景 谈话厅-晚】
    scene 阿草办公室 with dissolve
    play music "audio/bgm/裸体舞曲1 萨蒂.mp3" fadein 4.0 fadeout 4
     #【BGM 舒缓/例 酒吧】
     #【无立绘】
    #侍者
    "【侍者】" "乃琳小姐，这边请。"
     #【立绘 乃琳-冷漠】
    show nl sneer at r2 with dissolve
    nl "阿草啊……"
    "乃琳深吸一口气，在自己的面具橱柜挑挑拣拣，选择了最冷静的一副。"
    nl "姐姐我可是找到机会就来找你了。"
    nl "那今晚欠下的睡眠……谁给我补呢？"
    "气场全开的乃琳，和十几分钟前那个为了队友而头痛的乃琳，似乎完全就是两个人。"
    "慵懒的语调，从容的步态，像极了几千年前祸国殃民的妲己。"
    "她不急着去坐阿草特地为自己预留的位子，而是斜睨着眼，尽可能搜寻来自这个房间的信息。"
     #【立绘 阿草-日常】
    show nl normal at r2
    show ac normal at l2
    with dissolve
    ac "咳咳……你们先回避一下。"
    "【侍者】" "是！"
     #【立绘 乃琳-日常】
    "尽管这个会客厅表面上光鲜亮丽，但乃琳还是敏锐地注意到墙角堆着的石块木屑。"
    nl "（看来拉姐在这里大闹了一场啊。）"
    "价格不菲的吊灯没理由地晃来晃去，吱呀，吱呀，拉扯着她和阿草的影子,有些晃眼。"
    "窗外是今日的满月，宽敞的大窗气派异常，从座位走到窗边，似乎需要些时间。"
     #【立绘 阿草-日常】
    ac "乃琳小姐，请。"
     #【无立绘】
    "实木茶桌摆在两人中央，高脚杯里是鲜红透明的液体，洁净的手帕被叠好放在一侧，阿草就坐在空椅对面，举杯等着她。"
    "再也没有老鼠的声音了。"
    "这里是富人区。"
    "这里是枝江大厦。"
     #【立绘 乃琳-日常】
    show ac normal at l2
    show nl normal at r2
    with dissolve
    nl "你们被搞得很狼狈啊~"
    "她用眼神环视四周，眸子里满是调侃的意味。"
     #【立绘 阿草-得意】
    show ac proud at l2 with dissolve
    ac "我们一向对自家的员工不设防。"
    "他凑近乃琳。"
    ac "尤其是你。"
    "阿草笑起来，取来一张档案，把它铺在餐桌上，用手摁住"
    ac "记得吧？刚加入时签署的特工合约。"
    "他把档案翻了个面。"
    ac "这里是你父母的签名。"
    ac "下面是你老师的。"
     #【立绘 乃琳-阴沉】
    show nl gloomy with dissolve
    "乃琳死死地盯着那张纸，鲜红的字迹刺痛她的眼。"
    #【无背景】

    scene 枝江大厦幕墙 
    show nl sad at rc,dark
    show screen memory_filter 

    with fade
    #同事
    "【同事A】" "她就是新来的？"
    "【同事B】" "呦呦，身材不错啊~"
    "【同事C】" "哼，人家可是高岭之花，枝江大学法学生~咱哪能跟她比啊？"
    "【同事D】" "真逗，学法的来做特工？"
    "【同事ABC】" "可笑！"
    #【立绘：乃琳-悲伤】
    nl "……"
    #【场景：谈话厅-晚】
    scene 阿草办公室 
    hide screen memory_filter
    with fade
    #【BGM：舒缓/例：酒吧】
    #【立绘：阿草-愤怒】

    play music "audio/bgm/玄秘曲 萨蒂.mp3" fadein 4.0 fadeout 4
    show nl normal at r2
    show ac angery at l2
    with dissolve
    "阿草直视着乃琳，语气里满是威胁和轻蔑。"
    ac "都想起来了？"
    ac "这是你为我们做出贡献的唯一凭证。"
    "——是啊，只是在和棋子说话罢了。"
    #【立绘：乃琳-冷笑】
    show nl sneer with dissolve
    nl "呵……"
    "他在威胁她。"
    "如果她的特工身份被队友知道了，她所珍惜的一切，都将弃她而去。"
    "这张纸，是她一生的噩梦。"
     #【立绘 阿草-得意】
    show ac proud with dissolve
    ac "那么，我们的嘉然小姐在哪呢？"
    "他顶着大脑袋，装模作样地向乃琳身后瞄。"
     #【立绘 乃琳-日常】
    show nl normal with dissolve
    nl "被我吃了。"
    "她眨眨眼，话语间却带着鱼死网破的决绝。"
    nl "呆毛味道不错哦~"
     #【立绘 阿草-愤怒】
    show ac angery with dissolve
    ac "你监视了她那么多年……"
    with vpunch
    ac "现在却连这点小事都做不到？！" #【文本框震动】
    "他从座位上窜起来，锤了一下桌子。"
    "他本以为最听话的乃琳一定不会给他增添烦恼，他失策了。"
     #【立绘 乃琳-日常】
    show nl normal with dissolve
    nl "阿草……其实我也不是不想和你合作啦~"
    "慵懒的语调完美掩盖了她内心的忐忑。"

    nl "只是，我真的不知道你们要嘉然有什么用啊？"

    "她曾经是问过这个问题的，但那时，她没有资格知道。"

    #【立绘 阿草-悲伤】
    show ac normal with dissolve
    play music "audio/bgm/诡异.mp3" fadein 4.0 fadeout 4
    ac "……"
    #【BGM 诡异】
    ac "唉，我这样形容吧……"
    ac "乃琳，在你来的路上，有看到一个行人、一户人家吗？"
     #【立绘 乃琳-疑惑】
    show nl thinking with dissolve #沉思
    nl "……？"

    #【场景 诡月-4】
    scene 夜空诡月 with fade

    "黑暗的城市里，有一条看不见的河流。"
    "【路人1】" "找到了吗？"
    "【路人2】" "没有！"
    "【路人3】" "你那边呢？"
    "【路人4】" "还在搜！"
    with vpunch
    "【路人1】" "天亮之前，必须找到嘉然小姐！必须！" #【文本框震动】
    #【场景谈话厅-晚】
    scene 阿草办公室 
    show nl normal at r2
    show ac normal at l2
    with dissolve
    "会客桌的侧面，是一扇可以俯视全城的大窗。"
    "阿草带乃琳来到这里，看远处的人造光源整齐地移动"
     #【立绘 阿草-日常】
    ac "傍晚开始，有一小批人，从城南到城北，缓慢地搜索着嘉然的踪迹。"
    ac "啧。"
    "他在冷笑，像个事不关己的观众。"
     #【立绘 乃琳-惊讶】
    show nl shock with dissolve
    nl "怎么会这样？！"
     #【立绘 阿草-悲伤】
    ac "……"
     #【黑屏转场】
     #【场景-枝江市全景-深夜】
     #【BGM 黑暗】
     #【无立绘】
    # play music "audio/bgm/阴间的枝江.mp3" fadeout 1.0 fadein 1.0
    scene 枝江市广景深夜 with fade
    ac "枝江……是一座虚假的城市。"
    ac "它的出现本身，就是一个悖论。"
    ac "——它建立在居住者的希冀和憧憬之上，如果没有这些积极的情绪，它将土崩瓦解，消弭于黑暗。"
    ac "为了维持这个城市的稳定，我们不得不建立学院，培养能带给人们希望快乐的偶像。"
    ac "而如果有一天，我们精心挑选出的偶像……"
     #【场景 谈话厅-晚】
    scene 阿草办公室 
    show nl shock at r2
    show ac normal at l2

    with dissolve
     #【立绘 阿草-日常】
    ac "她消失了，或者——"
    ac "被人保护起来了呢？"
     #【立绘 乃琳-惊讶】
    nl "……！"
     #【立绘 阿草-日常】
    ac "黑夜是个贪吃的孩子，要是人类的情绪不足以满足他，他就会勃然大怒，用人类的理智代餐。"
     #【立绘 乃琳-惊讶】
    nl "他们因为嘉然的消失，开始丧失理智了……"
    "无力感突然袭来，她靠在窗玻璃上，远方\"扫描仪\"的光，离嘉然的所在地，似乎仅是咫尺之遥。"
    "\"夺走\"嘉然……？"
     #【立绘 乃琳-愤怒】
    show nl angery with dissolve
    nl "既然这样，你们为什么还要给嘉然吃那种\"药\"！就是因为药效失控，才让她变成现在这样的！"
     #【立绘 阿草-日常】
    ac "就算偶像再怎么完美，观众也总有看腻的那天啊……"
    ac "乃琳小姐，你能保证……一个魂真的会永远喜欢你们吗？"
     #【立绘 乃琳-惊讶】
    show nl shock with dissolve
    nl "……！"
     #【场景 枝江大厦-夜】
    scene 枝江大厦夜 with dissolve
     #【无立绘】
    ac "直到某天，粉丝贡献的\"能源\"会少到入不敷出。"
    ac "热爱，变得廉价。人们大喊着，变质啦，回不去啦，然后纷纷离去，匆忙到不会回头看哪怕一眼。"
    ac "到那时，再赤诚的心，恐怕也疲惫不堪了吧？"
     #【场景 谈话厅-晚】
    scene 阿草办公室 
    show ac normal at l2
    show nl angery at r2
    with dissolve
    ac "我们需要“药”。能让偶像变成粉丝“神偶”的药。"
     #【立绘 乃琳-愤怒】
    nl "哪怕会对服用者本人造成巨大的危害？！她还是个女孩！"
     #【立绘 阿草-悲伤】
    ac "……"
    ac "哪怕如此。"
    "说这句话的时候，阿草没有挪动他肥胖滑稽的身躯，仅仅机械地转动脑袋，面向乃琳。"
    "这将是她今晚看到过的最诡异的一幕。"
 
 
    ac "哦，对了，乃琳。"
    show ac happy with dissolve
    ac "嘉然是自愿的。"
 
      #【场景 病房房间-夜】
    scene 病房强月光 
    show xw sad at center 
    with Dissolve(3)
     #【无BGM】
    xw "嘉然……"
     #【立绘 向晚-悲伤】
    xw "我到底怎么做……才能知道你为什么要牺牲自己呢……？"
    "抬头时，向晚还瞪着红肿的眼。"
    "她有些疲惫了，甚至一度想过放弃。"
    "可她的潜意识总告诉她，昏迷的嘉然，还在向她传递着某些信号。"
    "很重要的信号。"
    xw "……"
    xw "我想去看看乃琳的情况。"
    "她揽回放在椅子上的外衣，给嘉然盖上。"
    xw "想到了什么，记得和我说。"
     #【无立绘】
    hide xw with moveoutright
     #【BGM 关门声】
    play sound "audio/se/砰的一声关门.mp3"
    "房间很快安静了，屋内仅剩嘉然一人。"
    "谁都没有注意到，窗外的圆月，不知何时又转回了这一方。"
    "——在屋外窸窸窣窣由远而近的人声掩映下，规律地闪烁着诡异的光辉。"
     #【黑屏转出】

     #【场景 谈话厅-晚】
    scene 阿草办公室 
    show ac normal at l2
    show nl angery at r2

    with fade
     #【BGM 黑暗】
    # play music "audio/bgm/争吵.mp3" fadein 1.0
    "这根本就不是什么自愿献祭。"
    "这是有预谋的逻辑闭环。"
    "就像被爱神的两支箭，同时射入了心脏。爱与恨缠绕交织，用无力的挣扎撕裂自我。"
    "然后，代代轮回。"
     #【立绘 乃琳-愤怒】
    nl "之前\"偶像\"，都是因为这个\"毕业\"了，对吗？"
     #【立绘 阿草-日常】
    ac "唔……倒是有一些也不太痛快……"
     #【立绘 乃琳-愤怒】
    nl "……"
     #【立绘 阿草-得意】
    show ac proud with dissolve
    ac "那群疯子马上就要接近这边了，乃琳。"
    "他还端着高脚杯，向窗外随意地一指。"
    "黑暗，已经渐渐被机械的光芒覆盖……"
    ac "你不会真想让那一小撮疯子找到嘉然吧？"

    #【立绘：乃琳-疑惑】
    show nl thinking with dissolve
    "乃琳看着窗外，看着刺眼的灯光，猜想着。"
    "——这些人里面，会不会有她的奶淇琳们呢？"
    "他们怎么样了？"
    "向晚呢？她会怎样呢？"
    "她想起自己在大厦门口看到的那封信。"
    #【场景：枝江大厦-夜】
    play music "audio/bgm/钢琴1 缓和.mp3" fadeout 4.0 fadein 4.0
    scene 枝江大厦夜 with dissolve
    #【BGM：温暖/例：初夏的风】
    #【无立绘，独白】
    #"奶淇琳D"
    "【奶淇琳D】" "乃老师，今天……不想发病了，想和你说点真心话。"
    "【奶淇琳D】" "我是个普通的大学生，成绩一般，长相一般，才能一般，只是沙滩上不起眼的一枚贝壳。"
    "【奶淇琳D】" "我家里没钱，不能在经济上支持你，但是，你真的帮了我很多……"
    "【奶淇琳D】" "你说，要和我们不知疲惫地双向奔赴，你说‘行也思君，坐也思君’，你说，我们每一个人都是独一无二的。"
    "【奶淇琳D】" "你的温柔，我以前从未感受过。"
    "【奶淇琳D】" "只品尝了一次，我就再也没办法回头。"
    "【奶淇琳D】" "乃琳，最近你们没有出现，我知道，一定是出了什么事情。"
    "【奶淇琳D】" "没关系，我可以等。你曾经告诉给我的，我还要花好久好久，细细品味，足够你调整状态，和我们再次相见。"
    "【奶淇琳D】" "我，也在慢慢变好。"
    "【奶淇琳D】" "\"我知道蛾子是碰不到灯芯的，但有光就好。\""
    #【无背景】
    scene 夜空满月 with dissolve
    #【立绘：乃琳-阴沉】
    # show nl gloomy with dissolve
    "【乃琳的内心】" "你就在期待这个？有光就好……这算什么？？？"
    "【乃琳的内心】" "你给我站住，乃琳……你！"

    "【乃琳的内心】" "你就不考虑一下自己的未来吗？！" with sshake#【文本框震动】
    #【场景：枝江大厦-夜】
    scene 枝江大厦夜 with dissolve
    nl "未来啊……"
    #【立绘：乃琳-喜悦】
    show nl smile at center with dissolve
    nl "嗯，有光就好。"
    #【黑屏转场】
    #【场景：病房房间-夜】
    scene 病房强月光 
    show screen memory_filter
    show xw sad at center 

    with fade
    #【立绘：向晚-悲伤】
    xw "还有那个……只能留给自己看的，柔软的自己。"
    #【场景：谈话厅-晚】
    scene 阿草办公室 
    show nl smile
    hide screen memory_filter 
    with fade

    nl "那就是……光啊。"
    nl "谢谢你们，奶淇琳。"
    nl "谢谢你，晚晚。"
    "洁净的玻璃映照出她因接受了太多信息而憔悴的脸。"
    "她看着自己乱成一团的长发，想起某一天，嘉然为她梳头时，一句无心的话。"

    scene 客厅夜 
    show screen memory_filter
    show jr smile at center 
    with fade
    #【立绘：嘉然-日常】
    jr "乃琳~你这么漂亮的长头发，要是绑住刷——地盘起来，也一定很好看！"
    "手舞足蹈地，可爱死了。"
    #【场景：谈话厅-晚】
    scene 阿草办公室 
    show nl normal
    hide screen memory_filter 
    with fade

    play music "audio/bgm/争吵.mp3" fadeout 4.0 fadein 4.0
    #【无立绘】
    #【BGM：黑暗】
    "让别人\"夺走\"嘉然？"
    "她扬起嘴角。"
    "——当然不。"

     #【立绘 乃琳-日常】
    nl "好啊，我们合作。"
    "阿草不可抑制地露出笑容，事情似乎只是拐了个小弯。"
    "现在，它即将回归正轨。"
    nl "在此之前……你也知道，我挺注重仪式感的。"
    nl "我们碰个杯吧，纪念这一刻。"
    "她去寻找自己的酒杯。"



    scene 枝江大厦幕墙 
    show ac happy at l2
    show nl sad at r2
    show screen memory_filter 
    with fade
    ac "我很高兴你能同意我们的决策，乃琳。"
    ac "监视你的队友——嘉然。"
    ac "如果某天我们给她服用的药物出现问题，第一时间把她带到我们这里来。记住了吗？"
    #【立绘：乃琳-悲伤】
    nl "……"
    #【无立绘】
    
    ac "这是为她好！记住了吗！？" with sshake
    #【立绘：乃琳-悲伤】
    show nl helpless with dissolve
    nl "……记住了。"
    #【无立绘】
    ac "很好。"
    ac "乃琳，这种经历，会成就你的一生。"
    ac "把字签了吧，就在你父母和老师名字下面。"
    #【立绘：乃琳-悲伤】
    nl "是。"
    #【无立绘】
    ac "哈哈哈哈……"
    ac "干杯。"

    #【场景：谈话厅-晚】
    scene 阿草办公室 
    show nl normal at r2
    show ac proud  at l2

    hide screen memory_filter
    with fade
    #【无立绘】
    "这些回忆……太陈旧了。"
    "也太苦涩了。"
    "真正的她，要的是什么？"
    "能决定自己前程的，真的是其他人吗？"
    #【立绘：阿草-得意】
    ac "好消息是，我们已经决定让你继续做下一任偶像了。"
    ac "你该庆幸自己一直很听话。"
    #【立绘：乃琳-冷笑】
    show nl sneer at r2 with dissolve
    nl "是嘛……"

    #【屏幕震动】
    #【BGM：激动（特殊音乐）】

    play music "audio/bgm/第四章反转.mp3"
    #【特殊CG】
    play sound "audio/se/泼水飞溅.mp3"
    #【屏幕震动】
    scene 乃琳CG with dissolve
    "哗——！" 

    ac "等等……！"
    "听话？"
    "我的所有努力，最后难道只剩一句听话吗？！"
    "可笑。"
    nl "再见了，我的过去。"
    "她不想再一遍一遍地重复\"是\"\"好的\"\"对不起\"了。"
    "从今天起，她只是她自己。"
    "从今天起，她的爱，便不再是偶然。"
    nl "呼……"
    "倾倒这一杯酒，几乎花费了乃琳全部的体力。"
    "她看着被红酒浸湿，不成样子的档案纸，悲哀的双眼露出璀璨的笑容。"
    with vpunch
    ac "你疯了吗！？"#【文本框震动】
    ac "你这是自毁前程！乃琳！你这样怎么面对你的父母和老师？！"
    with vpunch
    ac "没有了档案，你别想找到下一个去处！"#【文本框震动】
    nl "关于未来……我早该跟他们谈一谈的。"
    "乃琳微笑着，声音还有些颤，心脏因为她生命里的第一次反抗而砰砰乱跳。"
    nl "工作的话……我现在已经是偶像了呀~"
    "她的双眸晶亮，看不见一丝灰尘。"
    ac "对，队友……你还有队友！"
    with vpunch
    ac "你要把嘉然交给那群疯子吗？！"#【文本框震动】
    "阿草伸出小短手，颇为凌乱地指向窗外。"
    "乃琳满不在乎地耸了耸肩。"
    "无回应的奉献，就像在冷风中抓住一根稻草，要克服无数的阻力，甚至伤害自己，才能让稻草不随风飘摇。"
    "而倘若这些付出，得到了哪怕一点来自真心的回应，这回应所生发的暖意，就会融化刺骨的寒风，直融进心里，让人忍不住地，嘴角带笑。"
    "人，也就有了无上的勇气。"
    nl "我们打个赌吧，阿草。"
    nl "就赌……我们的嘉然小朋友和向晚小朋友……能不能把她们的粉丝从\"贪吃孩子\"手里救回来~"
    nl "要是我赢了，下次偶像谁来做，可就我说了算了哦……"
    #【场景：谈话厅-晚】
    scene 阿草办公室 with dissolve
    #【立绘：阿草-愤怒】
    show ac angery at l2
    show nl normal at r2
    with dissolve
    ac "……！"
    #【立绘：乃琳-日常】
    "乃琳绕过愤怒到无法行动的阿草，回到窗边。"
    "人群的亮光在嘉然的所在处聚集，几乎掩盖了圆月的光芒，把整个城市都照个透亮。"
    #【无背景】

    scene 枝江大厦幕墙 
    show ac proud at l2
    show nl thinking at r2

    show screen memory_filter 
    with fade
    nl "前面的那四个女孩，就是我的队友吗？"
    ac "对，你的假同事，你可以和她们随意相处，别暴露身份就好。"
    nl "哦……"
    #【场景：天空-晴】
    play music "audio/bgm/放松 温暖 平静.mp3" fadeout 4.0 fadein 4.0
    scene 客厅夜 with dissolve
    #【BGM：温暖/例：初夏的风】
    #【立绘：嘉然-喜悦】
    show jr happy at center with dissolve
    jr"乃~~琳~~"
    jr"我们去那边看看好不好——我闻到蛋糕的味道了……"
    hide jr with dissolve
    #【立绘：向晚-害羞】
    show xw shy at center with dissolve
    xw"诶呀~乃琳！你……你别瞎起哄嘛……"
    hide xw with dissolve
    #【立绘：珈乐-日常】
    show jl normal at center with dissolve
    jl"乃老师——一起去逛街嘛？跟你说啊我昨天……"
    hide jl with dissolve
    #【立绘：贝拉-愤怒】
    show bl serious at center with dissolve
    bl"啧，乃琳，你怎么还是做不对啊！来，再来一次！"
    hide bl with dissolve
    #【无立绘】
    "我们是！A-SOUL！"

    scene 天空晴
    hide screen memory_filter 
    with dissolve
    "向晚、嘉然、珈乐、贝拉……"
    "她好想她们。"
    "若是她们中有一人站在身旁，她一定会毫不犹豫地，抱着对方放声大笑，抑或失声痛哭。"
    "不过现在，忍一会儿也无妨。她深呼吸。"
    scene black with dissolve
    show screen saying("我爱这座城。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    show screen saying("因为这里有你们。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)

    #【场景：谈话厅-晚】
    scene 阿草办公室 
    show nl smile at r2
    show ac normal at l2

    with fade
    #【立绘：乃琳-喜悦】
    with dissolve
    nl "医院旁边有个广场……"
    #【立绘：阿草-日常】
    ac "....？"
    #【场景：枝江市广景-深夜】
    scene 枝江市广景深夜 with dissolve
    nl "只要选个好点的角度，就能看见广场中央威严帅气的骑士塑像。"
    nl "卖糖果和冰激凌的小贩，不需要吆喝，就会有一群孩子，自觉地端着小瓷碗排好队，像一群小鸭子。"
    #【场景：繁星】
    scene 夜空繁星 with dissolve
    nl "到了晚上，要是不敢走夜路，也可以抬头看看天。明亮的北极星，正悄悄地守护着自己。"
    nl "——为什么如今，就变成这副鬼样子了呢？"
    #【场景：谈话厅-晚】
    scene 阿草办公室 with dissolve
    #【立绘：乃琳-喜悦】
    show ac normal at l2
    show nl smile at r2
    with dissolve
    nl "阿草啊……"
    nl "爱是值得相信的。"
    #【无立绘】
    show  nl normal at r4 with move
    "在阿草还傻傻不知道做些什么的时候，乃琳已经不知不觉挪到了房门边。"
    #【立绘-乃琳-日常】
    nl "阿草……到点儿了，我是不是该下班了呀~"
    nl "我也有自己要负责的事……"
    nl "家里那两小只肯定想死我了~"
    #【立绘：阿草-悲伤】
    show ac sad at l2 with dissolve
    ac "……唉。"
    ac "你走吧。"
    #【立绘：乃琳-喜悦】
    show nl happy with dissolve
    nl "呵呵，别气馁嘛，我还是很感谢你给我的工作机会的~"
    nl "再见！"
    hide nl with moveoutright
    play sound "audio/se/砰的一声关门.mp3"
    ac "……"
    #【场景：枝江大厦-夜】
    scene 枝江市广景午夜 with dissolve
    #【无BGM】
    #【无立绘】
    "梦想家期待的黎明，悄然而至。"
    #【黑屏转出】

    scene black with Dissolve(3)
    jump cp6_start


image 道路夜放大:
    "bg/8 5道路(夜).png"
    align (0,0) xoffset -2080 yoffset -1460
    1.0
    easeout 1.0 xoffset -1280 yoffset -1460
    easein_cubic 3.0 xoffset -1280 yoffset -400
    easein 1.5 xoffset -1280 yoffset -1300
init python:
    declare('阿草办公室', 'bg/5 阿草办公室.png', 'p')
    declare('街道_night', 'bg/2 5 街道（夜）.png', 'p')
    declare('道路_night', 'bg/8 5道路(夜).png', 'p')
    declare('夜空满月', 'bg/2 5 夜空（满月）.png', 'p')
    declare('夜空繁星', 'bg/2 5 夜空（繁星）.png', 'p')
    declare('夜空诡月', 'bg/2 5 夜空（诡月）.png', 'p')
    declare('道路早', 'bg/8 5道路(早).png', 'p')
    declare('道路夜', 'bg/8 5道路(夜).png', 'p')
    declare('病房', 'bg/0 3 病房.png', 'p')
    declare('病房1', 'bg/5 病房(早).png', 'p')
    declare('病房晚', 'bg/5 病房(晚).png', 'p')
    declare('病房强月光', 'bg/5 病房(强月光).png', 'p')
    declare('医院角落菜地白天', 'bg/5 9医院角落菜地(白天).png', 'p')
    declare('医院角落菜地夜', 'bg/5 9医院角落菜地(夜).png', 'p')
    declare('乡村仓库', 'bg/5 乡村仓库（午）.png', 'p')
    declare('枝江市广景傍晚', 'bg/5 8枝江市广景（傍晚）.png', 'p')
    declare('枝江市广景深夜', 'bg/5 8枝江市广景（深夜）.png', 'p')
    declare('枝江市广景午夜', 'bg/5 8枝江市广景（午夜）.png', 'p')
    declare('枝江市广景昼', 'bg/5 8枝江市广景(昼).png', 'p')
    declare('天空晴', 'bg/5 天空(晴).png', 'p')
    declare('天空阴', 'bg/5 天空(阴).png', 'p')
    declare('河边', 'bg/5 河边.png', 'p')
    declare('神界树', 'bg/5 神界(树）.png', 'p')
    declare('枝江大厦夜', 'bg/1 4 5枝江大厦外景(夜晚).png', 'p')
    declare('枝江大厦白天', 'bg/1 4 5枝江大厦外景(白天).png', 'p')
