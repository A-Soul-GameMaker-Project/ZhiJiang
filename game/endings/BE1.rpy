label be1:
    xw "这么晚了，你要去哪里呢？"
    #立绘【珈乐 怒】
    show jl angery at r2 with dissolve
    jl "只不过是出去转转而已。"
    jl "我去哪里和你有什么关系？"
    #立绘【向晚 哀】
    show xw sad at l2 with dissolve
    xw "我们可是队友啊……珈乐！"
    jl "不要再说了！"
    hide jl with moveoutright

    p "珈乐甩开了向晚拉过来的手，头也不回的向门外走去，只留下向晚在原地呆呆的看着。"
    $ renpy.pause(1.5)
    xw "...."
    hide xw with dissolve
    #场景【枝江外景】
    scene 枝江边上 with Dissolve(3)
    "第二天，珈乐没有回来。"

    "社交软件没有消息，电话也打不通，仿佛从人世间蒸发了一般。"

    "有在公司上班的人和同事说自己早上上班的时候在楼后的地面上看到了血迹。"

    "但是其他人并没有看到哪里有血迹，那个胡言乱语的员工也被阿草停职了。"

    "人来人往，繁华的枝江会逐渐将她遗忘。在时间中，她被替代。"

    "只不过，夜晚的霓虹灯似乎比往日更加闪耀了。"

    scene 海底向晚4 with Dissolve(3)
    show screen saying("水母又回到了海底" ,0.5,0.4,30) with Dissolve(3)
    $ achievement.grant('be1')
    stop music fadeout 20
    $ renpy.pause(15.0)

    hide screen saying with Dissolve(3)


    $ persistent.be1 = True
    $ check_playthrough()
