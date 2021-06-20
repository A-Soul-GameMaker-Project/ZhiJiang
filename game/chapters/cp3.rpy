label cp3_start:
    window hide
    $ save.cp_name = "第三章"
    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/3.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True


    scene black
    show screen saying("独狼的旅途本没有终点，但是它若仰望星空，便会知晓方向。" ,0.5,0.4,30,addImg=True) with Dissolve(3)
    $ renpy.pause(4.0)
    hide screen saying with Dissolve(1)

    show screen saying("每一个艺术生都希望自己是C位。\n但是当我看见她的那一刻，我就知道，\n她才是真正的C位。只要她起舞，我就愿意为她献上歌喉。" ,0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(7.0)
    hide screen saying with Dissolve(1)

    #BGM【忧伤】
    play music "audio/bgm/第二章 悲伤回忆.mp3" fadein 2.0
    #! 回忆开始：

    scene  练舞室 
    show screen memory_filter

    #立绘【小贝拉 乐】
    show bl child at l2 
    show jl child at r2 
    with fade
    window show

    bl "你好，我叫贝拉，让我们一起组队吧～"
    bl "我的梦想就是成为一个很专业很专业的芭蕾舞者。"
    bl "我们一起努力实现梦想吧～"

    scene  练舞室 
    show bl child sad at l2 
    show jl child sad at r2 
    with fade
    bl "不要放弃！珈乐，我们要一起实现梦想呀"

    with fade

    show bl child sad at l2
    bl "珈乐，我的家没有了，我已经没有地方可以去了..."
    #立绘【小贝拉 乐】
    scene  练舞室 

    show bl child at l2
    show jl child at r2
    with fade

    bl "谢谢你的玩偶，我很喜欢...让你担心了，我会努力打起精神来的！"
    #立绘【贝拉 哀】

    scene  练舞室 
    show jl child sad at r2
    show bl child sad at l2
    with fade

    bl "为什么...动起来啊！为什么，动不了..."
    bl "珈乐，我好像没有办法跳芭蕾舞了...我已经，什么都没有了..."
    hide bl 
    hide jl 

    
    show jl sad
    with dissolve
    #无立绘
    jl "(曾经，她是耀眼的星，我追着她的光前行。)"
    jl "(如今，她跌落尘埃，那么我想站在更高处，在那里等她。)"
    jl "(她曾经是我的梦想，我想努力成为她的目标。)"


    scene  LivingRoom_light 

    #场景【贝拉房间】
    #立绘【珈乐 日常】
    show jl normal at r2
    show bl normal at l2 
    with fade
    jl "贝拉，这是新的开始，我们一起，成为偶像吧！"
    #立绘【贝拉 无神】
    bl "偶...偶像，舞台..."
    #立绘【贝拉 喜】
    show bl smile at l2 with dissolve
    bl "我会继续努力的！我们一起成为枝江市最闪耀的女团吧！"

    #! 回忆结束

    #场景【嘉然病房】
    scene 病房房间晚上

    show jl sad at center

    hide screen memory_filter 
    with fade


    jl "明明...都已经这样约定过了，不是吗？"
    jl "为什么要放弃自己的前程啊！"
    jl "大家一起迈过了那么多难关...可为什么偏偏在这个时候..."
    jl "嘉然..."

    show jl helpless  with dissolve
    p "昔日最活泼可爱的队友，此时仿佛等待王子亲吻的公主一般静静地躺在床上沉睡着。"
    p "然而A-SOUL没有能够唤醒奇迹的王子，就算有，醒来的嘉然也不会记得任何人，不能再做偶像了。"
    p "珈乐叹了口气，移开了视线。"

    show jl sad  with dissolve

    p "不早了，快要到和阿草约定好的时间了。"
    p "珈乐站起身，向屋外走去。"
    scene 医院走廊2

    show jl anxiety at r2
    show xw unconcerned at l2
    with dissolve

    xw "珈乐。"
    p "刚刚走出病房的门，珈乐的手突然被人拉住了。"
    p "她转过身，看到是向晚，眉头微微皱了一下，不留声色地甩开了向晚的手。"
    #立绘【珈乐 日常】
    jl "向晚...有什么事吗？"
    #立绘【向晚 哀】
    show xw sad at l2 with dissolve
    xw "没什么...只是有些事想跟你说。"
    jl "抱歉，我还有事..."

menu:
    xw "(我该说什么？)"
    "你要去找阿草，对吧？":
        jump cp3_branch1
    "这么晚了，你要去哪里呢？":
        jump be1

label cp3_branch1:
    #立绘【珈乐 无奈】
    xw "你要去找阿草，对吧？"
    show jl helpless  with dissolve

    jl "...是。"
    jl "对不起，我没办法再继续等下去了..."
    #立绘【珈乐 悲伤】
    show jl sad at r2 with dissolve
    jl "每小时我们都在失去成百上千的粉丝，而嘉然的病..."
    jl "我没有办法在这个时候放弃我的梦想。"
    #立绘【向晚 日常】
    show xw gloomy at l2 with dissolve
    xw "我没有让珈乐放弃梦想的意思啦！"
    xw "珈乐...我是想说..."
    xw "你对嘉然怎么想？"
    #立绘【珈乐 日常】
    show jl helpless at r2 with dissolve
    jl "我对她？"
    jl "(最乐观，最活泼，却在最初承受了最多压力的嘉然。)"
    jl "(在最后大家都触摸到梦想的时候倒下的嘉然。)"
    jl "(为什么要问我对她的想法...？)"
    #立绘 【珈乐 悲伤】
    show jl sad at r2 with dissolve
    jl "你也在埋怨我..."
    xw "不对...我不是这个意思！"
    #立绘 【珈乐 怒】
    show jl angery at r2 with dissolve
    jl "那你是什么意思...！"
    #立绘 【珈乐 悲伤】
    show jl sad at r2 with dissolve
    jl "你也好，贝拉也好，为什么都这么想我..."
    jl "我只是...不想放弃舞台啊..."
    #立绘【向晚 日常】
    show xw normal at l2 with dissolve
    xw "我没有埋怨你呀！"
    xw "我知道珈乐是很温柔的女孩。"
    xw "虽然不熟悉的时候像冰块一样冷，不过熟悉起来就知道你的内心是很柔软很柔软的呢。"
    xw "所以，我理解你..."
    #立绘【珈乐 日常】
    show jl anxiety at r2 with dissolve
    jl "...别说了。"
    # hide xw
    
    jl "(刚刚加入A-SOUL的时候，我很不合群。)"
    jl "(只愿意和贝拉亲近，和其他人仿佛是两个世界的人。)"
    jl "(是从什么时候，把这间房子当成是家的呢？)"
    jl "(嘉然的撒娇，乃琳的使坏，向晚的冒失仿佛也成了习惯。)"
    jl "(一起努力过，一起哭泣过，欢笑过，奉献出了真心之后又怎么可能置身事外呢？)"
    jl "(但是...)"
    jl "(梦想近在咫尺，因为这种事被禁止通行，怎么可能会甘心！)"

    xw "虽然我们总是吵架，但我们依然是同伴，珈乐心里也是装着我们四个人的吧？"
    xw "不仅有贝拉，而且有乃琳，有我，当然也有嘉然。"
    xw "你也一定希望我们一起继续走下去吧？"

    #立绘【珈乐 哀】
    show jl sad  with dissolve
    jl "..."
    jl "(为什么一定要逼着我把两样珍贵的东西摆在天平的两端比较呢？)"
    jl "(我和贝拉的约定，还是A-SOUL，哪边更重要，不是好不容易才狠下心决定好的吗？)"
    jl "(现在，又要想不清了...)"

    show xw normal with dissolve
    xw "曾经有人和我说，水母是没有梦想的。"
    xw "只能在深海里度过相对失败的一生。"
    xw "但是有一只水母，它有了梦想。"
    xw "可能依然只是随波逐流..."
    xw "不过现在，这只水母也会发光了吧？"
    xw "水母觉得，如果被海浪冲回了原处，那么再漂回去就好了。"
    xw "水母不会失败..."

    #立绘【珈乐 怒】
    show jl angery at r2 with dissolve
    jl "别再说了，晚晚..."
    "原本以为已经整理好了的思绪，又被搅成了一团糟。"
    "珈乐转身推开了门，想要离开，却被向晚快走几步一把拉住。"

    #立绘【向晚 哀】
    show xw worried at l2 with dissolve
    xw "这个给你...不要太相信阿草了。"
    "向晚语气急促地说着，一边递过一个东西。"
    xw "珈乐去做珈乐想做的事吧。"
    xw "你一定要小心..."

    #立绘 【珈乐 日常】
    show jl helpless at r2 with dissolve
    jl "..."
    "珈乐接过向晚递过来的东西，看也没看便随手塞进了口袋，如逃跑一般转身向屋外走去。"
    hide jl with moveoutright

    xw "..."
    #场景【枝江外景】
    #【无立绘】
    scene NightStreet 
    show jl sad
    with fade
    "太阳已经落山了，漆黑的天幕上除了一轮圆月，再看不见一颗星斗，枝江五颜六色的霓虹勾勒出了一栋栋大楼的轮廓，在几乎要刺伤眼睛的灯光下，整座城市一如白昼。"
    "几乎在所有高楼上都能看到B-SPIRIT的巨幕广告，令人目眩。"
    "短短一周之前，那里还是A-SOUL的位置。"
    "珈乐独自在人行横道上快速的走着，她的每一步都狠狠的踩在地上，像是要把自己厌恶的东西踩碎一般。"
    "下雨了。"
    "雨落在她的身上，带走残存的体温。"
    "头发被雨水浸湿打成了绺。"
    "很讨厌。"

    "整颗心变得有点嗨～"
    "oh～都是你看看看过来..."
    "穿过人流，熟悉的音乐敲击着珈乐的耳膜。"
    "仔细去听的时候，却又消失不见了。"
    jl "(是错觉吧？)"
    jl "(现在怎么还会有人去听A-SOUL的歌呢？)"
    "她撇了一眼B-SPIRIT的巨幅广告，苦笑一声，继续迈开步子。"

    #【黑屏转场】
    #场景【公司大楼13层草的办公室】
    scene 阿草办公室 夜 with fade
    #BGM【焦虑】
    "工作人员把珈乐带到了阿草的办公室后就离开了，她在房间等了十几分钟，阿草也没有来。"
    #立绘【珈乐 日常】
    show jl anxiety at center with dissolve
    jl "之前不是打电话预约过了吗...阿草到底在忙什么，是B-SPIRIT的事吗？"
    "珈乐等得有些无聊了，随手拿起了桌子上的一本杂志。"
    show jl normal at center with dissolve

    jl "唔...X团吗？我记得之前挺火的来着，不过..."
    "珈乐翻动到杂志，找到了发行日期。"
    jl "怎么是去年的杂志，我就说嘛，最近X团已经没什么消息了..."
    #立绘【阿草 日常】
    show jl at r2 
    show ac normal at l2 
    with easeinleft
    ac "抱歉，让你久等了。最近我负责B-SPIRIT的宣发工作，实在很难挤出时间来。"
    "翻了几页杂志后，阿草推开门走了进来，在办公桌后坐下。"

    show ac normal
    show jl anxiety
    with dissolve

    jl "没关系，也没有等很久。"
    "珈乐把杂志放下，收起翘着的双腿。"
    ac "嗯，我们也用不着寒暄了，说实话，你能愿意联系我，我很满意。"
    ac "你是个很棒的偶像，没有必要跟着嘉然一起埋没。"
    ac "嗯，还有贝拉，我可以让你们成为双人组合出道，至于乃琳和向晚要是再执迷不悟的话，就让她们陪着嘉然一起淡出大众的视野好了。"
    #立绘【珈乐 哀】
    show jl sad with dissolve
    jl "抱歉...我不能答应。"
    hide jl
    hide ac

    #【回忆演出】
    show screen memory_filter 
    #「
    #立绘【和第一章这句话一样】
    show bl sad at center

    with fade

    bl "在利益的天平上衡量这个问题本身，就已经是对队友的背叛了。"
    hide bl
    #立绘【向晚 日常】
    show xw normal at center with dissolve
    xw "水母觉得，如果被海浪冲回了原处，那么再漂回去就好了。"
    hide xw
    #」

    show jl normal at r2 
    show ac normal at l2 
    with quick_fade
    hide screen memory_filter 
    play music "audio/bgm/争吵.mp3" fadeout 5.0 fadein 4.0

    jl "(让我...再感性一次吧。)"

    ac "哦？你是怎么想的呢？"
    "阿草的语调有些疑惑。"
    #立绘【珈乐 日常】
    jl "可不可以让我们在不和嘉然切割的前提下进行四人的偶像活动呢？我们是A-SOUL...缺了任何一个都不行。"
    ac "我应该已经说过了，你们现在只有两个选择，切割嘉然，或者停止偶像活动。这是公司的决定。"
    show jl helpless with dissolve

    jl "切割嘉然和维持热度之间并没有直接的关系，我们可以用更柔性的解决方案，比如先进行四人直播，安抚粉丝..."
    #立绘 【阿草 愤怒】
    show ac angery with dissolve
    ac "够了！"
    ac "如果你要说这些的话就可以闭嘴了。"
    ac "我本来以为你是能看清形势的人，可惜。"
    #立绘【珈乐 哀】
    show jl sad with dissolve
    jl "我觉得事情还有商量的余地..."
    #立绘【阿草 日常】
    show ac normal with dissolve
    ac "没有这种余地了。"
    ac "你也看见B-SPIRIT现在有多火了，像你们这种偶像，公司想捧红多少都可以，不是缺了你们几个就不行的。"
    jl "我..."
    ac "你可以走了。"
    ac "看在一起共事过几年的份上，我奉劝你一句。"
    ac "不要再守着那个注定没有办法好起来的嘉然了。"
    ac "等到B-SPIRIT真的取代了你们的位置，你再哭着回来求我撇清关系，我也不会再理你了。"
    jl "对不起，我...同..."

    hide ac with dissolve

    show jl sad2 at center with dissolve
    jl "(等等，为什么连提出意见的机会也没有？)"
    jl "(公司的态度为什么这么强硬，难道真的没有什么回旋的余地了吗？)"
    jl "(只能...背叛...然然了吗？)"
    show jl doubt at center with dissolve
    jl "(等下，阿草刚才说了什么？)"

    #记忆闪回演出【类似老电视，泛黄带一些雪花】
    #BGM【紧张】
    #! 回忆开始
    hide jl

    show screen memory_filter 
    show ac normal at center 
    with fade
    ac "不要再守着那个注定没法好起来的嘉然了。"
    #【无立绘】
    hide ac

    show jl doubt at center 
    with quick_fade
    hide screen memory_filter 

    jl "(它为什么会这么说...)"
    hide jl

    show screen memory_filter 
    #立绘【向晚 哀】
    show xw sad at center 
    with fade
    xw "...不要太相信阿草了。"

    hide xw

    #【无立绘】 （感觉这里放上珈乐的立绘会更自然）
    show jl doubt at center 
    with quick_fade
    hide screen memory_filter 

    jl "(阿草确实很怪，不过究竟是哪个方面...？)"
    jl "(为什么一定要切割嘉然呢？明明还有更好的选择的...)"
    jl "(不对，不是这里，虽然很不合理，不过这有可能是公司的决定...)"
    hide jl

    #立绘【同第一章】
    show screen memory_filter 
    show nl gloomy at center 
    with fade
    nl "但我发现我们宿舍区搬进了五个新来的女孩。"

    hide nl

    #【无立绘】
    show jl doubt at center 
    with quick_fade
    hide screen memory_filter 

    jl "(就算B-SPIRIT最近势头很猛，公司也不会这么轻易就放弃我们吧？)"
    jl "(还有粉丝...)"
    jl "(仅仅是停播一周，评论区就只剩下谩骂和侮辱了，甚至激进到做出暴力行为，为什么？)"

    #立绘【同第一章】
    scene 医院走廊1 
    show screen memory_filter
    with fade
    "【医生】" "据我们诊断不像是受外部刺激导致的选择性失忆，倒更可能是无明显诱因导致的连续性失忆。"
    scene 阿草办公室 夜 
    show jl doubt at center
    hide screen memory_filter 
    with fade

    jl "(嘉然的病真的是没有任何诱因的怪病吗？)"
    #立绘【珈乐 日常】
    show screen memory_filter
    with fade
    show jl normal at center with dissolve
    jl "唔...X团吗？我记得之前挺火的来着，不过..."
    hide screen memory_filter 
    show jl doubt
    with fade

    jl "(X团是怎么糊的？停播，然后被粉丝攻击，然后...)"
    jl "(杳无音信？)"
    jl "(X团的工具人是...)"
    jl "(第一个发现嘉然失忆，给嘉然叫救护车的人是...)"
    show jl shock
    jl "(都是阿草？！)" with sshake
    hide jl

    show screen memory_filter 
    #立绘【嘉然 喜】
    show jr happy at center 
    with fade

    jr "阿草真好，经常给我糖吃～"
    hide jr
    #! 回忆结束
    show ac normal at l2
    show jl angery at r2   
    hide screen memory_filter 
    with fade


    #立绘【珈乐 怒】

    jl "阿草。"
    ac "怎么，回心转意了？现在答应我的提议还来得及。"
    jl "嘉然的昏迷是不是和你有关系？"
    #立绘【阿草 疑惑】
    show ac panic with dissolve
    ac "..."
    ac "你为什么会这么想？我理解你很着急，不过..."
    jl "我问你，是不是你让嘉然昏迷的？"
    ac "..."
    show jl firm with dissolve

    jl "是你做的。"
    "珈乐的语气无比坚定，双目如炬死死的盯着阿草，阿草和她对视了几分钟，然后笑出了声。"
    #立绘【阿草 得意】
    show ac proud with dissolve
    ac "没错，是我做的"
    ac "不过...你为什么会知道？"
    #立绘【珈乐 日常】
    jl "推理，加上一点点直觉..."
    ac "有趣，我以前都不知道你还有侦探的天赋。"
    #立绘【珈乐 怒】
    show jl angery with dissolve
    jl "你为什么要这么做！"
    show ac happy with dissolve
    ac "哈哈哈哈哈哈哈～"
    ac "珈乐，你比我想象的要聪明很多，我应该给你什么奖励才好呢？"
    jl "奖励？你在说什么，你已经犯法了！"
    "咔！咔咔！"
    play sound "audio/se/iron_door2_O.mp3"
    "珈乐后退几步，想要打开门跑出去，然而徒劳的转动了几次把手后她绝望的发现，不知何时房门已经被反锁上了。"
    stop sound

    ac "究竟给你什么好呢...对了，不如带你看一下..."
    ac "这个世界真实的一面。"
    "阿草站起身来，一步步缓慢的向珈乐走去。"
    show jl shock  with dissolve

    jl "你...你不要过来！"
    show jl pain  with dissolve

    "珈乐闭上眼睛，从口袋里摸出随身携带的防狼电击器向前猛捅过去。"
    #【黑屏】【音效：电弧声】
    scene black with fade
    play sound "/audio/se/电流声2.wav"
    "滋啦——！"
    stop sound

    "手上传来了击中的触感，耳边也响起了噼啪的电弧声。"

    "珈乐砰砰乱跳的心脏稍微变得安定了下来，她缓缓睁开眼睛，却发现..."
    #【恢复场景】
    scene 阿草办公室 夜 
    #立绘【阿草 日常】
    show ac proud at l2
    show jl shock at r2 
    with fade
    ac "很不可思议吗？习惯就好了，你一会就会看到更加超越你常识的...现实。"
    "能轻松让成年男子失去反抗能力的电流在阿草身上游走着，却无法伤害它分毫。"
    "啪嗒——"
    "它的身体没有任何动作，可珈乐却感觉身体被从四面八方挤压住了，吃痛之下，电击器也掉落在了地上。"
    play sound "/audio/se/金属爆炸2.mp3"

    "轰隆隆——" with sshake
    #【屏幕晃动】
    
    "随着一阵巨响，办公室的墙壁向两侧分开，露出了一台电梯。"
    #立绘【珈乐 焦急】
    play sound "audio/se/电梯开门.mp3"

    show jl pain with dissolve
    jl "你要干什么...你要带我去哪？快放开我！"

    
    jl "放开！让我出去，你这是犯罪你知道吗？！"

    scene 电梯内部 with dissolve
    play sound "audio/se/电梯运行.mp3"

    "不管珈乐怎样挣扎，她都无法移动哪怕一丝肌肉，只能惊慌地看着电梯上显示的数字飞快的跳动。"
    "20，30，100...最后停留在了168层"
    stop sound
    #这里可以插入电梯运行的音效 等待实现
    ac "见识一下吧，大楼的顶层，真正的世界。"
    play sound "audio/se/电梯开门.mp3"

    "电梯的门打开了。"
    stop sound

    play music "audio/bgm/危机1.mp3" fadeout 5.0 fadein 4.0

    #场景【公司顶楼 总控制室】
    scene 总控制室 with fade
    "无数的监视器屏幕环绕着一个奇怪的装置，充斥着整个房间，忠实的传递着城市每个角落的影像。"
    "透过透明的玻璃幕墙，可以俯瞰整个枝江。"
    "站在这个房间的中心，就仿佛坐上了枝江的王座。"
    #立绘【珈乐 震惊】
    show jl shock at r2 with dissolve
    jl "这...这是..."
    #立绘【阿草 日常】
    show ac normal at l2 with dissolve
    ac "感到荣幸吧，你可以见证这神圣的一刻。"
    "阿草按下了了房间中心台子上的按钮。"
    "随着一阵仿佛祈祷却又无法听懂哪怕一个音节的空灵女声，圣洁的白光从地平线上升起，逐渐笼罩了整个枝江，最后汇聚到了大楼的天台。"
    #【演出 背景泛起白光】
    "然而，仿佛除了珈乐，没有人能感觉得到异常一样，监视器屏幕上的人们还在有条不紊的继续做着原来的事。"
    ac "枝江市的繁荣来自哪里，你知道吗？"
    #立绘【珈乐 日常】
    show jl shock at r2 with dissolve
    jl "..."
    ac "来自偶像。当然，指的不是偶像所带来的经济效益，而是..."
    ac "情绪能量。"
    ac "见识到我的力量之后，你对于这种能量也稍微理解一点了吧？"
    ac "献祭粉丝数量众多的偶像可以获得大量的能量，公司也正是依靠这份能量逐渐成长成了庞然大物。"
    ac "在枝江，公司就是秩序。"
    ac "而嘉然..."
    "其中一个屏幕上显示出了嘉然房间内的景象。"
    "她的身上泛起的白光无比浓郁，熟睡的脸颊上带着一丝神圣不可侵犯的韵味。"
    ac "是天生就可以吸引大量粉丝的人，如果将她献祭，能够得到的情绪能量将不可估量。"
    #立绘【珈乐 震惊】
    show jl shock at r2 with dissolve
    jl "这怎么可能..."
    ac "你很震惊...我能够理解。"
    #立绘【珈乐 怒】
    show jl angery at r2 with dissolve
    jl "你是想献祭嘉然，来得到能量？"
    ac "当然。"
    ac "不过，你为什么会觉得气愤呢？"
    jl "为什么不会！你害了之前那些无辜的偶像，现在又要来害嘉然...！"
    show ac angery
    ac "无辜？别逗我笑了！"
    "阿草狠狠的咬了咬牙，压迫住珈乐的无形力量瞬间增大了几分，珈乐闷哼了一声，眉头紧锁。"
    #立绘【珈乐 痛苦】
    show jl pain at r2 with dissolve
    jl "唔..."
    ac "你知道吗？我来自贫民窟。"
    ac "你可能都无法想象，这个枝江还会有那么落后的地方。"
    ac "几公里外的人们享受着现代化的舒适生活，而我们住在一百年前的房子里，捞他们的泔水为食。"
    ac "后来我加入了公司，一步一步的爬到这个地位。"
    ac "我就更能够体会到，人一出生在这个世界上，就伴随着不平等。"
    ac "在公司的眼里，偶像，民众，都只是食粮。"
    ac "而贫民，只能算得上无用的残渣。"
    ac "这个世界，运行在一个错误的秩序中。"
    ac "今天的枝江，绝对不可能靠换一批偶像，换一批管理者就能改变，它需要彻底颠覆。"
    ac "而能够调动远超其他偶像情绪能量的嘉然，就能让我改变这个秩序。"
    ac "而混乱就是阶梯，我会颠覆秩序，然后重造它。"
    #立绘【珈乐 怒】
    show jl angery at r2 with dissolve
    jl "你觉得秩序错了，你就去改变啊！"
    jl "要带来混乱，还要牺牲嘉然去实现，这算什么！"
    ac "你应该这么说吗？"
    ac "你不应该赞同我吗？"
    ac "明明你和我一样...都只不过是注定被屠宰的猎物罢了！"
    #立绘【珈乐 震惊】
    show jl shock at r2 with dissolve
    jl "你说...我是猎物？"
    ac "没错...你以为你是光鲜亮丽的顶流偶像吗？"
    ac "你只不过是这座城市可有可无的一个人罢了！"
    jl "你在说什么？我是A-SOUL的一员，才不是什么可有可无的人！"
    ac "是吗？"
    ac "你觉得，你和她们是一样的吗？"
    ac "你和贝拉是青梅竹马吧..."
    ac "站在天才的身边，你真的觉得世界是公平的吗？"
    "一股冰冷的感觉沿着神经从珈乐的脚直窜到头顶，她打了个寒战，无数记忆不受控制地从大脑的深处涌出。"

    scene 练舞室 
    show screen memory_filter
    #立绘【小珈乐 日常】
    show jl child at center 
    with fade
    jl "(每个艺术生都有自己的骄傲。)"
    jl "(然而看到她的那一刻，我就知道，她才是C位。)"
    jl "(她就像永远高悬在夜空的北极星，星河在她的面前都会黯淡无光。)"
    show jl child expect 
    jl "(我也想像她一样闪闪发光。)"
    jl "(后来，我成了小有名气的童星。)"
    jl "(还确定在巡演中和她同台演出。)"
    jl "(我终于可以站在她的身边，光芒和她交相辉映。)"
    show jl child sad at center
    with fade
    #立绘【小珈乐 痛苦】
    jl "啊...啊..."
    jl "呵...呼...啊啊..."
    jl "呜呜...呜呜呜呜呜..."
    #立绘【小珈乐 失落】
    show jl child sad at center with dissolve
    jl "(为什么，没有办法发出声音...)"
    jl "(明明...)"
    jl "(距离演出只有三天了...)"
    # hide jl with dissolve
    #医生：

    "【医生】" "你这是练习过度了，要是再继续这样下去，可能会对声带造成不可逆的损伤。"

    show jl child sad at center with dissolve
    jl "(不要...我还没有追上她...)"
    hide jl with dissolve
    #立绘【小贝拉 日常】
    show bl child smile at center with dissolve
    bl "不要放弃！珈乐，我们要一起实现梦想呀！"

    scene 总控制室 
    show ac normal at l2 
    show jl angery at r2 
    hide screen memory_filter 
    with fade
    jl "(你懂什么！像你这样...不管在哪里，都掩盖不住光芒的人，有什么立场说出这种话！)"

    ac "苟且偷生的东西，也渴望触摸星辰吗？"
    #立绘【珈乐 怒】
    jl "我才...不是！"
    jl "我是贝拉的朋友...是和她一起互相追逐对方的身影，追逐梦想的挚友啊！"
    ac "互相追逐？"
    ac "你不会以为，自己在某个时间段是贝拉的榜样吧？"


    scene 练舞室 
    show screen memory_filter

    show jl happy at r2
    show bl normal at l2
    with fade

    jl "我被公司录取了。"
    jl "和我一起，成为偶像吧！"
    # hide bl with dissolve
    jl "(她是我一直在追逐的目标。)"
    jl "(我不甘心...让这一切以她跌落尘埃为结局。)"
    jl "(我会成为你的标杆，和我一起，在新的赛道上奔跑吧！)"
    #场景【客厅】
    scene LivingRoom_light 
    show jl normal at center 
    with fade
    "【总监】" "嗯，这五个人里面实力最强的果然还是贝拉。"

    "【总监】" "就让贝拉当队长吧。"
    show jl sad with dissolve 
    #【无立绘】

    jl "(虽然先被签下的是我，可是最后的队长是她。)"
    jl "(果然明珠在哪里都不会蒙尘。)"
    #! 回忆结束
    scene 总控制室 

    show ac normal at l2 
    show jl anxiety at r2 
    hide screen memory_filter 
    with fade

    ac "她只是按照自己的步调在前进而已，你就又被她甩在身后了。"
    ac "人和人，生来就是不一样的。"
    ac "除非...这个世界没有任何秩序存在。"
    #立绘【珈乐 日常】
    jl "我才没有那么想。"
    ac "嘴巴会骗人，可是大脑不会。"
    ac "你的想法，只有自己知道。"
    ac "你和我一样，都只是偶然混进了上流社会的..."
    ac "残渣。"
    jl "..."


    #演出【回忆】
    #! 回忆开始
    #场景【珈乐首播场景】
    scene LivingRoom_light 
    show screen memory_filter

    #立绘【珈乐 日常】
    show jl normal at center 
    with fade
    $ tmp_dmk_list = ["猜不中", "我急了，不猜了", '取关取关', '学嘉然那一套折磨观众是吧？', '就嗯猜？' ,'不看弹幕吗？', "rp？rp？"]

    show screen dmk_screen(haveColor=True)

    jl "大家好啊，再向大家做一下自我介绍，我是偶像，珈乐，很高兴今天...遇见你。"
    jl "(第一次直播，一定要成功...)"
    window hide
    $ renpy.pause(4)
    window show
    show jl anxiety at center with dissolve
    jl "(应该怎么做？他们在说什么？我...我...)"

    $ tmp_dmk_list.append('不给点提示？')
    jl "给...给啥提示啊，你们要是都猜出来了..."
    jl "没有提示，猜吧猜吧猜吧。"
    jl "....你们真的要再靠几个字来判断歌曲吗？"

    $ tmp_dmk_list = ["\尬乐/\尬乐/\尬乐/", "尬住乐", "人设是吧", "玩rp？", "下播下播下播下播", "乐乐乐乐乐"]

    jl "(为什么...我会搞成这个样子...)"
    jl "(明明为了首播准备了那么久，可是为什么...)"
    #场景【客厅】
    hide screen dmk_screen

    show jl sad at center 
    with fade
    "【总监】" "珈乐！你首播这弄的是什么东西！" with sshake
    "【总监】" "我看你也不用再继续直播了，给我停播再练一个月，不行就收拾东西走人！"

    #! 回忆结束

    scene 总控制室 
    show ac normal at l2
    show jl anxiety at r2
    hide screen memory_filter 
    with fade
    ac "你和她们不一样。"
    ac "你只是普通人，却混进了天才的队伍里。"
    ac "你难道不想毁掉这不公平的一切吗？"
    #立绘【珈乐 痛苦】
    jl "不...不！不是这样的！"

    hide ac
    hide jl 


    #演出【回忆】
    #! 回忆开始
    show screen memory_filter
    with fade

    jl "(我和她们不一样...)"
    #立绘【轮流出现四人的立绘】
    show bl normal at center with dissolve
    jl "(贝拉有专业的舞蹈功底，娇憨可爱的形象。)"
    hide bl with dissolve
    show nl normal at center with dissolve
    jl "(乃琳很会聊天，控场能力一流。)"
    hide nl with dissolve
    show xw normal at center with dissolve
    jl "(向晚和粉丝打成一片，是大家的好兄弟。)"
    hide xw with dissolve
    show jr normal at center with dissolve
    jl "(嘉然...没有人不喜欢她。)"
    hide jr with dissolve
    show jl sad at center with dissolve

    jl "(而我只会唱歌。)"
    jl "(不会聊天，也不好相处。)"
    jl "(只会把一切都搞砸。)"
    jl "(她们的粉丝疯长，而我却...)"
    jl "(我只是普普通通的女孩，却幻想与她们一并成为星辰。)"
    #! 回忆结束

    #立绘【阿草 得意】
    show ac proud at l2 
    show jl sad at r2 
    hide screen memory_filter 
    with fade
    
    ac "看来你懂了，乖女孩。"
    ac "站到我这一边，我会用公司的力量让你单独出道。"
    ac "让我们一起，把那些生来优越的人当成燃料焚烧吧。"
    ac "而你，将会是我的羽翼。"
    "一直压迫着珈乐的怪力消失了。"
    hide ac

    show jl helpless at center with dissolve
    "珈乐落在了地上，缓缓的向阿草走去。"
    #【上CG】（下面回忆部分撤CG，现实部分上CG）

    scene 监控室珈乐 with slow_fade
    jl "我...将会成为你的臂膀。"
    jl "(我只是普通人，所以...)"
    jl "(我不需要再管她们了...)"
    jl "(我只要独自闪耀就够了...)"
    jl "(...为什么？)"
    jl "(这真的是我的选择吗？)"
    with vpunch
    $renpy.pause(0.5)
    "一步，一步。" with vpunch
    "珈乐距离阿草越来越近了。"


    #回忆
    #! 回忆开始
    scene 练舞室 
    show screen memory_filter
    #场景【练舞房】
    #立绘【小珈乐 日常】
    show jl child expect at r2
    show bl child 练习 at l2
    with fade
    jl "哇，你的舞蹈服都被汗给浸透了啊，你不累吗？"
    #立绘【小贝拉 日常】
    #bl
    show bl child smile2 with dissolve
    bl "不累呀，因为我喜欢舞蹈，我想成为最专业的芭蕾舞演员！"

    jl "(我也要像她那样出众...)"
    jl "(所以我起得更早，睡得更晚。)"
    jl "(变得更加优秀。)"
    #! 回忆结束

    scene 监控室珈乐
    hide screen memory_filter
    with fade

    jl "(但是...)"
    jl "(不也没能追得上她吗？)"
    jl "(一点点的天分就可以抹煞掉几年的努力...)"


    with vpunch
    $renpy.pause(0.5)
    "一步，一步。" with vpunch


    scene 练舞室 
    show screen memory_filter
    #场景【练舞房】
    #立绘【贝拉 痛苦】
    show bl child sad at l2
    show jl child sad at r2
    with fade
    bl "啊...！"
    bl "呼...呼..."
    #立绘【珈乐 担忧】

    jl "你要不要休息一下..."
    jl "毕竟才刚刚痊愈..."
    #立绘【贝拉 日常】

    bl "我要...站起来。"
    bl "我要回到舞台上去。"
    bl "毕竟珈乐已经在那里等着我了。"
    #立绘【贝拉 喜】
    show bl child smile2 at l2 with dissolve
    bl "我的梦想要和你一起实现，约好了哦！"

    scene 监控室珈乐
    hide screen memory_filter
    with fade
    jl "(连她自己都忘记了！)"
    jl "(我...为什么还要在意约定呢？)"
    jl "(自取...其辱。)"
    #演出【屏幕晃动】
    with vpunch
    $renpy.pause(0.5)
    "一步，一步。" with vpunch


    #演出【回忆】
    #! 回忆开始
    #场景【客厅】
    scene LivingRoom_light 
    show screen memory_filter

    show jl happy at center 
    with fade


    "【总监】" "声乐老师跟我说了，珈乐你的歌唱技巧很好。"
    #总监：
    "【总监】" "以后你的定位就是A-SOUL的歌唱担当了。"
    #总监：
    "【总监】" "我对你的期望很高。"
    #总监：
    "【总监】" "不要让我失望。"
    #! 回忆结束


    scene 监控室珈乐
    hide screen memory_filter
    with fade

    jl "(只是唱歌好又有什么用呢？)"
    jl "(直播效果尴尬，接不上梗。)"
    jl "(我只不过是笑话...！)"
    #演出【屏幕晃动】
    with vpunch
    $renpy.pause(0.5)
    "一步，一步。" with vpunch
    jl "(....)"
    jl "(我...我以前是这么做的吗？)"
    jl "(靠摧毁他人来抬高自己？)"
    jl "(不是，不是不是不是...！)"
    jl "(我是...怎么做的？)"
    jl "(我是...)"


    play music "audio/bgm/有点逆天的可控的日常.mp3" fadeout 5.0 fadein 5.0

    scene LivingRoom_light
    show screen memory_filter
    show jl sad at center 
    show bl sad at l2 
    show nl normal at r2 
    show xw normal at l4 
    show jr normal at r4 
    with fade
    bl "珈乐，哭的时候就不要唱歌了吧..."
    #立绘【珈乐 痛苦】
    jl "我要唱...我...我练了这么多年...为什么到了现在却...没有办法控制住声线..."
    jl "我是不是真的不行..."

    #立绘【乃琳 日常】
    nl "你可以的，珈乐一直都是最棒的。"
    #立绘【向晚 日常】
    xw "没事没事，珈乐很厉害的！"
    #立绘【 嘉然 日常】
    jr "多多练习一定能掌握的，毕竟珈乐那么专业嘛..."
    show bl normal at l2 with dissolve
    bl "不要放弃！我们一起努力呀！"
    jl "(难过时候不流泪)"
    jl "(流泪也不算伤悲)"
    jl "(哭着唱了三个小时之后，我可以自如地控制低音了。)"    

    #! 回忆结束
    #演出【屏幕晃动】
    scene 监控室珈乐
    hide screen memory_filter
    with fade
    with vpunch
    $renpy.pause(0.5)
    "一步...一步..." with vpunch


    #回忆
    #! 回忆开始
    #场景【客厅】
    #立绘【向晚 日常】
    scene LivingRoom_light
    show screen memory_filter
    show xw normal at l2 
    
    show jl normal at r2 
    with fade

    xw "珈乐，你怎么这么早就醒了啊？"
    "向晚端着泡面锅从厨房出来，看着坐在沙发上写写画画的珈乐，有些诧异。"
    #立绘【珈乐 日常】
    jl "如果不了解粉丝们喜欢的东西，就没办法接他们的梗了。"
    jl "我既然首播失利，就得更努力一些才行..."
    xw "只有三十个人的内测直播会不会很辛苦啊？"
    xw "毕竟平时的功课训练也不能落下。"
    show jl sad at r2 with dissolve
    #立绘【珈乐 哀】
    jl "很辛苦...很累啊。"
    #立绘【珈乐 喜】
    show jl happy at r2 with dissolve
    jl "不过，我也变得更强大了。"
    jl "下次，应该能让他们喜欢吧？"
    #立绘【向晚 喜】
    show xw happy at l2 with dissolve
    xw "珈乐...好厉害！"
    xw "泡面给你吃一口？"
    show jl normal at r2 with dissolve
    #立绘【珈乐 日常】
    jl "才不要！会变胖的！"
    #! 回忆结束

    scene 监控室珈乐2
    hide screen memory_filter
    with fade

    jl "(我只是一个普通人。)"
    jl "(我来自普通的家庭，过着普通的生活，拥有普通的才能。)"
    jl "(但是我想要的是不普通的自己。)"
    jl "(所以，我...)"

    with vpunch
    $renpy.pause(0.5)
    "一步...一步..." with vpunch
    "珈乐走到了阿草的面前。"
    # show ac normal at center with dissolve
    ac "很好，走过来...我们一起破坏这个不公平的世界。"
    # hide ac with dissolve


    #回忆
    #! 回忆开始
    scene LivingRoom_light
    show screen memory_filter
    show jl happy at center 
    with fade
    #立绘【珈乐 喜】
    jl "爱上了也没办法，不管对方是什么人哦～"
    jl "(我渴望闪耀...)"
    #立绘【珈乐 日常】
    show jl normal at center with dissolve
    jl "该怎么去形容你～最贴切～"
    jl "(我喜欢唱跳...)"
    #总监：

    "【总监】" "嗯，内测直播的效果很不错。"
    #总监：
    "【总监】" "这段时间你的辛苦大家都看在眼里，你复播的日子已经确定了。"
    #总监：
    "【总监】" "这次一定要加油！"

    #立绘【珈乐 焦急】
    show jl anxiety at center with dissolve
    jl "(身体有些颤抖。)"
    jl "(一半是激动，一半是紧张。)"
    hide jl with dissolve
    #立绘【贝拉 日常】
    show bl normal at center with dissolve
    bl "放轻松啦，你不是都记了这么多笔记了嘛？一定没事的！"
    hide bl with dissolve
    #【无立绘】
    jl "(那一次直播的记忆已经变淡了，记不清到底发生了什么。)"
    jl "(但是我成功了。)"
    jl "(得不到的东西便伸手去够，做不到的事就花时间去学。)"
    #! 回忆结束


    #【撤CG】
    #立绘【珈乐 日常】
    scene 总控制室 
    show jl normal at r2 
    show ac normal at l2 
    hide screen memory_filter
    with fade

    "珈乐向阿草缓缓地伸出了手。"
    ac "要握手吗？好吧..."
    show jl firm  with dissolve
    
    jl "哼！"

    play sound "audio/se/拍击_耳光_巴掌声音.wav"
    show ac angery
    "啪！"
label cp3_test:


    #音效【巴掌声】
    #立绘【阿草 愤怒】
    ac "你..."
    ac "你敢打我？！你怎么配打我？"
    ac "你怎么，你怎么敢！你这底层的残渣！"
    ac "明明你所有的负面情绪都已经被我调动起来了！"
    ac "怎么会..."
    ac "你怎么会感觉到希望啊！"


    #回忆
    #! 回忆开始
    scene 直播用房间
    show screen memory_filter
    #场景【珈乐房间】
    #立绘【珈乐 日常】
    show jl normal at center
    with fade
    $ tmp_dmk_list = ["珈乐珈乐珈乐", "乐乐乐乐乐",'乐乐乐乐乐乐乐乐乐', '风情！', 
    '骑士团骑士团', '宝藏女孩大家点点关注' ,'我一直都是皇珈骑士啊','好听','好好好好好','好好好',
    '\珈乐/\珈乐/\珈乐/','好！','乐！']

    show screen dmk_screen(inteval_set=(50,100),max_dmk=200,haveColor=True)
    play music "audio/voice/珈乐云烟成雨.mp3" fadeout 4.0 fadein 3.0 noloop
    jl "若一切 都已云烟成雨"
    jl "我能否变成淤泥，再一次沾染你~"
    jl "若生命 如过场电影"
    jl "Oh 让我再一次 甜梦里惊醒"
    jl "我多想再见你"
    jl "哪怕匆匆一眼就别离"
    jl "路灯下昏黄的剪影"
    jl "越走越漫长的林径"
    show jl happy at center with dissolve
    window hide
    $ renpy.pause(15.0)
    window show
    jl "谢谢大家！"
    jl "谢谢大家的支持～～大家的应援～"
    jl "以后也请陪王力口乐一起走下去吧！"
    jl "皇珈骑士你们真是太棒啦"
    play music "audio/bgm/第二章-希望.mp3" fadeout 5.0 fadein 2.0

    hide screen dmk_screen
    #立绘【珈乐 坚定】
    scene 总控制室 
    show jl firm at r2
    show ac normal at l2
    hide screen memory_filter 
    with fade
    jl "我不是任何人的猎物...！"
    jl "我或许只是...一个普通人。"
    jl "但是..."
    jl "我的直播效果变得很棒了。"
    jl "我拥有了许多皇珈骑士们。"
    jl "红色高跟鞋成了枝江街头巷尾传唱的曲目。"
    jl "我已经变得强大起来了。"
    jl "我是...狼，我是独一无二的，Carol珈乐！"
    jl "像你这样注定要被宰割的猎物，想要得到什么只能靠别人施舍。"
    jl "就算偶然站到了高处，也只会担心失去这捡来的一切。"
    jl "而我，会靠我的双手去取！"
    jl "(我是一天又一天，唱到嗓子沙哑才走到这里的！)"
    jl "(虽然生来平凡，虽然命运捉弄...)"
    jl "(但是，我是...)"
    jl "(靠着自己的双腿走到第一女团的位置上的！)"

    "阴冷的猎物抬着头，只能看到墙角一隅。"
    "而孤狼长啸，于无星之夜，仍能轻易窥得星斗。"
    show ac angery at l2 with dissolve
    ac "我不是被施舍！"
    ac "是你！你被道貌岸然的公司欺骗了，你被虚无缥缈的梦想迷惑了！"
    ac "你明明都已经知道真相了，为什么还要执迷不悟！"
    ac "看看这片虚伪的霓虹吧！我要让它们熄灭，让它们变为一片废墟！"
    show jl pain with dissolve
    "阿草怒吼着，无形的怪力又一次将珈乐抓了起来，将她的骨骼挤压得咯吱作响。"

    jl "我...知道了真相，那我会去推翻公司，停止用偶像当情绪能源的燃料，改造贫民窟，创造新秩序！"
    jl "而不是去用嘉然的命去摧毁，去破坏，去带来混乱！"
    #音效【撞击声 玻璃破碎声】
    play sound "/audio/se/身体撞在墙上.mp3"
    "咚——！"
    play sound "/audio/se/玻璃破碎.mp3"
    show jl pain with dissolve

    "珈乐的身体在怪力的作用下猛地撞在了玻璃幕墙上，她的脸色瞬间变得惨白，闷哼出声。"
    ac "你...你只会说些漂亮话！"
    #立绘【珈乐 微笑】
    show jl smile at r2 with dissolve
    jl "或许吧..."
    jl "但是我之前说的漂亮话，最后可是都努力做到了..."
    jl "(偶像，是贩卖梦想的职业。)"
    jl "(我和伙伴们相遇，编织出梦想，然后卖给粉丝。)"
    jl "(而粉丝的支持，也会反馈给我力量。)"
    jl "(我要让所有的人都得到幸福。)"
    jl "(这就是我，这就是A-SOUL。)"
    #立绘【珈乐 自信】
    show jl firm at r2 with dissolve
    jl "因为我是...枝江小狼王。"
    jl "狼的视野，要比猎物更远..."
    ac "我...我原本还以为你能想清楚的！"
    ac "既然这样你也没有什么用了，给我变成燃料吧！"
    jl "不...我可没想过要当你的燃料。"
    jl "防身喷雾，快要渗进去了吧？"
    ac "你说什么？"

    play sound "audio/se/爆炸声.mp3"
    hide ac
    show jl normal at center with dissolve

    "轰隆——！" with sshake
    "刚刚在阿草不注意时丢下的防身喷雾流的液体到了被高跟鞋磨破胶封的电线上，引发了一串连环爆炸。"
    #演出【屏幕震动】
    "阿草的身影被浓烟遮蔽了，那一股怪力也变得松懈下来，珈乐短暂的恢复了自由行动的能力。"
    #立绘【珈乐 日常】
    show jl normal at center with dissolve
    jl "再见了。"
    play sound "/audio/se/玻璃破碎.mp3"
    "珈乐的身体向后倒去，刚刚就已经被她撞得龟裂的玻璃幕墙彻底粉碎了。"
    #场景【枝江外景】
    scene 夜空满月 with fade
    #【无立绘】
    "身体仿佛漂浮在了空中，仰起头就能看见夜空。"
    "星河闪耀。"
    "从168楼自由落体的时间是10秒以上。"
    "珈乐摸出了手机。"
    "贝拉...首字母是B的话，应该在是通讯录的第一个吧？"
    "按住语音键。"
    jl "小心，阿草有问题。"
    jl "他的办公室有秘密电梯。"
    jl "对不起，约定...没办法..."
    "发送成功"
    "收件人：AvA向晚。"
    #音效【玻璃破碎声】

    "手机掉落在地上，摔得粉碎。"
    #【黑屏】
    scene black with Dissolve(3)
    "手不自觉的会往你的方向摸一下～"
    "想确定你就在身旁～"
    "熟悉的旋律还在街边某些人的手机中回响着。"
    "这绝不是错觉。"
    stop music fadeout 3.0
    scene black with Dissolve(3)

    jump cp4_start
