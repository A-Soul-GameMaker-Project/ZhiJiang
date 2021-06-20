init python:
    declare('病房走廊', 'bg/1 医院走廊2.png', 'p')
    declare('嘉然病房', 'bg/0 3 病房.png', 'p')
    declare('枝江街头模糊', 'bg/9 枝江街头模糊.png', 'p')
    declare('枝江街头不模糊', 'bg/9 枝江街头不模糊.png', 'p')
    declare('天台', 'bg/1 9 天台.png', 'p')

default goNe = True
default goTe = False

label cp8_n_start:
    window hide
    $ save.cp_name = "第八章"
    $ goNe = True
    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/8.1.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True
    jump cp8_n.part1


label cp8_n:

label .part1:
    #########
    #"PART1"
    #【病房走廊，向晚冷漠】
    play music "audio/bgm/抒情1.mp3" fadeout 5.0 fadein 4.0

    scene black
    show 逆时针 zorder 5 at normal_size
    with dissolve
    $ renpy.pause(3, hard=True)
    hide 逆时针

    scene 病房走廊
    show screen memory_filter
    show xw unconcerned at center
    with dissolve
    window show

    xw "（珈乐仍会尝试说服贝拉，寻求她的认同，但这种举动注定是徒劳无功。）"
    xw "（所以她们会继续为是否放弃嘉然的问题而继续纠结一段时间，但最终什么结果都得不出来。）"
    show xw anxiety at center with dissolve
    xw "（而对我来说，只要她们争执起来就已经不需要我的存在了。）"
    xw "（我此时的任务就是让她们吵起来，而我已经完成了任务。）"
    #【脚步声】
    play sound "audio/se/高跟鞋走路.wav" fadeout 1.0 fadein 3.0
    xw "（比起平息她们的争吵，还有更重要的事情等着我去做。）"

    scene 医院角落菜地白天
     ##加菜地背景 5 9医院角落菜地(白天)
    show xw unconcerned at center

    with dissolve
    "病房，一楼屋檐。"
    stop sound

    xw "（在窗户下面站定，做好准备，等待三秒。）"
    xw "（三，二，一...）"
    xw "（小的要来了）"
    #【屏幕震动】
    with sshake
    "猫咪从三楼嘉然的病房窗户上失足坠落下来，它坠落的缘故是嘉然睡着了，没有人陪它玩，珈乐和贝拉在门口吵架，于是它想从窗户溜出来。"
    "最近下了雨，窗沿布满了湿漉漉的雨迹，猫咪掉下来的原因是脚滑了。"
    "如果把窗户关上，它会不断地喵喵叫，直到把然然吵醒。"
    "然然已经很累了..."
    "所以，顺手接住它是最好的选择。"
    "向晚轻轻抱着它的腰，将它放到地上。"
    ##还没有猫叫吗
    #【猫叫两声】
    play sound "audio/se/cat1a.mp3"
    "猫咪蹭了一下向晚的腿，往医院的远处撒欢地抛开，消失在医院的拐角里，它会在嘉然起床的时候，被贝拉发现抱回去。"

    xw "（它的名字叫崽崽，如果我再晚来一秒，它会躺在地上，一动不动，嘴角带着斑斑血迹。）"
    xw "（嘉然明天会抱着它的身体，在病院的角落里，蹲着流着眼泪，不肯动弹，就算我来拉她也一样。）"
    show xw unconcerned at center with dissolve
    xw "（这只猫咪从窗台上坠下的过程已经重复了611次)"
    xw " (世界对我的存在漠不关心，它无动于衷地维持着每一件事的分毫不差。）"
    xw "（而我却一直期待着世界因为我的举动而发生改变。）"
    show xw normal eyeclosd at center with dissolve
    xw "（周围的每一处细节在不断地轮回后已经刻印在我的脑海当中。）"
    xw "（如果没有必要，我保证自己每一次的行为和上一次轮回保持一致。）"
    show xw unconcerned at center with dissolve
    xw "（控制变量法，是能够让我通向更好结局的唯一解。）"
    xw "（我等待着一次机会，一次能够彻底改变这个世界的机会。但现在这个时间点显然我不该轻举妄动。）"
    xw "（我该回去了。）"

    #【转场，嘉然病房，向晚温柔】
    scene 嘉然病房
    show xw unconcerned at center
    with dissolve

    "嘉然此刻正在白色的床单上熟睡着，传来安眠时细微的呼吸声，珈乐和贝拉已经不知所踪，向晚轻轻地扭开了病房的把手。"
    xw "（现在，我最好在这里等待着，珈乐几分钟后会从我的身旁跑过。）"
    show xw wronged at center with dissolve
    xw "（在这间病房的这几分钟，是我每次轮回里最自由的时候。此后的时间，不属于我，属于一个名为向晚的机器人。）"
    xw "（向晚的时间已经停止在询问嘉然“为什么会选择成为偶像呢”那一刻。）"
    show xw gloomy at center with dissolve
    xw "（无论是过去，现在，还是将来。向晚将不复存在，留在这里的是一个不断重复不断失败的观测者。）"
    show xw wronged at center with dissolve
    xw "（这次，乃琳还会在我的怀里再无动静吗...）"
    show xw proud at center with dissolve
    xw "（对了，今晚的温度会下降很快。）"
    ##布料摩擦声还没有吗
    #【布料摩擦声】
    "向晚将嘉然的被子提上了一点，妥实地掖好。"
    ##时钟滴答声还没有吗
    #【时钟滴答声】
    "抬手看了看表，距离珈乐到来的时刻还有一分钟。"

    show xw normal at center with dissolve
    xw "（我还能再看她最后几眼...）"
    "嘉然温顺的长睫毛轻轻颤动着，时光在她美好的睡颜里缱绻。"
    xw "做个好梦。"
    show xw normal eyeclosd with dissolve
    xw "（三，二，一）"
    show xw normal at center with dissolve
    xw "（自由活动时间结束，我该早点离开病房了，珈乐该来了。）"
    #【医院走廊，向晚疲劳】

    play music "audio/bgm/kirl老师的旋律发散.mp3" fadeout 5.0 fadein 4.0

    scene 病房走廊 with dissolve
    show xw wronged at l2 with dissolve
    "向晚倚靠着走廊拐角的白色墙壁，这能稍微地缓解一下她的疲惫，让她不至于直接瘫倒下去。"
    "每一次的轮回，她都要目睹至少一个伙伴倒在自己面前，目睹自己的无能为力。"
    "身体会自动恢复到轮回前的状态，但心灵的疲惫不会消失，黑色的红色的记忆顺着血管流淌到心脏，像凝滞的焦油渗透到每一个角落。"
    xw "玛卡巴卡、阿卡哇卡、米卡玛卡呣..."
    "这是嘉然教给她的一句神奇的咒语，只要默念几次，心灵就会自然而然地平静下来。"
    "没有悲伤的余裕，没有留给她休息的时间。"
    show xw calm with dissolve
    xw "珈乐。"
    # show jl shock at r2 with dissolve

    "向晚伸手拉住了珈乐。珈乐吓了一跳，露出了吃惊的表情。"
    "这个动作运用了心理学上的一个小技巧，先让对方陷入惊慌，对方就会更加情绪化，情绪化的珈乐比理智的珈乐更容易说服。"
    show xw sad with dissolve
    "这个小技巧是第313次遇到的乃琳教给我的，她还给我唱了一首《鸽子》。"
    "那个乃琳因为救我已经倒在了血泊当中，她的鲜血染上了我的手，怎么也擦不掉..."
    show xw calm with dissolve
    xw "没什么……只是有些事想跟你说。"
    xw "你要去找阿草，对吧？"
    "（先把她要去找阿草的事情说出来，击碎珈乐的谎言，不然现在的她听不进我说的话。）"
    show xw shock with dissolve
    xw "珈乐……那个……"
    xw "你对嘉然怎么想？"
    "（再用嘉然增加她的愧疚心。）"
    show xw doubt with dissolve
    xw "我没有埋怨你啊！"
    "（珈乐会误会，不过马上解释就可以了。）"
    #【向晚日常】
    show xw smile with dissolve

    xw "我知道珈乐是很温柔的女孩。"
    xw "虽然不熟悉的时候觉得你像冰块一样冷，不过熟悉起来就知道你的内心是很柔软很柔软的呢。"
    "（和她共情，与她情绪同调。）"
    show xw happy with dissolve
    xw "虽然我们总是吵架，但是我们依然是同伴，珈乐心里也是装着我们四个人的吧？"
    xw "不仅有贝拉，而且有乃琳，有我，当然也有嘉然，"
    "（减轻她的愧疚感。）"
    show xw wronged with dissolve
    xw "所以，我理解你……"
    "（一锤定音！）"
    show xw happy with dissolve
    xw "曾经有人和我说，水母是没有梦想的。只能在深海里度过相对失败的一生。但是有一只水母，它有了梦想。可能依然只是随波逐流……"
    xw "不过现在，这只水母也会发光了吧？水母觉得，如果被海浪冲回了原处，那么再漂回去就好了。"
    xw "水母不会失败……"
    "（即使闭着眼睛背，也已经一个字都不会错了。）"
    #【向晚哀】
    show xw worried with dissolve
    xw "这个给你……不要太相信阿草了。"
    xw "珈乐去做珈乐想做的事吧。"
    xw "（好累......）"
    xw "（对不起，珈乐。）"
    xw "你一定要小心……"
    #【时钟顺时针旋转】
    ##时钟帧动画不是出来了吗 手表滴答声

    window hide
    scene black
    show 顺时针 zorder 5 at normal_size
    with dissolve
    $ renpy.pause(4, hard=True)
    hide 顺时针


    scene 鲜花阳光
    with dissolve
    play music "audio/bgm/有点逆天的可控的日常.mp3" fadeout 5.0 fadein 4.0
    window show

    #【鲜花阳光无立绘对话框】
    xw "我对于世界的了解，源自于朋友，学校，教师，父母……描绘好的景象。"
    xw "但总会有一天，一个不好的日子，把你强制推出这幅景象之外。掀开鲜花盛开和温暖阳光的玻璃罩之后，从外面观察，才发现是涂抹的颜料。"
    #【下一页黑屏风声】
    ##风声呢
    xw "而外面的世界，被寒风吹彻。"
    ##插入背景 7 半月_云
    #【嘉然剪影】"
    ##show jr cut_shadow
    jr "人类居住在幽暗的海洋中一座名为无知的小岛上，海洋浩淼无垠，蕴藏着无穷秘密，但我们并不应该航行过远，探究太深。不然，就再也回不去那座小岛了。"
    jr "所以，继续活在自己对世界的美好臆测里，活在一派祥和的表象中，难道不是一种幸福吗？"
    #【缓缓消失过度】
    window hide
    scene black
    show 顺时针 zorder 5 at normal_size
    with dissolve
    $ renpy.pause(4, hard=True)
    hide 顺时针


    #【枝江市大街行驶的模糊效果，向晚：常，车辆喇叭声滴滴两下，】"
    scene 枝江街头模糊
    with dissolve
    window show

    "一辆黑色的豪华车辆驶过，它的车牌标志由2个交叉的M拼成。"
    "这是一辆迈巴赫，迈巴赫62S，世界上最昂贵的汽车。"
    "车的内饰光源闪烁蒙蒙的蓝光，跳动着车辆的行驶速度，导航地图显示着终点——枝江大厦。"

    # show xw sad with dissolve
    xw "（最近，在我的脑海里反复回响着一个声音，一个来自深海的声音。）"
    xw "（梦里的场景是漆黑幽寂的深海，这里没有任何生物生存，这里也没有丝毫光亮，留在这里的只有黑暗和海水。）"
    xw "（在深海的最底部，传来反复的颂唱——向下，向下，就能获得永恒安眠。）"
    xw "（我是一个被迫走上钢丝的平衡小丑，这条路看不到尽头。）"
    xw "（平衡杆早已落入了深渊。或许这根钢丝断裂之前，不知道在哪一次轮回，我就会滑落下去，被拖入深海，不再醒来。）"


    "路过一个城市和乡村交界的转弯口。"
    #【向晚: 常，"【管家】"：黑色剪影】"
    # show "【管家】" at r2 with dissolve
    "【管家】" "大小姐，大小姐..."
    "【管家】" "到了你说的地方了。"
    "【管家】" "这边都是一些贫困人口居住的地方，治安混乱，可能不太安全，您看是不是..."
    xw "先停车。"
    #【刹车声。关门声】
    "车辆缓缓地停了下来。"
    #【枝江街道（去掉行驶模糊效果，换个冷色调），向晚哀】
    scene 枝江街头不模糊
    with dissolve

    show xw gloomy at l2 with easeinleft
    show gj at r2 with dissolve
    "向晚从车后部拿了张毯子给晕倒在路灯下的一个流浪汉铺上，将一个放在自行车道的钉子踢开。"
    "然后，向晚回到车上拿起手机把刚刚点给然然的高级外卖取消掉，换了一家草莓蛋糕店的蛋糕......"

    "【管家】" "大小姐，我没搞明白，您这...您这是在做什么？"

    xw "如果我不这样做，我点的这个高级外卖会让一个人今后一年的晚餐少一块午餐肉"
    xw "一个骑着自行车经过这里的人会因为这枚路上的图钉失去养家糊口的一个月工资，因为过度应酬，醉倒在地板上的他会因为没有毯子而冻死在这个气温下降的街头……"

    "【管家】" "这个城市的可怜人这么多，您这样心血来潮去发善心，做到什么时候是个尽头呢。"
    xw "我不是在发善心，我只是想做到我所见的，我所力所能及的事，至少，我以后不会因为自己撒手不管而感到愧疚..."
    "【管家】" "您这么善良，从来不会去伤害别人，大小姐为什么会感到愧疚呢？"

    show xw sad at l2 with dissolve
    xw "（她们因我的无能而死，我们的粉丝彻底对我们失去希望，我想要改变这一切...）"
    xw "……我们接着走吧，去下一个地方。"

    "【管家】" "大小姐，已经这么晚了，您还打算去哪儿，夫人和老爷会担心的。"
    "向晚没有说话，只是用着疲惫和坚定的眼神看着管家。"
    "【管家】" "既然您坚持的话……好吧。"

    scene 枝江大厦外 夜
    with fade
    #【枝江市大街行驶的模糊效果引擎声本图片持续2s】
    "入夜。"
    "古代的巴比伦通天塔，传说是古巴比伦国王为天上诸神前往凡间修筑的歇脚处，被称之为天与地的住所。"
    "枝江大厦这座全城最高的建筑，楼高612米，是巴比伦塔的六倍之上，在它的顶端，闪烁着隐隐的红色辉光。"
    show xw calm at l2 with dissolve
    show gj at r2 with dissolve
    "车辆缓缓地停了下来。"

    "向晚向着塔顶久久地看了一会儿。"
    "从车停下来的地方，向远离大厦的方向走了100米。"
    xw "管家，在这里，把刚刚准备的特质气垫展开。"
    "管家在角落里展开了一个大型特质气垫，并在周围拉上了警戒线，立了施工中的牌子，这张特质的垫子，能吸收从高处坠下来的冲击力。"
    xw "现在，我们在这里的任务已经完成。走吧管家，时间很紧，我们还有很多事情要做。"




    window hide
    scene black
    show 顺时针 zorder 5 at normal_size
    with dissolve
    $ renpy.pause(4, hard=True)
    hide 顺时针

    scene 天台
    show xw normal eyeclosd at lc
    with dissolve
    $ renpy.pause(1.5, hard=True)
    show xw normal with dissolve
    window show
    xw "时间到了。"
    xw "拉姐现在应该已经发现珈乐失踪，走在枝江大厦的路上了。"
    "向晚手中的定位仪闪烁着绿色的呼吸光点，显示着贝拉的具体位置。"
    "正在向‘拉姐’拨号中"
    show xw unconcerned with dissolve
    with fade

    bl "....别报警，晚晚。我现在就在枝江大厦下面那条街上，别来找我。"

    play sound "<from 0 to 3>audio/se/1电话挂断的嘟嘟声.mp3" fadeout 1.0
    "电话被挂断了..."
    stop sound
    "向晚拿起手机，给贝拉发送了一条语音消息"

    xw "“小心，阿草有问题，他的办公室有秘密电梯，只要下去就是紧急逃生通道了，那里还有一份文件，是情感能量转化装置说明书。”"
    xw "“对不起，约定……没办法……但你一定要从阿草那里拿到书，才能救然然。”"

    "手机弹出提示：信息发送，收信人: 拉姐"

    xw "拉姐，我给你的短信一定要看啊……"
    show xw expect at lc
    xw "就算前方是无尽的黑暗，就算曾经被梦想破碎和病痛折磨。"
    xw "你也能够将痛苦和困难全部跨越。"
    xw "这次对拉姐来说一定没问题的，毕竟你在此之前已经成功过一百次了。"
    show xw normal eyeclosd at lc
    xw "虽然拉姐对我们很严格。"
    xw "在我偷吃泡面被你发现的时候，你的铁棍打的我很痛"
    xw "但拉姐温柔起来的时候"
    show xw smile at lc
    xw "我也不禁依赖着你的肩膀"
    xw "我喜欢拉姐教我跳舞的认真模样"
    xw "在你的耐心指引下，我也渐渐能够开始翩翩起舞"
    xw "从你的舞蹈里，我总能汲取到重新出发的勇气 "
    show xw expect at lc
    xw "拉姐，你是我们的希望"
    xw "拉姐，你这次一定会回来的..."
    xw "我们会等着你..."



    window hide
    scene black
    show 顺时针 zorder 5 at normal_size
    with dissolve
    $ renpy.pause(4, hard=True)
    hide 顺时针

    scene 道路夜
    with dissolve

    play music "audio/bgm/emo.mp3" fadeout 5.0 fadein 4.0
    window show
    "入夜"
    "消音的子弹划破夜色，向着乃琳袭去"
    "【？？】" "快追，别让她跑了，背叛组织的人一个都不能活下来。"
    show nl angery at l2 with dissolve

    nl "就凭你们也想追上我"
    ##hide nl
    "身着黑色晚礼服女子消失在人群密集的街道中"
    "【？？】" "快追，快追！"

    "【奶淇琳】" "我刚刚是不是听到了乃琳的声音"
    "【奶淇琳】" "呜呜，乃琳你带我走吧"
    "粉丝们从街道奔跑而过寻找着乃琳，人群之中顿时一片混乱。"
    "乃琳乘机消失得无影无踪。"
    #【向晚激动】

    show nl surly at l2
    with dissolve
    nl "切，竟然让他们凑巧打中了手臂一枪"
    "【？？】" "乃琳..."
    show nl surly at body_shake
    $renpy.pause(0.5)
    "乃琳一惊，连忙举起手枪"
    show xw calm at r2 with dissolve
    "乃琳看到是向晚，松了口气，放下枪来。"

    show nl care with dissolve
    nl "晚晚你怎么在这里?"

    show xw normal with dissolve
    xw "我带了医药箱，我帮你包扎下吧。"

    nl "不是，你怎么在这儿？"
    show xw unconcerned frown with dissolve
    "向晚皱着眉头"
    xw "这不重要，先处理伤口要紧。"
    show nl thinking with dissolve
    "紫色的双马尾顺着发梢自然垂下，在低端自然地打着卷"
    "向晚小心翼翼地夹出弹头，用酒精仔细清洗起伤口来，然后用纱布包好打了个漂亮的蝴蝶结。"
    "乃琳把玩着向晚马尾的紫色钻头，脑子里浮现出和眼前的危机完全无关的想法。"
    nl "(是作为一只失去自由但不用思考的家猫被圈养，还是做一只自由孤独却可能得到幸福的野猫呢...)"

    show nl sad with dissolve
    nl "（自己已经做不成家猫了。）"
    xw "乃琳，别摸我的双马尾了。"
    "看着生气的向晚，乃琳忽然从心底涌起一股冲动，她什么都不想再管了，她只想从这座残酷的城市中逃出去"
    "至于贝拉和珈乐，她俩肯定能在任何情况下都能生活地游刃有余。"
    "至于嘉然，乃琳没有从组织手上保护好她的能力。"
    "至少，能救晚晚一个人也好..."
    "只有当自己真正与整座城市为敌的时候，才会发现自己的渺小。"
    "一股放弃的欲望从心底里冒出了芽，快速地生长蔓延到无法控制的程度，让乃琳说出了理智时候绝对不会说出的话。"
    nl "晚晚，我们一起逃吧。"

    show xw doubt with dissolve
    "晚晚一怔。"
    xw "逃？逃去哪里。"
    ##乃琳亮
    nl "我们逃出这个城市，逃到一个没有人的地方..."
    "乃琳看着向晚，却没说出下一句。"
    "乃琳也意识到自己所说的话毫无可行之处，她们是A-SOUL的成员，是大家的偶像，偶像是不能活在没有人的地方的。"
    "向晚也陷入了沉默..."
    nl "...."
    xw "乃琳，我们怎样才能从阿草手上逃出来呢？"
    nl "我也没有什么好办法...."
    nl "但阿草需要然然自愿牺牲，所以它绝对不会当着然然的面伤害我们"
    nl "至少在然然的身边，我们暂时是安全的。"
    nl "你放心吧，只要我们五个人团结起来的话，一定能打败阿草的。毕竟，我们可是A-SOUL啊，没有什么奇迹是我们不能创造的。"

    show xw sad with dissolve
    xw "我知道了。"
    xw "我还有别的事情要做，乃琳你没事就好了，关于打败阿草的问题等我们回去再说吧。"
    "乃琳收回了被包扎的手。"

    show nl helpless with dissolve
    nl "可以了，谢谢你晚晚。但我得先去甩开那些追踪我的人再去找你们，不能给你们添麻烦。"
    xw "乃琳你要小心点，遇到危险打电话给我，我会来救你的。"

    show nl smile with dissolve
    nl "（晚晚已经变得可以依赖了呢，如果不是我这么没有用，晚晚就能一直做那个无忧无虑的女孩...）"
    nl "对了晚晚，我想问你一个问题，被拘束的家猫和孤独的野猫，你会养哪一只呢。"

    show xw proud with dissolve
    xw "我..."
    xw "我都喜欢。"
    nl "嗯，看来晚晚是一个很贪心的女孩。"
    xw "我才不是呢。"
    nl "是吗？"
    nl "可晚晚贪心一点也是可以的，我也希望你这么做，毕竟你那么可爱，值得一点小贪心。"
    xw "那乃琳你呢？你喜欢哪一种？"

    show nl thinking with dissolve
    nl"我不知道啊，反正我不会说的。"

    show xw angery with dissolve
    xw "这不是耍赖吗？"
    show nl shock with dissolve

    nl "我也有闹小孩子脾气的时候嘛，我走了..."
    nl "别拉我衣角了，我会回来的。"
    show xw sad with dissolve

    xw "对不起"

    show nl sad with dissolve
    nl "（你不该道歉的，该道歉的是我）"
    nl "（如果可以，谁不想做一只温顺的家猫呢？）"
    nl "再见了，晚晚。"

    hide nl with dissolve
    xw "...."
    show xw gloomy at center with easeinright

    xw "（这一次……这一次…终于把乃琳救出来了）"
    show xw sad at center with dissolve

    xw "（所以，我也能…得到救赎了吗…）"

    window hide
    scene black
    show 顺时针 zorder 5 at normal_size
    with dissolve
    $ renpy.pause(4, hard=True)
    hide 顺时针


    scene 电梯井
    hide screen memory_filter
    with Dissolve(2)

    window show
    "两个人走过了长长的走廊，一路来到了电梯间。走廊里空无一人，但没有人对此感到奇怪。"
    "所有人都已经在另一个地方就位，她们两个是最后缺席的两位。"
    "向晚按下了电梯的上行按钮，在电子提示音响起后，机械装置的噪音隐约响起，电梯的声音从上至下的传了过来。"

