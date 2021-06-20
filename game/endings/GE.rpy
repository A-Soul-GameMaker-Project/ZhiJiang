label geGoTe:
    $ goTe = True
    jump ge.content


label ge:
    $ goTe = False

label .content:
    scene black
    play music "audio/bgm/纷乱 第三章.mp3" fadeout 4 fadein 4

    show screen saying("你又要看着她们再一次牺牲吗",0.5,0.4,30) with Dissolve(3)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(2)

    scene 枝江天台1 
    show xw despair
    with fade
    "向晚苏醒了过来..."
    "乃琳，贝拉，珈乐在天台的角落里不省人事。"

    xw "（这次，又失败了吗。）"
    "眼前变得模糊起来，手心连紧握起来那轻飘飘的短匕的力气都没有。"

    scene 墓园
    show jr smile 
    show screen memory_filter
    with slow_fade

    jr "晚晚，我希望你能在仪式上杀了我。"
    jr "今晚，你能否送我去野花丛中入眠？"
    jr "无论结果如何，我都不会怪你。"
    jr "我接受每一种结局，每一种你选择的结局。"

    scene 枝江天台1 
    show xw cry
    hide screen memory_filter
    with slow_fade


    xw "呵呵..."
    xw "呵呵呵呵...额咳咳咳" with sshake
    "向晚的眼泪在她的脸庞上肆意流淌着，滚动裹挟着白皙脸庞沾染的灰尘，变成浑浊的泪滴落到天台。"
    "她嘶声力竭地哭泣，像是要把自己的心肝脾肺一起咳出来。"

    scene 水族馆
    show jr smile 
    show screen memory_filter
    with slow_fade

    jr "晚晚，你要做你自己。"
    xw "然然...你把选择权都交给了我，那我会怎么选你肯定知道的吧..."
    xw "我们早该生死相依，我们早该以命相搏。"

    scene 枝江天台1 
    show xw calm
    hide screen memory_filter
    with slow_fade

    "为这一刻，为这打破命运的一刻，她已经把这把匕首握了太久，那些紫色的光晕完全遮盖住了原有的黑色材质，而闪光的纹路已经彻底布满了整个匕身。"
    "帷幕之末来源于一个古老繁荣的王国，国王日渐沉迷于虚幻的神明中，疏于朝政。"
    "终有一日，国王所迷信的神明化为真实，可神明，为这个国家带来的却是遍地荒芜。"
    "国王耗费举国之力，只为打造一把可以打破幻想，刺杀神明的武器。"
    "一位美丽而纯洁的女孩，被推选为刺客，她被打扮成最符合童话的仙女模样，却在进行刺杀时功亏一篑。"
    "以生命作为契约代价，被不属于此世的武器所反噬后，少女香消玉殒，这把武器也不知所踪，故事也落下了帷幕。"
    "随着向晚身上的血液流到匕首之上，匕首的纹路也越来越明亮，像附倚的蛇般爬上向晚的手，匕首从柄部泛起涟漪直至匕端。"
    "就像是曾经一个魂们挥舞的应援棒一样，指引照明着向晚的前路，亦支撑着向晚此刻虚弱无力的身体。"

    play music "audio/bgm/第四章反转.mp3" fadeout 4 fadein 4

    show xw angery with dissolve
    xw "命运吗？注定吗？如果命运注定这是如此悲伤的结局，那就由我来打破！"

    ##红光一闪
    with Fade(.25, 0.1, 0.1, color="#AA0000")
    "正当阿草打算将她的朋友们无情地再一次提起的时候，向晚轻轻地在自己的手指上划了一刀。"
    "艳红色的血珠滴落在那匕首之上，蒸发成了一道勃发着生机的血雾。"
    show xw normal with dissolve
    xw "等着我，我一定会把你们拯救出来的。"

    play sound "audio/se/血流声.mp3"

    "向晚的浑身又漫溢出了光与热，勇气，坚持...那些失去过的曾经给予她力量的东西重新涌入了她的血管。"

    scene 刺杀阿草 with dissolve
    "阿草听到了那心跳声。他转过了身去，看到了一道紫色光芒正朝着自己冲锋。"
    "向晚压低身子，胸膛近乎贴地滑掠过去，临近阿草时，她几步踏出，猛一下跃入空中，身躯伴着猎猎劲风直接冲到了阿草的面前。"
    "匕首划出一道优美的弧线，那就像是轻盈的舞蝶展翅所展现出的绚烂光芒。"
    "这刀声如蛇摩挲，割风作响。霍霍之声，如同雨点繁密。"
    stop sound
    ac "糟了…"
    

    "阿草赶紧催动身后那些有着超乎常人巨力的无形之手进行阻挡，却发现那道紫光像是刀切豆腐一样，轻易将它所放出的无形之手一劈而断！" with sshake
    "它发现自己和情绪能量失去了联系，它清楚地认识到要是被这把刀刺中，就会死。" 


    "这无以伦比的一刀，搏死的一刀，无畏的一刀，完全没法阻挡，它的肉体和无形之手都不能阻止这把匕首进入他的身体，那一刀直接捅入他的要害。"
    
    scene 枝江天台1
    show ac afraid
    with Fade(.25, 0.1, 0.1, color="#AA0000")

    "直到匕首进去的那一刻，向晚才发现阿草也只不过是和普通人一样，它一样有肉体，它的肉体一样脆弱。"
    show ac:
        ease 1 yoffset 200
    with Pause(1)


    "鲜血从阿草的伤口中喷了出来，阿草倒在了地上。"
    "阿草面临自己的死亡之时，第一次露出了人性化的表情——脆弱。"

    ac "自从当工具人以来，还是第一次有这种解脱的感觉..."

    scene 人群晚
    with dissolve

    "他看着楼下等待着的一个魂们，他们等待着自己的偶像归来，他们有着自己的希望，有自己崇拜的偶像，有五个美好的女孩陪着他们。"
    "是什么时候开始，他忘记了自己呢。"
    "大概是第一次被逼着把自己最喜欢的偶像推进深渊的时候吧..."
    ###枝江天台 回忆滤镜 嘉然黑色剪影

    scene 枝江天台1
    show screen memory_filter
    with fade

    "它还依稀记得她的模样，当它亲手将她推入黑色的火海当中的时候，她并没有埋怨诅咒它。"
    "她只是对着它笑笑，留下最后一句话。"
    "【偶像】" "对不起，不能再陪你了。"

    hide screen memory_filter
    with fade
    "阿草看着旁边的五个女孩..."
    "阿草想起它曾经也是一名粉丝，直到他成为了一名合格的工具人。"
    ac "下辈子有机会的话，我也…想成为一个魂啊，他们，好幸福啊。"

    "从阿草身上散发出来的黑色能量消失了。"

    hide ac with None
    show nl happy at l3
    show jl smile
    show bl care at r3
    with dissolve
    "珈乐撑起身子，寒风吹动她的紫发，她艰难地回头看向楼下的大家。"

    show jl pain with dissolve

    jl "咳咳咳..." 
    bl "别往下看了，你现在的形象要是给皇珈骑士看到他们会担心的。"
    nl "珈乐，我先帮你包下伤口吧。"
    jl "我倒是不用...你先帮贝拉，不对...还是先帮晚晚吧。"

    play music "audio/bgm/缓和弦乐.mp3" fadeout 4 fadein 4

    scene 英雄CG
    with Dissolve(3)
    "【贝拉/珈乐/乃琳】" "晚晚，晚晚？！你要干什么！！！"

    "听到珈乐的呼声，向晚回身看向三人，她提着帷幕之末，狂风吹起了她的长发。"
    "在装置的背光中，少女的眼中晶莹剔透，闪着银光，她侧过身，看向远方。"
   
    xw "我要，把她救回来。"
    "她的背后就是嘉然，嘉然已然被黑色的火焰包围，变成了一个巨大的黑色之茧，里面正在孕育着粉丝们理想的嘉然，向晚举起刀刃，匕首散发着幽幽的紫光。"
    "向晚的手落下，外层的黑色火焰被这一刀一分为二，像是在欢迎着英雄的到来。"
    "她背对着三人，走进了黑色火焰当中，像是被这一刀激怒一般，黑色的火焰升腾起来，很快就闭合起来，将向晚包含其中，吞噬殆尽。"
    
    scene 枝江天台1
    show xw despair at l2 

    show dirty_filter behind jr, xw
    show 火星 zorder 50:
        alpha 0.65
    with Dissolve(3)


    xw "不要...."

    show jr sacred dignified at r2 with dissolve
    sjr "向晚，你终于来了，我知道你能做到的，你肯定能让我们的共愿就此实现。"


    show xw angery at l2 
    xw "我的愿望就是把你救出来。"
    "向晚挥动着帷幕之末，用尽她的余力砍了过去。"
    "612次的轮回，才让向晚有机会挥下这一刀。"
    play sound "audio/se/践踏.mp3"
    "这把刀重重地劈在了围绕着黑色火焰的装置上"
    with sshake
    show xw sad  with dissolve
    sjr "向晚，不要！"
    sjr "你为什么不杀了我？"
    "那是黑火最为密集之所在，即使匕首将装置切开一道划痕，密集的火焰也很快将缝隙填满。"
    "这里的魔力浓度与阿草所控制的无形之手完全不是一个等级，原是专注于破魔的匕首也承受不住如此高的魔力纯度，被腐蚀出道道缺口。"
    "黑色火焰因为向晚的举动被激怒了，她企图毁了他们的神明，火焰变得更加疯狂，开始袭击入侵的向晚。"
    "向晚躲闪着，在黑色的火焰里躲闪着，穿梭着。"
    "她的紫色钻头摇摆着，随风飘舞，像是一只翩翩起舞的紫色蝴蝶。"
    show xw angery with dissolve
    play sound "audio/se/践踏.mp3"
    "向晚又一刀劈在了装置之上，黑色火焰化为巨盾实体，与帷幕之末相对峙。" with sshake
    play sound "audio/se/践踏.mp3"
    "一刀，又一刀，向晚将帷幕之末用力向装置砍去，重重火焰一次次被劈开又再次聚集，帷幕之末的破魔能力，在如此庞大的众愿魔力之下像是蜉蝣撼大树，支持不住的帷幕之末在最后一刀破碎四散，无数黑色碎片飞舞在空中。"
    "向晚的所有努力，只是在装置上留下了浅浅的刮痕。"
    show xw cry with dissolve
    xw "因为我不想你离开啊，然然！"
    "向晚无力地坐在了地上。"    #向晚【哭泣】


    xw "我好不容易才把珈乐，贝拉，乃琳救下来了，也把阿草打败了，你们却要把嘉然从我的身边夺走。"
    xw "不要…不要…"
    xw "把我的…嘉然…还回来啊…"
    window hide
    scene black 
    with dissolve


    show 嘉晚饭 zorder 5 at normal_size  
    $ renpy.pause(6, hard=True)

    hide 嘉晚饭

    show screen saying("不要放弃，伸出手...去拯救她！",0.5,0.4,30) with Dissolve(2)
    $ renpy.pause(2.0)
    hide screen saying with Dissolve(1)
   
    scene 枝江天台1 
    show xw angery 
    show dirty_filter behind jr, xw
    show 火星 zorder 50:
        alpha 0.65
    with fade
    window show

    "向晚站起身来，一步步越过重重的黑色火焰，即使它们撞击在自己的身上，在自己的身上焚烧着。" with sshake
    xw "然然，我这就来救你..."
    xw "你的愿望和痛苦，我们一起分担...."
    "向晚拥抱着黑色火焰的茧，对着火焰伸出手去，像是抚摸孩童一样温柔。"
    "一旦用手触碰魔力火焰，一股强烈的负面情绪和恶意就从漆黑的火焰传来。"
    "向晚被负面情绪撕扯起来，黑色火焰也在她的身上灼烧着，巨大的痛苦让向晚几乎失去理智。" with sshake
    "粉丝们的记忆和想法也借此传达到了向晚的心中。"
    scene 人群晚
    show screen memory_filter
    with Dissolve(3)
    "【众人】" "挤在工厂的宿舍里，或者在城中村的单间中。"
    "【众人】" "有时会遇到加班到凌晨的情况，早上推迟两小时上班。"
    "【众人】" "对于我们这些在厂房流水线上的工人，餐馆里的服务员，黝黑粗糙的农民工来说，这里的财富全都由我们创造出来，但这幢高耸入云的大厦，这座城市的繁华，这里的车水马龙，高楼的富丽堂皇都与我们无关。"
    "【众人】" "拥挤的公交，无限延长的工作时长，不断疯涨价格的劣质酒，破旧窄小的住房，随时被克扣的工资……只有这些和我们有关。"
    "【众人】" "我们的生活满是无意义，即使和恶魔祈祷也无所谓。"
    "【众人】" "与我们有关的美好，只有你们，只有A-SOUL。"
    "【众人】" "对于未来的期盼我们已经放弃了，如今我们的前方什么都看不见，做什么都是无用功。"
    "【众人】" "我们还没有团结起来的原因，只是因为你们在，还有一丝希望。"
    "【众人】" "我们，需要你们的存在。"
    "【众人】" "你们要是抛弃我们，我们就一无所有了。"
    "【众人】" "所以求求你们，不要离开我们。"
    "【众人】" "变成我们想要的样子。"
    show xw sad with dissolve
    xw "我知道，我知道啊，但这不是我一个人能够改变的啊，我已经做到我能做到的所有事情了，可求求你们，不要伤害嘉然，不要把她从我的身边夺走啊。"
    xw "对不起，对不起，对不起……"
    xw "你们需要你们理想中的嘉然，可如果她变成那个样子，她就不是原来的嘉然了啊，我不要，我不要那样的嘉然。"

    scene 枝江天台1
    hide screen memory_filter
    show dirty_filter behind jr, xw
    show 火星 zorder 50:
        alpha 0.65
    with Dissolve(3)
    show xw angery with dissolve
    xw "如果是一个魂的话，就相信我们，和我们一起努力，坚持下去，不要因为困难而放弃啊！"
    "这句话又给了向晚力量，让她将自己的理智从无意识中拉了回来。"
    "她努力地向前迈进，穿过密不透风的火茧。"
    "刚刚的透支战斗和现在的火焰灼烧让她的嘴角留下一丝鲜血。"
    "然后，有谁抱住了她。"
    "那是嘉然，她的身上留下了道道黑色火焰灼烧再修复的痕迹。"
    "她的身体颤抖着，只是轻轻地抱住向晚，她的声带已经被灼烧地说不出完整的话来.."

    play music "audio/bgm/第八章 夜蝶 he hope.mp3" fadeout 4 fadein 4
    
    show jr sacred dignified at r2 with dissolve
    sjr "晚...晚... "
    #嘉然【圣嘉然悲伤】
    sjr "再...见...  "
    show xw:
        easeout 0.5 xoffset -200
    "像是幻觉般短暂的一个拥抱，向晚发现自己被推开了，黑色火焰欢呼着，呐喊着，咆哮着，将向晚向远处推去。"
    "此时的仪式已经到达了最盛之处，嘉然小姐的献祭过程也伴随着升腾的黑色火焰达至顶点。"
    scene 枝江天台1
    with dissolve
    "黑色的火焰，渐渐被净化成白色的光芒。"
    "白色光芒化成无数的碎片，散落到了枝江城的每一个角落。"

    scene 枝江街道夜晚
    with fade

    "【？？】""不知道为什么，我感觉心里的压力都消失了，身上轻松了很多，我有种想哭泣的感觉..."
    "【？？】""我也是..."
    "【？？】""我也是啊，我也有这感觉..."
    "或许只有今天，不相识的人们也能聚在一起相拥而泣。"

    scene 病房房间晚上
    with fade

    "碎片落到了医院的病房里，被苦痛折磨的病人舒缓了自己的眉头。"
    "许多病房里的病人从床头柜，床底下翻出了他们藏起来打算不吃的药、"
    "【？？】""我还能坚持下去，我不会选择放弃的。"
    "失去肢体的病人，也再一次走上了复健装置，不再怨天尤人。"
    "【？？】""今天再试一次吧，一定能站起来的。"
    scene 贫民窟
    with fade

    "碎片落到了贫民窟里，被生活的重担压得喘不过气来的人也有了一丝希望。"
    "【？？】""明天洗把脸，借套衣服，尝试去找份新工作吧。"
    "【？？】""我们苦就算了，至少，我们省一点，让她去上学吧，她想要成为像A-SOUL一样的偶像，不上学是不行的。"
    scene 夜空繁星
    with fade

    "碎片落到了遭受挫折，痛苦，折磨，困难的人们心中，他们感觉像是被拥抱住了一般，神明在对他们低语着"
    "你不再孤单。"
    "【？？】""不就是一份合同谈失败了嘛，再来一次就好了。"
    "【？？】""虽然我这次月考考砸了，但下一次拼搏百天，我一定要考上枝江大学。"
    "就像点点星光落到了每个人的身上，手上，和心中。"
    "虽然不知道能够持续多久，但这座城市终于等到了救赎。"


    scene 拥抱1 with Dissolve(5)
    "最后一点黑色火焰也消逝成了白色光芒，晚晚挣扎着从角落里爬起，把灰烬中的然然挖了出来，但然然已经毫无反应了。"
    xw "然然，你赶紧起来吧"
    xw "你别装睡了..."
    xw "这样子很让人害怕啊。"
    xw "说好的啊，说好我们要一起成为最强偶像的。"
    xw "你要吃什么零食我都可以买，你理一下我好吗..."
    xw "我还想再和你一起去水族馆看一次水母。"
    "向晚的眼泪点点滴滴掉到了嘉然脸上。"
    "一切像是一场奇怪的梦，火焰烧却之后没有留下任何痕迹，只留下一些黑色的残渣。"
    window hide 
    $ renpy.pause(6, hard=True)
    scene 拥抱2 with dissolve
    scene 拥抱1 with dissolve
    $ renpy.pause(2, hard=True)

    scene 拥抱4 with dissolve
    $ renpy.pause(2, hard=True)

    scene 拥抱3 with dissolve
    scene 拥抱4 with dissolve
    scene 拥抱3 with dissolve
    $ renpy.pause(3, hard=True)

    scene 拥抱5 with Dissolve(4)
    window show
    jr "为什么哭的这么伤心呢。"

    "嘉然的手指抚摸着向晚流泪的脸庞。"

    jr "我是嘉然"
    jr "你的名字是？"
    scene 枝江市广景傍晚 with Dissolve(5)
    
    "这座城市的发展速度又加快了许多。"

    "大家过得比以前幸福了一点点，但很快，生活又会回到往常的轨道。"

    "他们最喜欢的偶像仍在演出，带给他们快乐和感动。"

    "他们或许还会遭受痛苦与悲伤，但在心中仍会埋有些许希望。"

    "这座城市曾经发生的事，也再无人知晓。"

    window hide
    show 项链 with Dissolve(3)

    $ persistent.ge = True
    $ check_playthrough()
    $ achievement.grant('he')
    stop music fadeout 4
    $ renpy.pause(3, hard=True)
    scene black with Dissolve(2)

    $ renpy.pause(2, hard=True)
    show screen unskip
    if goTe:
        if persistent.playthrough == 3:
            $ quick_menu = False
            $ _skipping = False

        $ renpy.movie_cutscene("audio/video/end/HE.webm")
        $ renpy.pause(1.5, hard=True)

        $ renpy.movie_cutscene("audio/video/end/倒放.webm")
        $ renpy.pause(1.5, hard=True)
        hide screen unskip

        if persistent.playthrough == 3:
            $ quick_menu = True
            $ _skipping = True

        jump te
    else:
        $ renpy.movie_cutscene("audio/video/end/HE.webm")
        $ renpy.pause(3, hard=True)
        hide screen unskip