# 【清脆的电子提示音】
# 【机械运作声音】
    play sound ["audio/se/清脆的电子提示音.mp3","audio/se/高端机械运作声音-4.mp3"]
# 【嘉然立绘亮】
    show jr normal at l2
# 【向晚立绘亮】
    show xw unconcerned at r2
    with dissolve

    xw "电梯快到了。"
    xw "我们在最底层，恐怕那电梯得花点功夫才能到。"
    xw "确认过了，电梯里没有监控。"

# 嘉然（日常）：
    show jr normal with dissolve
    jr "嗯，看来准备万全啊。"

# 向晚（冷漠）：
    show xw unconcerned with dissolve
    xw "也不至于啦。"
    xw "我没准备后手，只有这一次机会。"

# 嘉然（微笑）：
    show jr smile with dissolve
    jr "不要紧张哦，晚晚，不要紧张。"


    show xw unconcerned with dissolve
    xw "电梯到了。"

    jump .part3

label .part3:
# 3.	夜晚 电梯内（电梯井） 抒情的音乐
    play music "audio/bgm/抒情双吉他.mp3" fadeout 3.0 fadein 4.0
# 【清脆的电子提示音（可以有简单的几个音符的旋律）】
# 【清脆的脚步声】
    play sound ["audio/se/清脆的电子提示音.mp3","audio/se/清脆的脚步声-3.mp3"]
    pause(2.0)
    scene 电梯内部
    show jr normal at l2
# 【向晚立绘亮】
    show xw normal at r2

    with dissolve

    "银色的电梯门打开后，两人缓步走入。电梯有些狭小，但容纳两个人依旧绰绰有余。"
    "不同于普通电梯，这个电梯的外壁是透明的。透过近乎于玻璃一样的材质，可以看到混凝土构成的电梯井。"
    stop sound
    "红色的警示灯规律的在电梯井里闪烁，管道和阀门扭曲出一个又一个的直角，没有任何锈迹，但却落满灰尘。"
    "向晚想象着工人们灰头土脸的挂着安全绳，维护检修着这些也许永远都用不上的管道，他们用各种工具娴熟的敲打着管道，发出震颤的回响。"
    play sound "audio/se/电梯运行.mp3"

    "当电梯门再一次关闭，向晚按下了天台的按钮时，她正倾尽全力的思考着那回响会是一种怎么样的声音。"
    "她不能停止思考，像溺水的人无法停止摆动自己的双手，共同点在于，这种应激反应一样的行为都只是徒劳。"

    "电梯开始缓缓上升，速度不快，好像电梯在上升的过程中能得到某种病态的乐趣一样。"

# 【机械运作声音】
# 【嘉然立绘亮】

# 向晚（冷漠-皱眉）：
    show xw proud with dissolve
    xw "真够慢的。"

# 嘉然（日常）：
    show jr normal  with dissolve
    jr "那我们聊聊天吧，这样就不觉得慢了。"

# 向晚（冷漠）：
    show xw gloomy with dissolve
    xw "然然……我有点害怕。"

# 嘉然（微笑）：
    show jr smile with dissolve
    jr "别怕，晚晚。"
    jr "你还记得我们的首播吗，当时我们每个人都紧张的不行。"
    jr "我还因为过度呼吸差点没晕过去呢。"
    jr "不要紧张，来，跟着我慢慢深呼吸。"
    jr "就像我们练舞时候的那样。"

    show xw smile with dissolve
    xw "谢谢你，然然。"
    xw "我只是……"

    "向晚用左手捂住了自己的胸口，她抬起头，看向那反光的天花板。"
    "电梯的天花板总是大同小异，泛着同样的金属质感的光芒。"

    show jr smile at l2
    show xw normal at r2
    with dissolve

    jr "你可以的，我相信你。"
    jr "我告诉过你吧，向晚，我相信你，甚于相信我自己。"
    jr "就当这是一场彩排，好吗？"


# 旁白：
    "嘉然握住了向晚放在胸口的手，向晚可以感觉到嘉然那温暖的手指缓慢而有力地与自己的手指交缠在了一起。"
    "这让她的双眼刹那间被泪水盈满。"
    show xw cry with dissolve
    "向晚知道，面对残酷的命运，自己并非孤身一人。"

    play sound "audio/se/难分辨的人群噪音-2.mp3" noloop

    scene 电梯透明
    with flash

    "那电梯井似乎已经来到了尽头，随着周围噪音的骤然增大，电梯在一瞬间离开了阴暗逼仄的电梯井。"
    "此时此刻，电梯悬浮在半空之中，从透明的墙壁望去，可以看到聚集在枝江大厦广场上的人群。"
    "穿着各色服装的人们聚在一起，手里举着五颜六色的灯牌，他们的嘴里发出难以分辨的嘶吼。这些咆哮一样的音浪汇聚在一起，如遥远的海潮一样，拍击着透明的电梯外壁。"



    "从高处看，那些人群仿佛黑夜中，由光芒组成的湖泊。这让远处的枝江夜景都显得逊色的几分。"
    show jr laugh with dissolve
    "各式各样的灯光撒入了电梯里，嘉然的脸上化着淡妆，却美的惊心动魄，好像舞台已经就地展开，此时此刻，节目已经开场。"
    "栗发少女举起了她的食指，轻轻地放到嘴边。"

    scene 嘉然逆光 with flash

    jr "嘘。"
    window hide
    pause(5)
    play sound "audio/se/聚光灯打开的声音.mp3"

    window show
    show screen brightness_increase_1 with dissolve
    "刹那间，一束白光亮起，如剑一样，那道高度凝练的灯光迅速的找到了嘉然和向晚坐在的电梯，然后笔直的指了过来。"

# 【聚光灯被打开的声音】
# 旁白：
    "电梯里被照的有如白昼一样明亮，向晚立刻将右手背到身后，左手则用来遮挡那过于炫目的光芒。"


    hide screen brightness_increase_1
    show screen brightness_increase_2
    with dissolve

    scene 电梯透明
    show xw shock
    with Dissolve(2)

    "嘉然没有动，只是静静地感受着这白色的光芒将自己吞噬的过程。"
    "电梯还在不断上升，平台离自己越来越近，向晚感到自己的灵魂都要被这灯光所吸走。"
    "顺着光而来的，还有如同人世间所有声音合在一起所产生的噪音的洪流。那声音绕过一切介质，直接进入了向晚的大脑。"
    "但这一切，却都并非说给她听的。"

# 【画面彻底淡入白光】
    scene white
# 向晚（惊讶）：
    show xw shock
    xw "不！！！" with sshake

# 【画面震动】
# 旁白：
    show xw angery  with dissolve

    "向晚发出了连自己都无法听清的怒吼，但这声音迅速的湮没在了那白光之中。"

    show xw cry with dissolve


    "她眼中的嘉然如暴雨中的一叶扁舟，悄无声息地沉默于那铺天盖地袭来的浪潮之中。"
    "泪水如雨般洒落，向晚再也控制不住自己的情绪。一切来得的太快了，像一瞬间那么快。"
    "甚至来不及说一句正式的告别。"

    xw "然然....然然！"
# 【白光淡出】
    hide screen brightness_increase_2
    scene 电梯透明
    show jr sacred dignified at l2
    show xw cry at r2
    with dissolve

    "向晚轻声地呼唤着嘉然，但白光退去后，站在她面前的已不再是她熟悉的那个人。"
    "金色头发的少女身着颜色圣洁的白袍，而那之前粉白色的小裙子已不知所踪。"
    "向晚知道，有些东西和那身裙子一起，永远的消失了。"


    "向晚看向嘉然，而嘉然则看向自己脚下的人群。"
    "那双清澈的眸子此刻被金色的光所填满，向晚不知道的是，嘉然已不会再看向自己。"

    sjr "开幕吧。"

    window hide
    with Pause(3.0)

    scene white
    with dissolve
    with Pause(3.0)







label .part2:
    play music "audio/bgm/争吵.mp3" fadeout 5.0 fadein 4.0

    scene 枝江天台
    show xw angery at center
    with slow_fade

    window show
    if goNe:
        "612米的高空之上，巨大的黑色情感转化装置矗立在天台的正中央，除此以外这座天台之上空无一物。"
        "唯有寒风吹彻。"
        xw "（第一次在最后的战斗中，大家都在我的身边，已经没什么好害怕的了！）"
        xw "（不知道阿草会不会埋伏我们...)"
        xw "（我们的目标是占领装置，并阻止阿草干扰嘉然完成仪式。）"
        xw " (他们的负面情绪因为我们的停播而不断积累，没有经过引导化解的话，会变得越来越危险，这也让他们做出了一些过激的举动。)"
        xw " (并且这股负面情绪还在被公司放出的消息所放大，如果嘉然不赶快执行仪式的话，他们就要被负面情绪吞噬了。）"
        "天台上，寒风冷的彻骨，站在五人对面的只有一只站立着的白色羊驼。"
        xw "（没有埋伏...）"
    else:
        "612米的高空之上，巨大的黑色情感转化装置矗立在天台的正中央，除此以外这座天台之上空无一物。"
        "唯有寒风吹彻。"
        xw "（又一次来到了这里...）"
        xw "（我们的目标是占领装置，并阻止阿草干扰嘉然完成仪式。）"
        xw " (他们的负面情绪因为我们的停播而不断积累，没有经过引导化解的话，会变得越来越危险，这也让他们做出了一些过激的举动。)"
        xw " (并且这股负面情绪还在被公司放出的消息所放大，如果嘉然不赶快执行仪式的话，他们就要被负面情绪吞噬了。）"

    #【枝江大厦天台，向晚：常】
    scene 夜空诡月 with dissolve
    "傍晚，晴朗无云的天空带着残余的斜阳，低垂的夜幕之下，唯有月色照亮着天台。初春气候仍有些微寒，五人呼出的雾气结成了冰。"

    scene 枝江天台
    show jr sacred dignified at l2
    show bl angery at r1
    with dissolve
    "嘉然躲在贝拉的身后，她将目光望向将会吞噬她的装置，只要她顺利完成仪式，她所爱的大家就能得到救赎。"
    "她也会变成粉丝们理想的嘉然..."

    "【一个魂们】"  "A-SOUL！A-SOUL！A-SOUL！" with sshake

    "一个魂们的声音从楼下传来，从一个人开始喊，渐渐地更多人加入进来，逐渐变成震撼整个城市的声浪。"
    "他们已经一个星期没听到她们的消息了，但今天，从公司的公告传来了消息，她们会来到枝江大厦。"
    "所以他们放下自己的工作，放下家庭，放下所有，从城市的各个角落聚集在枝江大厦的周围。"
    "他们在楼下欢呼狂欢着，等待着一个好消息。A-SOUL毫无缘由的消失已经让他们压抑了太久，但他们的等待是有价值的，今天，她们终于出现了。"
    "他们什么都不想要，只是想看到他们的五个女孩再一次出现在舞台之上......"

    "但他们不知道，五个女孩正在为他们而战。"

    scene 枝江天台
    show xw sad at center
    with dissolve

    if goNe:
        xw "（身体控制不住地颤抖。）"
        xw "（一切都要结束了，无论是我的命运，还是所有人的命运，都会在这场战斗中得到最终的结果。）"
        xw "（这或许对我来说是一场解脱。）"
        "向晚闭上了眼睛，睁开眼睛的时候，她的眼里映照着的只有阿草，要是她不这样做的话，她会忍不住看向嘉然，这会让她分神，分神在这场以命搏命的关键战斗中是绝不可以发生的。"
        "如果可以的话，她恨不得将阿草扒皮拆骨。在曾经的一次次尝试中，面前的白色羊驼已经给她留下了无可匹敌的印象。"
        xw "（这一次我能做的到吗....）"
    else:
        xw "（身体控制不住地颤抖。）"
        xw "在无数的交汇中，有无数种可能，可是在现实中，我只能选最好的一个。"
        xw "这就是我的命运，即使有了存档和读档的权力，也只不过是命运的奴隶。"
        xw "时间有无数系列，背离的、汇合的和平行的时间织成一张不断增长、错综复杂的网。由互相靠拢、分歧、交错，或者永远互不干扰的时间织成的网络包含了所有的可能性。"
        xw "我是世界的错误，是不存在的幽灵，是被命运蛛网缠住的蝴蝶。"
        "向晚闭上了眼睛，睁开眼睛的时候，她的眼里映照着的只有阿草，要是她不这样做的话，她会忍不住看向嘉然，这会让她分神，分神在这场以命搏命的关键战斗中是绝不可以发生的。"
        "如果可以的话，她恨不得将阿草扒皮拆骨。在曾经的一次次尝试中，面前的白色羊驼已经给她留下了无可匹敌的印象。"
        xw "（为了小心谨慎起见，对于已经骗过我的东西，就绝不完全加以信任。）"

    if goNe:
        show screen memory_filter
        scene 阿草办公室 夜
        show ac normal
        with fade
        #【时间动画，逆时针转动】

        "即使炸弹从身边爆炸，烟尘消散之后阿草依然毫发无伤。"
        "就算从角落里偷偷开枪，也会被无形的力量所挡住。"
        "下毒，暗杀，焚烧，溺死......"

        "失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败失败。"
        "靠我自己是无法打败阿草的。"
        #【黑屏，阿草，常】

        "每一次对阿草的袭击，都会以失败而告终。"

        show ac angery with dissolve
        ac "你们无法改变命运。"
        #【时针顺时针动画】
        scene 枝江天台
        show xw sad
        hide screen memory_filter
        with fade


        xw "（又一次走上了命运的审判台，但这一次是我从来没有走到过的变动。）"
        xw "（在这一次轮回，我终于把乃琳救出来了，如果乃琳上次战斗也在的话，上次战斗的结果会大不一样的吧。——"
        xw "（在这个命运的分歧点，倘若我赌赢了，我就能得到彻底的救赎。）"
        xw "（如果即使大家都在，却还是只能迎来失败的结局，那我的轮回就只剩下痛苦。）"
        xw "（希望这是...最后一次...就好了...毕竟这次...大家都在...）"

    else:
        show xw normal at center with dissolve
        xw "（又一次，走上了命运的审判台。）"
        xw "（天台的狂风呼啸......）"
        xw "（这一次，把大家拯救出来吧......）"

    play music "audio/bgm/Silent elegy 可循环(1).mp3" fadeout 5.0 fadein 4.0

    scene 枝江天台
    show ac happy
    with sshake

    ac "你们终于来了呢，我们的A-SOUL。"
    ac "这里很适合表演吧，城市的最中央，在最高点举行一场最盛大的演出。"
    scene 枝江天台
    hide ac

    show bl angery with dissolve
    with dissolve
    bl "可这个舞台上只需要偶像，不需要工具人，你可以退下了。"
    hide bl
    #【高跟鞋声，三下，圣嘉然立绘，冷漠，向晚，哀】
    show jr sacred dignified
    with dissolve

    "嘉然一步步向着装置走去。"
    if goNe:
        show xw sad at l1
        show jr sacred dignified at r1
        with dissolve
        xw "（不要。）"
        xw "（为什么一定要牺牲嘉然呢，是我这次做的还不够好吗。）"
        "向晚伸手拉住了嘉然，嘉然停下了脚步，回过头来，看了向晚一眼。"
        sjr "怎么了向晚。"
        "嘉然虽然看着向晚，但却没有注意向晚，她的眼里全是楼下那些尖叫呐喊着的粉丝们。"
        "向晚像是被扼住了喉咙的大鹅一般，发不出声音，松开了手，此时她做什么都没可能留住嘉然了。"
        xw "（神明啊，如果你真的存在，就让一切在此结束吧。）"
    else:
        hide jr
        show xw sad at l1
        with dissolve
        xw "（昔者庄周梦为胡蝶，栩栩然蝴蝶也。不知周也。俄然觉，则蘧蘧然周也。不知周之梦为胡蝶与？蝴蝶之梦为周与？）"
        xw "（贝拉说过庄周梦蝶的故事，如果这一切只是一场噩梦就好了......）"
        "向晚只是目送嘉然走向装置，她没有阻止她。"
        xw "（...埃弗里特主张，相互作用后这两项分裂为不同的分支，在每一个分支中观测者都只能看到与自己的观测结果一致的世界，而无法看到不同测量结果的世界。）"
        xw "（也就是说，在一次量子相互作用后，宇宙就会分裂为不同的平行宇宙。）"
        xw "（在薛定谔猫实验中，真正的波函数确有活猫与死猫的叠加，只不过看到粒子衰变的观测者只能看到死猫，看到粒子未衰变的观测者只能看到活猫，而不会看到与自己的测量不一致的状态。）"
        xw "（但无论在哪一个平行世界，嘉然都会做出为了大家，牺牲自己的选择。）"
        xw "（你，我，我们的结局早已注定。）"
        xw "（可我们的相遇是命运所系，而非偶然。）"


    scene 枝江天台
    show jr sacred wind
    with dissolve

    "嘉然离装置越来越近，离四人的距离越来越远。"

    sjr "（风好大。）"
    "嘉然独自走向装置，身着白裙的娇小少女好像就要被吹下天台。"
    show jr sacred dignified with dissolve
    "但她走的很稳，很快就到达了装置的中心，装置的黑色光芒像是被她所吸引，随着她的动作围绕着，变化成火焰的形状，从她的指尖，足间燃起，逐渐化成白色星光。"

    scene 献祭1
    with Dissolve(3)
    "恶毒地涌动着的黑色负面情绪靠近了嘉然，可还未等它们碰到嘉然的发梢，就被一种不可见的光环所牢牢地摄住了。"
    "在一阵滋滋的响声后，黑色的情绪能量化作为一缕洁白的光辉。它们如温顺的绵羊般俯卧在嘉然的脚下，跟随着嘉然的心跳而搏动着。"
    "丝绸制成的裙摆在空中飞扬，光在闪耀，而火正热烈地燃烧。黑色的火舌舔过那如蝴蝶般摇曳的裙摆，却只是为华美的长裙增添了一份烫金的颜色。"
    "她轻轻地向前走去，好像要赴一场前所未有的晚宴。在人间这一方连天堂都不曾见过的小小世界里，无数囿于浑浊的人们在这一刻从嘉然的身上瞥见了梦与神话的一角。"
    "她似乎张开了嘴，却没有歌声从中如灵敏的鹿一跃而出，但自有人听到她将唱未唱的歌。"
    "自有人用全身心的感官注意到嘉然那如风中的野柳飞扬的发丝，那如春雷炸响时受惊的鸟一样敏锐的双眸，那如繁花在盛夏开出的第一片花瓣般的嘴唇，和一双在光中缓缓摇曳的手。"
    "黑色的火焰如狂怒的野兽撕咬着她周身的空气，却在一次又一次的尝试中徒劳地化作洁白的光。"
    "罪人们怒吼着自己的罪孽，却又渴望着得到某种解脱。而坚定的行者不在乎这些，她——嘉然——带着浅浅的微笑走着属于自己的路。"
    "于是那些白光绕上她的十指，如流苏般点缀她的裙子。她美得不可方物，连那遭人痛恨厌恶的献祭装置此刻也充盈了有机的情感，在不可抗拒的光芒前自惭形秽。"
    "嘉然走到那装置面前，如将一条流淌自天边的河走到尽头。枝江广场上，那如海般的恨火铺就成一张似帷幕般厚重的地毯。"
    "她打开了装置，深呼吸，然后摆出了舞蹈的起手式。"
    "在最后一缕光消失前，嘉然开始了她的舞蹈。"
    scene 枝江天台
    show jr sacred dignified
    with Dissolve(3)

    sjr "我准备好了。"
    show ac happy at r4 with dissolve
    ac "看来我们的嘉然小姐已经迫不及待开始演出了。"
    "阿草想要走近嘉然，但是被四人拦住了。"
    hide jr
    hide ac
    with dissolve

    show bl angery at r3
    show jl anxiety at r1
    show xw angery at l1
    show nl worried at l3
    with fade


    bl "站住！给我停下来。要是你再往前踏一步，我就不客气了。"
    "贝拉攥紧铁棍的白皙手背上爆出青筋，她把手上包裹长物的布囊流水般展开，露出藏在底下的漆黑细长铁棍，铁棍为自己的自由欢呼着，旋转着发出尖利哨声。"
    "贝拉站在前面，她似乎从未恐惧。"

    show xw calm with dissolve

    if goNe:
        xw "（终于走到这一步了，这一次也把乃琳救出来了，一定，一定没问题的。）"
        "向晚看着贝拉，似乎想要从她那里获得一些对抗未知结局的勇气。"

        xw "拉姐，为什么你一直这么勇敢呢？"
        bl "晚晚，你们就是我勇气的来源。就像以前的排练演出，我们一定能做到的。正如我相信你们，你们也要相信我，我会带大家走向胜利的。"
        "贝拉揉了揉向晚的头，让她的头发有点变得乱糟糟。"
        "贝拉的手心的温度很烫，她的武魂燃烧了起来，她的斗志昂扬向上，像是一把不屈的枪。"
    else:
        "向晚看着贝拉，似乎想要从她那里获得一些对抗未知结局的勇气。"

        xw "拉姐，准备好了吗？"

        show bl soft with dissolve
        bl "晚晚，我会带大家走向胜利的，我保证。"
        "贝拉揉了揉向晚的头，让她的头发有点变得乱糟糟。"
        "贝拉的手心的温度很烫，她的武魂燃烧了起来，她的斗志昂扬向上，像是一把不屈的枪。"

    show nl care with dissolve
    nl "晚晚，要保护好我的身后哦，要是回来了，我们再唱一次鸽子吧，这次可不是同事了哦。"
    "乃琳把她的下巴放在晚晚头上，只是轻轻从背后抱了一下就松了开来，渐渐将自己的身形潜藏在了夜色之中。"

    show jl smile with dissolve
    jl "晚晚，我们可以的。"
    "珈乐拍了拍向晚的肩膀，站在向晚身旁。"

    show bl angery at r3
    show jl anxiety at r1
    show xw angery at l1
    show nl worried at l3
    with dissolve

    play music "audio/bgm/Battle field可循环.mp3" fadeout 5.0 fadein 4.0

    bl "要上了，大家。"

    scene 枝江天台
    with dissolve
    show ac happy
    ac "你们也迫不及待要参与这场盛大演出了吗？那就让我们开始吧。"
    "凝滞着的时间开始再次转动，贝拉铁棍舞动的破风声吹响了战斗的号角。"

    show ac angery

    ac "你们无法改变命运。"
    "羊驼发出的声音很冷，正似高台上的晚风。他的视线望向远方正在起舞的嘉然，即使在场四人的攻击迫在眉睫，阿草也毫不在意，就像是他们只不过是行走时划过的落叶一样。"
    ac "A-SOUL的各位，你们，究竟在为什么而战斗。"
    show ac proud with dissolve

    ac "对于粉丝来说，你们只是随时都能抛弃的商品，他们付出金钱，你们付出表演，这只是一场交易而已，这不是很正常吗。"
    ac "就算没有你们，甚至你们还在，他们也能随时换一个人看。"

    show ac happy with dissolve

    ac "他们付出金钱就是为了看到他们想看到的东西，你要是不满足他们，做出与他们的期待不符的事情，只要你们不合他们的意，他们能随时抛弃你们。"
    ac "他们什么都不会失去。我不懂你们为他们牺牲自己有何意义。"
    show ac at l2
    show bl angery at r2
    with dissolve
    bl "正因为是偶像，所以才要为他们做一些没有意义的事情。"
    #【屏幕晃动，阿草立绘怒】
    show ac angery
    ac "可笑之至。"
    "阿草肥硕的每一块肉与毛都抖动了起来，那并不是战栗或者是害怕，而是一种梦想即将实现的兴奋和颤栗。" with sshake
    play sound "audio/se/2劲风或破空声swing1.mp3"
    show ac:
        easeout 0.2 xoffset -600
    "那只有着肉垫的蹶子尥了尥，身影在原地完全消失，就像是一道飘忽的幻影，如同一只穿梭在草地中的游蛇一般。"
    "他以不符合肥胖身躯的高速，像一条一触即杀的毒蛇穿行着，他光明正大的以自己的速度藏匿在向晚与其他的人视野盲区当中。"
    "贝拉自小以来可谓是身经百战，但尽管如此她依旧没有捕捉到阿草的身影的反应速度，他的速度太快了。"
    #【立绘震动，贝拉，怒】
    bl "珈乐！！！" with sshake
    show bl angery sweat:
        easeout 0.4 xoffset -300
    with Pause(1)
    hide bl with None
    show ac happy at l1:
        xoffset 0
    show jl pain at r1
    with dissolve
    "一声渗人的惨叫声从贝拉的胸腔里面吐了出来，她即使将手中的铁棍狠狠地够了出去以至于让自己失去了重心，也还是没有挡住阿草的袭杀。"
    "阿草的手捏住了珈乐的头，一声无力的呻吟自她的唇瓣而出，就像一只垂死的天鹅。"
    ac "我做的一切都是合法的，所有的行动，都是这座城市发展的必要之恶。"
    ac "为一群现在没有，将来也不会忠于你们的粉丝，背叛培养你们的公司，抛弃你们的未来，牺牲掉你们最重视的嘉然，真是愚蠢。"
    "珈乐望向枝江大厦楼底下的那片层层叠叠的曲折人涛，朝着他们虚弱地招着手，夜风呼啸，这让她似乎置身于某个海风习习的凉夜。"
    "珈乐已然有了那种预感。"
    "她将会纵身一跃，跃入由自己所爱的粉丝所构成的海底，正如她所看过的诗篇一样凄美。"
    #【珈乐常】
    # show jl anxiety at r4 with dissolve
    jl "我们为他们的爱而战。"

    "珈乐看向那些只知岁月安好的一个魂儿，傻傻地笑了起来。"

    scene 枝江天台

    show jr sacred dignified
    with dissolve

    show jr:
        easeout 0.3 offset (30,20)
    "嘉然的舞步踉跄了一瞬，那闪耀着的白色光芒的亮度黯淡了一瞬，就像是某种理想的流体受到了外部干扰停滞了一瞬一般，而那高台之下人海所构成的浪潮也因此紧缩了一瞬。"
    "控制时间行走的时针的齿轮仿佛被某种东西卡住了一般，顿在了那一刻。"



    "阿草撇见了那一幕，而向晚也看见了嘉然舞步的停滞。"

    scene 枝江天台

    show ac normal at l1
    show jl pain at r1
    with dissolve
    ac "你们很幸运，因为嘉然的怜悯。"
    ac "把感情看得越重的人，失去这份感情的时候也就越脆弱，这样的人也越容易被人利用。"
    ac "感情是很容易迁移的东西，他们有一天会讨厌你们，会喜欢上别的人，会把你们全部忘却，这样做的原因可能只是一时的疲惫，一个小误会，或者仅仅是，不喜欢了。"
    ac "但你们不一样，这是你们的工作和使命，你们被束缚在偶像的神坛上，没办法逃离。把他们的爱看得太重，当失去他们的时候，你们的痛苦由谁开解呢。"
    "他摇了摇头，没有将珈乐扔出高台之上。"
    "嘉然的祭祀之舞继续。"

    show jl:
        easein 0.3 yoffset 600
    with Pause(.3)
    with sshake
    hide jl
    "他猛地抓住了珈乐的头发，身后浮现了某种神秘的力量，将她往枝江大厦的地面上猛力一砸。"
    show ac angery with dissolve
    ac "就算是善意的欺骗也比坦诚虚伪无数倍。与其将来抛弃他们说爱过，不如从一开始就说清楚，从没爱过更让他们好受。虚伪者，当受到审判。"
    "地板碎裂开了细小的裂缝，可见珈乐究竟承受了何等的重压。"
    #【珈乐，痛苦】
    jl "贝拉…不要失去…理智，他能用…看不见的…力量…进行进攻，离他…远点，离他远点…，你会是…我们的…希望，你会成为…我们的英雄。"


    "阿草用力一挥，将珈乐甩到了天台边缘。" with sshake

    if not goNe:
        xw "（对不起...还不是时候...）"

    #【阿草喜悦】
    show ac happy with dissolve
    ac "珈乐已经被打倒了，乃琳不知道躲在了哪里，不过这没什么关系，剩下的向晚大小姐不会战斗，接下来就是你了，贝拉，A-SOUL的队长。”"
    #【贝拉怒】
    show bl angery at r3 with easeinright
    bl "混蛋。"
    "她攥紧了拳头，眼神里燃烧着火焰，向阿草的方向走出一步，地上开始出现裂纹。"
    ac "呵，贝拉，我说了这么多，你没想着离开，却是主动送上门来找死吗？珈乐用最后一口气，像是周一早上要收作业还在补的学生一样挣扎着，告诉你我的能力，你却还敢向我走近吗？"
    bl "要是不走近点，怎么把你揍趴下呢。"
    "贝拉挥出一拳，阿草以不可视之手迎上挡住"

    "在他用情绪能量实体化碰触到拳头那一刻，就意识到自己犯了一个致命的错误。"
    play sound "audio/se/击打.mp3"
    with Pause(0.25)
    show ac normal:
        easeout 0.3 xcenter 200
    "那一拳重逾千斤，发出破空的声音，就像是行驶中的高速火车，完全不是能够阻挡的东西，他整个肥胖的身躯被击飞了出去，弹到了墙壁上。" with sshake

    "阿草的嘴角流出了一丝鲜血，它从身躯下拿出一块钢板，扔到地上，那上面刻着一个拳印，钢板已经被打变形了，吸收了大部分的冲击力。"
    #【阿草痛苦】
    ac "咳…幸好我调查过你，做了一些准备，贝拉武圣果然名不虚传。"

    show ac angery with dissolve
    ac "如此强大的贝拉，却局限于一个偶像身份当中，岂不是大材小用。何况，他们喜欢的是你们还是我们呢？"
    show ac normal with dissolve
    "阿草的声音很低沉，也很冷漠，就像是西伯利亚从未融化的坚冰。"
    ac "你们固然有着强烈的个人魅力，这也是我们把你们找来参加A-SOUL的目的。但你们现在的成绩是靠我们的资源捧起来的。"
    ac "如果没有我们，你们只能在地上仰望星空。"
    show ac happy with dissolve

    ac "就算是现在，你们也不是什么不能替代的偶像。"
    ac "我们会开启新的计划，时间会孕育出一个新的时代，这是一个不断的社会规则循环。你们的反抗就像阻止那轮夕阳落下一样，毫无作用。我会留下你们的性命，让你们看着自黑夜而生的东西。"
    #【阿草恐怖】
    show ac angery with dissolve
    "阿草的背后似乎浮现出了某种不知名的轮廓，如同深山古寺中鎏金已落仅留黑痕的千手观音塑像。"
    "嘉然转化的情绪能量，源源不断地通过无线装置向着阿草传输过去，让他能够做出非人之事，一只无法从光学角度上看见的大手自他的背后浮现而出。"
    "那些手往向晚的方向延伸过去，向晚只能感受到风在动，气在动，但她看不见。"
    "一只一人高的巨手自地面凸伸出来，那无形的巨手居然有了形体，支撑起了一大片构成地板的水泥块。"
    #【阿草怒】
    ac "和这个舞台一起永远合而为一吧。"
    scene 枝江天台
    show xw despair at l3
    show ac normal at r2
    with dissolve


    "一只自地面升起的索命之手，要将向晚拉入地面当中直接活埋在此。"
    if goNe:
        "阿草太了解A-SOUL了，太了解A-SOUL的每一个人了。他曾是她的朋友，他曾是A-SOUL那人畜无害的吉祥物，但此时自己却要与他拔刀相向，短兵相接。"
        xw "但现在的我可并不还是那个唱歌跳舞，做着偶像梦的天真女孩啊"
    else:
        xw "（这次我能做到的...）"

    show xw angery with dissolve
    xw "A-SOUL可是能随着时间，创造奇迹的组合，放弃你那落后于时代的眼光吧。"
    #【金属撞击的铿声屏幕摇晃】
    play sound "audio/se/践踏.mp3"

    "向晚拾起贝拉扔下的铁棍，挡住了阿草的大手。" with sshake
    #【狙击枪声三响】

    play sound "audio/se/枪声三连.mp3"

    "向晚听到了数声巨大的枪响自她的背后而来，向着已经发动攻击的阿草袭去，那是乃琳隐藏在暗处的狙击。"
    "砰，砰，砰，三连发子弹已经锁定了阿草的头颅，弹壳下落砸到地面上，发出清脆的响声。"
    "子弹在空气中超过音速，破开音障，可以预见阿草的头颅将变成一只破西瓜，可惜，又一只大手从地底下升了起来。" with sshake
    "子弹在空中诡异地偏移，最终不知所踪。"
    show ac proud at r2

    ac "虽然只是一群小女孩无用的挣扎，但也不能小瞧你们，幸好我还留了一手，你们还有什么招式尽管使出来吧。"

    show xw calm with dissolve
    if goNe:
        xw "看啊...看啊，我可以的，我能做到，我拖住他了。"
        "向晚沉浸在用铁棍拖住阿草一只大手的愉悦中，她望着阿草的脸色，体会着他的心情，那究竟是什么感觉呢？像是喝了一口威士忌却发现没有加冰的滋味？"
    play sound "audio/se/2劲风或破空声swing1.mp3"

    "一道猛烈劲风划过，如同高速公路上时速200公里的大客车一般的冲击力的隐形拳头转瞬之间就到了向晚眼前，那是阿草控制的另外一只大手。"

    play music "audio/bgm/第二章 悲伤回忆.mp3" fadeout 5.0 fadein 4.0

    hide ac with None
    show bl anxiety at l2
    show xw despair at r3
    with fade
    bl "晚晚！！"

    if goNe:
        xw "（太快了...）"
        xw "（已经...躲不开了。）"
    else:
        xw "（没关系，不痛的...）"

    #【屏幕颤抖，晚晚痛苦】
    play sound "audio/se/践踏.mp3"
    with Pause(.1)

    show xw despair zorder 50:
        easeout 0.2 xoffset -480
    with Pause(.2)
    with sshake

    xw "痛——"
    "向晚感觉到自己的双马尾像是被强行往后扯一样，她整个人强行被往后拉退了数步，落到了贝拉的怀中。"
    "拳头转了一圈向着贝拉袭来。"
    hide xw
    show bl at dark_in

    "贝拉抓住向晚的肩膀，将其向一旁推开。"

    play sound "audio/se/践踏.mp3"
    with Pause(.1)

    show bl daze:
        easeout 0.2 xoffset -200
    with Pause(.2)
    with sshake
    show bl daze:
        easeout_quart 1 yoffset 55
    with Pause(1)
    show bl daze:
        ease 1 yoffset 90
    with Pause(1)

    "贝拉像一只破布人偶一样被无形的拳头打飞了出去，在地上滚了好几圈，撞到天台的墙壁边缘停了下来，身体不住地颤抖。"

    if goNe:
        xw "（还得再等等...）"


    "要是一般人，早像被高速行驶的客车撞到似的躺在地上动弹不得了。"
    #【向晚急】
    show xw worried at lc with dissolve
    xw "拉姐，拉姐！！"
    "向晚磕磕绊绊地跑了过去。"
    #【贝拉痛苦】
    show bl daze with dissolve
    bl "咳咳…晚晚"
    bl "被...你看到我...这么失败的样子....真是太丢脸了"
    bl "我一直在追逐..咳..武术和舞蹈的梦想，但是寺庙被推平了，舞蹈也不成样子"
    bl "我...咳咳...这一生，好像从来没有实现过自己的梦想。"
    "贝拉把落在身旁不远的铁棍递给晚晚。"
    bl "但是我希望你...我知道你能做到...拿着这根铁棍...你能实现我的梦想...你能...咳咳...比我走得更远，这样的话，我也算...能实现自己的梦想了吧..."
    #【向晚哀】
    show xw cry with dissolve

    if goNe:
        xw "为什么要救我呢，明明我这么弱，把一切都交给我，要是我做不到怎么办才好啊。"
    else:
        xw "拉姐...对不起..."


    "眼泪掉在了贝拉的手上。"
    "贝拉伸出手擦掉了晚晚的眼泪。"
    bl "我可是A-SOUL队长贝拉啊，保护队员是我的责任。"
    bl "因为我相信晚晚啊…，咳咳…，我相信晚晚能够做到，就像相信自己一样。"

    xw "可恶啊！你给我过来"
    show xw:
        easein .3 xoffset 300
    "向晚哭着拿着铁棍，把剩下的那只无形之手从贝拉所在的地方引开。"

    scene 枝江天台
    show bl daze
    with fade

    bl "珈乐…要是我们能再跳一支TroubleMaker就好了…"
    "贝拉离躺着的珈乐还有些距离，贝拉挣扎着，磨蹭着，缓缓向着昏迷的珈乐接近。"
    scene 练舞室
    #【回忆特效】
    show screen memory_filter
    show jl normal at l2
    show bl normal at r2

    with fade
    #珈乐【常】
    jl "如果我不在的话，真不知道你会惹出什么麻烦"
    #贝拉【常】：
    bl "那就，把你的红色发带借给我吧"
    #珈乐【疑惑】：
    show jl doubt with dissolve
    jl "这个？"
    window hide
    scene black
    hide screen memory_filter
    with dissolve

    show screen saying("嗯，如果有这个就相当于珈乐在我身边了",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
    #【天台贝拉：挣扎】
    scene 枝江天台
    show bl daze
    with fade
    "贝拉向着珈乐伸出手。"

    scene 练舞室
    show jl happy at l2
    show bl normal at r2
    show screen memory_filter
    with fade
    jl "那条红色缎带，一定要还给我哦"
    bl "我知道的，珈乐"
    scene black
    hide screen memory_filter
    with dissolve
    window hide
    show screen saying("你就放心吧",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)


    show 贝贝珈 zorder 5 at normal_size
    $ renpy.pause(6, hard=True)

    hide 贝贝珈

    scene 牵手 with Dissolve(3)
    "贝拉终于来到了珈乐的身旁，拉住了昏迷的珈乐的手。"
    window hide
    $ renpy.pause(5.0)

    scene 枝江天台
    show ac happy at l4
    show xw cry  at r3
    with Dissolve(4)
    window show

    "阿草的眉毛高挑起来，虽然他的脸上基本上都是毛，这让人看不清楚他的表情波动。"
    ac "哦？看来好像是打错人了。"
    ac "不过这样子更好，最大的威胁消失了。"


    show ac proud with dissolve
    ac "战斗中在意队友是一种非常低效且无用的行为，像贝拉这么强的武圣因为这个原因有了弱点真是一个天大的笑话。"
    ac "就像我们利用粉丝一样，我们从来没有把注意力放在他们身上。反正他们随时都会离开，也随时会有新的粉丝补充进来。"

    play music "audio/bgm/第三章重点曲3阶段悲壮战斗.mp3" fadeout 5.0 fadein 4.0

    "【??】" "是吗？愚蠢的是你。"
    "随着话音落下，一道影梭扫了过去。"

    play sound "audio/se/2劲风或破空声swing1.mp3"
    show nl angery at rc with easeinright
    show xw expect with dissolve
    "乃琳的手中反握着一把短刀，呜呜的破风声只在耳边响起了一瞬，向晚便再也看不到乃琳的影子了。"
    "以前的乃琳，跳舞动作比机器人还僵硬，挥舞着匕首的她，灵巧得像只成了精的猫咪。"
    play sound "audio/se/2劲风或破空声swing1.mp3"
    "乃琳一刀反握劈杀过去，刺目的冷光直接对准了阿草的喉咙，阿草收回袭击贝拉的无形之手，和乃琳战至一起。" with sshake
    "向晚提着铁棍边抵挡着隐形大手边后退，很快就逃到了乃琳旁边。"

    show ac at l4
    show xw unconcerned frown at r3
    show nl angery at rc
    with dissolve

    xw "乃琳，这下怎么办啊，就剩我们两个了。"
    #乃琳【无奈】
    show nl helpless with dissolve
    nl "我也不知道啊，小可爱。"
    #乃琳【喜】
    show nl happy with dissolve
    nl "我有几颗手榴弹，要不我们把那台装置给炸掉吧。"
    "那台机械的每一个机械零件传递着某种并非是机械感而更像是是生命感的律动，烤漆蓝的游丝与钻石制成的避震器与束缚着钻石的套筒接连地跳动着"
    "这是个堪称完美的装置艺术，足以让所有的腕表收藏家都痴狂的多重球型陀飞轮与三问系统在这个巨大的装置上和谐地达成了一种平衡，发泡的液态装置形成了一个圈，没有人能想象这样的机械装置居然存在。"

    show nl angery with dissolve
    nl "那台机器应该是阿草的力量来源，只要我们把这个装置毁了，阿草就是个普通羊驼。"

    ac "确实，破坏这台机械后你们就可以断绝我的超凡力量了，但是你不顾及一下嘉然的和粉丝的性命吗。"
    ac "如果破坏这仪式，不仅是嘉然会被负面情绪反噬，仪式也无法完成，粉丝们也会陷入疯狂。"
    "乃琳掏出了几颗手榴弹。"

    show nl angery with dissolve
    show ac panic with dissolve
    nl "你在教我做事啊。"

    xw "乃琳！！！"
    xw "不行，不能破坏这仪式。"
    #乃琳【喜】
    show nl happy with dissolve
    nl "晚晚，你个小笨蛋，谁管你啊，我接到的任务就是干掉然然啊，现在能阻碍我的贝拉和珈乐都不在了，这不是一个大好机会吗。"
    #阿草【慌】
    show nl angery
    show ac happy
    with dissolve

    ac "向晚，现在你明白了吧，你的铁棍，该对的不是我，而是乃琳吧。"
    "向晚把铁棍指向了乃琳。"
    "阿草对乃琳鼓了鼓掌，肥硕的肉垫响了几声。"
    ac "你们之间的信任就是这么脆弱的东西，只要一点小小的波澜和引动就会破碎。"
    ac "只要利益不同，从最亲密的人变成恨彻心扉的仇敌，也只需要几分钟。"
    ac "看看你们楼下的粉丝吧，他们已经因为我们放出可能解散的信息，发散得更加疯狂。"
    ac "他们对你们的信任相当的脆弱，现实中就算同一个宿舍的室友也会背叛，你怎么就能相信楼下这些甚至连面都没见过，和你们距离这么遥远的人呢？"
    #乃琳【怒】
    show nl angery with dissolve
    nl "真是聒噪！"
    "乃琳拉开了手榴弹扣环，向着装置扔了过去。"
    #向晚【哀】
    show xw angery with dissolve
    xw "乃琳，不要！！"
    "向晚举着铁棍，向乃琳狂奔过去， 她已经没办法阻止手榴弹的爆炸了。"
    "铁棍向着没有防备的乃琳挥了下去。"

    #【金属声】
    play sound "audio/se/践踏.mp3"
    with Pause(.1)
    "这棍棒仿若有了它自己的意志，借力给向晚。"
    "她用铁棍挡住了乃琳背后进攻的大手。" with sshake
    nl "晚晚，做的好。"
    show xw calm with dissolve
    xw "骗过敌人前，先要骗过队友。"
    xw "还有，一定要相信自己的队友。"
    if goNe:
        xw "（以前乃琳教过我这个道理。）"
    else:
        xw "（毕竟不是第一次了嘛。）"
    #阿草【惊慌】
    show ac panic with dissolve
    ac "什么！！"

    play sound "audio/se/沉默爆炸2.mp3"

    "阿草一只魔力之手此时正袭击乃琳的背后，被向晚阻止住了，另一只手挡住了手榴弹对于装置的伤害，已经没有余力去挡住乃琳的子弹了。"
    ac "幸好我还留有..."


    #【回忆特效】
    scene 枝江天台
    show jl smile at center
    show screen memory_filter
    #【天台，回忆特效】
    #珈乐【喜】
    jl "贝拉...我在阿草的身上留了香水，贝拉你闻到香味就可以出拳了！"
    scene 枝江天台
    show ac panic at l4
    show jl angery at r4
    show xw calm at l1
    show bl angery at r2
    hide screen memory_filter
    with fade
    #珈乐【怒】/贝拉【怒】
    "【珈乐/贝拉】" "你还有什么！？"

    "贝拉快速地靠近向晚，从她手里接过了铁棍，闭上了眼睛，那是她最熟悉的香味，淡淡的，七里香。"
    show xw at r2
    show bl at lc
    with move
    play sound "audio/se/践踏.mp3"
    with Pause(.1)

    "铁棍一挥，就击飞了挡在向晚身前的大手。" with sshake
    #贝拉【怒】
    show bl angery with dissolve
    bl "铁棍岂是如此不便之物，伸长！"

    "铁棍瞬间变长，贝拉化棍为枪，向上挑起阿草胸前即将成型的能量。"



    bl "乃琳！"
    scene 枝江天台
    show nl angery at l2
    show ac panic at r2
    with dissolve
    "乃琳反手将子弹上膛，瞄准了阿草，微眯瞳孔。"

    play sound "audio/se/枪声三连.mp3"

    "抵近射击，连开三枪。" with sshake
    "乃琳的三发子弹贯穿了阿草的头颅。"

    show ac :
        easein 2 yoffset 500
    with Pause(2)
    play sound "audio/se/down.mp3"

    "阿草的身躯倒了下去，和贝拉对峙的那只手也失去了踪迹。"

    scene 枝江天台
    if goNe:
        show xw smile zorder 41 at l2
    else:
        show xw unconcerned frown zorder 41 at l2
    show nl care zorder 40
    show bl smile at r2

    show jl smile at r4
    with Dissolve(3)

    if goNe:
        xw "终于，结束了吗？"
        "向晚浑身脱力，她已经不想动了，她感觉自己能就此睡个一天一夜。"

    else:
        xw "（还没有结束...）"

    "贝拉和珈乐也瘫在地上，乃琳正在处理她们的伤势。"


    "突然，出乎意料的刚刚已经完全消失的拳风袭来，向晚一时间没有防备，被结结实实地打在了身上。"
    play sound "audio/se/践踏.mp3"

    show xw despair:
        easein .2 yoffset 100
    show bl angery
    show jl angery

    with sshake
    "空气震动，像大河崩塌，像暴风袭来，身体像是被一辆大卡车辗轧而过。"
    "向晚觉得自己浑身的骨头都被碾得碎裂了开来，似乎身体的每一个孔都在往外冒血。"

    "【乃琳、珈乐、贝拉】" "晚晚！！"
    show ac happy zorder 50 at l4
    with easeinbottom
    ac "真是太危险了啊。"
    ac "控制感情是会遭到反噬的，过热的感情能够灼烧人心，冰冷的感情也会分隔众人。"
    ac "幸好有嘉然去控制让这股情绪平和下来，连接上这股类似神明的力量，连濒死回复也能做到吗？"
    ac "哈哈哈哈哈！"

    show screen black_filter1 with dissolve

    xw "（耳鸣声涌上了我的大脑，这就是贝拉当时被击中的感觉吗，自己的身体疼痛的无法自制，四肢的骨头也已经粉碎。）"

    show xw despair:
        easein 2 yoffset 300
    with None
    hide screen black_filter1
    show screen black_filter2
    with dissolve

    "向晚朦胧地看到乃琳向着她冲过来，然后被阿草用无形之手从背后提起勒晕，像一块破布一样被扔到一边。"
    "珈乐被重拳横扫晕了过去，只剩下贝拉孤军奋战。"
    "她没有看到那一切接下来所发生的一切。"
    window hide
    scene black with Dissolve(3)
    hide screen black_filter2
    if  not goNe:
        xw "（但...时机快到了。）"
        jump cp9_g_end
    window show

    jump .cp8_n_end


label .cp8_n_end:
    #########
    jump ne
